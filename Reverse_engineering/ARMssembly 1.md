# Assembly Challenge Writeup

## Overview
This challenge involves analyzing an x86-64 assembly program that takes an integer input and determines whether the user wins or loses based on specific arithmetic operations. The goal is to determine the correct input that results in a "You win!" message.

## Assembly Code Analysis

### Function: `func`
This function takes an integer argument `X` and performs the following operations:
1. Initializes specific memory locations with constants.
2. Performs a left shift operation.
3. Executes an integer division.
4. Subtracts the input value `X` from the result.
5. Returns the final computed value.

#### Step-by-Step Breakdown:
```assembly
.intel_syntax noprefix
.section .text
.globl func
.type func, @function
func:
    push    rbp                   // Save base pointer
    mov     rbp, rsp               // Set base pointer to current stack pointer
    sub     rsp, 32                // Allocate 32 bytes on stack for local variables
    mov     DWORD PTR [rbp+12], edi // Store argument X (passed in edi) at rbp+12
    mov     DWORD PTR [rbp+16], 68  // Store constant 68 at rbp+16
    mov     DWORD PTR [rbp+20], 2   // Store constant 2 at rbp+20
    mov     DWORD PTR [rbp+24], 3   // Store constant 3 at rbp+24
    
    mov     eax, DWORD PTR [rbp+16] // Load value at rbp+16 (68) into eax
    mov     ecx, DWORD PTR [rbp+20] // Load value at rbp+20 (2) into ecx
    shl     eax, cl                 // Left shift eax by cl (2 bits), eax = 68 << 2 = 272
    mov     DWORD PTR [rbp+28], eax // Store result (272) at rbp+28
    
    mov     eax, DWORD PTR [rbp+28] // Load rbp+28 (272) into eax
    mov     ecx, DWORD PTR [rbp+24] // Load rbp+24 (3) into ecx
    cdq                             // Sign-extend eax into edx:eax (EDX:EAX = 0:272)
    idiv    ecx                     // Integer division (EDX:EAX) ÷ ECX → (0:272) ÷ 3
                                    // Quotient = 90 → stored in eax
                                    // Remainder = 2 → stored in edx
    mov     DWORD PTR [rbp+28], eax // Store quotient (90) at rbp+28
    
    mov     eax, DWORD PTR [rbp+28] // Load rbp+28 (90) into eax
    sub     eax, DWORD PTR [rbp+12] // Subtract X (rbp+12) from eax (90 - X)
    mov     DWORD PTR [rbp+28], eax // Store result (90 - X) at rbp+28
    
    mov     eax, DWORD PTR [rbp+28] // Load rbp+28 into eax (final result)
    add     rsp, 32                 // Restore stack pointer
    pop     rbp                      // Restore base pointer
    ret                              // Return from function
```

### Function: `main`
This function handles command-line input and calls `func(X)`, checking if the result is zero.

#### Step-by-Step Breakdown:
```assembly
.text
.globl main
.type main, @function
main:
    push    rbp                      // Save base pointer
    mov     rbp, rsp                  // Set base pointer to current stack pointer
    sub     rsp, 48                   // Allocate 48 bytes on stack for local variables
    
    mov     DWORD PTR [rbp+28], edi   // Store argument count (argc) at rbp+28
    mov     QWORD PTR [rbp+16], rsi   // Store argument vector (argv) at rbp+16
    
    mov     rax, QWORD PTR [rbp+16]   // Load argv pointer into rax
    add     rax, 8                    // Move to argv[1]
    mov     rdi, QWORD PTR [rax]      // Load argv[1] (string argument) into rdi
    call    atoi                      // Convert argv[1] to integer
    mov     DWORD PTR [rbp+44], eax   // Store converted integer at rbp+44
    
    mov     edi, DWORD PTR [rbp+44]   // Move integer argument into edi
    call    func                      // Call func(X)
    test    eax, eax                  // Check if result is zero (eax == 0)
    jne     .L4                        // If not zero, jump to losing condition
    
    lea     rdi, .LC0[rip]            // Load address of "You win!" string into rdi
    call    puts                      // Print "You win!"
    jmp     .L6                        // Jump to function exit
.L4:
    lea     rdi, .LC1[rip]            // Load address of "You Lose :(" string into rdi
    call    puts                      // Print "You Lose :("
.L6:
    nop                               // No operation (padding instruction)
    add     rsp, 48                   // Restore stack pointer
    pop     rbp                        // Restore base pointer
    ret                               // Return from main
```

