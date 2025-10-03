# Pwntools Tutorial Level 2.0 Writeup

## Objective

The goal of this challenge is to provide an assembly code snippet that sets the `rax` register to the specific value `0x12345678`. We will use the `asm` function from the `pwntools` library to compile our assembly instruction into machine code (bytes) and send it to the challenge binary to bypass its check.

## Solution

To accomplish this, we need to use an assembly instruction that moves the desired value into the `rax` register. In x86-64 assembly, the `mov` instruction is used for this purpose.

The specific instruction is:
```assembly
mov rax, 0x12345678
```

This instruction tells the processor to move the immediate 64-bit value `0x12345678` into the `rax` register.

We will integrate this into the provided Python script. The `asm()` function from `pwntools` will take our assembly instruction as a string and return the corresponding compiled bytes, which we can then send to the process.

## Final Script

Here is the complete Python script to solve the challenge. The `NOP` instruction has been replaced with our `mov` instruction.

```python
from pwn import *

def print_lines(io):
    """
    Helper function to continuously print received lines from the process
    until the process closes.
    """
    info("Printing io received lines")
    while True:
        try:
            line = io.recvline()
            success(line.decode())
        except EOFError:
            break

# Set the context for the target architecture (64-bit AMD) and OS.
# Setting the log level to 'info' provides useful feedback from pwntools.
context(arch="amd64", os="linux", log_level="info")

# Define the path to the challenge binary.
challenge_path = "/challenge/pwntools-tutorials-level2.0"

# Start the challenge binary as a new process.
p = process(challenge_path)

# This is the core of the solution.
# The `asm()` function takes our assembly instruction as an argument
# and compiles it into the raw bytes that the CPU can execute.
shellcode = asm("mov rax, 0x12345678")

# The script waits until it receives the specified string from the process,
# and then it sends our compiled shellcode as the payload.
p.sendafter("Please give me your assembly in bytes", shellcode)

# Print any output from the process to see the flag or result.
print_lines(p)
```
