```bash
remnux@remnux:~/Downloads$ file stupidrop 
stupidrop: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=4f0ff8340bc3eead42d0f7b14535ee7c74a6ca7d, not stripped

```

```
remnux@remnux:~/Downloads$ ./stupidrop
muffinnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```

Let's see the dissasembly in ghidra 

<img width="1920" height="913" alt="Screenshot from 2025-11-25 15-47-03" src="https://github.com/user-attachments/assets/3ee657d5-3f7b-48e3-8e54-65191aaa74e2" />


```c

undefined8 main(void)

{
  char local_38 [48];
  
  setvbuf(stdout,(char *)0x0,2,0);
  alarm(0x20);
  gets(local_38);
  return 0;
}

```
Before calling `execve`, we need a real pointer to the string `/bin/sh`. That means the string must exist somewhere writable in the program’s memory at a known address. The `.bss` slot at `0x601050` works perfectly because it is empty, writable, and its address does not change. We use a `pop rdi; ret` gadget to load that address into `rdi` and then call `gets`, which lets us type `/bin/sh\x00` directly into that location. After that, `execve` can simply use `rdi = 0x601050` to find the string.
<img width="1920" height="913" alt="Screenshot from 2025-11-25 15-58-49" src="https://github.com/user-attachments/assets/d2f5f102-880b-475b-bccc-b8398999f768" />

To trigger SIGROP we must do  you must trigger sigreturn, which is syscall number 0xf on x86_64 !!

The kernel decides which syscall to run based on the value in rax, so before we hit the syscall gadget, we need rax to be exactly 0xf. The problem is that the binary gives you no gadget that directly sets rax:(( But alarm looks vulnable ?

Every time you call alarm(x), its return value lands in rax. If you call alarm(0xf) the return value is zero, because you are setting a new timer. If you then immediately call alarm(0) you cancel the timer, and the return value is the number of seconds that were left on the old timer, which is 0xf.


So we build two small ROP chains. First, load 0xf into rdi and call alarm. Then load 0 into rdi and call alarm again. After the second call, rax contains 0xf

<img width="1920" height="913" alt="Screenshot from 2025-11-25 16-08-09" src="https://github.com/user-attachments/assets/62e70ddf-e10a-4305-b91a-a7d1608399a5" />

