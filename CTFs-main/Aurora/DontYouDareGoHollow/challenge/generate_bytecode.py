#!/usr/bin/env python3
"""
Dark Souls VM - Bytecode Generator
"Prepare to Die" Edition

Generates spells.bin containing the bytecode program that performs
the 5 transformation passes and verification.
"""

import struct
import sys

# ============================================================================
# OPCODE DEFINITIONS - Must match challenge_vm.h
# ============================================================================

# Sorcery (Data Movement) - 0x0X
SOUL_ARROW      = 0x01  # Push immediate byte
SOUL_SPEAR      = 0x02  # Push memory[idx]
SOUL_MASS       = 0x03  # Pop to memory[idx]
CRYSTAL_SOUL    = 0x04  # Push memory[pop()]
HOMEWARD        = 0x05  # Pop and discard

# Pyromancy (Transformations) - 0x1X
FIREBALL        = 0x10  # XOR
COMBUSTION      = 0x11  # ROL
GREAT_CHAOS     = 0x12  # SUB
IRON_FLESH      = 0x13  # AND
POWER_WITHIN    = 0x14  # ADD

# Miracles (Control Flow) - 0x2X
FORCE           = 0x20  # Unconditional jump
WRATH           = 0x21  # Jump if idx < imm
EMIT_FORCE      = 0x22  # Jump if stack != 0
HOMEWARD_BONE   = 0x23  # Return success
DARKSIGN        = 0x24  # Return failure
LIGHTNING       = 0x25  # Jump if stack == 0

# Hexes (Index/Loop) - 0x3X
DARK_ORB        = 0x30  # Push idx
DARK_BEAD       = 0x31  # Increment idx
LIFEDRAIN       = 0x32  # Set idx = pop()
SCRAPS          = 0x33  # Reset idx to 0
PURSUERS        = 0x34  # Push (idx & 0x0F)

# Items (Utility) - 0x4X
ESTUS           = 0x40  # Duplicate stack top
LLOYD           = 0x41  # Swap top two
PRISM_STONE     = 0x42  # Push 0x17
TITANITE        = 0x43  # Push 0x5A
TWINKLING       = 0x44  # Push 0x0F
GREEN_BLOSSOM   = 0x45  # Push 0x03
HUMANITY        = 0x46  # Compare with check
MOSS_CLUMP      = 0x47  # Push 0x08
DIVINE_BLESSING = 0x48  # Push 64

# Decoys - 0xFX
PENDANT         = 0xF0  # NOP
RUBBISH         = 0xF1  # Fake side effect
DUNG_PIE        = 0xF2  # Swap twice
SKULL_LANTERN   = 0xF3  # Read and discard
BROKEN_SWORD    = 0xF4  # Dec then inc

MAX_SIZE = 64

# ============================================================================
# Bytecode Assembler
# ============================================================================

class DarkSoulsAssembler:
    def __init__(self):
        self.bytecode = []
        self.labels = {}
        self.fixups = []  # (position, label_name)

    def emit(self, *bytes_):
        """Emit raw bytes"""
        for b in bytes_:
            self.bytecode.append(b & 0xFF)

    def label(self, name):
        """Define a label at current position"""
        self.labels[name] = len(self.bytecode)

    def emit_jump(self, opcode, label_name, imm=None):
        """Emit a jump instruction with label reference"""
        self.emit(opcode)
        if imm is not None:
            self.emit(imm)  # For WRATH which has an immediate before address
        self.fixups.append((len(self.bytecode), label_name))
        self.emit(0x00, 0x00)  # Placeholder for 16-bit address

    def resolve(self):
        """Resolve all label references"""
        for pos, label in self.fixups:
            if label not in self.labels:
                raise ValueError(f"Undefined label: {label}")
            addr = self.labels[label]
            self.bytecode[pos] = addr & 0xFF
            self.bytecode[pos + 1] = (addr >> 8) & 0xFF

    def get_bytecode(self):
        """Get final bytecode"""
        self.resolve()
        return bytes(self.bytecode)


