<img width="1918" height="1077" alt="image" src="https://github.com/user-attachments/assets/8eaf791e-1acf-43e9-b5a3-eb399c6481f2" />

This program is a **32-bit ARM binary**. This means it is meant to run on ARM systems and not on regular x86 machines, so it cannot be run directly. The binary is also **stripped**, meaning there are no useful function names, and it is **dynamically linked**. Even though it cannot be executed easily, running it is not required. Static analysis is enough to understand the logic and solve the challenge.

<img width="719" height="170" alt="image" src="https://github.com/user-attachments/assets/cc12c285-c423-4261-b4cf-6a6c4822f213" />

When the program starts, it prints a message and waits for user input. The input is read using the `read()` function. Instead of keeping the input as raw text, the program parses it into numbers and stores them contiguously in a heap-allocated buffer. These parsed values are later treated as fake registers for a custom virtual machine implemented by the binary.

<img width="690" height="364" alt="image" src="https://github.com/user-attachments/assets/35848f1e-cb63-4e04-b57b-7bb69be7b01e" />

After parsing the input, execution jumps into a function named `fcn.00008410`. This function works as the main VM interpreter. From this point onward, the program is no longer executing normal ARM instructions. Instead, it starts reading and executing VM bytecode stored as data inside the binary.

Each VM instruction is **4 bytes long**. The first byte is the opcode, which decides what operation to perform. The remaining three bytes are arguments. The opcode is used as an index into a jump table, which then jumps to the corresponding instruction handler.

The VM maintains its own execution state similar to a real CPU. It has its own registers, its own stack, and its own instruction pointer. Register index 30 is used as the stack pointer, while register index 31 stores the current VM instruction pointer.

By analyzing where the jump table leads and observing what each handler does, the VM instruction set can be identified. As the purpose of each handler becomes clear, they are renamed in radare2 to match their behavior. For example, one instruction was identified as a load lower immediate and renamed `LLi`.

<img width="823" height="725" alt="image" src="https://github.com/user-attachments/assets/cca78975-6f58-428a-8aad-c973ce39438d" />

Another similar instruction was identified as **Load Upper Immediate**.

<img width="913" height="973" alt="image" src="https://github.com/user-attachments/assets/0b8bf34c-1e5b-4afe-9e57-fc0ba556d6ee" />

The next instruction handled addition between values, and was renamed as `vm_add`.

<img width="837" height="773" alt="image" src="https://github.com/user-attachments/assets/0362481e-a096-4641-b0ca-c0cc0a0cdcf6" />

The next instruction took significantly more time to understand. Below is the full disassembly of the handler.

