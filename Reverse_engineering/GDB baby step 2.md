# Debugging a CTF Challenge Using GDB

## **Challenge Description**
We need to determine the value stored in the `eax` register at the end of the `main` function and format it as `picoCTF{n}`, where `n` is the decimal equivalent of the final `eax` value.

---

## **Step 1: Disassembling the Binary**
First, we use `gdb` to disassemble the `main` function:

```sh
$ gdb debugger0_a
(gdb) set disassembly-flavor intel
(gdb) disassemble main
```

This gives us the following assembly code:

```assembly
0x0000000000401106 <+0>:     endbr64
0x000000000040110a <+4>:     push   rbp
0x000000000040110b <+5>:     mov    rbp,rsp
0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x1e0da
0x000000000040111c <+22>:    mov    DWORD PTR [rbp-0xc],0x25f
0x0000000000401123 <+29>:    mov    DWORD PTR [rbp-0x8],0x0
0x000000000040112a <+36>:    jmp    0x401136 <main+48>
0x000000000040112c <+38>:    mov    eax,DWORD PTR [rbp-0x8]
0x000000000040112f <+41>:    add    DWORD PTR [rbp-0x4],eax
0x0000000000401132 <+44>:    add    DWORD PTR [rbp-0x8],0x1
0x0000000000401136 <+48>:    mov    eax,DWORD PTR [rbp-0x8]
0x0000000000401139 <+51>:    cmp    eax,DWORD PTR [rbp-0xc]
0x000000000040113c <+54>:    jl     0x40112c <main+38>
0x000000000040113e <+56>:    mov    eax,DWORD PTR [rbp-0x4]
0x0000000000401141 <+59>:    pop    rbp
0x0000000000401142 <+60>:    ret
```

---

## **Step 2: Understanding the Code**
The main operations in the code are:

1. **Initialization**
   - `mov DWORD PTR [rbp-0x4], 0x1e0da` → Sets `rbp-0x4` (sum) to `0x1e0da` (123866 in decimal).
   - `mov DWORD PTR [rbp-0xc], 0x25f` → Sets `rbp-0xc` (iteration limit) to `0x25f` (607 in decimal).
   - `mov DWORD PTR [rbp-0x8], 0x0` → Sets `rbp-0x8` (loop counter `i`) to 0.

2. **Loop Execution**
   - The loop runs while `i < 607`.
   - At each iteration:
     - `eax = i`
     - `sum += i`
     - `i++`
   - This follows the formula for the sum of an arithmetic series:

     
     \[
     S = \sum_{i=0}^{606} i = \frac{606 \times 607}{2}
     \]

3. **Final Value of `eax`**
   - After exiting the loop, `eax` contains the final sum value stored in `rbp-0x4`.
   - The final sum is:

     ```
     S = 0x1e0da + (606 * 607) / 2
     ```

     ```
     S = 123866 + 184221 = 307019
     ```

---

## **Step 3: Extracting the Flag**
The flag format is `picoCTF{n}`, where `n` is the decimal value of `eax` at the end. Thus, the final flag is:

```
picoCTF{307019}
```

---

## **Summary of Execution**

1. Initialize `sum = 0x1E0DA = 123866`.
2. Loop from `i = 0` to `i = 606`:
   - Add `i` to `sum`.
   - Increment `i`.
3. Compute final sum: `307019`.
4. Flag: `picoCTF{307019}`.



