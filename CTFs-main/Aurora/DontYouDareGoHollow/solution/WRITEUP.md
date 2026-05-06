# Aurora

`aur{th15_1r_w45_n0t_m34nt_t0_b3_cu7e}`

## Unpacking

The challenge binary is UPX packed:

```
$ file challenge_vm
challenge_vm: ELF 64-bit LSB pie executable, x86-64, statically linked, no section header
```

No section headers and statically linked is a dead giveaway. Unpack:

```
$ upx -d challenge_vm -o challenge_vm_unpacked
                       Ultimate Packer for eXecutables
        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
     18648 <-     10188   54.63%   linux/amd64   challenge_vm_unpacked
```

## r2 Analysis

Load into radare2 and run analysis:

```
$ r2 -A challenge_vm_unpacked
[0x000010c0]> afl
0x00001030    1      6 sym.imp.strncpy
0x00001040    1      6 sym.imp.fread
0x00001050    1      6 sym.imp.fclose
0x00001060    1      6 sym.imp.__stack_chk_fail
0x00001070    1      6 sym.imp.printf
0x00001080    1      6 sym.imp.memset
0x00001090    1      6 sym.imp.ftell
0x000010a0    1      6 sym.imp.fseek
0x000010b0    1      6 sym.imp.fopen
0x000010c0    1     37 entry0
0x00001f80   10    328 main
0x00001250    6    181 fcn.00001250
0x000011c0    3    139 fcn.000011c0
0x00001310   89   3128 fcn.00001310
```

Key functions: `main` at 0x1f80, VM init at 0x11c0, VM executor at 0x1310 (3128 bytes - the big switch).

Check strings:

```
[0x000010c0]> iz~spell,DIED,DEFEAT,Usage
0   0x000033d7 0x000033d7 17  18   .rodata ascii Usage: %s <flag>\n
2   0x000033fb 0x000033fb 10  11   .rodata ascii spells.bin
3   0x00003406 0x00003406 53  54   .rodata ascii Failed to load spells.bin - The bonfire has faded...\n
4   0x0000343c 0x0000343c 13  14   .rodata ascii YOU DEFEATED\n
5   0x0000344a 0x0000344a 9   10   .rodata ascii YOU DIED\n
```

## main @ 0x1f80

```
[0x00001f80]> pdf
/ 328: int main (uint32_t argc, char **argv);
|           0x00001f80      push rbp
|           0x00001f81      mov rbp, rsp
|           0x00001f84      sub rsp, 0x1170
|           ...
|           0x00001faf      cmp dword [var_1160h], 2      ; argc check
|       ,=< 0x00001fb6      je 0x1fed
|       |   0x00001fc2      lea rdi, str.Usage:__s__flag__n  ; 0x33d7
|       |   0x00001fcb      call sym.imp.printf
|       |   0x00001fd0      lea rdi, str._Prepare_to_Die__n  ; 0x33e9
|       |   ...
|       `-> 0x00001fed      lea rsi, [var_1010h]          ; bytecode buffer
|           0x00001ff4      lea rdi, str.spells.bin       ; 0x33fb
|           0x00001ffb      mov edx, 0x1000               ; max size
|           0x00002000      call fcn.00001250             ; load_bytecode
|           0x00002035      mov rsi, qword [rax + 8]      ; argv[1]
|           0x00002039      lea rdi, [var_1156h]          ; vm state
|           0x00002040      call fcn.000011c0             ; vm_init
|           0x0000205a      call fcn.00001310             ; vm_execute
|           0x0000205f      cmp eax, 0
|       ,=< 0x00002062      je 0x207e
|       |   0x00002064      lea rdi, str.YOU_DEFEATED_n   ; 0x343c
|       |   ...
|       `-> 0x0000207e      lea rdi, str.YOU_DIED_n       ; 0x344a
```

Flow: check argc → load spells.bin → init VM with argv[1] → execute → print result.

## VM State Structure

Reverse `fcn.000011c0` (vm_init):

