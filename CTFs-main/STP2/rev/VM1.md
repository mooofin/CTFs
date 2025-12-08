### Binary Overview

Running `file` on the binary shows a standard ELF executable:

![file info](https://github.com/user-attachments/assets/045f0e79-743e-495b-bf71-e659cf48e529)

Nothing unusual here at first glance.


### Runtime Behavior

When executed, the binary asks for user input. Supplying anything incorrect leads to an immediate failure response, with no visible comparison or transformation in plaintext:

![runtime input](https://github.com/user-attachments/assets/22333440-13b2-45dc-b729-17359151a572)



Opening the binary in Binary Ninja reveals that the validation logic is **not normal control flow**. Instead, it looks like a **nested VM / emulator**, where execution is handled through multiple small functions acting like opcode handlers:

![vm view](https://github.com/user-attachments/assets/df9c875f-828a-4de1-9ef1-9524d25f782d)

Rather than direct comparisons, input seems to be processed through this interpreter.




Below the opcode-handling logic are several **hardcoded byte arrays** that resemble Base64-encoded data:

![b64 array 1](https://github.com/user-attachments/assets/fc80bc60-f72f-4c6a-8517-cd48512a9f04)

![b64 array 2](https://github.com/user-attachments/assets/3c5f69b1-5edd-4fee-8873-140500aa47a4)

These are likely VM data or encrypted constants consumed by the interpreter rather than decoded directly in native code.



The registers are 25 in count so we need to figure out the opcode for the instructions that the emulator will process.


Ill use radare 2 for finding what each of the instrucions mean ; 


<img width="579" height="606" alt="image" src="https://github.com/user-attachments/assets/f2ebfca8-6050-489a-ab95-aaac3d1af051" />

Before the virtual machine executes any bytecode, it initializes an opcode dispatch table. This is done through a helper function (fcn.00001238), which is repeatedly called during VM setup.

<img width="840" height="870" alt="image" src="https://github.com/user-attachments/assets/7c3bcd85-f42f-484b-b555-34cfdd51cc92" />

In my best attempts this would be like 

```c
entry = calloc(1, sizeof(opcode_entry));
entry->opcode = opcode;
entry->handler = handler;

bucket = opcode_table[hash(opcode)];
entry->next = bucket;
opcode_table[hash(opcode)] = entry;

```

It seems like it is indeed the dispatcher for the architecture 

<img width="776" height="966" alt="image" src="https://github.com/user-attachments/assets/10311753-cc48-4357-a730-67b8a7a235d6" />


After allocating the opcode table, the program registers every VM instruction by pairing:

an encoded opcode value (32-bit constant in edi) ,a handler function (function pointer in rsi)

So i'll move onto the next function here which is 

```bash
[0x00001d44]> s 0x000014cd
[0x000014cd]> pdf
ERROR: Cannot find function at 0x000014cd
[0x000014cd]> af
[0x000014cd]> pdf
            ; DATA XREF from main @ 0x1dde(r)
┌ 195: fcn.000014cd (int64_t arg1);
│ `- args(rdi) vars(3:sp[0xc..0x20])
│           0x000014cd      55             push rbp
│           0x000014ce      4889e5         mov rbp, rsp
│           0x000014d1      48897de8       mov qword [var_18h], rdi    ; arg1
│           0x000014d5      488b45e8       mov rax, qword [var_18h]
│           0x000014d9      488b10         mov rdx, qword [rax]
│           0x000014dc      488b45e8       mov rax, qword [var_18h]
│           0x000014e0      8b4038         mov eax, dword [rax + 0x38]
│           0x000014e3      4898           cdqe
│           0x000014e5      48c1e002       shl rax, 2
│           0x000014e9      4801d0         add rax, rdx
│           0x000014ec      8b00           mov eax, dword [rax]
│           0x000014ee      8945fc         mov dword [var_4h], eax
│           0x000014f1      488b45e8       mov rax, qword [var_18h]
│           0x000014f5      8b4038         mov eax, dword [rax + 0x38]
│           0x000014f8      8d50ff         lea edx, [rax - 1]
│           0x000014fb      488b45e8       mov rax, qword [var_18h]
│           0x000014ff      895038         mov dword [rax + 0x38], edx
│           0x00001502      488b45e8       mov rax, qword [var_18h]
│           0x00001506      488b10         mov rdx, qword [rax]
│           0x00001509      488b45e8       mov rax, qword [var_18h]
│           0x0000150d      8b4038         mov eax, dword [rax + 0x38]
│           0x00001510      4898           cdqe
│           0x00001512      48c1e002       shl rax, 2
│           0x00001516      4801d0         add rax, rdx
│           0x00001519      8b00           mov eax, dword [rax]
│           0x0000151b      8945f8         mov dword [var_8h], eax
│           0x0000151e      488b45e8       mov rax, qword [var_18h]
│           0x00001522      8b4038         mov eax, dword [rax + 0x38]
│           0x00001525      8d50ff         lea edx, [rax - 1]
│           0x00001528      488b45e8       mov rax, qword [var_18h]
│           0x0000152c      895038         mov dword [rax + 0x38], edx
│           0x0000152f      488b45e8       mov rax, qword [var_18h]
│           0x00001533      8b4038         mov eax, dword [rax + 0x38]
│           0x00001536      8d5001         lea edx, [rax + 1]
│           0x00001539      488b45e8       mov rax, qword [var_18h]
│           0x0000153d      895038         mov dword [rax + 0x38], edx
│           0x00001540      8b55fc         mov edx, dword [var_4h]
│           0x00001543      8b45f8         mov eax, dword [var_8h]
│           0x00001546      8d0c02         lea ecx, [rdx + rax]
│           0x00001549      488b45e8       mov rax, qword [var_18h]
│           0x0000154d      488b10         mov rdx, qword [rax]
│           0x00001550      488b45e8       mov rax, qword [var_18h]
│           0x00001554      8b4038         mov eax, dword [rax + 0x38]
│           0x00001557      4898           cdqe
│           0x00001559      48c1e002       shl rax, 2
│           0x0000155d      488d3402       lea rsi, [rdx + rax]
│           0x00001561      4863d1         movsxd rdx, ecx
│           0x00001564      4889d0         mov rax, rdx
│           0x00001567      48c1e01e       shl rax, 0x1e
│           0x0000156b      4801d0         add rax, rdx
│           0x0000156e      48c1e820       shr rax, 0x20
│           0x00001572      89c2           mov edx, eax
│           0x00001574      c1fa1d         sar edx, 0x1d
│           0x00001577      89c8           mov eax, ecx
│           0x00001579      c1f81f         sar eax, 0x1f
│           0x0000157c      29c2           sub edx, eax
│           0x0000157e      89d0           mov eax, edx
│           0x00001580      89c2           mov edx, eax
│           0x00001582      c1e21f         shl edx, 0x1f
│           0x00001585      29c2           sub edx, eax
│           0x00001587      89c8           mov eax, ecx
│           0x00001589      29d0           sub eax, edx
│           0x0000158b      8906           mov dword [rsi], eax
│           0x0000158d      90             nop
│           0x0000158e      5d             pop rbp
└           0x0000158f      c3             ret
```
This opcode handler implements the VM’s ADD instruction. It operates on the VM stack by popping two 32-bit values, decrementing the stack pointer accordingly. The two values are added together, and the resulting sum is reduced using a modulo operation with 0x7fffffff to constrain it within a fixed range. 

After identifying the VM structure, the next step is manually identifying each opcode handler (would not reccomend) 


We backtrack to the first opcode registration point:

```asm
s 0x00001dde
```

## MUL Opcode

This instruction pops two values from the VM stack, multiplies them, applies modulo `0x7fffffff`, and pushes the result back onto the stack.

![MUL](https://github.com/user-attachments/assets/5a78b6ac-82ff-4197-94d4-4503f9e24eb4)

---

## XOR Opcode

```
Opcode: 0x48c5ccc6  
Handler: 0x00001438
```

The XOR instruction pops two values from the stack, performs a bitwise XOR, and pushes the result back.
Unlike other arithmetic operations, XOR does **not** apply modulo.

![XOR](https://github.com/user-attachments/assets/908da7f2-c71c-415e-8f35-9cba4a3a6a65)

---

## AND Opcode

```
Opcode: 0x542010a0  
Handler: 0x00001590
```

Performs bitwise AND between two stack values and pushes the result.

![AND](https://github.com/user-attachments/assets/a308a294-587a-4047-8aec-5abd66199b8a)

---

## RET Opcode

```
Opcode: 0xbdecfe55  
Handler: 0x000017bb
```

Returns from a VM function by restoring the program counter from the Link Register (LR).

![RET](https://github.com/user-attachments/assets/7b61d34d-f73e-438b-b567-099e143a4a4a)

---

## ABORT Opcode

```
Opcode: 0x41f93b4b  
Handler: 0x000017d4
```

Immediately terminates execution by calling `exit(1)`.
Used for invalid execution paths.

![ABORT](https://github.com/user-attachments/assets/d065fb47-827b-4cc7-9c00-255dae69fa21)

---

## PUSH_IMM Opcode

```
Handler: 0x000017ea
```

Pushes a 32-bit immediate value (fetched from ROM) onto the VM stack.

![PUSH\_IMM](https://github.com/user-attachments/assets/0ac161da-17f5-4fc1-a85c-1a5675452559)

---

## JZ (Jump if Equal)

```
Opcode: 0x180bc12d  
Handler: 0x00001866
```

Pops two values from the stack.
If they are equal, the program counter is adjusted using a signed immediate offset.

![JZ](https://github.com/user-attachments/assets/7a0712a2-f6fb-4459-aa35-83f44be8d74f)

---

## JNZ (Jump if Not Equal)

```
Opcode: 0x5a0f38fc  
Handler: 0x000018f9
```

Pops two values from the stack.
If they are **not** equal, PC is updated by a signed immediate offset.

![JNZ](https://github.com/user-attachments/assets/f7ae199b-444a-4ae7-abc3-9fef92f33e15)

---

## FAIL Opcode

```
Opcode: 0x27497906  
Handler: 0x0000198c
```

Another hard failure instruction that immediately exits the program.

![FAIL](https://github.com/user-attachments/assets/550f0ca8-0053-4f12-8fab-46bbef4b2725)

---

## SET_MEMPTR Opcode

```
Opcode: 0xba1116a9  
Handler: 0x000019a2
```

Updates the VM memory pointer, used for subsequent memory read/write instructions.

![SET\_MEMPTR](https://github.com/user-attachments/assets/2d1bf26d-de93-4d80-a445-8f94800173f6)

---

## CALL Opcode

```
Opcode: 0xfa83fa5e  
Handler: 0x000019de
```

Stores the current PC into the Link Register (LR) and jumps to a new address.

![CALL](https://github.com/user-attachments/assets/71663722-a784-4b29-bcae-ddb9d24c5309)

---

## HALT Opcode

```
Opcode: 0x818cd6b5  
Handler: 0x00001a1d
```

Sets the exit code and terminates VM execution cleanly.

![HALT](https://github.com/user-attachments/assets/d9659e0e-1b82-4620-9dab-e8d34179e6a3)

---

## LOAD_REG Opcode

```
Opcode: 0x8d67bae1  
Handler: 0x00001a64
```

Loads a 32-bit value from ROM into a register.

![LOAD\_REG](https://github.com/user-attachments/assets/da5d0f84-9458-44df-a390-e047d621503b)

---

## PUTCHAR Opcode

```
Opcode: 0xd1450d67  
Handler: 0x00001abf
```

Outputs a character using `putchar()` and sets the VM `PUT_FLAG`.

![PUTCHAR](https://github.com/user-attachments/assets/8d25fd9a-1d96-4e0e-bb36-3bc244f0b94d)

---

## INC / DEC Register Opcodes

### INC

```
Handler: 0x00001b03
```

![INC](https://github.com/user-attachments/assets/b5efc681-ad4f-4045-b91f-1ea4bc737550)

### DEC

```
Handler: 0x00001b46
```

![DEC](https://github.com/user-attachments/assets/c4b7dfbd-68fc-4920-bb3a-5022570ec6b2)

---

## MOD Opcode

```
Handler: 0x00001724
```

Performs modulo operation using a register and pushes the result onto the stack.

![MOD](https://github.com/user-attachments/assets/579d41d8-d2c0-46ec-b249-35fbdd6d3f5a)

---

## POP_REG Opcode

```
Handler: 0x00001be5
```

Pops a value from the stack into a register.

![POP\_REG](https://github.com/user-attachments/assets/a7553de8-b589-4f85-b2df-c38d06f59df5)

---

## SET_MEM_PTR Opcode

```
Handler: 0x00001c41
```

Adjusts internal VM memory pointers.

![SET\_MEM\_PTR](https://github.com/user-attachments/assets/bd1d0a5c-acbc-48b5-8af2-c6a25670f9aa)

---

## MEMSTORE Opcode

```
Handler: 0x00001ca4
```

Stores a register value into VM memory at `VM_MEM_PTR`.

![MEMSTORE](https://github.com/user-attachments/assets/b2640f51-dd28-4533-b55d-3c9fb82ff527)

---

## MEMFETCH Opcode

```
Handler: 0x00001cf7
```

Loads a value from VM memory into a register.

![MEMFETCH](https://github.com/user-attachments/assets/6f56d714-437f-4725-9b09-e14cd8820a4b)


TO put it simply here's the functioning of the VM 

<img width="709" height="388" alt="image" src="https://github.com/user-attachments/assets/d1081542-ade3-4c9e-8977-92a7e21b7af3" />








