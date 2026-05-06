#!/usr/bin/env python3

import sys

OPCODES = {
    0x01: ("SOUL_ARROW",     1),
    0x02: ("SOUL_SPEAR",     0),
    0x03: ("SOUL_MASS",      0),
    0x04: ("CRYSTAL_SOUL",   0),
    0x05: ("HOMEWARD",       0),

    0x10: ("FIREBALL",       0),
    0x11: ("COMBUSTION",     0),
    0x12: ("GREAT_CHAOS",    0),
    0x13: ("IRON_FLESH",     0),
    0x14: ("POWER_WITHIN",   0),

    0x20: ("FORCE",          2),
    0x21: ("WRATH",          3),
    0x22: ("EMIT_FORCE",     2),
    0x23: ("HOMEWARD_BONE",  0),
    0x24: ("DARKSIGN",       0),
    0x25: ("LIGHTNING",      2),

    0x30: ("DARK_ORB",       0),
    0x31: ("DARK_BEAD",      0),
    0x32: ("LIFEDRAIN",      0),
    0x33: ("SCRAPS",         0),
    0x34: ("PURSUERS",       0),

    0x40: ("ESTUS",          0),
    0x41: ("LLOYD",          0),
    0x42: ("PRISM_STONE",    0),
    0x43: ("TITANITE",       0),
    0x44: ("TWINKLING",      0),
    0x45: ("GREEN_BLOSSOM",  0),
    0x46: ("HUMANITY",       0),
    0x47: ("MOSS_CLUMP",     0),
    0x48: ("DIVINE_BLESSING", 0),

    0xF0: ("PENDANT",        0),
    0xF1: ("RUBBISH",        0),
    0xF2: ("DUNG_PIE",       0),
    0xF3: ("SKULL_LANTERN",  0),
    0xF4: ("BROKEN_SWORD",   0),
}

def read_u16(bc, pc):
    return bc[pc] | (bc[pc + 1] << 8)

def find_labels(bc):
    labels = {}
    pc = 0

    while pc < len(bc):
        op = bc[pc]
        pc += 1

        if op not in OPCODES:
            continue

        name, size = OPCODES[op]

        if name == "FORCE":
            labels[read_u16(bc, pc)] = True
            pc += 2
        elif name == "WRATH":
            pc += 1
            labels[read_u16(bc, pc)] = True
            pc += 2
        elif name in ("EMIT_FORCE", "LIGHTNING"):
            labels[read_u16(bc, pc)] = True
            pc += 2
        elif name == "SOUL_ARROW":
            pc += 1

    return labels

def disasm(bc):
    labels = find_labels(bc)
    pc = 0

    while pc < len(bc):
        if pc in labels:
            print(f"\nloc_{pc:04x}:")

        addr = pc
        op = bc[pc]
        pc += 1

        if op not in OPCODES:
            print(f"  {addr:04x}: .byte 0x{op:02x}")
            continue

        name, size = OPCODES[op]
        operands = ""

        if name == "SOUL_ARROW":
            operands = f"0x{bc[pc]:02x}"
            pc += 1
        elif name == "FORCE":
            target = read_u16(bc, pc)
            operands = f"loc_{target:04x}"
            pc += 2
        elif name == "WRATH":
            limit = bc[pc]
            target = read_u16(bc, pc + 1)
            operands = f"{limit}, loc_{target:04x}"
            pc += 3
        elif name in ("EMIT_FORCE", "LIGHTNING"):
            target = read_u16(bc, pc)
            operands = f"loc_{target:04x}"
            pc += 2

        print(f"  {addr:04x}: {name:<16} {operands}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <bytecode>")
        sys.exit(1)

    with open(sys.argv[1], 'rb') as f:
        bc = f.read()

    print(f"; {sys.argv[1]} ({len(bc)} bytes)\n")
    disasm(bc)
