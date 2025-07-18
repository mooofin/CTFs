from pwn import *

elf = ELF("./vuln")

p = process("./vuln")
p.sendline(cyclic(200, n=8))
p.wait()

core = p.corefile

print cyclic_find(core.read(core.rsp, 8), n=8)
