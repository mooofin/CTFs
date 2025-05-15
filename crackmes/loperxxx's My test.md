# Reverse Engineering Writeup: Credential Extraction from Obfuscated Binary

## Introduction

This document presents a detailed analysis of a reverse engineering challenge involving a binary that implements a simple login system with anti-debugging techniques. The objective was to retrieve the correct username and password required to trigger the "Access granted" message. The approach utilized x86-64 disassembly and decompiled C++ logic to extract and verify the hidden credentials.

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

These strings suggested the presence of anti-debugging logic and a credential validation system.


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

## Final Credentials

* **Username**: `admin`
* **Password**: `password`



**Analysis Summary:**

* Anti-debugging: `IsDebuggerPresent`, `DebugBreak`, invalid handle close
* Obfuscation: XOR-based encoding of credentials
* Credential recovery: Manual decoding using XOR keys (`0x6A`, `0x65`)
* Recovered login: `admin:password`
