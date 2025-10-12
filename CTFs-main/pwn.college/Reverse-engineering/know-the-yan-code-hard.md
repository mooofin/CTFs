
<img width="1921" height="929" alt="screenshot-1760279045" src="https://github.com/user-attachments/assets/5ac0e078-5416-4e0a-b446-47b7cd87c20f" />



Running the binary shows:

```
[+] Welcome to ./challenge!
[+] This challenge is an custom emulator. It emulates a completely custom
[+] architecture that we call "Yan85"! You'll have to understand the
[+] emulator to understand the architecture, and you'll have to understand
[+] the architecture to understand the code being emulated, and you will
[+] have to understand that code to get the flag. Good luck!
```

The challenge clearly states this is a VM based obfuscation challenge.

## VM State Structure

### Memory Layout

* **Bytes 0x00-0xFF**: 256 bytes of emulated RAM
* **Bytes 0x100-0x106**: 7 registers

### Register Mapping

By analyzing `FUN_00101343` (register read) and `FUN_001013f5` (register write):

| Register ID | Offset | Purpose                    |
| ----------- | ------ | -------------------------- |
| `0x01`      | 0x100  | General purpose register A |
| `0x02`      | 0x101  | General purpose register B |
| `0x40`      | 0x102  | General purpose register C |
| `0x08`      | 0x103  | General purpose register D |
| `0x10`      | 0x104  | Stack Pointer (SP)         |
| `0x04`      | 0x105  | Instruction Pointer (IP)   |
| `0x20`      | 0x106  | Flags register             |

### Flag Register Bits

From `FUN_0010171d` (compare operation):

* Bit 0 (`0x01`): Less than
* Bit 1 (`0x02`): Not equal
* Bit 2 (`0x04`): Greater than
* Bit 3 (`0x08`): Equal
* Bit 4 (`0x10`): Both zero

## Instruction Mapping

Mapping each function to its VM instruction:

| Function       | Instruction      | Description                      |
| -------------- | ---------------- | -------------------------------- |
| `FUN_00101513` | MOV reg, imm     | Move immediate value to register |
| `FUN_00101548` | ADD reg1, reg2   | Add reg2 to reg1                 |
| `FUN_001015aa` | PUSH/POP         | Stack operations                 |
| `FUN_00101667` | STM [reg1], reg2 | Store reg2 to memory[reg1]       |
| `FUN_001016c6` | LDM reg1, [reg2] | Load memory[reg2] to reg1        |
| `FUN_0010171d` | CMP reg1, reg2   | Compare registers, set flags     |
| `FUN_00101823` | JCC flags, reg   | Conditional jump to reg          |
| `FUN_00101876` | SYSCALL          | System call interface            |

## System Call Interface (`FUN_00101876`)

Examining the syscall function, parameter byte bits control different operations:

| Bit  | Value | Operation | Parameters                                 |
| ---- | ----- | --------- | ------------------------------------------ |
| 0x10 | 16    | OPEN      | file=reg[0x01], flags=reg[0x02]            |
| 0x04 | 4     | READ      | fd=reg[0x01], buf=reg[0x02], len=reg[0x03] |
| 0x20 | 32    | WRITE     | fd=reg[0x01], buf=reg[0x02], len=reg[0x03] |
| 0x08 | 8     | SLEEP     | seconds=reg[0x01]                          |
| 0x01 | 1     | EXIT      | status=reg[0x01]                           |

## VM Program Trace (`FUN_00101a77`)

```
MOV  reg[0x02], 0x37      # Buffer at memory offset 0x37
MOV  reg[0x40], 6         # Read 6 bytes
MOV  reg[0x01], 0         # O_RDONLY
SYSCALL 4                 # Read from stdin into memory[0x37]
```

```
MOV  reg[0x02], 0x57      # Start of comparison buffer
# Store 6 expected bytes:
MOV  reg[0x01], 0x9b
STM  [reg[0x02]], reg[0x01]
ADD  reg[0x02], reg[0x40] # Increment pointer by 6

MOV  reg[0x01], 0xd6
STM  [reg[0x02]], reg[0x01]
ADD  reg[0x02], reg[0x40]

# ... continues for all 6 bytes
```

The expected values stored at memory[0x57-0x5c] are:

* **0x9b, 0xd6, 0x59, 0x14, 0xa2, 0x37**

```
# For each byte (i = 0 to 5):
MOV  reg[0x02], 0x57 + i      # Expected value location
LDM  reg[0x02], [reg[0x02]]   # Load expected
MOV  reg[0x01], 0x37 + i      # Input value location
LDM  reg[0x01], [reg[0x01]]   # Load input
CMP  reg[0x01], reg[0x02]     # Compare
# If equal, flag[0x08] is set
```

```
# Check if ALL 6 flags are set (flag & 0x08)
if all_equal:
    # Print "CORRECT! Your flag:\n"
    # Build string "/flag" in memory[0-5]
    # Open file "/flag"
    # Read 100 bytes
    # Write to stdout
else:
    # Print "INCORRECT!\n"
    EXIT 1
```

The program reads 6 bytes from stdin and compares them to the hardcoded sequence:

```
0x9b, 0xd6, 0x59, 0x14, 0xa2, 0x37
```

```
echo -ne '\x9b\xd6\x59\x14\xa2\x37'
```
