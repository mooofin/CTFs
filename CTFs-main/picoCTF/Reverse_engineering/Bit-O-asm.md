# Bit-O-Asm-1 Writeup

## Challenge Description
We are given an assembly dump and need to determine the contents of the `eax` register. The flag format is `picoCTF{n}`, where `n` is the decimal value stored in `eax`.

## Given Assembly Code
```assembly
<+0>:     endbr64
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
```

## Analyzing the Code
Let's break down the instructions:

1. `endbr64`: This is related to Intel CET (Control-Flow Enforcement Technology). It is not relevant to our analysis.
2. `push rbp`: Saves the base pointer.
3. `mov rbp, rsp`: Sets up the stack frame.
4. `mov DWORD PTR [rbp-0x4], edi`: Stores `edi` in a local variable.
5. `mov QWORD PTR [rbp-0x10], rsi`: Stores `rsi` in another local variable.
6. `mov eax, 0x30`: Loads `0x30` (hexadecimal) into the `eax` register.
7. `pop rbp`: Restores the previous base pointer.
8. `ret`: Returns from the function.

Since `eax` holds `0x30` at the end of execution and `0x30` in decimal is `48`, our final answer is:

## Flag
```
picoCTF{48}
```

