#ifndef CHALLENGE_VM_H
#define CHALLENGE_VM_H

#include <stdint.h>

#define MAX_SIZE	64
#define STACK_SIZE	256
#define MAX_BYTECODE	4096

/* opcodes: sorcery (data) */
#define SOUL_ARROW	0x01
#define SOUL_SPEAR	0x02
#define SOUL_MASS	0x03
#define CRYSTAL_SOUL	0x04
#define HOMEWARD	0x05

/* opcodes: pyromancy (math) */
#define FIREBALL	0x10
#define COMBUSTION	0x11
#define GREAT_CHAOS	0x12
#define IRON_FLESH	0x13
#define POWER_WITHIN	0x14

/* opcodes: miracles (control) */
#define FORCE		0x20
#define WRATH		0x21
#define EMIT_FORCE	0x22
#define HOMEWARD_BONE	0x23
#define DARKSIGN	0x24
#define LIGHTNING	0x25

/* opcodes: hexes (index) */
#define DARK_ORB	0x30
#define DARK_BEAD	0x31
#define LIFEDRAIN	0x32
#define SCRAPS		0x33
#define PURSUERS	0x34

/* opcodes: items (utility) */
#define ESTUS		0x40
#define LLOYD		0x41
#define PRISM_STONE	0x42
#define TITANITE	0x43
#define TWINKLING	0x44
#define GREEN_BLOSSOM	0x45
#define HUMANITY	0x46
#define MOSS_CLUMP	0x47
#define DIVINE_BLESSING	0x48

/* opcodes: decoys (nop) */
#define PENDANT		0xF0
#define RUBBISH		0xF1
#define DUNG_PIE	0xF2
#define SKULL_LANTERN	0xF3
#define BROKEN_SWORD	0xF4

typedef struct {
	uint8_t stack[STACK_SIZE];
	uint8_t sp;
	uint8_t memory[MAX_SIZE];
	uint8_t idx;
	uint16_t pc;
	uint8_t hollowing;
} vm_state;

extern unsigned char check[MAX_SIZE];

void vm_init(vm_state *vm, const unsigned char *input);
int load_bytecode(const char *filename, uint8_t *bytecode, size_t max_size);
int vm_execute(vm_state *vm, const uint8_t *bytecode, size_t bytecode_size);

static inline uint8_t rol(uint8_t v, int n)
{
	return (v << n) | (v >> (8 - n));
}

static inline uint8_t ror(uint8_t v, int n)
{
	return (v >> n) | (v << (8 - n));
}

#endif
