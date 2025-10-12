Of course! Let's dive deep into the `trust-the-yancode-hard` challenge. This is a fantastic example of a custom architecture emulation challenge, and understanding it piece-by-piece is very rewarding.

Here is a detailed, step-by-step write-up of the solution process.

---

### **Trust-The-Yancode-Hard: A Detailed Write-up**

#### **Objective:**
Our goal is to understand the custom "Yan85" architecture emulated by the `./trust-the-yancode-hard` binary, analyze the code it's running, and provide the correct input to receive the flag.

#### **Strategy:**
The binary itself is the emulator. The Ghidra decompilation gives us the complete source code for this emulator. Our strategy will be:

1.  **Deconstruct the Yan85 Virtual Machine:** Analyze the provided C code to understand the fundamental components of the emulated environment: its memory layout and its registers.
2.  **Reverse Engineer the Yan85 Instruction Set:** Identify the C functions that correspond to Yan85 opcodes (like `MOV`, `ADD`, `CMP`, `SYSCALL`) and understand what each one does.
3.  **Analyze the Emulated Program:** Trace the logic of the main challenge function (`FUN_00101a97`), which contains the sequence of Yan85 instructions, to determine what it expects as input.
4.  **Craft the Payload:** Use our understanding to provide the correct input and solve the challenge.

---

### **Part 1: Deconstructing the Yan85 Virtual Machine**

The entire state of the virtual machine (its memory and registers) is stored in a single C struct passed around between functions. In the `main` function (`FUN_0010279c`), this is created on the stack as `local_118`.

```c
// from FUN_0010279c (main)
undefined8 local_118 [33]; // This is our 264-byte VM state buffer
...
FUN_00101a97(local_118); // The main logic is called with the VM state
```

This `local_118` buffer is effectively the computer we are hacking.

#### **Memory Layout**

By analyzing functions like `FUN_001014e6` (read from memory) and `FUN_00101507` (write to memory), we can see they take the VM state buffer (`param_1`) and an offset (`param_2`) to access bytes.

```c
// FUN_001014e6 - Read from VM memory
undefined1 FUN_001014e6(long param_1, byte param_2)
{
  return *(undefined1 *)(param_1 + (int)(uint)param_2);
}
```

This tells us that the first part of the buffer (`param_1`) is a simple byte-addressable memory space. Based on the syscalls, this memory appears to be **256 bytes** (0x00 to 0xFF).

#### **The Registers**

The functions `FUN_00101363` (get register value) and `FUN_00101415` (set register value) are the keys to understanding the registers. They use specific character constants to identify which register to access. These registers are stored in the VM state buffer at offsets starting from `0x100`.

Let's map them out:

| Identifier | Hex Value | VM State Offset | Inferred Purpose |
| :--- | :--- | :--- | :--- |
| `'\x10'` | `0x10` | `+0x100` | General Purpose Register A |
| `'@'` | `0x40` | `+0x101` | General Purpose Register B / Address Pointer |
| `' '` | `0x20` | `+0x102` | General Purpose Register C / Counter |
| `'\x01'` | `0x01` | `+0x103` | General Purpose Register D |
| `'\x04'` | `0x04` | `+0x104` | **SP** (Stack Pointer) |
| `'\x02'` | `0x02` | `+0x105` | **IP** (Instruction Pointer) |
| `'\b'` | `0x08` | `+0x106` | **FLAGS** (Status Flags) |

For this specific challenge, we don't see a main execution loop that uses the IP register, but its presence is noted. The FLAGS register is set by the `CMP` instruction.

---

### **Part 2: Reverse Engineering the Yan85 Instruction Set**

The C functions are direct implementations of the Yan85 instructions.

*   `FUN_00101533`: **`MOV reg, imm`**
    *   Moves an immediate (constant) value into a register.
    *   `FUN_00101533(vm_state, 0x40, 0x50)` translates to `MOV REG_B, 0x50`.

*   `FUN_00101568`: **`ADD reg_dest, reg_src`**
    *   Adds the values in two registers and stores the result in `reg_dest`.
    *   `FUN_00101568(vm_state, 0x40, 0x20)` translates to `ADD REG_B, REG_C`.

*   `FUN_00101687`: **`STORE [reg_addr], reg_val`**
    *   Stores the value from `reg_val` into the memory location pointed to by `reg_addr`.
    *   `FUN_00101687(vm_state, 0x40, 0x10)` translates to `STORE [REG_B], REG_A`.

*   `FUN_0010173d`: **`CMP reg1, reg2`**
    *   Compares two registers and updates the FLAGS register (`0x106`) to reflect the result (less than, greater than, equal, etc.).

*   `FUN_00101896`: **`SYSCALL`**
    *   This is the most critical instruction for I/O. It performs a system call based on a bitmask.
    *   `if ((param_2 & 0x10) != 0)` corresponds to `read()`. The registers are used for arguments: `REG_A` (fd), `REG_B` (buffer address), `REG_C` (count).
    *   `if ((param_2 & 8) != 0)` corresponds to `write()`.
    *   `if ((param_2 & 0x20) != 0)` corresponds to `exit()`.

