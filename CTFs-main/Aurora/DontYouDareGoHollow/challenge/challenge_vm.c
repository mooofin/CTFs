#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "challenge_vm.h"

unsigned char check[MAX_SIZE] = {
	0xF2, 0x45, 0x64, 0x67, 0xBE, 0x97, 0x78, 0x7E,
	0x29, 0xA3, 0x0D, 0x34, 0x5C, 0x59, 0x17, 0x38,
	0xA0, 0x63, 0x15, 0xFC, 0xAC, 0x41, 0x8E, 0xFB,
	0x13, 0x62, 0x7A, 0x62, 0x8F, 0xDF, 0x07, 0x53,
	0xE2, 0x53, 0xC2, 0xAF, 0x85, 0x49, 0x58, 0x2B,
	0x5A, 0x55, 0xA4, 0x77, 0xA6, 0x51, 0xA0, 0xB3,
	0x52, 0x4D, 0x5C, 0x6F, 0x5E, 0x49, 0x58, 0x2B,
	0x5A, 0x55, 0xA4, 0x77, 0xA6, 0x51, 0xA0, 0x68,
};

void vm_init(vm_state *vm, const unsigned char *input)
{
	memset(vm->stack, 0, STACK_SIZE);
	vm->sp = 0;
	memset(vm->memory, 0, MAX_SIZE);
	if (input)
		strncpy((char *)vm->memory, (const char *)input, MAX_SIZE - 1);
	vm->idx = 0;
	vm->pc = 0;
	vm->hollowing = 0;
}

int load_bytecode(const char *filename, uint8_t *bytecode, size_t max_size)
{
	FILE *f;
	long size;
	size_t nread;

	f = fopen(filename, "rb");
	if (!f)
		return -1;

	fseek(f, 0, SEEK_END);
	size = ftell(f);
	fseek(f, 0, SEEK_SET);

	if (size > (long)max_size) {
		fclose(f);
		return -1;
	}

	nread = fread(bytecode, 1, size, f);
	fclose(f);

	return (int)nread;
}