```bash
[0x00008624]> pdf
00: fcn.00008624 ();
│ afv: vars(5:sp[0xd..0x16])
│           0x00008624      0f305be5       ldrb r3, [var_fh]           ; 0xf ; 15
│           0x00008628      0320a0e1       mov r2, r3
│           0x0000862c      0e305be5       ldrb r3, [var_eh]           ; 0xe ; 14
│           0x00008630      0334a0e1       lsl r3, r3, 8
│           0x00008634      033082e1       orr r3, r2, r3
│           0x00008638      b6314be1       strh r3, [var_16h]          ; 0x16 ; 22
│           0x0000863c      14101be5       ldr r1, [var_14h]           ; 0x14 ; 20
│           0x00008640      0d305be5       ldrb r3, [var_dh]           ; 0xd ; 13
│           0x00008644      7f3003e2       and r3, r3, 0x7f
│           0x00008648      0321a0e1       lsl r2, r3, 2
│           0x0000864c      0c3091e5       ldr r3, [r1, 0xc]
│           0x00008650      033082e0       add r3, r2, r3
│           0x00008654      003093e5       ldr r3, [r3]
│           0x00008658      010053e3       cmp r3, 1                   ; 1
│       ┌─< 0x0000865c      1c00001a       bne 0x86d4
│       │   0x00008660      dd305be1       ldrsb r3, [var_dh]          ; 0xd ; 13
│       │   0x00008664      000053e3       cmp r3, 0
│      ┌──< 0x00008668      0b0000aa       bge 0x869c
│      ││   0x0000866c      14301be5       ldr r3, [var_14h]           ; 0x14 ; 20
│      ││   0x00008670      7c20a0e3       mov r2, 0x7c                ; '|'
│      ││   0x00008674      003093e5       ldr r3, [r3]
│      ││   0x00008678      031082e0       add r1, r2, r3
│      ││   0x0000867c      14301be5       ldr r3, [var_14h]           ; 0x14 ; 20
│      ││   0x00008680      7c20a0e3       mov r2, 0x7c                ; '|'
│      ││   0x00008684      003093e5       ldr r3, [r3]
│      ││   0x00008688      033082e0       add r3, r2, r3
│      ││   0x0000868c      003093e5       ldr r3, [r3]
│      ││   0x00008690      043083e2       add r3, r3, 4
│      ││   0x00008694      003081e5       str r3, [r1]
│     ┌───< 0x00008698      290000ea       b 0x8744
│     │││   ; CODE XREF from fcn.00008624 @ 0x8668(x)
│     │└──> 0x0000869c      14301be5       ldr r3, [var_14h]           ; 0x14 ; 20
│     │ │   0x000086a0      7c20a0e3       mov r2, 0x7c                ; '|'
│     │ │   0x000086a4      003093e5       ldr r3, [r3]
│     │ │   0x000086a8      030082e0       add r0, r2, r3
│     │ │   0x000086ac      14301be5       ldr r3, [var_14h]           ; 0x14 ; 20
│     │ │   0x000086b0      7c20a0e3       mov r2, 0x7c                ; '|'
│     │ │   0x000086b4      003093e5       ldr r3, [r3]
│     │ │   0x000086b8      031082e0       add r1, r2, r3
│     │ │   0x000086bc      f6315be1       ldrsh r3, [var_16h]         ; 0x16 ; 22
│     │ │   0x000086c0      0321a0e1       lsl r2, r3, 2
│     │ │   0x000086c4      003091e5       ldr r3, [r1]
│     │ │   0x000086c8      023083e0       add r3, r3, r2
│     │ │   0x000086cc      003080e5       str r3, [r0]
│     │┌──< 0x000086d0      1b0000ea       b 0x8744
│     │││   ; CODE XREF from fcn.00008624 @ 0x865c(x)
│     ││└─> 0x000086d4      dd305be1       ldrsb r3, [var_dh]          ; 0xd ; 13
│     ││    0x000086d8      000053e3       cmp r3, 0
│     ││┌─< 0x000086dc      0d0000aa       bge 0x8718
│     │││   0x000086e0      14301be5       ldr r3, [var_14h]           ; 0x14 ; 20
│     │││   0x000086e4      7c20a0e3       mov r2, 0x7c                ; '|'
│     │││   0x000086e8      003093e5       ldr r3, [r3]
│     │││   0x000086ec      030082e0       add r0, r2, r3
│     │││   0x000086f0      14301be5       ldr r3, [var_14h]           ; 0x14 ; 20
│     │││   0x000086f4      7c20a0e3       mov r2, 0x7c                ; '|'
│     │││   0x000086f8      003093e5       ldr r3, [r3]
│     │││   0x000086fc      031082e0       add r1, r2, r3
│     │││   0x00008700      f6315be1       ldrsh r3, [var_16h]         ; 0x16 ; 22
│     │││   0x00008704      0321a0e1       lsl r2, r3, 2
│     │││   0x00008708      003091e5       ldr r3, [r1]
│     │││   0x0000870c      023083e0       add r3, r3, r2
│     │││   0x00008710      003080e5       str r3, [r0]
│    ┌────< 0x00008714      0a0000ea       b 0x8744
│    ││││   ; CODE XREF from fcn.00008624 @ 0x86dc(x)
│    │││└─> 0x00008718      14301be5       ldr r3, [var_14h]           ; 0x14 ; 20
│    │││    0x0000871c      7c20a0e3       mov r2, 0x7c                ; '|'
│    │││    0x00008720      003093e5       ldr r3, [r3]
│    │││    0x00008724      031082e0       add r1, r2, r3
│    │││    0x00008728      14301be5       ldr r3, [var_14h]           ; 0x14 ; 20
│    │││    0x0000872c      7c20a0e3       mov r2, 0x7c                ; '|'
│    │││    0x00008730      003093e5       ldr r3, [r3]
│    │││    0x00008734      033082e0       add r3, r2, r3
│    │││    0x00008738      003093e5       ldr r3, [r3]
│    │││    0x0000873c      043083e2       add r3, r3, 4
│    │││    0x00008740      003081e5       str r3, [r1]
│    │││    ; CODE XREFS from fcn.00008624 @ 0x8698(x), 0x86d0(x), 0x8714(x)
│    └└└──> 0x00008744      0c00a0e3       mov r0, 0xc
│           0x00008748      0cd04be2       sub sp, fp, 0xc
└           0x0000874c      00a89de8       ldm sp, {fp, sp, pc}
...
```

