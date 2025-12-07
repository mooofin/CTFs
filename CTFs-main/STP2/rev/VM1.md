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
This opcode handler implements the VM’s ADD instruction. It operates on the VM stack by popping two 32-bit values, decrementing the stack pointer accordingly. The two values are added together, and the resulting sum is reduced using a modulo operation with 0x7fffffff to constrain it within a fixed range. The final value is then written back to the stack, and the stack pointer is updated to reflect the pushed result. SO add function . 

<img width="652" height="809" alt="image" src="https://github.com/user-attachments/assets/5a78b6ac-82ff-4197-94d4-4503f9e24eb4" />

This opcode implements the VM’s MUL instruction by popping two values from the stack, multiplying them. 


From here it's a manual work of identifying each OP codes so . fastforwaring to the next 23 more functions 