int vm_execute(vm_state *vm, const uint8_t *bytecode, size_t bytecode_size)
{
	uint8_t a, b, op, shift;
	uint16_t addr;

	while (vm->pc < bytecode_size) {
		op = bytecode[vm->pc++];

		switch (op) {
		case SOUL_ARROW:
			if (vm->pc >= bytecode_size)
				return 0;
			vm->stack[vm->sp++] = bytecode[vm->pc++];
			break;

		case SOUL_SPEAR:
			vm->stack[vm->sp++] = vm->memory[vm->idx];
			break;

		case SOUL_MASS:
			if (vm->sp == 0)
				return 0;
			vm->memory[vm->idx] = vm->stack[--vm->sp];
			break;

		case CRYSTAL_SOUL:
			if (vm->sp == 0)
				return 0;
			a = vm->stack[--vm->sp];
			if (a >= MAX_SIZE)
				return 0;
			vm->stack[vm->sp++] = vm->memory[a];
			break;

		case HOMEWARD:
			if (vm->sp == 0)
				return 0;
			vm->sp--;
			break;

		case FIREBALL:
			if (vm->sp < 2)
				return 0;
			b = vm->stack[--vm->sp];
			a = vm->stack[--vm->sp];
			vm->stack[vm->sp++] = a ^ b;
			break;

		case COMBUSTION:
			if (vm->sp < 2)
				return 0;
			shift = vm->stack[--vm->sp];
			a = vm->stack[--vm->sp];
			vm->stack[vm->sp++] = rol(a, shift & 7);
			break;

		case GREAT_CHAOS:
			if (vm->sp < 2)
				return 0;
			b = vm->stack[--vm->sp];
			a = vm->stack[--vm->sp];
			vm->stack[vm->sp++] = (a - b) & 0xFF;
			break;

		case IRON_FLESH:
			if (vm->sp < 2)
				return 0;
			b = vm->stack[--vm->sp];
			a = vm->stack[--vm->sp];
			vm->stack[vm->sp++] = a & b;
			break;

		case POWER_WITHIN:
			if (vm->sp < 2)
				return 0;
			b = vm->stack[--vm->sp];
			a = vm->stack[--vm->sp];
			vm->stack[vm->sp++] = (a + b) & 0xFF;
			break;

		case FORCE:
			if (vm->pc + 1 >= bytecode_size)
				return 0;
			addr = bytecode[vm->pc] | (bytecode[vm->pc + 1] << 8);
			vm->pc = addr;
			break;

		case WRATH:
			if (vm->pc + 2 >= bytecode_size)
				return 0;
			a = bytecode[vm->pc++];
			addr = bytecode[vm->pc] | (bytecode[vm->pc + 1] << 8);
			vm->pc += 2;
			if (vm->idx < a)
				vm->pc = addr;
			break;

		case EMIT_FORCE:
			if (vm->sp == 0)
				return 0;
			if (vm->pc + 1 >= bytecode_size)
				return 0;
			a = vm->stack[--vm->sp];
			addr = bytecode[vm->pc] | (bytecode[vm->pc + 1] << 8);
			vm->pc += 2;
			if (a != 0)
				vm->pc = addr;
			break;

		case HOMEWARD_BONE:
			return 1;

		case DARKSIGN:
			return 0;

		case LIGHTNING:
			if (vm->sp == 0)
				return 0;
			if (vm->pc + 1 >= bytecode_size)
				return 0;
			a = vm->stack[--vm->sp];
			addr = bytecode[vm->pc] | (bytecode[vm->pc + 1] << 8);
			vm->pc += 2;
			if (a == 0)
				vm->pc = addr;
			break;

		case DARK_ORB:
			vm->stack[vm->sp++] = vm->idx;
			break;

		case DARK_BEAD:
			vm->idx++;
			break;

		case LIFEDRAIN:
			if (vm->sp == 0)
				return 0;
			vm->idx = vm->stack[--vm->sp];
			break;

		case SCRAPS:
			vm->idx = 0;
			break;

		case PURSUERS:
			vm->stack[vm->sp++] = vm->idx & 0x0F;
			break;

		case ESTUS:
			if (vm->sp == 0)
				return 0;
			a = vm->stack[vm->sp - 1];
			vm->stack[vm->sp++] = a;
			break;

		case LLOYD:
			if (vm->sp < 2)
				return 0;
			a = vm->stack[vm->sp - 1];
			vm->stack[vm->sp - 1] = vm->stack[vm->sp - 2];
			vm->stack[vm->sp - 2] = a;
			break;

		case PRISM_STONE:
			vm->stack[vm->sp++] = 0x17;
			break;

		case TITANITE:
			vm->stack[vm->sp++] = 0x5A;
			break;

		case TWINKLING:
			vm->stack[vm->sp++] = 0x0F;
			break;

		case GREEN_BLOSSOM:
			vm->stack[vm->sp++] = 0x03;
			break;

		case HUMANITY:
			vm->stack[vm->sp++] = (vm->memory[vm->idx] != check[vm->idx]);
			break;

		case MOSS_CLUMP:
			vm->stack[vm->sp++] = 0x08;
			break;

		case DIVINE_BLESSING:
			vm->stack[vm->sp++] = MAX_SIZE;
			break;

		case PENDANT:
			break;

		case RUBBISH:
			vm->hollowing++;
			vm->hollowing--;
			break;

		case DUNG_PIE:
			if (vm->sp >= 2) {
				a = vm->stack[vm->sp - 1];
				vm->stack[vm->sp - 1] = vm->stack[vm->sp - 2];
				vm->stack[vm->sp - 2] = a;
				a = vm->stack[vm->sp - 1];
				vm->stack[vm->sp - 1] = vm->stack[vm->sp - 2];
				vm->stack[vm->sp - 2] = a;
			}
			break;

		case SKULL_LANTERN:
			(void)vm->memory[vm->idx];
			break;

		case BROKEN_SWORD:
			vm->idx--;
			vm->idx++;
			break;

		default:
			return 0;
		}
	}

	return 0;
}

int main(int argc, char **argv)
{
	uint8_t bytecode[MAX_BYTECODE];
	int bytecode_size;
	vm_state vm;

	if (argc != 2) {
		printf("Usage: %s <flag>\n", argv[0]);
		printf("\"Prepare to Die\"\n");
		return 1;
	}

	bytecode_size = load_bytecode("spells.bin", bytecode, MAX_BYTECODE);
	if (bytecode_size < 0) {
		printf("Failed to load spells.bin - The bonfire has faded...\n");
		return 1;
	}

	vm_init(&vm, (const unsigned char *)argv[1]);

	if (vm_execute(&vm, bytecode, bytecode_size)) {
		printf("YOU DEFEATED\n");
		return 0;
	}

	printf("YOU DIED\n");
	return 1;
}