This handler combines two bytes into a 16-bit value and then performs conditional logic based on comparisons. It checks whether a condition is met and updates the VM instruction pointer accordingly. Based on its behavior, this instruction appears to act like a **conditional jump**. However, it is still unclear whether this should strictly be labeled as `JE`, `JNE`, or a more generic conditional jump instruction.

After that, another instruction was identified which performs comparisons between values.

<img width="807" height="796" alt="image" src="https://github.com/user-attachments/assets/8531adb1-db6f-452f-b975-d7d90edb8316" />

The next instruction pushes values onto the VM stack.

<img width="833" height="812" alt="image" src="https://github.com/user-attachments/assets/48244433-89e2-4b31-be13-3663f7fd0cf9" />

This instruction pops values from the VM stack.

<img width="890" height="823" alt="image" src="https://github.com/user-attachments/assets/f409dddc-c0b5-4d86-aa5f-e0201eaee3d7" />

Another instruction performs subtraction between values.

<img width="852" height="744" alt="image" src="https://github.com/user-attachments/assets/c2f9934d-97fb-46ad-9b8e-bacd341f9b38" />

This instruction was more math-heavy and performs bit shifting operations before producing a result.

<img width="857" height="861" alt="image" src="https://github.com/user-attachments/assets/9c088e99-0d15-42c7-b5c5-759c171756bc" />

The next instruction performs an XOR operation.

<img width="859" height="730" alt="image" src="https://github.com/user-attachments/assets/269ec89c-d8ae-4676-9867-13d38aa897b7" />

Finally, this instruction does nothing and serves as a NOP.

<img width="857" height="606" alt="image" src="https://github.com/user-attachments/assets/866b648f-bf23-4709-95f5-ed04ab2731f7" />



After finally renaming all the VM instructions in radare2, I ended up with a clear structure of how the virtual machine works internally.

<img width="526" height="585" alt="image" src="https://github.com/user-attachments/assets/bb133f61-4aa6-4a51-9e3d-e57f5318c423" />

I also identified the main VM dispatcher, which is responsible for fetching each instruction, decoding the opcode, and jumping to the correct handler.

<img width="1887" height="930" alt="image" src="https://github.com/user-attachments/assets/065cdeb5-05e2-4f25-845f-8acff8550c11" />

Since the opcode handlers were already renamed and understood, I mapped out the full opcode table.

<img width="685" height="63" alt="image" src="https://github.com/user-attachments/assets/5cd0ae9b-ae6b-4596-8568-63569a457807" />

With this information, the extracted VM bytecode could now be mapped properly, because we know what each register represents and what each instruction does.

<img width="713" height="284" alt="image" src="https://github.com/user-attachments/assets/b82156c0-6f2d-4e91-b237-3df7b5f332f7" />

At this point, the next goal was figuring out how to convert this raw bytecode dump into readable pseudocode.

When the VM starts running, it first loads two constant values. One of them is `0x9e3779b9`, which is a well-known constant used in the TEA encryption algorithm. This immediately hints that some kind of encryption or mixing logic is involved.

<img width="603" height="269" alt="image" src="https://github.com/user-attachments/assets/aae098c2-50c5-43c6-91e6-bc26e0a0d2df" />

Instead of explaining everything line by line, the image below gives a clean high-level view of what the VM is actually doing.

<img width="761" height="476" alt="image" src="https://github.com/user-attachments/assets/4258c9a6-6c76-4355-a6f7-1407bca94bf8" />

In short, the program takes your input key and scrambles it using a small encryption-like routine that runs for 32 rounds. After all rounds are done, the final result is compared against two hardcoded secret values. If the values match, the key is accepted.












