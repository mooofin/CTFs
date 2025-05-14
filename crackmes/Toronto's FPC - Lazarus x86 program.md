
---

# CrackMe Challenge Writeup

**CrackMe ID**: `66621cc7e7b35c09bb26692e`
**Author**: SnakeG0d
**Platform**: `crackmes.one`
**Difficulty**: Easy
**Tools Used**: IDA, x64dbg, Ghidra

---

## Challenge Overview

When executed, the binary prompts the user with the message:

```
Input your passwd:
```

The program then reads user input, compares it to a hardcoded password, and prints either a success or failure message based on the result.

---

## Reverse Engineering Process

### Input Handling

At address `project1.1000072F0`, the program displays the password prompt. It then calls the input-reading function at `project1.1000078A0`:

```asm
00000001000014B4 | lea rdx, [0x10000F000]     ; buffer for user input
00000001000014C4 | call project1.1000078A0    ; read user input
```

This stores the user's input at memory address `0x10000F000`.

### Password Retrieval and Comparison

The password retrieval function at `project1.100007640` is called to return the input string, which is placed into `rax`:

```asm
00000001000014D1 | call project1.100007640
```

After that, the program loads the hardcoded string from `0x10000D030` into `rdx` and the user input into `rcx` for comparison:

```asm
00000001000014DB | lea rdx, [0x10000D030]     ; "11111"
00000001000014E2 | mov rcx, [0x10000F000]     ; user input
00000001000014E9 | call project1.1000029A0    ; compare strings
```

The comparison function behaves as follows:

* If the strings differ in length: returns `len(input) - len("11111")`
* If the strings have the same length:

  * Returns `1` if `input > "11111"`
  * Returns `-1` if `input < "11111"`
  * Returns `0` if equal

The result is stored in `rax`. The following check is performed:

```asm
00000001000014EE | test rax, rax
00000001000014F1 | jne project1.100001523    ; jump to failure message if rax != 0
```

If `rax` is zero (input equals "11111"), execution proceeds to a success message via `project1.1000072F0`. Otherwise, it jumps to a failure message (`project1.100001523`), which prints `"= Not ;-( "`.

---

## Conclusion

By statically analyzing the binary, we discovered that the password is hardcoded as `"11111"`. Supplying this input causes the program to print a congratulatory message, confirming successful reverse engineering and challenge completion.

**Password**: `11111`
**Result**: Success Message Triggered


![image](https://github.com/user-attachments/assets/28df424f-d798-4978-8c99-fc4f88ba6b54)

![image](https://github.com/user-attachments/assets/1730d912-60c7-4786-b190-dc62d8129427)

