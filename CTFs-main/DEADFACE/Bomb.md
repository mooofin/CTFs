<img width="457" height="273" alt="image" src="https://github.com/user-attachments/assets/fb1227ad-1a88-422b-b486-9e5e0937ccaa" />


So the binary prompts us for a password ? 


<img width="1142" height="763" alt="image" src="https://github.com/user-attachments/assets/70850f9a-290c-4e72-a540-12b2c8d7e216" />


using strings we can see that D34DC0DE is the password  , but we'll need more than that .


Lets use objdump because why not and try to figure this out from the dissasembly :) 



Since , for comparing the password , the binary should use strcmp , so we'll try to search that in the objdump 


<img width="886" height="292" alt="image" src="https://github.com/user-attachments/assets/6fc884ef-704a-4f13-8965-7ab4b6e2ec73" />


I'll try to break this down into what it means : 3 




| Addr   | Instruction                           | what that means                                                       |
| ------ | ------------------------------------- | ------------------------------------------------------------------------- |
| 0x1905 | `lea rdx, [rip + 0xb10]`              | Load address of CORRECT password into `rdx` (target addr comment: 0x241c) |
| 0x190c | `lea rax, [rbp - 0x12]`               | Load address of USER INPUT into `rax`                                     |
| 0x1910 | `mov rdi, rax`                        | 1st arg = user input                                                      |
| 0x1913 | `mov rsi, rdx`                        | 2nd arg = correct password                                                |
| 0x1916 | `call strcmp`                         | Compare strings at `rdi` and `rsi`                                        |
| 0x191b | `test eax, eax` / `je 0x191d` (range) | If `strcmp` returned 0 (equal) jump to success                            |
| 0x191f | `call explode`                        | Otherwise call the explode/fail function                                  |

Lets now dump the string at 0x241c and see . 



```
Raw hex bytes at offset 0x241c:
  44 33 34 44 43 30 44 45  00 00 00 00 0A 4F 68 2C
```

which is hex for Deadcode . 

<img width="1874" height="979" alt="image" src="https://github.com/user-attachments/assets/6f682b74-4da6-4e4c-9925-ea66790aa7f1" />


So lets look for what green wire and blue wire is 


After more investigating , the objdump , we see that there are 4 things we need to patch to ge through 


1.  Password Check (requires input)
2.  Anti-Debugging Check (ptrace detection)
3.  Success Display (no check, just messages)
4.  Time Validation (year must be 1995)

Hmm so lets start with the 2nd since we alr know the password  .


**Option 1: Make ptrace check always return 0 (not debugged)**



Lets scan the objdump for ptrace which is the most common one , and we can see this .


```assembly
1784:   call   1341                    ; Call ptrace detection function
1789:   test   eax,eax                 ; Check return value
178b:   je     1793                    ; Jump if NOT being debugged (good)
178d:   call   13fc                    ; EXPLODE if being debugged

; Ptrace detection function at 0x1341:
1341:   push   rbp
1345:   mov    ecx,0x0
134a:   mov    edx,0x0
134f:   mov    esi,0x0
1354:   mov    edi,0x0
1359:   mov    eax,0x0
135e:   call   1060 <ptrace@plt>       ; Call ptrace
1363:   cmp    rax,0xffffffffffffffff  ; Compare with -1
1367:   sete   al                       ; Set AL=1 if debugger detected
136a:   movzx  eax,al
136d:   ret
```

Uhm so we can do 3 things here actually and they should all work !


Make ptrace check always return 0  , Skip the bomb explosion check , NOP out the entire check 


Lets make ptrace return 0 because its more fun . 
```
Address: 0x1367
Original: 0f 94 c0          (sete al)
Patched:  31 c0 90          (xor eax,eax; nop)

 Always returns 0 
```

What this means is that , `sete al` is a conditional instruction that sets the low byte `al` to 1 if the Zero Flag (ZF) is set, otherwise it sets it to 0. In this case, it means `al = (ZF ? 1 : 0)`. 

would make the function return 1 or 0 depending on whether the comparison was true. In my patch, I replaced `0f 94 c0` (`sete al`) with `31 c0 90` (`xor eax, eax; nop`), which forces `eax` to always be 0. That means the function will now always return 0  essentially making it always think it’s *not being debugged*.

Other options are much simpler 

**Option 2: Skip the bomb explosion check**
```
Address: 0x178b
Original: 74 06             (je 1793)
Patched:  90 90             (nop; nop)

 Always jump to success path ehe 
```

**Option 3: NOP out the entire check**
```
Address: 0x1784 (5 bytes)
Original: e8 b8 fb ff ff    (call 1341)
Patched:  90 90 90 90 90    (5 NOPs)

Address: 0x1789 (2 bytes)
Original: 85 c0             (test eax,eax)
Patched:  90 90             (nop nop)
```

Now thats done , lets move onto the next one's . 