```
[0x000011c0]> pdf
/ 139: fcn.000011c0 (char *arg1, char *arg2);
|           0x000011d0      mov rdi, qword [dest]
|           0x000011d6      mov edx, 0x100              ; memset 256 bytes
|           0x000011db      call sym.imp.memset         ; clear stack[256]
|           0x000011e4      mov byte [rax + 0x100], 0   ; sp = 0
|           0x000011ef      add rdi, 0x101
|           0x000011f8      mov edx, 0x40               ; memset 64 bytes
|           0x000011fd      call sym.imp.memset         ; clear memory[64]
|           0x0000121d      call sym.imp.strncpy        ; copy input to memory
|           0x00001226      mov byte [rax + 0x141], 0   ; idx = 0
|           0x00001231      mov word [rax + 0x142], 0   ; pc = 0
|           0x0000123e      mov byte [rax + 0x144], 0   ; hollowing = 0
```

Recovered struct:

```c
struct DarkSoulsVM {
    uint8_t stack[256];     // 0x000 - 0x0FF
    uint8_t sp;             // 0x100
    uint8_t memory[64];     // 0x101 - 0x140
    uint8_t idx;            // 0x141
    uint16_t pc;            // 0x142
    uint8_t hollowing;      // 0x144 (unused)
};  // total: 0x145 bytes
```

## VM Executor @ 0x1310

The big function. Key dispatch logic:

```
[0x00001310]> pdf
/ 3128: fcn.00001310 (int64_t arg1, int64_t arg2, signed int64_t arg3);
|       .-> 0x00001324      mov rax, qword [var_10h]
|       :   0x00001328      movzx eax, word [rax + 0x142]  ; fetch pc
|       :   0x0000132f      cmp rax, qword [var_20h]       ; bounds check
|      ,==< 0x00001333      jae 0x1f38                     ; exit if pc >= bytecode_size
|      |:   0x00001353      mov al, byte [rax + rcx]       ; fetch opcode
|      |:   0x0000135d      dec eax                        ; opcode - 1
|      |:   0x00001365      sub eax, 0xf3                  ; range 0x01-0xf4
|     ,===< 0x0000136a      ja case.0x1382.5               ; default case
|     ||:   0x00001374      lea rax, [0x00003004]          ; jump table
|     ||:   0x0000137b      movsxd rcx, dword [rax + rcx*4]
|     ||:   0x0000137f      add rax, rcx
|     ||:   0x00001382      jmp rax                        ; dispatch
```

Jump table at 0x3004 has 244 entries (opcodes 0x01 to 0xf4). Dump first 16 dwords:

```
[0x00001310]> pxw 64 @ 0x3004
0x00003004  0xffffe380 0xffffe3e7 0xffffe424 0xffffe478
0x00003014  0xffffe4ff 0xffffef26 0xffffef26 0xffffef26
0x00003024  0xffffef26 0xffffef26 0xffffef26 0xffffef26
0x00003034  0xffffef26 0xffffef26 0xffffef26 0xffffe533
```

These are signed offsets from 0x3004. For example:
- Entry 0 (opcode 0x01): 0xffffe380 → 0x3004 + (-0x1c80) = 0x1384 (SOUL_ARROW handler)
- Entry 15 (opcode 0x10): 0xffffe533 → 0x3004 + (-0x1acd) = 0x1537 (FIREBALL handler)

Most entries are 0xffffef26 → points to default NOP handler at 0x1f2a.

## Opcode Handlers

Tracing each case handler to recover operations:

**Case 0 (opcode 0x01) - SOUL_ARROW @ 0x1384:**
```asm
movzx eax, word [rax + 0x142]     ; pc
mov cx, word [rdx + 0x142]
add si, 1                          ; pc++
mov byte [rax + rcx], dl           ; stack[sp++] = bytecode[pc-1]
```
Push immediate byte from bytecode.

**Case 1 (opcode 0x02) - SOUL_SPEAR @ 0x13eb:**
```asm
movzx ecx, byte [rcx + 0x141]      ; idx
mov dl, byte [rax + rcx + 0x101]   ; memory[idx]
mov byte [rax + rcx], dl           ; stack[sp++] = memory[idx]
```
Push memory[idx] to stack.

**Case 2 (opcode 0x03) - SOUL_MASS @ 0x1428:**
```asm
mov cl, byte [rdx + 0x100]         ; sp
add cl, 0xff                       ; sp--
mov dl, byte [rax + rcx]           ; stack[sp]
movzx ecx, byte [rcx + 0x141]      ; idx
mov byte [rax + rcx + 0x101], dl   ; memory[idx] = popped value
```
Pop stack to memory[idx].

Continue for all handlers...

## Complete Opcode Map

