# **Reverse Engineering `asm1` – CTF Writeup**  

## **Overview**  
In this challenge, we analyze an assembly function `asm1` that performs conditional checks and arithmetic operations on an input value. Our goal is to determine the **final return value**, convert it to **hexadecimal**, and obtain the flag.

---

## **Assembly Code Breakdown**
The function operates as follows:

### **Initial Setup**
```assembly
 <+0>:  push   ebp   
 <+1>:  mov    ebp, esp   ; Set up stack frame
```
- The function **saves the base pointer (`ebp`)** and sets it up for stack operations.

### **Comparisons and Jumps**
```assembly
 <+3>:   cmp    DWORD PTR [ebp+0x8], 0x3fb   ; Compare argument with 1019
 <+10>:  jg     0x512 <asm1+37>   ; Jump if greater
```
- If the input value **is greater than 1019 (`0x3FB`)**, jump to `<asm1+37>`.
- Otherwise, continue execution.

```assembly
 <+12>:  cmp    DWORD PTR [ebp+0x8], 0x280  ; Compare argument with 640
 <+19>:  jne    0x50a <asm1+29>   ; Jump if not equal
```
- If the value **is not 640 (`0x280`)**, jump to `<asm1+29>`.
- Otherwise, continue execution.

### **Execution Paths**
#### **Path 1: If Input == 640**
```assembly
 <+21>:  mov    eax, DWORD PTR [ebp+0x8]
 <+24>:  add    eax, 0xa  ; Add 10 to input
 <+27>:  jmp    0x529 <asm1+60>
```
- If the input **is 640**, the function returns `640 + 10 = 650`.

#### **Path 2: If Input ≠ 640 (Default Path)**
```assembly
 <+29>:  mov    eax, DWORD PTR [ebp+0x8]  ; eax = input (736)
 <+32>:  sub    eax, 0xa   ; Subtract 10 from input (736 - 10 = 726)
 <+35>:  jmp    0x529 <asm1+60>
```
- If the input **is 736**, it follows this path and returns **726**.

#### **Final Steps**
```assembly
 <+60>:  pop    ebp  ; Restore stack
 <+61>:  ret    ; Return value stored in eax
```
- The function **returns 726**.

---

## **Flag Extraction**
Since the **final return value is 726**, the flag is its **hexadecimal representation**:

```python
hex(726)  # Convert to hex
```
Result:
```
0x2D6
```

### **Final Flag**
```
picoCTF{0x2D6}
```

---

## **Summary**
- The function takes an **input argument**.
- If the input **isn't 640**, it takes the default execution path.
- With an input of **736**, it **subtracts 10** and returns **726**.
- Converting `726` to **hexadecimal** gives `0x2D6`, which is the **flag**.
