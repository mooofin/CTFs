The formula is implemented by translating each arithmetic operation into its corresponding assembly instruction in the correct sequence.

1.  **Modulo Operation (`rax % rbx`)**: The `div` instruction in x86-64 is used for both division and modulo. The instruction `div rbx` divides the 128-bit value represented by `rdx:rax` by `rbx`. The quotient is stored in `rax`, and the remainder is stored in `rdx`. Since the challenge specifies that `rdx` is pre-set to `0`, this setup is ideal for performing a 64-bit modulo operation on the initial value of `rax`. After `div rbx` executes, the result of `rax % rbx` is located in the `rdx` register.

2.  **Result Transfer**: To continue the calculation, the remainder must be moved into the accumulator register, `rax`. This is accomplished with the instruction `mov rax, rdx`.

3.  **Addition (`+ rcx`)**: The value in `rcx` is added to the current result stored in `rax`. The `add rax, rcx` instruction performs this operation.

4.  **Subtraction (`- rsi`)**: Finally, the value in `rsi` is subtracted from the result in `rax`. The `sub rax, rsi` instruction completes the calculation.

### Final Assembly Sequence

The sequence of instructions to correctly implement the formula is:
```assembly
div rbx
mov rax, rdx
add rax, rcx
sub rax, rsi
```

```python
from pwn import *

def print_lines(io):
    """
    Utility function to print all subsequent output from the process.
    """
    info("Printing io received lines")
    while True:
        try:
            line = io.recvline()
            success(line.decode())
        except EOFError:
            break

# Set the execution context for 64-bit Linux.
context(arch="amd64", os="linux", log_level="info")

# Define the path to the challenge binary.
challenge_path = "/challenge/pwntools-tutorials-level2.2"

# Execute the challenge binary as a new process.
p = process(challenge_path)

# Assembly instructions to calculate the formula: rax = rax % rbx + rcx - rsi
shellcode = asm("""
    div rbx         # rax = (rdx:rax / rbx), rdx = (rdx:rax % rbx). rdx is pre-zeroed.
    mov rax, rdx    # Move the remainder (result of %) into rax.
    add rax, rcx    # Add rcx to the result.
    sub rax, rsi    # Subtract rsi for the final answer.
""")

# Send the compiled shellcode after receiving the prompt.
p.sendafter("Please give me your assembly in bytes", shellcode)

# Print any output from the process to display the challenge result.
print_lines(p)
```

Or you could just do :)
```bash
python -c 'from pwn import *; context(arch="amd64", os="linux", log_level="info"); p = process("/challenge/pwntools-tutorials-level2.2"); p.sendafter("Please give me your assembly in bytes", asm("div rbx; mov rax, rdx; add rax, rcx; sub rax, rsi")); p.interactive()'
```
<img width="1293" height="415" alt="screenshot-1759513536" src="https://github.com/user-attachments/assets/4834eecd-d95b-4e75-ac7c-53f6cec35171" />