## Finding the Winning Input
The `func` function calculates the value `90 - X`. The program prints "You win!" if the result is `0`, meaning:

```
90 - X = 0
X = 90
```

Thus, the correct input to win is `90`.

## Flag Calculation
The flag format is `picoCTF{XXXXXXXX}`, where `XXXXXXXX` is a 32-bit hex value of `90`.

```
90 in hexadecimal = 0x5A
Zero-padded 32-bit representation = 0000005A
```

Final flag:
```
picoCTF{0000005a}
```
# Assembly Challenge Writeup

## Assembly Code Analysis

```assembly
.intel_syntax noprefix
.section .text
.globl func
.type func, @function
func:
    push    rbp                   // Save base pointer
    mov     rbp, rsp               // Set base pointer to current stack pointer
    sub     rsp, 32                // Allocate 32 bytes on stack for local variables
    mov     DWORD PTR [rbp+12], edi // Store argument X (passed in edi) at rbp+12
    mov     DWORD PTR [rbp+16], 68  // Store constant 68 at rbp+16
    mov     DWORD PTR [rbp+20], 2   // Store constant 2 at rbp+20
    mov     DWORD PTR [rbp+24], 3   // Store constant 3 at rbp+24
    
    mov     eax, DWORD PTR [rbp+16] // Load value at rbp+16 (68) into eax
    mov     ecx, DWORD PTR [rbp+20] // Load value at rbp+20 (2) into ecx
    shl     eax, cl                 // Left shift eax by cl (2 bits), eax = 68 << 2 = 272
    mov     DWORD PTR [rbp+28], eax // Store result (272) at rbp+28
    
    mov     eax, DWORD PTR [rbp+28] // Load rbp+28 (272) into eax
    mov     ecx, DWORD PTR [rbp+24] // Load rbp+24 (3) into ecx
    cdq                             // Sign-extend eax into edx:eax (EDX:EAX = 0:272)
    idiv    ecx                     // Integer division (EDX:EAX) ÷ ECX → (0:272) ÷ 3
                                    // Quotient = 90 → stored in eax
                                    // Remainder = 2 → stored in edx
    mov     DWORD PTR [rbp+28], eax // Store quotient (90) at rbp+28
    
    mov     eax, DWORD PTR [rbp+28] // Load rbp+28 (90) into eax
    sub     eax, DWORD PTR [rbp+12] // Subtract X (rbp+12) from eax (90 - X)
    mov     DWORD PTR [rbp+28], eax // Store result (90 - X) at rbp+28
    
    mov     eax, DWORD PTR [rbp+28] // Load rbp+28 into eax (final result)
    add     rsp, 32                 // Restore stack pointer
    pop     rbp                      // Restore base pointer
    ret                              // Return from function

    .section .rodata
    .align 8
.LC0:
    .string "You win!"              // String for winning message
    .align 8
.LC1:
    .string "You Lose :("           // String for losing message

    .text
    .globl main
    .type main, @function
main:
    push    rbp                      // Save base pointer
    mov     rbp, rsp                  // Set base pointer to current stack pointer
    sub     rsp, 48                   // Allocate 48 bytes on stack for local variables
    
    mov     DWORD PTR [rbp+28], edi   // Store argument count (argc) at rbp+28
    mov     QWORD PTR [rbp+16], rsi   // Store argument vector (argv) at rbp+16
    
    mov     rax, QWORD PTR [rbp+16]   // Load argv pointer into rax
    add     rax, 8                    // Move to argv[1]
    mov     rdi, QWORD PTR [rax]      // Load argv[1] (string argument) into rdi
    call    atoi                      // Convert argv[1] to integer
    mov     DWORD PTR [rbp+44], eax   // Store converted integer at rbp+44
    
    mov     edi, DWORD PTR [rbp+44]   // Move integer argument into edi
    call    func                      // Call func(X)
    test    eax, eax                  // Check if result is zero (eax == 0)
    jne     .L4                        // If not zero, jump to losing condition
    
    lea     rdi, .LC0[rip]            // Load address of "You win!" string into rdi
    call    puts                      // Print "You win!"
    jmp     .L6                        // Jump to function exit
.L4:
    lea     rdi, .LC1[rip]            // Load address of "You Lose :(" string into rdi
    call    puts                      // Print "You Lose :("
.L6:
    nop                               // No operation (padding instruction)
    add     rsp, 48                   // Restore stack pointer
    pop     rbp                        // Restore base pointer
    ret                               // Return from main
```



