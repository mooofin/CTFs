# PicoCTF 2022 - bbbloat Writeup

## Introduction
The challenge **bbbbloat** was part of **picoCTF 2022**, categorized under **Reverse Engineering**. In this challenge, we were given a binary file `bbbbloat`, and our goal was to analyze it and extract the hidden flag.

## Initial Reconnaissance
Before diving into reverse engineering, let's check the file type and permissions:

```bash
$ file bbbloat
bbbbloat: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux)
```

From this, we confirm that `bbbbloat` is a **64-bit ELF executable** built for Linux.

Next, let's check its security properties:

```bash
$ checksec --file=bbbbloat
```

This helps us determine if there are protections like **NX (No eXecute), PIE (Position Independent Executable), Canary, or RELRO** enabled.

Running the binary directly gives the following prompt:

```bash
$ ./bbbbloat

What's my favorite number?
```

Entering a random number results in:

```bash
Sorry, that's not it!
```

This suggests that the program is verifying the input against a specific number.

## Static Analysis with Ghidra
Since the binary is compiled, we decompile it using **Ghidra** to analyze its functions. The primary function of interest is:

### **Function Analysis: `FUN_00101307`**
This function prompts the user to enter a number and compares it against a predefined value.

#### **Important Code Snippet (Decompiled)**
```c
undefined8 FUN_00101307(void)
{
  long in_FS_OFFSET;
  int local_48;
  undefined4 local_44;
  char *local_40;
  char local_38 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  builtin_strncpy(local_38,"A:4@r%uL4Ff0f9b03=_cf0cc7fc2e_N",0x20);
  local_44 = 0xd2c49;
  printf("What\'s my favorite number? ");
  local_44 = 0xd2c49;
  __isoc99_scanf(&DAT_00102020,&local_48);
  local_44 = 0xd2c49;
  if (local_48 == 0x86187) {
    local_44 = 0xd2c49;
    local_40 = FUN_00101249(0,local_38);
    fputs(local_40,stdout);
    putchar(10);
    free(local_40);
  }
  else {
    puts("Sorry, that\'s not it!");
  }
  return 0;
}
```

#### **Key Observations**
- The user input (`local_48`) is compared against **0x86187** (hexadecimal for **549255** in decimal).
- If the input matches, the function **FUN_00101249** is executed with `local_38` as an argument.
- The string in `local_38` seems obfuscated: `A:4@r%uL4Ff0f9b03=_cf0cc7fc2e_N`.
- The output is printed using `fputs`.

## Extracting the Flag
From our analysis, we conclude that the correct input is **549255**. Running the program with this input:

```bash
$ ./bbbbloat
What's my favorite number? 549255
picoCTF{cu7_7h3_bl047_44f74a60}
```

We successfully retrieve the flag!

## Conclusion
This challenge demonstrated basic **reverse engineering techniques**, including:
- **Static analysis** with Ghidra to inspect function logic.
- **Understanding assembly and decompiled C code** to identify key comparisons.
- **Extracting hidden conditions** to bypass input validation and reveal the flag.

### **Final Flag:**
```
picoCTF{cu7_7h3_bl047_44f74a60}
```

