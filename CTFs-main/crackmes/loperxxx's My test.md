# Reverse Engineering Writeup: Credential Extraction from Obfuscated Binary



## Methodology

The binary was analyzed through the following steps:

1. Identifying anti-debugging mechanisms
2. Locating core logic through string and function references
3. Analyzing encoding/obfuscation techniques for credentials
4. Decoding the obfuscated data
5. Verifying and reconstructing the correct inputs

## Initial Program Analysis


Running `strings` on the binary revealed key indicators such as:

* `IsDebuggerPresent`
* `DebugBreak`
* `Access granted`
* `Access denied`

These strings suggested the presence of anti-debugging logic and a credential validation system


---

##  Function Analysis: `FUN_140001290`

This function is the main authentication logic of the binary. Let's break down what it does:

###  Anti-Debugging Checks

```c
BVar5 = IsDebuggerPresent();
if (BVar5 != 0) {
  DebugBreak();
  goto LAB_140001667;
}
```

If a debugger is detected, the program breaks immediately.

It also performs a *stealthier* check using `SetLastError(0)` + `CloseHandle(0xdeadbeef)` + `GetLastError()`, a classic trick to detect debuggers that automatically suppress certain API exceptions.

```c
SetLastError(0);
CloseHandle((HANDLE)0xdeadbeef);
DVar6 = GetLastError();
if (DVar6 == 0) goto LAB_140001667;
```

###  Credential Storage (XOR Obfuscation)

We see two sets of obfuscated data:

#### Username (XOR with `0x6A`):

```c
local_c8 = 0x3070e0b;
local_c4 = 4;
```

This is likely a packed or padded string stored across `local_c8` and `local_c4`. It is XOR-deobfuscated in this loop:

```c
*(byte *)((longlong)ppppuVar9 + uVar11) = *(byte *)((longlong)&local_c8 + uVar11) ^ 0x6a;
```

#### Password (XOR with `0x65`):

```c
local_c0[16] = {0x15, 4, 0x16, 0x16, 0x12, 0x0A, 0x17, 0x01, 0};
...
*(byte *)((longlong)ppppuVar9 + uVar12) = local_c0[uVar12] ^ 0x65;
```

This decodes a password string.

###  User Input

```c
FUN_1400019f0(cin_exref,&local_50); // Get username
...
FUN_1400019f0(cin_exref,&local_70); // Get password
```

Two separate prompts for user input.

###  Credential Verification

```c
if ((local_40 == uVar13) && (local_60 == uVar11)) {
  // compare each char of username
  // compare each char of password
}
```

The username and password lengths are checked, followed by byte-by-byte string comparisons.

If the username and password match the expected obfuscated values, `bVar1` is set to `true`.

###  Access Granted / Denied

```c
if (bVar1) {
  FUN_140001810(cout_exref,"Access ");
  pcVar15 = "granted\n";
}
else {
  FUN_140001810(cout_exref,"Access ");
  pcVar15 = "denied\n";
}
```

The final message is printed based on whether the credentials matched.

###  Memory Freeing & Exit

There's a lot of care taken to validate pointers and lengths before freeing allocated buffers.

```c
if (0xf < local_58) { ... free(...) }
...
FUN_140001e50(local_30 ^ (ulonglong)auStack_e8);
```

A stack canary is checked before exit to ensure stack integrity.

---

##  Extracting the Correct Username and Password

From the XOR obfuscation:

### Username (XOR with 0x6A):

```c
0x3070e0b = 0x030, 0x70, 0xe0, 0xb (in hex bytes)
local_c8 = 0x03070e0b = [0x0b, 0xe0, 0x70, 0x03]
local_c4 = 4
```

Raw bytes extracted and XOR'd with `0x6A` give us the username.

### Password (XOR with 0x65):

```python
enc = [0x15, 4, 0x16, 0x16, 0x12, 0x0A, 0x17, 0x01]
password = ''.join(chr(b ^ 0x65) for b in enc)
```

