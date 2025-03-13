

## Challenge Description



![Assembly Code](sandbox:/mnt/data/image.png)

## Analyzing the Code
### **Step 1: Stack Frame Setup**
1. `endbr64`: This is a security-related instruction for indirect branch tracking (not relevant here).
2. `push rbp`: Saves the previous base pointer.
3. `mov rbp, rsp`: Establishes a new stack frame.

### **Step 2: Variable Storage**
4. `mov DWORD PTR [rbp-0x14], edi`: Stores the value in `edi` (which is **20**) at memory location `[rbp-0x14]`.
5. `mov QWORD PTR [rbp-0x20], rsi`: Stores the value in `rsi` (which is **32**) at memory location `[rbp-0x20]`.
6. `mov DWORD PTR [rbp-0x4], 0x9fe1a`: Stores **0x9fe1a** (which is **654874** in decimal) at memory location `[rbp-0x4]`.

### **Step 3: Loading Value into `eax`**
7. `mov eax, DWORD PTR [rbp-0x4]`: Copies the value stored at `[rbp-0x4]` (which is **654874**) into `eax`.

### **Step 4: Function Cleanup**
8. `pop rbp`: Restores the old base pointer.
9. `ret`: Returns from the function with `eax = 654874`.

## Final Answer
The function ultimately returns **654874**, so the flag is:
```
picoCTF{654874}
```

