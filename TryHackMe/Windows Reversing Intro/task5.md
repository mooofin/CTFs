# Reverse Engineering Write-up: `Loop.exe` Analysis

## Objective

The goal of this exercise is to reverse engineer a binary executable, `Loop.exe`, using IDA Pro to understand how it processes input and utilizes a loop to perform character analysis.

## Initial Observation

Upon execution, the program prompts for user input, counts the number of lowercase letters in the input string, and then prints the result. While this can be inferred from the output behavior alone, the purpose of the analysis is to understand *how* it performs this internally.

## Using IDA

After loading `Loop.exe` into IDA and navigating to the `main()` function, it is clear that the function is relatively large. IDA's Graph View is particularly helpful in understanding the control flow.

### Skimming for Relevance

The upper portion of the function primarily consists of setup and printing functions. These can be skimmed initially, but it's important to return to them if clarity is needed later. The real analysis begins near the bottom of the first major block—where the loop is initialized.

## Loop Initialization

The loop setup involves the following key observations:

* `mov rsi, [rsp+58h+var_20]`: RSI is loaded with a value from the stack.
* `test rdx, rdx` followed by `jz`: This checks if `RDX` is zero, and if so, skips the loop.
* Based on surrounding instructions, it's inferred that:

  * `RDI` contains the buffer (user input),
  * `RDX` holds the length of the string,
  * `RSI` is set to `0xF`, possibly for input validation purposes.

## Identifying the Loop Counter

At the bottom of the loop, the instruction:

```
inc     rcx
```

reveals that `RCX` is the loop counter. It is compared against `RDX` (string length) to determine whether the loop should continue:

```
cmp     rcx, rdx
jb      loc_loop_start
```

This confirms that the loop iterates over each character in the input string.

## Loop Logic

The loop has two main decision points:

1. **First Block**:

   * `RAX` is assigned the address of the string.
   * The current character is checked against `'a'` (ASCII 0x61).
   * If less, it jumps to the loop end, skipping further processing.

2. **Second Block**:

   * The character is then checked against `'z'` (ASCII 0x7A).
   * If greater, it jumps to the loop end.
   * If the character is between `'a'` and `'z'`, it is lowercase, and:

     * `inc rbx` is executed, incrementing the lowercase count stored in `RBX`.

## Post-loop Analysis

After the loop completes, the result stored in `RBX` is printed. Additional code checks `RSI` against `0x10` and calls error handling functions if needed. This indicates `RSI` is used for some form of internal or compiler-generated parameter validation, unrelated to the loop logic.

## Summary

* The loop iterates over each character in the user-provided string.
* `RCX` is the loop counter, confirmed by the instruction `inc rcx`.
* `RBX` holds the count of lowercase characters, incremented conditionally.
* `RDX` represents the length of the input string.
* The logic filters characters based on ASCII ranges for `'a'` to `'z'`.

## Key Instruction Identified

To determine the loop counter, the critical instruction is:

```
inc     rcx
```

This clearly indicates `RCX` is being used to index through the input string.


