 When i first ran the binary , it checks for a login and a password :


 <img width="583" height="214" alt="image" src="https://github.com/user-attachments/assets/402a5a57-97fd-4193-8ae5-96f0fed78384" />



So i loaded up the exe in binary ninja and started looking for symbols but there were none , which meant that the instructions might be inside a VM and the actual flag logic would be there . 



Then next i got the the security cookie check function , which has a initilised value to it 

<img width="857" height="185" alt="image" src="https://github.com/user-attachments/assets/a127d280-3463-42a4-9cf0-2c6452fd19fb" />


Also some intresting things like :


<img width="1047" height="473" alt="image" src="https://github.com/user-attachments/assets/0a60e3af-e098-4179-b4c4-de2e9958d521" />




Also some more checks which i thought would need patching before understanding the logic :

<img width="1140" height="733" alt="image" src="https://github.com/user-attachments/assets/fa6dc177-97d1-46df-9d18-f4c523f044eb" />

 
 
 This thing is packed with obfuscation and anti-debugging tricks scattered everywhere


 When i looked at the function  graph for the main flow logic with a plugin on ghidra for VM obsfucation i found a function which was peculiar :


 <img width="1919" height="1008" alt="image" src="https://github.com/user-attachments/assets/98ca5282-cacb-4fb3-aace-3f6a0599977b" />


FUN_140002d30 and it's doing something weird. Instead of just comparing strings like a normal program, it's building some kind of custom bytecode on the fly.






Digging deeper, i  there's a full VM interpreter at FUN_1400048e0. This thing supports 21 different opcodes (0x00 through 0x15) and can do all sorts of operations:

Basic arithmetic (add, multiply, divide, modulo)
Memory reads/writes
Conditional and unconditional jumps
Stack operations
Even some specialized math operations like Fibonacci calculation, prime checking, and factorial

The VM has registers, a stack, and memory space. It's actually pretty sophisticated for a crackme challenge .


```
                             *************************************************************
                             *                           FUNCTION                          
                             *************************************************************
                             int  __fastcall  FUN_1400033b0 (undefined8  param_1 , undefi
                               assume GS_OFFSET = 0xff00000000
             int               EAX:4          <RETURN>
             undefined8        RCX:8          param_1
             undefined8        RDX:8          param_2
             undefined8        R8:8           param_3
             undefined8        R9:8           param_4
             undefined8        Stack[0x20]:8  local_res20                             XREF[2]:     1400033cc (W) , 
                                                                                                   1400033de (*)   
             undefined1        Stack[-0x38]:1 local_38                                XREF[1]:     1400033be (*)   
             undefined8        Stack[-0x40]:8 local_40                                XREF[2]:     1400033da (W) , 
                                                                                                   1400035ce (R)   
             undefined8        Stack[-0x58]:8 local_58                                XREF[2]:     14000340b (*) , 
                                                                                                   1400034c0 (*)   
             undefined8        Stack[-0x60]:8 local_60                                XREF[2]:     140003439 (W) , 
                                                                                                   14000349a (W)   
             undefined8        Stack[-0x68]:8 local_68                                XREF[4]:     1400033f0 (*) , 
                                                                                                   14000343e (W) , 
                                                                                                   14000349f (W) , 
                                                                                                   1400034fe (*)   
             undefined8        Stack[-0x70]:8 local_70                                XREF[2]:     140003539 (W) , 
                                                                                                   1400035a2 (W)   
             undefined8        Stack[-0x78]:8 local_78                                XREF[2]:     14000353e (W) , 
                                                                                                   1400035a7 (W)   
                             FUN_1400033b0                                   XREF[3]:     FUN_140001ab0:140001eaf (c) , 
                                                                                          FUN_140001ab0:140001fcf (c) , 
                                                                                          14000f0f0 (*)   
```


