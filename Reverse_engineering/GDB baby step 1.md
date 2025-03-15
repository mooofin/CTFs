# Debugging and Extracting EAX Register Value

## **Challenge Overview**
The task is to determine the value of the `eax` register at the end of the `main` function and submit it in the PicoCTF flag format: `picoCTF{n}`, where `n` is the decimal representation of `eax`.

## **Disassembling the Binary**
We begin by running `gdb` on the binary `debugger0_a` to analyze the function `main`.

### **1. Load the binary in GDB**
```bash
$ gdb debugger0_a
```
Since there are no debugging symbols, we proceed by checking the available functions.

### **2. List Functions**
```bash
(gdb) info functions
```
Output:
```
Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001030  __cxa_finalize@plt
0x0000000000001040  _start
0x0000000000001070  deregister_tm_clones
0x00000000000010a0  register_tm_clones
0x00000000000010e0  __do_global_dtors_aux
0x0000000000001120  frame_dummy
0x0000000000001129  main
0x0000000000001140  __libc_csu_init
0x00000000000011b0  __libc_csu_fini
0x00000000000011b8  _fini
```

### **3. Set Intel Assembly Syntax**(because  GDB uses AT&T by default, so we need to convert it to intel)
```bash
(gdb) set disassembly-flavor intel
```

### **4. Disassemble `main`**
```bash
(gdb) disassemble main
```
Output:
```
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   rbp
   0x000000000000112e <+5>:     mov    rbp,rsp
   0x0000000000001131 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000001134 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000001138 <+15>:    mov    eax,0x86342
   0x000000000000113d <+20>:    pop    rbp
   0x000000000000113e <+21>:    ret
End of assembler dump.
```

## **Analyzing the Assembly Code**
### **Step-by-Step Execution**
1. `endbr64` - Security instruction (not relevant to eax).
2. `push rbp` - Saves the base pointer.
3. `mov rbp,rsp` - Sets up the stack frame.
4. `mov DWORD PTR [rbp-0x4],edi` - Stores `edi` value (not affecting eax).
5. `mov QWORD PTR [rbp-0x10],rsi` - Stores `rsi` value (not affecting eax).
6. `mov eax,0x86342` - **Sets `eax` to `0x86342` (548674 in decimal).**
7. `pop rbp` - Restores the base pointer.
8. `ret` - Returns from `main`, with `eax` still holding `0x86342`.

## **Extracting the Flag**
The final value of `eax` is `0x86342`, which is **548674** in decimal. Thus, the flag is:
```plaintext
picoCTF{548674}