```
DATA:
  0x01 SOUL_ARROW     push imm8
  0x02 SOUL_SPEAR     push memory[idx]
  0x03 SOUL_MASS      pop to memory[idx]
  0x04 CRYSTAL_SOUL   push memory[pop()]
  0x05 HOMEWARD       pop and discard

MATH:
  0x10 FIREBALL       a = pop(); b = pop(); push(a ^ b)
  0x11 COMBUSTION     shift = pop(); val = pop(); push(ROL(val, shift))
  0x12 GREAT_CHAOS    a = pop(); b = pop(); push((b - a) & 0xFF)
  0x13 IRON_FLESH     a = pop(); b = pop(); push(a & b)
  0x14 POWER_WITHIN   a = pop(); b = pop(); push((a + b) & 0xFF)

CONTROL:
  0x20 FORCE          pc = read_u16()
  0x21 WRATH          limit = read_u8(); target = read_u16(); if (idx < limit) pc = target
  0x22 EMIT_FORCE     target = read_u16(); if (pop() != 0) pc = target
  0x23 HOMEWARD_BONE  return 1
  0x24 DARKSIGN       return 0
  0x25 LIGHTNING      target = read_u16(); if (pop() == 0) pc = target

INDEX:
  0x30 DARK_ORB       push(idx)
  0x31 DARK_BEAD      idx++
  0x32 LIFEDRAIN      idx = pop()
  0x33 SCRAPS         idx = 0
  0x34 PURSUERS       push(idx & 0x0F)

CONSTANTS:
  0x42 PRISM_STONE    push(0x17)
  0x43 TITANITE       push(0x5A)
  0x45 GREEN_BLOSSOM  push(0x03)
  0x46 HUMANITY       cmp memory[idx] with check[idx], push result
  0x48 DIVINE_BLESSING push(64)

DECOYS:
  0xF0 PENDANT        nop
  0xF1 RUBBISH        nop (fake side effect)
  0xF2 DUNG_PIE       swap; swap (cancels out)
  0xF3 SKULL_LANTERN  read and discard
  0xF4 BROKEN_SWORD   dec; inc (cancels out)
```

## Check Array

The HUMANITY opcode (0x46) compares against a hardcoded array. Find it:

```
[0x00001310]> px 64 @ 0x5060
- offset -  0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x00005060  f245 6467 be97 787e 29a3 0d34 5c59 1738  .Edg..x~)..4\Y.8
0x00005070  a063 15fc ac41 8efb 1362 7a62 8fdf 0753  .c...A...bzb...S
0x00005080  e253 c2af 8549 582b 5a55 a477 a651 a0b3  .S...IX+ZU.w.Q..
0x00005090  524d 5c6f 5e49 582b 5a55 a477 a651 a068  RM\o^IX+ZU.w.Q.h
```

64 bytes in .data section.

## Bytecode Disassembly

Disassemble spells.bin (110 bytes):

