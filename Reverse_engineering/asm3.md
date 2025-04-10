

```
# ASM3 Challenge Writeup

## Understanding the Problem
We need to determine what the function `asm3` returns when called with these arguments:
```c
asm3(0xd73346ed, 0xd48672ae, 0xd3c8b139)
```

## The Assembly Code
Here's the disassembled function with comments:
```asm
asm3:
    push   ebp
    mov    ebp,esp
    xor    eax,eax            ; Zero out EAX
    mov    ah,BYTE PTR [ebp+0xa]  ; Load 2nd byte of 1st arg (0x33) into AH
    shl    ax,0x10            ; Shift AX left by 16 (problematic!)
    sub    al,BYTE PTR [ebp+0xc] ; Subtract LSB of 2nd arg (0xae) from AL
    add    ah,BYTE PTR [ebp+0xd] ; Add 2nd byte of 2nd arg (0x72) to AH
    xor    ax,WORD PTR [ebp+0x10] ; XOR with first 2 bytes of 3rd arg
    nop
    pop    ebp
    ret
```

## Step-by-Step Execution

### 1. Memory Layout (Little-Endian)
When the function is called, the stack looks like this:

| Address  | Value (Bytes) | Argument |
|----------|---------------|----------|
| ebp+0x8  | ed 46 33 d7   | a (0xd73346ed) |
| ebp+0xc  | ae 72 86 d4   | b (0xd48672ae) |
| ebp+0x10 | 39 b1 c8 d3   | c (0xd3c8b139) |

### 2. Instruction Breakdown

1. `xor eax,eax`  
   - EAX = `0x00000000`

2. `mov ah,BYTE PTR [ebp+0xa]`  
   - Reads from `ebp+0xa` (between 1st and 2nd args)
   - Gets `0x33` (from `d7 33 46 ed`)
   - EAX = `0x00003300`

3. `shl ax,0x10`  
   - **Issue**: Shifting 16-bit AX by 16 clears it!
   - AX becomes `0x0000` (likely a disassembly error)
   - *Assumed intended*: `shl eax,0x10` → EAX = `0x33000000`

4. `sub al,BYTE PTR [ebp+0xc]`  
   - Subtracts `0xae` (from `ae 72 86 d4`)
   - `0x00 - 0xae` = `0x52` (with underflow)
   - EAX = `0x33000052`

5. `add ah,BYTE PTR [ebp+0xd]`  
   - Adds `0x72` to AH (`0x00 + 0x72`)
   - EAX = `0x33007252`

6. `xor ax,WORD PTR [ebp+0x10]`  
   - XORs AX (`0x7252`) with `0xb139` (first 2 bytes of 3rd arg)
   - `0x7252 ^ 0xb139` = `0xc36b`
   - Final EAX = `0x3300c36b` (but only AX is returned)

## Key Observations
1. The `shl ax,0x10` instruction appears incorrect - it would zero out AX
2. The likely intended operation was `shl eax,0x10`
3. Without this correction, the function wouldn't work logically

## Final Answer
After executing all operations, the function returns:  
**`0xc36b`**
```