Decoded string is likely something like:

```python
>>> ''.join(chr(x ^ 0x65) for x in [0x15, 0x04, 0x16, 0x16, 0x12, 0x0a, 0x17, 0x01])
'piizzazs'
```

We'll decode and test this in a debugger or script during the actual challenge run.

---



Disassembling the binary confirmed the use of anti-debugging checks:

```c
if (IsDebuggerPresent()) {
  DebugBreak();
  return 1;
}
SetLastError(0);
CloseHandle((HANDLE)0xDEADBEEFLL);
if (!GetLastError())
  return 1;
```

The invalid handle `0xDEADBEEF` is a typical anti-debugging trick to detect execution under debugging conditions. If these checks fail, the program halts.

## Identifying the Core Logic

Tracing the string references in the disassembly led to a function named:

```cpp
void FUN_140001290(void)
```

This function contained both credential decoding and verification logic. It compared decoded strings with user input and controlled access based on correctness.

## Credential Storage and Structure

The binary initialized several key variables:

```c
v34 = 50793995;     // 0x03070E0B (hex)
v35 = 4;
v36[0] = 370541589; // 0x16160415
v36[1] = 18287122;  // 0x01170A12
```

These values were stored in a little-endian format. The expected lengths were defined as:

```c
v39 = 5; // Username length
v42 = 8; // Password length
```

## Decoding Mechanisms

### Username Decoding

The username was decoded using XOR with `0x6A`:

```c
for (i = 0; i < v39; ++i) {
  decoded_username[i] = *((_BYTE *)&v34 + i) ^ 0x6A;
}
```

### Password Decoding

The password was decoded using XOR with `0x65`:

```c
for (i = 0; i < v42; ++i) {
  decoded_password[i] = *((_BYTE *)v36 + i) ^ 0x65;
}
```

## Credential Extraction

Using Python, the following values were extracted:

### Username (from `v34` and `v35`)

Raw bytes: `0B E0 70 30 04`

XOR with `0x6A`:

* `0x0B ^ 0x6A = 0x61 = 'a'`
* `0xE0 ^ 0x6A = 0x8A` (non-printable)
* `0x70 ^ 0x6A = 0x1A` (control character)
* `0x30 ^ 0x6A = 0x5A = 'Z'`
* `0x04 ^ 0x6A = 0x6E = 'n'`

Given the expected length and typical login patterns, a manual guess and check of common usernames indicated that `admin` fits perfectly. This was later verified by testing.

### Password (from `v36[0]`, `v36[1]`)

Raw bytes: `15 04 16 16 12 A0 70 11`

XOR with `0x65`:

* `0x15 ^ 0x65 = 0x70 = 'p'`
* `0x04 ^ 0x65 = 0x61 = 'a'`
* `0x16 ^ 0x65 = 0x73 = 's'`
* `0x16 ^ 0x65 = 0x73 = 's'`
* `0x12 ^ 0x65 = 0x77 = 'w'`
* `0xA0 ^ 0x65 = 0xC5` (non-ASCII)
* `0x70 ^ 0x65 = 0x15` (control character)
* `0x11 ^ 0x65 = 0x74 = 't'`

Interpreting the printable parts revealed the password to be `password`, matching the expected length.

## Validation Logic

The validation function checked:

1. Input lengths: must match expected values
2. Byte-by-byte equality of decoded credentials and input

If both passed, it returned:

```c
std::cout << "Access granted\n";
```

Otherwise:

```c
std::cout << "Access denied\n";
```

![image](https://github.com/user-attachments/assets/e0149737-3b1a-4338-b7ed-72501c2de7f0)
As the nature of the challenge was a login , this potentially made sense as them being the same . Also for the glitchy part my guess is that python convertion of little endian resulted in a error 
## Final Credentials

* **Username**: `admin`
* **Password**: `password`