def generate_bytecode(add_decoys=True):
    """Generate the transformation bytecode program"""
    asm = DarkSoulsAssembler()

    # =========================================================================
    # PASS 0: XOR with (i ^ 0x17)
    # for (i = 0; i < 64; i++) memory[i] ^= (i ^ 0x17)
    # =========================================================================
    if add_decoys:
        asm.emit(PENDANT)           # Decoy: The pendant does nothing
        asm.emit(RUBBISH)           # Decoy: Fake operation

    asm.emit(SCRAPS)                # idx = 0
    asm.label("pass0_loop")
    asm.emit_jump(WRATH, "pass0_body", MAX_SIZE)  # if idx < 64, continue

    # Pass 0 done, go to pass 1
    asm.emit_jump(FORCE, "pass1_start")

    asm.label("pass0_body")
    asm.emit(SOUL_SPEAR)            # push memory[idx]
    asm.emit(DARK_ORB)              # push idx
    asm.emit(PRISM_STONE)           # push 0x17
    asm.emit(FIREBALL)              # idx ^ 0x17
    asm.emit(FIREBALL)              # memory[idx] ^ (idx ^ 0x17)
    asm.emit(SOUL_MASS)             # memory[idx] = result
    asm.emit(DARK_BEAD)             # idx++

    if add_decoys:
        asm.emit(SKULL_LANTERN)     # Decoy: read and discard

    asm.emit_jump(FORCE, "pass0_loop")

    # =========================================================================
    # PASS 1: ROL by 3
    # for (i = 0; i < 64; i++) memory[i] = ROL(memory[i], 3)
    # =========================================================================
    asm.label("pass1_start")
    asm.emit(SCRAPS)                # idx = 0

    if add_decoys:
        asm.emit(DUNG_PIE)          # Decoy: swap twice (no effect)

    asm.label("pass1_loop")
    asm.emit_jump(WRATH, "pass1_body", MAX_SIZE)
    asm.emit_jump(FORCE, "pass2_start")

    asm.label("pass1_body")
    asm.emit(SOUL_SPEAR)            # push memory[idx]
    asm.emit(GREEN_BLOSSOM)         # push 3
    asm.emit(COMBUSTION)            # ROL(value, 3)
    asm.emit(SOUL_MASS)             # memory[idx] = result
    asm.emit(DARK_BEAD)             # idx++
    asm.emit_jump(FORCE, "pass1_loop")

    # =========================================================================
    # PASS 2: XOR with next byte (rolling)
    # for (i = 0; i < 63; i++) memory[i] ^= memory[i+1]
    # =========================================================================
    asm.label("pass2_start")
    asm.emit(SCRAPS)                # idx = 0

    if add_decoys:
        asm.emit(PENDANT)           # Decoy
        asm.emit(BROKEN_SWORD)      # Decoy: dec then inc

    asm.label("pass2_loop")
    asm.emit_jump(WRATH, "pass2_body", MAX_SIZE - 1)  # if idx < 63, continue
    asm.emit_jump(FORCE, "pass3_start")

    asm.label("pass2_body")
    # memory[idx] ^= memory[idx + 1]
    asm.emit(SOUL_SPEAR)            # push memory[idx]
    asm.emit(DARK_ORB)              # push idx
    asm.emit(SOUL_ARROW, 1)         # push 1
    asm.emit(POWER_WITHIN)          # idx + 1
    asm.emit(CRYSTAL_SOUL)          # push memory[idx + 1]
    asm.emit(FIREBALL)              # memory[idx] ^ memory[idx+1]
    asm.emit(SOUL_MASS)             # memory[idx] = result
    asm.emit(DARK_BEAD)             # idx++
    asm.emit_jump(FORCE, "pass2_loop")

    # =========================================================================
    # PASS 3: SUB (i & 0x0F)
    # for (i = 0; i < 64; i++) memory[i] -= (i & 0x0F)
    # =========================================================================
    asm.label("pass3_start")
    asm.emit(SCRAPS)                # idx = 0

    asm.label("pass3_loop")
    asm.emit_jump(WRATH, "pass3_body", MAX_SIZE)
    asm.emit_jump(FORCE, "pass4_start")

    asm.label("pass3_body")
    asm.emit(SOUL_SPEAR)            # push memory[idx]
    asm.emit(PURSUERS)              # push (idx & 0x0F)
    asm.emit(GREAT_CHAOS)           # memory[idx] - (idx & 0x0F)
    asm.emit(SOUL_MASS)             # memory[idx] = result
    asm.emit(DARK_BEAD)             # idx++

    if add_decoys:
        asm.emit(RUBBISH)           # Decoy

    asm.emit_jump(FORCE, "pass3_loop")

    # =========================================================================
    # PASS 4: XOR with 0x5A
    # for (i = 0; i < 64; i++) memory[i] ^= 0x5A
    # =========================================================================
    asm.label("pass4_start")
    asm.emit(SCRAPS)                # idx = 0

    if add_decoys:
        asm.emit(SKULL_LANTERN)     # Decoy

    asm.label("pass4_loop")
    asm.emit_jump(WRATH, "pass4_body", MAX_SIZE)
    asm.emit_jump(FORCE, "verify_start")

    asm.label("pass4_body")
    asm.emit(SOUL_SPEAR)            # push memory[idx]
    asm.emit(TITANITE)              # push 0x5A
    asm.emit(FIREBALL)              # memory[idx] ^ 0x5A
    asm.emit(SOUL_MASS)             # memory[idx] = result
    asm.emit(DARK_BEAD)             # idx++
    asm.emit_jump(FORCE, "pass4_loop")

    # =========================================================================
    # VERIFICATION: Compare with check array
    # =========================================================================
    asm.label("verify_start")
    asm.emit(SCRAPS)                # idx = 0

    if add_decoys:
        asm.emit(PENDANT)           # The pendant... still does nothing

    asm.label("verify_loop")
    asm.emit_jump(WRATH, "verify_body", MAX_SIZE)

    # All bytes matched! Success!
    asm.emit(HOMEWARD_BONE)         # "YOU DEFEATED" - Link the Fire

    asm.label("verify_body")
    asm.emit(HUMANITY)              # Compare memory[idx] with check[idx]
    asm.emit_jump(EMIT_FORCE, "verify_fail")  # If not equal, fail
    asm.emit(DARK_BEAD)             # idx++
    asm.emit_jump(FORCE, "verify_loop")

    asm.label("verify_fail")
    asm.emit(DARKSIGN)              # "YOU DIED" - Go Hollow

    return asm.get_bytecode()


def main():
    output_file = "spells.bin"
    if len(sys.argv) > 1:
        output_file = sys.argv[1]

    print("Dark Souls VM - Bytecode Generator")
    print("=" * 50)

    bytecode = generate_bytecode(add_decoys=True)

    print(f"Generated {len(bytecode)} bytes of bytecode")
    print(f"Writing to {output_file}...")

    with open(output_file, "wb") as f:
        f.write(bytecode)

    print("Done!")
    print()
    print("Bytecode hexdump (first 64 bytes):")
    for i in range(0, min(64, len(bytecode)), 16):
        hex_part = " ".join(f"{b:02X}" for b in bytecode[i:i+16])
        print(f"  {i:04X}: {hex_part}")

    if len(bytecode) > 64:
        print(f"  ... ({len(bytecode) - 64} more bytes)")


if __name__ == "__main__":
    main()
