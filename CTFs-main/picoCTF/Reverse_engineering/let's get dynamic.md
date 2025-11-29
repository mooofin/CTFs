Looking at the assembly, uhm  the flow:

```
1. Store encoded data in buffer at [rbp-0x90]  (enc buffer)
2. Store a key in buffer at [rbp-0x50]         (key buffer)
3. Read user input into [rbp-0xd0]             (input buffer)
4. XOR transformation loop:
   result[i] = enc[i] ^ key[i] ^ i ^ 0x13
5. Compare input with result using memcmp()
6. Print message based on comparison
```



The interesting part is this loop :

```c
for (i = 0; i < len(enc); i++) {
    result[i] = enc[i] ^ key[i] ^ i ^ 0x13;
}
```

This means:
- Take a byte from the encoded buffer (`enc[i]`)
- XOR it with the corresponding key byte (`key[i]`)
- XOR it with the loop index (`i`)
- XOR it with the constant `0x13` (19 in decimal)

The result is what our input needs to match



Looking at the assembly around the comparison:

```asm
memcmp(input, result, 0x31);  // Compare buffers
test   %eax,%eax              // Check if memcmp returned 0 (match)
je     .L4                    // Jump if equal (strings match!)

// If NOT equal (didn't jump):
puts("Correct! You entered the flag.")  
mov $0, %eax
jmp end

.L4:  // If strings DO match:
puts("No, that's not right.")
mov $1, %eax
```


- When your input matches  "No, that's not right."
- When your input doesn't match  "Correct! You entered the flag."



Since XOR is its own inverse: `A ^ B ^ B = A`

If: `result[i] = enc[i] ^ key[i] ^ i ^ 0x13`

Then to find what `result` is, we just perform the XOR operation

```python
#!/usr/bin/env python3

# Encoded bytes from the .LC0 section
enc = bytes([
    0x4b, 0x6f, 0xf8, 0x60, 0xb6, 0x85, 0xbc, 0x00,
    0x5c, 0x49, 0x9c, 0x43, 0x12, 0xdb, 0x81, 0x16,
    0xb0, 0x82, 0x96, 0x28, 0x6c, 0xa7, 0xd1, 0x42,
    0xcc, 0x6e, 0x37, 0xad, 0xd4, 0x20, 0x6d, 0xf3,
    0xa2, 0xb2, 0x37, 0xd3, 0x15, 0xe7, 0xf9, 0xee,
    0xf8, 0xf0, 0xab, 0x77, 0x9c, 0xbd, 0xfd, 0x11,
    0x6f, 0x00
])

# Key from the movabsq instructions (converted to little-endian)
key_vals = [
    0x6fefc7e21f8a1428,
    0x55fff4606feb2a23,
    0x19a7901244a3ee87,
    0x8d535eae906117f6,
    0x85a0a444d075f5ce,
    0x48f6e1952ea1fdf1,
    0x0000000000000031
]

key = b''
for val in key_vals:
    key += val.to_bytes(8, 'little')  # Convert to bytes (little-endian)


flag = ''
for i in range(len(enc)):
    if i < len(key):
        flag += chr(enc[i] ^ key[i] ^ i ^ 0x13)

print(flag)
```


# aliter


```bash

gcc -o chall chall.S


gdb ./chall
(gdb) break *main+369    # Right before memcmp call
(gdb) run
muffin #any input works : 3 
(gdb) x/s $rsi           # $rsi points to the decoded buffer
```




`picoCTF{dyn4m1c_4n4ly1s_1s_5up3r_us3ful_273a6b6e}`


