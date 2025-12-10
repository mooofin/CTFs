

Running `file` on the binary shows a standard ELF executable:

![file info](https://github.com/user-attachments/assets/045f0e79-743e-495b-bf71-e659cf48e529)

Nothing unusual here 




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

 MUL Opcode

This instruction pops two values from the VM stack, multiplies them, applies modulo `0x7fffffff`, and pushes the result back onto the stack.

![MUL](https://github.com/user-attachments/assets/5a78b6ac-82ff-4197-94d4-4503f9e24eb4)

---

 XOR Opcode

```
Opcode: 0x48c5ccc6  
Handler: 0x00001438
```

The XOR instruction pops two values from the stack, performs a bitwise XOR, and pushes the result back.
Unlike other arithmetic operations, XOR does **not** apply modulo.

![XOR](https://github.com/user-attachments/assets/908da7f2-c71c-415e-8f35-9cba4a3a6a65)

---

 AND Opcode

```
Opcode: 0x542010a0  
Handler: 0x00001590
```

Performs bitwise AND between two stack values and pushes the result.

![AND](https://github.com/user-attachments/assets/a308a294-587a-4047-8aec-5abd66199b8a)

---

 RET Opcode

```
Opcode: 0xbdecfe55  
Handler: 0x000017bb
```

Returns from a VM function by restoring the program counter from the Link Register (LR).

![RET](https://github.com/user-attachments/assets/7b61d34d-f73e-438b-b567-099e143a4a4a)

---

 ABORT Opcode

```
Opcode: 0x41f93b4b  
Handler: 0x000017d4
```

Immediately terminates execution by calling `exit(1)`.
Used for invalid execution paths.

![ABORT](https://github.com/user-attachments/assets/d065fb47-827b-4cc7-9c00-255dae69fa21)

---

 PUSH_IMM Opcode

```
Handler: 0x000017ea
```

Pushes a 32-bit immediate value (fetched from ROM) onto the VM stack.

![PUSH\_IMM](https://github.com/user-attachments/assets/0ac161da-17f5-4fc1-a85c-1a5675452559)

---

 JZ (Jump if Equal)

```
Opcode: 0x180bc12d  
Handler: 0x00001866
```

Pops two values from the stack.
If they are equal, the program counter is adjusted using a signed immediate offset.

![JZ](https://github.com/user-attachments/assets/7a0712a2-f6fb-4459-aa35-83f44be8d74f)

---

 JNZ (Jump if Not Equal)

```
Opcode: 0x5a0f38fc  
Handler: 0x000018f9
```

Pops two values from the stack.
If they are **not** equal, PC is updated by a signed immediate offset.

![JNZ](https://github.com/user-attachments/assets/f7ae199b-444a-4ae7-abc3-9fef92f33e15)

---

 FAIL Opcode

```
Opcode: 0x27497906  
Handler: 0x0000198c
```

Another hard failure instruction that immediately exits the program.

![FAIL](https://github.com/user-attachments/assets/550f0ca8-0053-4f12-8fab-46bbef4b2725)

---

 SET_MEMPTR Opcode

```
Opcode: 0xba1116a9  
Handler: 0x000019a2
```

Updates the VM memory pointer, used for subsequent memory read/write instructions.

![SET\_MEMPTR](https://github.com/user-attachments/assets/2d1bf26d-de93-4d80-a445-8f94800173f6)

---

 CALL Opcode

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

 INC / DEC Register Opcodes

 INC

```
Handler: 0x00001b03
```

![INC](https://github.com/user-attachments/assets/b5efc681-ad4f-4045-b91f-1ea4bc737550)

 DEC

```
Handler: 0x00001b46
```

![DEC](https://github.com/user-attachments/assets/c4b7dfbd-68fc-4920-bb3a-5022570ec6b2)

---

 MOD Opcode

```
Handler: 0x00001724
```

Performs modulo operation using a register and pushes the result onto the stack.

![MOD](https://github.com/user-attachments/assets/579d41d8-d2c0-46ec-b249-35fbdd6d3f5a)

---

 POP_REG Opcode

```
Handler: 0x00001be5
```

Pops a value from the stack into a register.

![POP\_REG](https://github.com/user-attachments/assets/a7553de8-b589-4f85-b2df-c38d06f59df5)

---

 SET_MEM_PTR Opcode

```
Handler: 0x00001c41
```

Adjusts internal VM memory pointers.

![SET\_MEM\_PTR](https://github.com/user-attachments/assets/bd1d0a5c-acbc-48b5-8af2-c6a25670f9aa)

---

 MEMSTORE Opcode

```
Handler: 0x00001ca4
```

Stores a register value into VM memory at `VM_MEM_PTR`.

![MEMSTORE](https://github.com/user-attachments/assets/b2640f51-dd28-4533-b55d-3c9fb82ff527)

---

 MEMFETCH Opcode

```
Handler: 0x00001cf7
```

Loads a value from VM memory into a register.

![MEMFETCH](https://github.com/user-attachments/assets/6f56d714-437f-4725-9b09-e14cd8820a4b)


TO put it simply here's the functioning of the VM 

<img width="709" height="388" alt="image" src="https://github.com/user-attachments/assets/d1081542-ade3-4c9e-8977-92a7e21b7af3" />







After that i came across this article which was a very embedded emulator type VM which has also very much OP codes ;
[https://miasm.re/blog/2016/09/03/zeusvm_analysis.html](https://miasm.re/blog/2016/09/03/zeusvm_analysis.html)



### WHy miasm ??

Miasm helps automate this process. After instructions are converted to IR, Miasm can symbolically execute them, meaning it treats inputs as unknown variables and follows all possible program paths automatically.

In this challenge, the binary does not directly compare user input. Instead, it runs everything inside a custom VM. Traditional tools struggle here because they do not understand the VM’s instruction set.

By implementing this VM as a custom architecture in Miasm, the VM bytecode can be executed symbolically instead of manually emulated. Miasm automatically tracks relationships between registers, stack values, and memory, and generates constraints on user input. These constraints can then be solved using SMT solvers.


So after reading some guides u need to make some files for misam , which like in the diagram below

![miasm vm architecture layout](https://github.com/user-attachments/assets/b50939b3-d433-4ca0-b085-46ff8b62b4a8)



the `regs.py` file is used to define the VM registers, `arch.py` ties the architecture together and describes basic properties like the program counter, and `sem.py` defines the actual semantics of each VM instruction

I first needed the bytecode that the VM actually executes, because the main binary never runs it directly on the CPU. The program decodes some Base64 data at runtime and then passes the decoded result to the VM as its instruction stream. Instead of trying to analyze everything at once, I focused on grabbing this decoded data and saving it as a raw binary file. This became the input for Miasm. For the later VM layers, the VM itself loads another bytecode buffer from a ROM-like area in its memory, so I reused those unpacked buffers as well.  


Once I had the custom VM architecture wired up in Miasm, the next step was actually getting a disassembler working for the bytecode. I am not a Miasm wizard, so I did the simple thing: I read through the original writeup and kept Miasm’s own blog open as a reference, especially their “Playing with dynamic symbolic execution” article, just to understand how they build CFGs and IR and then simplify them:
https://miasm.re/blog/2017/10/05/playing_with_dynamic_symbolic_execution.html#enhancing-coverage-breaking-a-crackme
Using that as a guide, I wrote a small Python script that feeds the VM bytecode into Miasm’s Machine("vmv"), walks over all the basic blocks, looks for simple patterns like PUSH_REG; PUSH_IMM; JE to recover opcode values, and then saves out the control flow and simplified IR as .dot graphs. It is basically a hacked-together disassembler pass that does just enough for this challenge: discover opcodes for each nesting level, teach Miasm about them, then spit out IR I can actually reason about instead of staring at raw 32 bit words.


```python

from collections import defaultdict
import struct
import subprocess

from miasm.analysis.machine import Machine
from miasm.analysis.simplifier import (
    IRCFGSimplifierCommon,
    IRCFGSimplifierSSA,
)
from miasm.core.locationdb import LocationDB
from miasm.core.utils import ExprInt

from miasm.arch.vmv.regs import *
from miasm.arch.vmv.arch import *
import miasm.arch.vmv.arch as arch_vmv


#
# Dispatcher offsets -> semantic opcode mapping
# These offsets are stable across VM layers.
#
vm_handler_map = {
    0xcb8: ("EXIT_REG",      reg_idx),
    0xbcc: ("DEC",           reg_idx),
    0xd70: ("RET",),
    0x6e8: ("MEMFETCH",      reg_idx),
    0xcd8: ("CALL",          imm32),
    0x358: ("PUTCHAR_REG",   reg_idx),
    0x444: ("JMP",           imm32),
    0x980: ("XOR",),
    0x8fc: ("MUL",),
    0x770: ("AND",),
    0xb68: ("INC",           reg_idx),
    0x4ac: ("JE",            imm32),
    0x67c: ("MEMSTORE",      reg_idx),
    0x878: ("ADD",),
    0x380: ("PUSH_IMM",      imm32),
    0x3f0: ("ROMFETCH",      reg_idx),
    0x3b0: ("PUSH_REG",      reg_idx),
    0x594: ("JNE",           imm32),
    0xa04: ("PUTCHAR_IMM",   putchar_imm32),
    0xa44: ("EXIT_IMM",      imm32),
    0xa54: ("MEMSHIFT_IMM",  imm32),
    0xaa0: ("MEMSHIFT_REG",  reg_idx),
    0xafc: ("POP",           reg_idx),
    0xc30: ("MOD",           reg_idx),
}


def dump_cfg(cfg, path):
    """Dump CFG/IR to .dot and render it using graphviz."""
    with open(path, "w") as f:
        f.write(cfg.dot())

    subprocess.call([
        "dot", "-Tpng",
        path,
        "-o", path.replace(".dot", ".png"),
    ])


#
# Opcode discovery logic
#
def vm_opcode_probe(mdis, block, _):
    """Inspect VM basic blocks for dispatcher patterns."""

    # Dispatcher entry:
    #   PUSH_REG
    #   PUSH_IMM <opcode>
    #   JE <handler>
    #
    lines = block.lines
    if (
        len(lines) == 3
        and lines[0].name == "PUSH_REG"
        and lines[1].name == "PUSH_IMM"
        and lines[2].name == "JE"
    ):
        imm = lines[1].args[0]
        dst = lines[2].args[0]

        if isinstance(imm, ExprInt):
            opcode = int(imm.arg)
            handler = mdis.loc_db.get_location_offset(dst.loc_key)
            vm_opcodes[opcode] = handler

    #
    # VM layer init block (xor constants)
    #
    if mdis.loc_db.get_location_offset(block.loc_key) == 0xe8:
        arch_vmv.putchar_xorlist.append(
            int(lines[0].args[0]) & 0xff
        )
        arch_vmv.reg_xorlist.append(
            int(lines[2].args[0]) & 0xff
        )


def register_vm_opcodes(opcodes, level):
    """Register decoded opcode values into Miasm."""
    print(f"\n[vm{level}] registering opcodes")

    for opcode, handler_off in opcodes.items():
        name_def = vm_handler_map[handler_off]
        mnemonic = name_def[0]
        operands = name_def[1:] if len(name_def) > 1 else []

        print(f"  {hex(opcode)} -> {mnemonic}")

        if operands:
            addop(mnemonic, [bs32(opcode), operands[0]])
        else:
            addop(mnemonic, [bs32(opcode)])


#
# Bytecode loader
#
def load_vm_bytecodes():
    """Load initial and nested VM bytecode blobs."""
    blobs = []

    with open("vmv_bytecode.bin", "rb") as f:
        blobs.append(f.read())

    with open("vmv_nested_bytecode.bin", "rb") as f:
        while True:
            hdr = f.read(4)
            if not hdr:
                break

            count = struct.unpack("<I", hdr)[0]
            blobs.append(f.read(count * 4))

    return blobs


#
# Main analysis loop
#
machine = Machine("vmv")
bytecodes = load_vm_bytecodes()

print(f"[+] detected {len(bytecodes)} VM layers")

results = []
entry = 0x0

for level, bc in enumerate(bytecodes, start=1):
    print(f"[vm{level}] bytecode size: {len(bc) // 4:#x}")

    vm_opcodes = defaultdict(int)
    loc_db = LocationDB()

    mdis = machine.dis_engine(bc, loc_db=loc_db)
    mdis.dis_block_callback = vm_opcode_probe

    asmcfg = mdis.dis_multiblock(entry)
    results.append((loc_db, asmcfg))

    dump_cfg(
        asmcfg,
        f"output/vmv_asmcfg{level}.dot"
    )

    arch_vmv.nest_level += 1

    if len(vm_opcodes) == 24:
        register_vm_opcodes(vm_opcodes, level)


#
# IR lifting (final VM layer)
#
nl = 4
loc_db, asmcfg = results[nl]

ira = machine.ira(loc_db)
ircfg = ira.new_ircfg_from_asmcfg(asmcfg)

dump_cfg(ircfg, f"output/vmv_ircfg{nl + 1}.dot")

entry_loc = loc_db.get_offset_location(entry)

simp = IRCFGSimplifierCommon(ira)
simp.simplify(ircfg, entry_loc)
dump_cfg(ircfg, f"output/vmv_ircfg_simp_common{nl + 1}.dot")

simp = IRCFGSimplifierSSA(ira)
simp.simplify(ircfg, entry_loc)
dump_cfg(ircfg, f"output/vmv_ircfg_simp_ssa{nl + 1}.dot")


```
At some point while trying to hook my VM into Miasm, I ran into this error saying that miasm.arch.vmv.jit did not contain something called jitter_vmv. After some digging, I realized this wasn’t actually a VM bug but a Miasm integration issue. When Miasm loads a new architecture through machine.py, it assumes that a JIT (Just-In-Time execution) backend exists and tries to import it automatically. In my case, vmv/jit.py turned out to be completely empty, so there was nothing named jitter_vmv to import. Since my disassembly and analysis pipeline never used the JIT at all, the simplest fix was to remove the JIT-related import lines for vmv inside machine.py. This effectively told Miasm that the vmv architecture does not support JIT execution, which was totally fine for static disassembly and IR lifting.

After fixing the JIT issue, Miasm failed again, this time complaining about a missing LifterModelCallVmv class in vmv/ira.py. This was another case of Miasm expecting a conventionally named class without checking whether it actually existed. I opened vmv/ira.py and found that it instead defined classes named ir_a_vmv_base and ir_a_vmv. Based on the existing Miasm architectures and how the lifter is usually named, it was clear that ir_a_vmv was the correct lifter to use. To fix this, I updated the vmv branch in machine.py to import ir_a_vmv instead of LifterModelCallVmv. Once this change was made, Miasm could successfully lift VM instructions into IR without looking for non-existent classes

With my knowledge , ill try to summarise how jitter the execution layer works :( 

Miasm has a component called **Jitter**, which is used to *execute* instructions after they have been translated into Miasm’s intermediate representation (IR). You can think of Jitter as a simple emulator that understands IR instead of raw machine code. It keeps track of things like registers, memory, and the current instruction pointer, and then steps through instructions one by one.

At the core of this system is a generic `Jitter` class, which provides common execution logic that works the same for every architecture. On top of that, Miasm defines architecture-specific subclasses such as `jitter_x86_64`, `jitter_arm`, or `jitter_mips32`. Each of these subclasses explains how instructions for that particular CPU should behave at runtime. This is why Miasm’s documentation shows a large inheritance diagram: many different architectures all extend the same base Jitter class.


<img width="1408" height="711" alt="image" src="https://github.com/user-attachments/assets/fe3b2f8c-c18d-4408-a56b-b102a13b3c56" />

Jitter is also closely tied to **symbolic execution**. Instead of running instructions with real concrete values, Miasm can execute them symbolically, meaning registers and memory can hold expressions rather than actual numbers. As Jitter steps through instructions, it updates these symbolic expressions and builds constraints that describe how program inputs affect the program state. This is useful for exploring multiple execution paths, understanding key checks, or reasoning about conditions without needing a specific input. In short, symbolic execution uses Jitter as its execution engine, but replaces concrete values with symbolic ones.

<img width="447" height="442" alt="image" src="https://github.com/user-attachments/assets/9bd6dff1-8750-4178-ac25-2daeec804f2b" />

Each layer produced an assembly-level CFG (*_asmcfg*.png), which shows the decoded VM instructions and their control flow, and for the final VM layer an IR-level CFG (*_ircfg*.png) was also generated
<img width="762" height="248" alt="image" src="https://github.com/user-attachments/assets/ca618b69-a0c0-4526-bd03-e317bd27916e" />

Ng



After setting up the custom disassembler, I began analyzing the generated assembly-level control flow graphs (CFGs) for each VM layer. These graphs show the decoded VM instructions and how control flows within each virtual machine. Since the challenge uses nested virtualization, examining these CFGs layer by layer helps understand how complexity is gradually peeled away until the real logic is exposed.




![VM Layer 1 CFG](https://github.com/user-attachments/assets/bbe373c4-9da6-4fcb-a551-15af7a587d62)

The first VM layer is the largest and most complex. It is dominated by dispatcher logic: instruction fetch loops, register movement, memory initialization, and indirect jumps. At this stage, the VM mainly focuses on setting up the execution environment and preparing the next bytecode buffer. There are no meaningful input-dependent checks here, only infrastructure code required to emulate the VM.





![VM Layer 2 CFG](https://github.com/user-attachments/assets/adc916a5-b277-4eaa-9d78-8b91368e2960)

The second VM layer closely resembles the first. While some constants and register roles differ due to re-encoding, the overall structure remains the same: a large dispatcher loop with instruction handlers branching from it. 




![VM Layer 3 CFG](https://github.com/user-attachments/assets/ecf8ffa4-5558-4d23-8cc6-cc2fcd15f2c0)

By the third VM layer, the CFG begins to shrink slightly. While dispatcher logic is still clearly visible, there are fewer blocks and less overall noise. 




![VM Layer 4 CFG](https://github.com/user-attachments/assets/764eba8b-9de7-4ffb-9ae3-cbe5d782bcf8)
 Although a dispatcher is still present, the CFG is noticeably smaller and more structured. Many repetitive VM bookkeeping blocks disappear tho 





![VM Layer 5 CFG](https://github.com/user-attachments/assets/164ed9e3-e381-47e2-a6f8-3229b057aae8)

 The CFG is much smaller and no longer dominated by VM dispatch infrastructure. Instead, it consists of relatively straight-line code with arithmetic operations and branches based on computed values.




![Final SSA IR CFG](https://github.com/user-attachments/assets/f1170f17-6a0f-4b96-85aa-390c5fe1e731)

The VM abstraction is very less honestly and we can see the register data's etc . 





From the SSA graph, it becomes clear that the input key is read from the VM ROM buffer in four 32-bit chunks. These correspond to the 16-byte input split as input[0:4], input[4:8], input[8:12], and input[12:16]. Each chunk is processed independently through a sequence of arithmetic checks. The first and third chunks are multiplied by fixed constants and reduced modulo 0x7fffffff, with the result compared against the value 1. This directly translates into modular inverse equations. The second and fourth chunks are validated using two different modulo comparisons each, forming classic Chinese Remainder Theorem (CRT) constraints. 

Only if all constraints succeed does execution reach the final block, which consists of a series of putchar calls that print the flag one character at a time.

<img width="762" height="621" alt="image" src="https://github.com/user-attachments/assets/7f29c980-f747-4ee5-9ab8-0d8bb91b833a" />


So i made a smol keygen 


<img width="1915" height="955" alt="image" src="https://github.com/user-attachments/assets/f6ae443b-05b4-4e88-855c-dd707409d225" />

<img width="454" height="88" alt="image" src="https://github.com/user-attachments/assets/a1ce76a8-babe-48e1-848c-6660e64d8e61" />




### References

* Miasm official blog and documentation
  [https://miasm.re/blog/](https://miasm.re/blog/)

* Miasm v0.1.0 release notes (IRCFG, SSA, symbolic execution improvements)
  [https://miasm.re/blog/2018/12/20/release_v0_1_0.html](https://miasm.re/blog/2018/12/20/release_v0_1_0.html)

* Tigress-based protection and virtualization examples
  [https://github.com/JonathanSalwan/Tigress_protection](https://github.com/JonathanSalwan/Tigress_protection)

* Dynamic Symbolic Execution with Miasm (crash course + crackme coverage)
  [https://miasm.re/blog/2017/10/05/playing_with_dynamic_symbolic_execution.html](https://miasm.re/blog/2017/10/05/playing_with_dynamic_symbolic_execution.html)

* Data flow analysis and dependency graphs in Miasm
  [https://miasm.re/blog/2017/02/03/data_flow_analysis_depgraph.html](https://miasm.re/blog/2017/02/03/data_flow_analysis_depgraph.html)

* Nanomite-protected binary analysis using Miasm symbolic execution
  [https://doar-e.github.io/blog/2014/10/11/taiming-a-wild-nanomite-protected-mips-binary-with-symbolic-execution-no-such-crackme/](https://doar-e.github.io/blog/2014/10/11/taiming-a-wild-nanomite-protected-mips-binary-with-symbolic-execution-no-such-crackme/)

* Deobfuscation of OLLVM-protected programs (Quarkslab)
  [https://blog.quarkslab.com/deobfuscation-recovering-an-ollvm-protected-program.html](https://blog.quarkslab.com/deobfuscation-recovering-an-ollvm-protected-program.html)



