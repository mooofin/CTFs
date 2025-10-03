# Pwntools Tutorial Level 2.0 Technical Writeup

## Objective

The objective of this challenge is to construct an assembly code snippet that sets the `rax` register to the hexadecimal value `0x12345678`. The `asm` function from the `pwntools` library is to be used for compiling the assembly instruction into machine code. This payload is then sent to the target binary to bypass a programmatic check.

## Solution

The solution requires an assembly instruction to load an immediate value into the `rax` register. On the x86-64 architecture, the `mov` instruction is utilized for this operation.

The specific instruction is:
```assembly
mov rax, 0x12345678
```

This instruction directs the CPU to load the 64-bit immediate value `0x12345678` into the `rax` register.

This assembly instruction is then passed as a string to the `pwntools` `asm()` function. The function compiles it into the corresponding machine code byte sequence. The resulting bytes are transmitted to the running process to be executed

## Final Script



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
# The `asm()` function takes the  assembly instruction as an argument
# and compiles it into the raw bytes that the CPU can execute.
shellcode = asm("mov rax, 0x12345678")

# The script waits until it receives the specified string from the process,
# and then it sends the  compiled shellcode as the payload.
p.sendafter("Please give me your assembly in bytes", shellcode)

# Print any output from the process to see the flag or result.
print_lines(p)
```

<img width="1295" height="350" alt="screenshot-1759511946" src="https://github.com/user-attachments/assets/9229f5fd-e6ec-4969-bca4-f6760c2ec0b4" />

