# Analysis of ARMv8 Assembly Code

This is an ARMv8 assembly program with two functions: `func1` and `main`. Let me break it down in detail.

## Function `func1`

```assembly
func1:
        sub     sp, sp, #32             ; Allocate 32 bytes on stack
        str     w0, [sp, 12]            ; Store input argument (w0) at sp+12
        str     wzr, [sp, 24]           ; Initialize [sp+24] to 0 (wzr is zero register)
        str     wzr, [sp, 28]           ; Initialize [sp+28] to 0
        b       .L2                      ; Jump to loop condition check
.L3:                                    ; Loop body:
        ldr     w0, [sp, 24]            ; Load value from [sp+24] into w0
        add     w0, w0, 3               ; Add 3 to w0
        str     w0, [sp, 24]            ; Store result back to [sp+24]
        ldr     w0, [sp, 28]            ; Load value from [sp+28] into w0
        add     w0, w0, 1               ; Increment by 1
        str     w0, [sp, 28]            ; Store result back to [sp+28]
.L2:                                    ; Loop condition:
        ldr     w1, [sp, 28]            ; Load [sp+28] into w1 (counter)
        ldr     w0, [sp, 12]            ; Load original input into w0
        cmp     w1, w0                  ; Compare counter with input
        bcc     .L3                      ; Branch if counter < input (unsigned comparison)
        ldr     w0, [sp, 24]            ; Load final value from [sp+24] into return register
        add     sp, sp, 32              ; Deallocate stack space
        ret                              ; Return
```

### What `func1` does:
- Takes one integer input (in w0)
- Initializes two variables to 0 (let's call them `sum` at [sp+24] and `i` at [sp+28])
- Loops `i` from 0 to input-1
- In each iteration, adds 3 to `sum` and increments `i` by 1
- Returns `sum` (which will be 3 * input)

In C, this would be equivalent to:
```c
int func1(int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += 3;
    }
    return sum;
}
```

## Function `main`

```assembly
main:
        stp     x29, x30, [sp, -48]!    ; Store frame pointer and link register, allocate 48 bytes
        add     x29, sp, 0              ; Set up frame pointer
        str     w0, [x29, 28]           ; Store argc
        str     x1, [x29, 16]           ; Store argv
        ldr     x0, [x29, 16]           ; Load argv
        add     x0, x0, 8               ; Get argv[1] (skip argv[0])
        ldr     x0, [x0]                ; Load the string at argv[1]
        bl      atoi                     ; Convert string to integer
        bl      func1                    ; Call func1 with the converted integer
        str     w0, [x29, 44]           ; Store result from func1
        adrp    x0, .LC0                ; Get address of format string "Result: %ld\n"
        add     x0, x0, :lo12:.LC0       ; Complete address calculation
        ldr     w1, [x29, 44]           ; Load result as printf argument
        bl      printf                   ; Print the result
        nop                              ; No operation (alignment/padding)
        ldp     x29, x30, [sp], 48      ; Restore frame pointer and link register
        ret                              ; Return
```

### What `main` does:
1. Sets up the stack frame
2. Takes command line arguments (argc in w0, argv in x1)
3. Gets the first command line argument (argv[1])
4. Converts it to an integer using `atoi`
5. Calls `func1` with that integer
6. Prints the result using printf with format "Result: %ld\n"
7. Cleans up and returns

## Program Summary

This program:
1. Takes a number as command line argument
2. Multiplies it by 3 (using repeated addition in a loop)
3. Prints the result

The assembly shows typical ARMv8 conventions:
- w registers are 32-bit (x registers are 64-bit)
- Function arguments passed in w0-x7
- Return value in w0/x0
- Stack grows downward (subtract to allocate space)
- Function prologues/epilogues that save/restore registers




### Given Input

The input argument is `2610164910`. We need to compute `3 * 2610164910` and determine how it's represented as a 32-bit signed integer, then convert that to hexadecimal.

### Calculating `3 * 2610164910`

First, compute the exact mathematical product:
```
2610164910 * 3 = 7830494730
```

### 32-bit Integer Representation

A 32-bit signed integer can represent values from `-2,147,483,648` to `2,147,483,647`. Our result `7,830,494,730` is larger than `2,147,483,647`, so it will overflow and wrap around.

To find the actual 32-bit representation:

1. Compute `7830494730 mod 2³²`:
   - `2³² = 4,294,967,296`
   - `7830494730 ÷ 4294967296 = 1` with a remainder.
   - `7830494730 - 4294967296 = 3535527434`

2. Now, `3535527434` is still larger than `2,147,483,647`, so as a **signed 32-bit integer**, this represents a negative number. To find its signed value:
   - `3535527434 - 4294967296 = -759439862`

So, the 32-bit signed integer representation of `7830494730` is `-759439862`.

The program prints the result as a signed 32-bit integer, which is `-759439862`, represented in 32-bit hexadecimal as `d2bbde0a`.

**Flag:** `picoCTF{d2bbde0a}`
