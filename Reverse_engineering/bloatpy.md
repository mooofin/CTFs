# picoCTF 2022 - Reverse Engineering Challenge Writeup

## Introduction

picoCTF 2022 concluded a month ago and was an exciting competition, especially for beginners looking to learn about Capture The Flag (CTF) challenges. This writeup covers one of the Reverse Engineering challenges in the competition, analyzing its structure, deobfuscating the code, and ultimately retrieving the flag.

## Challenge Overview

The challenge provides us with:
- A Python program (`challenge.py`) in its source code form
- An encrypted flag (`flag.txt.enc`)

Our objective is to reverse-engineer the Python program to decrypt and retrieve the flag.

## File Analysis

### Reviewing the Source Code

Upon opening the Python file, we notice that the code is obfuscated. The script uses an unusual method to construct strings, making it difficult to read. Specifically, the variable `a` is a long string containing various characters, which the program accesses using array notation to extract specific characters.

### Understanding the Obfuscation

To make sense of the script, let's analyze the function `arg133`, which contains a conditional statement:

```python
if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]:
```

By extracting the corresponding characters from `a`, we determine that it checks whether the user input is equal to `happychance`.

Similarly, we analyze other functions and rename them to more meaningful names for better readability.

## Deobfuscated Code Structure

1. **Reading the Encrypted Flag**
   - The script opens `flag.txt.enc` and reads its contents into `arg444`.

2. **User Input Validation**
   - The program prompts the user to enter a string (`arg432`).
   - If the user does not input `happychance`, the program exits.

3. **Decryption Process**
   - If the correct input (`happychance`) is provided, the script decrypts the flag using the `decoder()` function.

4. **Flag Display**
   - The decrypted flag is printed to the console.

## Extracting the Flag

1. **Manually provide the required input:**
   ```sh
   python challenge.py
   ```
   Enter `happychance` when prompted.

2. **The script will proceed to decrypt and print the flag.**

