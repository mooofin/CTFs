## Overview of the picoCTF Picker I Challenge  
The picoCTF Picker I challenge is a reverse engineering exercise designed to test participants' ability to analyze and manipulate compiled binaries to extract hidden flags. This challenge involves exploiting a program that allows users to execute predefined functions by name, with the goal of triggering a hidden `win` function that reveals the flag. The solution requires understanding hexadecimal encoding, function pointer manipulation, and basic Python scripting for data conversion.  

## Binary Analysis and Vulnerability Identification  
### Program Functionality and Source Code Insights  
The challenge binary presents a menu-driven interface where users can execute functions such as `getRandomNumber`. However, the critical vulnerability lies in the program’s lack of input validation: it allows users to **directly specify function names** instead of selecting from a predefined list. By analyzing the source code (or decompiled output), participants discover a hidden `win` function that prints the flag in hexadecimal format when invoked.  

### Key Observations:  
The program contains three critical elements for successful exploitation:  
1. Input handling that accepts arbitrary function names without validation  
2. A `win` function containing hex-encoded flag bytes  
3. Clear-text storage of flag components in memory  

## Solution Methodology  
### Step 1: Triggering the win Function  
Execute the program and input `win` when prompted for a function name:  

```
==> win
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d
```

### Step 2: Hexadecimal to ASCII Conversion  
Use this Python script to decode the hex values:  

```python
hex_str = "0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d"
bytes_list = [bytes.fromhex(byte.replace("0x", "")).decode('utf-8') for byte in hex_str.split()]
print(''.join(bytes_list))
```

### Step 3: Flag Extraction  
The final decoded flag will be:  
`picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}`  



