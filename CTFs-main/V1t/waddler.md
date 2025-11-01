This binary exploitation challenge involves a straightforward buffer overflow to redirect execution and read the flag. The program reads 80 bytes into a 64-byte buffer, creating a 16-byte overflow that allows overwriting the return address. Since the binary has no PIE or stack canaries, we can directly overwrite RIP with the address of the `duck()` function at `0x40128c`, which reads and prints `flag.txt`. The payload consists of 64 bytes to fill the buffer, 8 bytes to overwrite RBP, followed by the target address. When `main()` returns, execution jumps to `duck()`, revealing the flag.

**Exploit:**
```python
from pwn import *
payload = b'A'*64 + b'B'*8 + p64(0x40128c)
print(payload)
```


**FLAG: v1t{w4ddl3r_3x1t5_4e4d6c332b6fe62a63afe56171fd3725}**