```
0000: F0           PENDANT              ; nop
0001: F1           RUBBISH              ; nop
0002: 33           SCRAPS               ; idx = 0

; === PASS 0: XOR with (idx ^ 0x17) ===
0003: 21 40 0A 00  WRATH 64, 0x000A
0007: 20 15 00     FORCE 0x0015
000A: 02           SOUL_SPEAR           ; push mem[idx]
000B: 30           DARK_ORB             ; push idx
000C: 42           PRISM_STONE          ; push 0x17
000D: 10           FIREBALL             ; xor → (idx ^ 0x17)
000E: 10           FIREBALL             ; xor → mem[idx] ^ (idx ^ 0x17)
000F: 03           SOUL_MASS            ; mem[idx] = result
0010: 31           DARK_BEAD            ; idx++
0011: F3           SKULL_LANTERN        ; nop
0012: 20 03 00     FORCE 0x0003

; === PASS 1: ROL by 3 ===
0015: 33           SCRAPS
0016: F2           DUNG_PIE
0017: 21 40 1E 00  WRATH 64, 0x001E
001B: 20 26 00     FORCE 0x0026
001E: 02           SOUL_SPEAR
001F: 45           GREEN_BLOSSOM        ; push 3
0020: 11           COMBUSTION           ; ROL
0021: 03           SOUL_MASS
0022: 31           DARK_BEAD
0023: 20 17 00     FORCE 0x0017

; === PASS 2: XOR with mem[idx+1] ===
0026: 33           SCRAPS
0027: F0           PENDANT
0028: F4           BROKEN_SWORD
0029: 21 3F 30 00  WRATH 63, 0x0030     ; note: 63, not 64
002D: 20 3C 00     FORCE 0x003C
0030: 02           SOUL_SPEAR
0031: 30           DARK_ORB
0032: 01 01        SOUL_ARROW 0x01
0034: 14           POWER_WITHIN         ; idx + 1
0035: 04           CRYSTAL_SOUL         ; push mem[idx+1]
0036: 10           FIREBALL             ; xor
0037: 03           SOUL_MASS
0038: 31           DARK_BEAD
0039: 20 29 00     FORCE 0x0029

; === PASS 3: SUB (idx & 0x0F) ===
003C: 33           SCRAPS
003D: 21 40 44 00  WRATH 64, 0x0044
0041: 20 4D 00     FORCE 0x004D
0044: 02           SOUL_SPEAR
0045: 34           PURSUERS             ; push (idx & 0x0F)
0046: 12           GREAT_CHAOS          ; sub
0047: 03           SOUL_MASS
0048: 31           DARK_BEAD
0049: F1           RUBBISH
004A: 20 3D 00     FORCE 0x003D

; === PASS 4: XOR 0x5A ===
004D: 33           SCRAPS
004E: F3           SKULL_LANTERN
004F: 21 40 56 00  WRATH 64, 0x0056
0053: 20 5E 00     FORCE 0x005E
0056: 02           SOUL_SPEAR
0057: 43           TITANITE             ; push 0x5A
0058: 10           FIREBALL
0059: 03           SOUL_MASS
005A: 31           DARK_BEAD
005B: 20 4F 00     FORCE 0x004F

; === VERIFY ===
005E: 33           SCRAPS
005F: F0           PENDANT
0060: 21 40 65 00  WRATH 64, 0x0065
0064: 23           HOMEWARD_BONE        ; return 1 (success)
0065: 46           HUMANITY             ; compare
0066: 22 6D 00     EMIT_FORCE 0x006D    ; if != 0 goto fail
0069: 31           DARK_BEAD
006A: 20 60 00     FORCE 0x0060
006D: 24           DARKSIGN             ; return 0 (failure)
```

## Transformation Summary

```
Pass 0:  mem[i] ^= (i ^ 0x17)           for i in 0..63
Pass 1:  mem[i] = ROL(mem[i], 3)        for i in 0..63
Pass 2:  mem[i] ^= mem[i+1]             for i in 0..62   (chain dependency)
Pass 3:  mem[i] -= (i & 0x0F)           for i in 0..63
Pass 4:  mem[i] ^= 0x5A                 for i in 0..63
```

## Inversion

Reverse order, inverse operations:

```
Undo Pass 4:  d[i] ^= 0x5A              (XOR self-inverse)
Undo Pass 3:  d[i] += (i & 0x0F)        (SUB → ADD)
Undo Pass 2:  d[i] ^= d[i+1]            (iterate 62→0, not 0→62)
Undo Pass 1:  d[i] = ROR(d[i], 3)       (ROL → ROR)
Undo Pass 0:  d[i] ^= (i ^ 0x17)        (XOR self-inverse)
```

Pass 2 is the critical insight. Forward does `mem[0] ^= mem[1]`, `mem[1] ^= mem[2]`, etc. Each output depends on the next value. To reverse, must start from the end: `mem[62] ^= mem[63]` first, then `mem[61] ^= mem[62]`, down to `mem[0] ^= mem[1]`. Going forward corrupts values before they're used.

## Solve

```python
def ror(v, n):
    return ((v >> n) | (v << (8 - n))) & 0xFF

check = bytes.fromhex(
    "f2456467be97787e29a30d345c591738"
    "a06315fcac418efb13627a628fdf0753"
    "e253c2af8549582b5a55a477a651a0b3"
    "524d5c6f5e49582b5a55a477a651a068"
)

d = list(check)
for i in range(64): d[i] ^= 0x5A
for i in range(64): d[i] = (d[i] + (i & 0xF)) & 0xFF
for i in range(62, -1, -1): d[i] ^= d[i + 1]
for i in range(64): d[i] = ror(d[i], 3)
for i in range(64): d[i] ^= (i ^ 0x17)

print(bytes(d).rstrip(b'\x00').decode())
# aur{th15_1r_w45_n0t_m34nt_t0_b3_cu7e}
```
