# Writeup: Lilsan44444's Validator 

## Challenge Name and Category
**Name:** Lilsan44444's Validator  
**Category:** Reverse Engineering (Crackme)  
**Difficulty:** Easy (1.0)  
**Platform:** Windows  
**Architecture:** x86-64  

## Brief Description
This is a C++ crackme challenge compiled with g++. The goal is to either find the correct password or bypass the validation to reach the success message. The binary includes a debugger check and the password is stored in Base64 encoded form. No packers or obfuscators were used in the binary.

## Tools Used
- **Ghidra**: For static analysis and decompilation
- **Strings**: To extract interesting strings from the binary
- **Base64 decoder**: To decode the discovered password

## Initial Observations
Running the binary initially prompts for a password. Using the `strings` utility revealed several interesting strings:
- "Correct Password!" (success message)
- "Wrong Password!" (failure message)
- A Base64-encoded string (suspected to be the password)
- Strings related to debugger detection (e.g., "Debugger Detected!")

The presence of a debugger check suggested that dynamic analysis might be challenging without first understanding or patching this protection.

## Static Analysis (Ghidra)
Loading the binary into Ghidra revealed the main validation logic:
1. The program checks for an attached debugger (likely using `IsDebuggerPresent` API)
2. If no debugger is found, it prompts for user input
3. The input is compared against a Base64-encoded string stored in a local variable (`local_28` in the decompilation)
4. Based on the comparison, it either displays the success or failure message

The key discovery was the hardcoded Base64 string in the decompiled code:
```c
local_28 = "VHJ1ZFBhc3N3b3JkQnlMaWxzYW40NDQ0NA==";
```

## Dynamic Analysis
Due to the debugger check, running the binary under a debugger would trigger the anti-debugging protection. However, since we already found the password through static analysis, dynamic analysis wasn't strictly necessary for this challenge.

## Vulnerability or Logic Identified
The vulnerability in this challenge was the hardcoding of the Base64-encoded password in the binary. The lack of proper obfuscation or dynamic password generation made it trivial to extract the password through static analysis.

## Exploit or Bypass Method
The solution involved:
1. Locating the Base64-encoded password in the decompiled code (`VHJ1ZFBhc3N3b3JkQnlMaWxzYW40NDQ0NA==`)
2. Decoding the string using a Base64 decoder, which revealed: `TruePasswordByLilsan44444`
3. Entering this password when running the binary to receive the "Correct Password!" message and flag
![image](https://github.com/user-attachments/assets/30c686b6-1b2f-43f9-853f-ece0a6862166)
![image](https://github.com/user-attachments/assets/ff86f32a-2d4f-48ac-8a90-4c8fb5dc8144)



