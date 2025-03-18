# GDB Test Drive Write-up

## Author: LT 'syreal' Jones

### Description
Can you get the flag? Download the provided binary and follow these test drive instructions:

```bash
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

## Solution Walkthrough

### Step 1: Grant Execution Permissions
Before debugging, we need to allow the binary to be executed:

```bash
chmod +x gdbme
```

### Step 2: Run the Binary
Try running it normally:

```bash
./gdbme
```

The program seems to be stuck, indicating we need to debug it.

### Step 3: Start GDB Debugger
Attach GDB to the binary:

```bash
gdb gdbme
```

### Step 4: View Assembly Code
To view the assembly layout:

```bash
layout asm
```

You will see the assembly code of the program.

#### Change Disassembly Syntax (Optional)
If you prefer Intel syntax, switch using:

```bash
set disassembly-flavour intel
layout asm
```

### Step 5: Identify the Issue
We notice that the program calls the `sleep` function, which delays execution for `0x186a0` (100000 seconds).

### Step 6: Set a Breakpoint and Run the Program
We place a breakpoint before the `sleep` function:

```bash
break *(main+99)
run
```

This will pause execution before `sleep` is executed.

### Step 7: Skip the Sleep Function
To bypass the delay, jump to the next instruction after `sleep`:

```bash
jump *(main+104)
```

### Step 8: Retrieve the Flag
After executing the jump command, the flag is displayed:

```
picoCTF{d3bugg3r_dr1v3_7776d758}
```

## GDB Quick Reference

### Starting and Stopping GDB
```bash
gdb               # Start GDB without a file
gdb filename      # Start GDB with a file
quit              # Quit GDB
```

### Running the Program
```bash
run               # Run the program
run arguments     # Run the program with arguments
```

### Setting Breakpoints
```bash
break location        # Set a breakpoint at a location
info breakpoints      # List all breakpoints
```

### Stepping Through the Program
```bash
next                 # Run the program until the following line
step                 # Step into function calls
```

### Inspecting Variables
```bash
print variable       # Print the value of a variable
display variable     # Continually display the value of a variable
```

### Inspecting Source Code
```bash
list                # List the source code
list function       # List the source code of a function
list line           # List the source code around a specific line
```

### Inspecting Assembly Code
```bash
disassemble function     # Disassemble the code of a function
disassemble/r function   # Disassemble the code of a function with raw opcodes
```

### Inspecting Registers
```bash
info registers       # Display all register values
print/d $register    # Print the value of a register in decimal
print/x $register    # Print the value of a register in hexadecimal
```

### Inspecting the Stack
```bash
info stack          # Display information about the stack
x/10wx $sp         # Show the top 10 words on the stack
```


