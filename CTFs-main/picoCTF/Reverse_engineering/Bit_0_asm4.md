## Assembly Code Analysis

### **Disassembly of `main` Function**

```assembly
<+0>:     endbr64  // 
<+4>:     push   rbp  // moves into rbp 
<+5>:     mov    rbp,rsp  // move into rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi  // edi = rbp-0x14
<+11>:    mov    QWORD PTR [rbp-0x20],rsi  // rsi = rbp-0x20
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a  // 654874 = rbp=0x4
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710  // compare with 10000
<+29>:    jle    0x55555555514e <main+37>  // will not jump 
<+31>:    sub    DWORD PTR [rbp-0x4],0x65  // subtract 101 (654773)
<+35>:    jmp    0x555555555152 <main+41>  // jump to +41
<+37>:    add    DWORD PTR [rbp-0x4],0x65  
<+41>:    mov    eax,DWORD PTR [rbp-0x4]  // move it to eax 
<+44>:    pop    rbp  
<+45>:    ret  // return ? 
```

### **Explanation**

#### **Function Prologue**
- `<+0>: endbr64` → This is an indirect branch protection instruction (Intel CET).
- `<+4>: push rbp` → Saves the base pointer of the previous stack frame.
- `<+5>: mov rbp, rsp` → Sets up the new stack frame.

#### **Variable Assignments**
- `<+8>: mov DWORD PTR [rbp-0x14], edi` → Stores `edi` (a function argument) into `[rbp-0x14]`.
- `<+11>: mov QWORD PTR [rbp-0x20], rsi` → Stores `rsi` (another argument) into `[rbp-0x20]`.
- `<+15>: mov DWORD PTR [rbp-0x4], 0x9fe1a` → Stores `654874` into `[rbp-0x4]`.

#### **Comparison and Conditional Jump**
- `<+22>: cmp DWORD PTR [rbp-0x4], 0x2710` → Compares `654874` with `10000`.
- `<+29>: jle 0x55555555514e <main+37>` → `JLE` (Jump if Less or Equal) will **not jump** because `654874 > 10000`.

#### **Subtraction and Unconditional Jump**
- `<+31>: sub DWORD PTR [rbp-0x4], 0x65` → Subtracts `101`, making the value `654773`.
- `<+35>: jmp 0x555555555152 <main+41>` → Jumps to instruction at `<+41>`.

#### **Alternative Path (Skipped Due to Jump)**
- `<+37>: add DWORD PTR [rbp-0x4], 0x65` → This is **not executed** because of the jump at `<+35>`.

#### **Return Value Setup**
- `<+41>: mov eax, DWORD PTR [rbp-0x4]` → Moves `654773` into `eax` (return value).
- `<+44>: pop rbp` → Restores old base pointer.
- `<+45>: ret` → Returns to the caller.

### **Key Takeaways**
- The function assigns `654874` to a local variable and checks if it's ≤ `10000`.
- Since the condition fails, it subtracts `101` (`0x65`) from `654874`, resulting in `654773`.
- The function returns `654773` (`0x9FDB5`).
