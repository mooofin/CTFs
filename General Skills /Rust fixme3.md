# XOR Decryption Challenge Writeup

## Overview

This challenge demonstrates how to decrypt an XOR-encrypted message in Rust while highlighting important memory safety concepts. The solution involves:

1. Converting hexadecimal strings to bytes
2. Decrypting using a known XOR key
3. Properly handling string manipulation in Rust
4. Addressing common compilation issues

## Solution Code


![image](https://github.com/user-attachments/assets/c09bef0a-e7a5-48c8-b250-eb3b44604157)


## Key Learning Points

### 1. Memory Safety in Rust

The original code attempted to use unsafe Rust operations unnecessarily. Rust's borrow checker ensures memory safety by:

- Enforcing ownership rules
- Validating references at compile time
- Preventing data races

### 2. XOR Cryptography Basics

XOR (exclusive OR) encryption works by:
- Applying bitwise XOR between plaintext and key
- Using the same key for encryption and decryption
- Being vulnerable to known-plaintext attacks

### 3. Error Handling Patterns

The solution demonstrates proper error handling:
- Using `Result` types for fallible operations
- The `?` operator for concise error propagation
- Boxing errors for flexibility

### 4. String Manipulation

Key string operations shown:
- Building strings efficiently with `push_str`
- Safe UTF-8 conversion with `from_utf8_lossy`
- Mutable string references for in-place modification

## Common Pitfalls

1. **Deprecation Warnings**
   - The `decrypt_vec` method is deprecated but still functional
   - Production code should use the recommended alternative

2. **Unsafe Rust Misuse**
   - Raw pointer operations were unnecessary
   - Rust provides safe alternatives for most use cases

3. **Hexadecimal Parsing**
   - Proper error handling for invalid hex digits
   - Using `from_str_radix` with proper error propagation
![image](https://github.com/user-attachments/assets/77b8a857-5c1f-4a6b-a3e6-5ba9be5491bf)
