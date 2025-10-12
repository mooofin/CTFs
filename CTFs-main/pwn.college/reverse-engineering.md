This was very similar to a chip8 emulator where you had to write a custom .ch8 game rom to get the flag 





<img width="1921" height="1081" alt="screenshot-1760273157" src="https://github.com/user-attachments/assets/6155d546-b93c-4688-878f-255914cf5ca1" />
















ok looking at the `execute_program` function. This is the "code" that is being run on the fake computer. It's just a long list of these "instructions".

```c
void execute_program(long param_1)
{
  int iVar1;

  interpret_imm(param_1,0x20,0x5f); // Instruction 1
  interpret_imm(param_1,0x10,8);     // Instruction 2
  interpret_imm(param_1,0x40,0);     // Instruction 3
  interpret_sys(param_1,1,0x40);     // Instruction 4
  ...
  // A lot more instructions
  ...
  iVar1 = memcmp((void *)(param_1 + 0x7f),(void *)(param_1 + 0x5f),8); // The GOAL!
  ...
}
```

 By looking at the C code for each function, we can translate them:

*   `interpret_imm(machine, register, value)`: This is the "Immediate" instruction. It means "load this `value` directly into this `register`." Think of registers as tiny storage spots, like variables `a`, `b`, `c`, etc.
*   `interpret_sys(machine, syscall_code, register)`: This is a "System Call." This is how the fake Yan85 computer asks the *real* computer to do something. For example:
    *   `syscall_code 1`: Read from the keyboard.
    *   `syscall_code 4`: Write to the screen.
    *   `syscall_code 0x10`: Open a file.
    *   `syscall_code 0x20`: Exit the program.
*   `interpret_stm(machine, address_register, value_register)`: This is the "Store to Memory" instruction. It takes the value from one register and stores it in the fake computer's memory at the location pointed to by another register.

The most important line in the entire program is this one:
`iVar1 = memcmp((void *)(param_1 + 0x7f),(void *)(param_1 + 0x5f),8);`

`memcmp` is a standard C function that **compares two chunks of memory**.
*   It's comparing 8 bytes of memory starting at address `0x7f`.
*   It's comparing it with 8 bytes of memory starting at address `0x5f`.
*   If the two chunks of memory are **exactly the same**, `memcmp` returns `0`.

The code right after this line checks if the result is `0`. If it is, it runs the code to print "CORRECT!" and show the flag. If not, it prints "INCORRECT!".

We need to make the 8 bytes at memory address `0x5f` identical to the 8 bytes at memory address `0x7f`.**



Let's trace the code to see what goes into those two memory locations 

**1. What's at memory address `0x5f`?**
Looking at the very first instructions:
*   `interpret_imm(param_1, 0x20, 0x5f)`: Load the value `0x5f` into a register.
*   `interpret_imm(param_1, 0x10, 8)`: Load the value `8` into another register.
*   `interpret_sys(param_1, 1, 0x40)`: Make a system call to `read`.
The `sys_read` function uses these registers. It reads **8** bytes from your keyboard and stores them in memory at address **0x5f**.
**Conclusion:** The memory at `0x5f` is **our input**.

**2. What's at memory address `0x7f`?**
This is the secret password ehe  The program builds it step-by-step right before the `memcmp`.
*   `interpret_imm(param_1, 0x20, 0x7f)`: Set a pointer register to `0x7f`.
*   `interpret_imm(param_1, 0x40, 0xda)`: Load `0xda` into a value register.
*   `interpret_stm(param_1, 0x20, 0x40)`: Store that value (`0xda`) into memory at the pointer's location (`0x7f`).
*   `interpret_add(...)`: The program then adds 1 to the pointer, so it now points to `0x80`.
It repeats this process for all 8 bytes:
*   It stores `0xda` at address `0x7f`
*   It stores `0xce` at address `0x80`
*   It stores `0xc0` at address `0x81`
*   It stores `0xaf` at address `0x82`
*   It stores `0x4f` at address `0x83`
*   It stores `0x6f` at address `0x84`
*   It stores `0x04` at address `0x85`
*   It stores `0x43` at address `0x86`

Hmmm so ** The memory at `0x7f` contains the 8-byte sequence: `DA CE C0 AF 4F 6F 04 43`.



So now i jus need to give the input : 0 


```bash
printf '\xda\xce\xc0\xaf\x4f\x6f\x04\x43' | ./trust-the-yancode-easy
```