---

### **Part 3: Analyzing the Emulated Program (`FUN_00101a97`)**

This function is not an emulator loop; it's a hardcoded sequence of Yan85 instructions. We can now translate it line-by-line.

**Step A: Reading User Input**
The program first reads 6 bytes from your input.

```c
// Yan85 Assembly Translation:
// MOV REG_B, 0x50      ; Set destination buffer address for input
FUN_00101533(param_1,0x40,0x50);
// MOV REG_C, 6         ; Set number of bytes to read
FUN_00101533(param_1,0x20,6);
// MOV REG_A, 0         ; Set file descriptor to 0 (stdin)
FUN_00101533(param_1,0x10,0);
// SYSCALL read         ; Execute the read
FUN_00101896(param_1,0x10,0x10);
```
**Conclusion:** The program reads **6 bytes** from us and stores them in its emulated memory at address `0x50`.

**Step B: Constructing the Secret Password**
Next, the program meticulously constructs a 6-byte value in memory starting at address `0x70`.

```c
// Set the destination address for the secret to 0x70
FUN_00101533(param_1,0x40,0x70);
// Set a counter to 1, used for incrementing the address
FUN_00101533(param_1,0x20,1);

// Write byte 1: 0x80
FUN_00101533(param_1,0x10,0x80);        // MOV REG_A, 0x80
FUN_00101687(param_1,0x40,0x10);        // STORE [REG_B], REG_A  (at addr 0x70)
FUN_00101568(param_1,0x40,0x20);        // ADD REG_B, REG_C      (REG_B is now 0x71)

// Write byte 2: 0x3c
FUN_00101533(param_1,0x10,0x3c);         // MOV REG_A, 0x3c
FUN_00101687(param_1,0x40,0x10);         // STORE [REG_B], REG_A  (at addr 0x71)
FUN_00101568(param_1,0x40,0x20);         // ADD REG_B, REG_C      (REG_B is now 0x72)

// Write byte 3: 0x42
FUN_00101533(param_1,0x10,0x42);         // MOV REG_A, 0x42
FUN_00101687(param_1,0x40,0x10);         // STORE [REG_B], REG_A  (at addr 0x72)
FUN_00101568(param_1,0x40,0x20);         // ... and so on

// Write byte 4: 0xf9
FUN_00101533(param_1,0x10,0xf9);
FUN_00101687(param_1,0x40,0x10);
FUN_00101568(param_1,0x40,0x20);

// Write byte 5: 0x51
FUN_00101533(param_1,0x10,0x51);
FUN_00101687(param_1,0x40,0x10);
FUN_00101568(param_1,0x40,0x20);

// Write byte 6: 0x51
FUN_00101533(param_1,0x10,0x51);
FUN_00101687(param_1,0x40,0x10);
FUN_00101568(param_1,0x40,0x20);```
**Conclusion:** The program builds the 6-byte secret `\x80\x3c\x42\xf9\x51\x51` in its memory at address `0x70`.

**Step C: The Verification**
This is the moment of truth. The program calls the real C `memcmp` function to compare our input with the secret it just built.

```c
// memcmp(our_input_buffer, secret_buffer, 6)
iVar1 = memcmp((void *)(param_1 + 0x70), (void *)(param_1 + 0x50), 6);

if (iVar1 == 0) {
  // SUCCESS: Print "CORRECT! You get your flag:" and read/print /flag
}
else {
  // FAILURE: Print "INCORRECT!"
}```
The comparison is `memcmp(vm_state + 0x70, vm_state + 0x50, 6)`. Whoops! It seems I've swapped the arguments in my description, but for `memcmp` it doesn't matter for a simple equality check. The core logic is clear: it compares the buffer at `0x70` (the secret) with the buffer at `0x50` (our input).

---

### **Part 4: Crafting the Payload**

To pass the check, our input must be identical to the secret constructed by the program.

**The Secret:** `\x80\x3c\x42\xf9\x51\x51`

These are raw byte values, not printable ASCII characters. We cannot simply type them. We must pipe these exact bytes into the program's standard input.

**The Solution:**
We can use a simple python script or `echo` with the `-e` flag to send the raw bytes.

**Method 1: Using Python (Recommended)**
This method is reliable for sending arbitrary byte data.

```bash
hacker@reverse-engineering~trust-the-yancode-hard:/challenge$ python -c 'import sys; sys.stdout.buffer.write(b"\x80\x3c\x42\xf9\x51\x51")' | ./trust-the-yancode-hard
```

**Method 2: Using `echo`**
This works in many shell environments like bash.

```bash
hacker@reverse-engineering~trust-the-yancode-hard:/challenge$ echo -e -n '\x80\x3c\x42\xf9\x51\x51' | ./trust-the-yancode-hard
```
*(The `-n` flag prevents `echo` from adding a trailing newline, which would make our input 7 bytes long and cause the check to fail.)*

Upon running either of these commands, the program will receive the correct 6-byte sequence, the `memcmp` will return `0`, and the success branch will be executed, printing the flag.
