This was fairy easy than The part 2 

<img width="1919" height="1032" alt="image" src="https://github.com/user-attachments/assets/1ef597b2-9361-4ac0-8962-f3a366bfaeee" />

 
 The binary uses a parent-child process model. The parent process continuously spawns child processes of itself, waits for them to finish, and checks their exit codes. If a debugger is detected, the child processes return specific exit codes (0xFF, 0xFE, or 0xFD), and the parent shows error messages. After each spawn, it sleeps for 5 seconds and repeats the whole thing in an infinite loop.The interesting part is that the same executable behaves differently depending on how it's called. When run normally, it acts as the parent. When spawned with certain parameters, it acts as the child that performs the actual flag logic.

 First i unpacked it using upx :

 <img width="1878" height="633" alt="image" src="https://github.com/user-attachments/assets/6785348c-02f9-4aed-8077-e07c791ae293" />


The main function has two execution paths controlled by this check:

```
asm004037c0  mov eax, 0x1      ; Set eax to 1
004037c5  test eax, eax     ; Test if eax is 0
004037c7  je 0x4038e0       ; Jump to flag code if zero
```

Since eax=1, the jump is not taken, and execution continues into an infinite loop that:

It sets eax to 1, tests it, and then does a conditional jump. Since eax is 1, the jump never happens and execution falls through to the parent process loop. But if eax were 0, it would jump directly to 0x4038e0, which is where all the flag-related code lives.
The weird thing is that this value is hardcoded. There's no runtime check, no command-line argument parsing at this point, just a static constant.


At address 0x4038e0, there's completely different logic. This path calls some initialization functions, then calls two important functions (sub_402cb0 and sub_402b30) that appear to generate or decrypt the flag. After that, it displays the flag in a MessageBox with the title "You got the flag!" and also outputs it using OutputDebugStringW for good measure.
So the flag logic is already in the binary, just hidden behind this branch condition.



So At address 0x4037C0, the bytes are B8 01 00 00 00 (mov eax, 1) i Changed that 01 to 00, making it B8 00 00 00 00 (mov eax, 0)

After patching, I just ran the modified executable and got the flag 






