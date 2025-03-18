**Reverse Engineering and Decoding ROT47 Cipher**

## Introduction
In this write-up, we will analyze a Python script that encodes and stores a secret using the ROT47 cipher. Our objective is to reverse engineer the encryption and recover the hidden message.

## Code Analysis

The given Python script consists of two main functions:
1. `decode_secret(secret)`: This function implements ROT47 decryption.
2. `choose_greatest()`: A function that takes two user inputs and returns the greater value.

The most interesting part of the script is the `decode_secret(secret)` function, which applies the ROT47 cipher to a hidden string `bezos_cc_secret`.

### Understanding ROT47 Cipher
ROT47 is a simple encryption algorithm that shifts ASCII characters by 47 places within a specific range (33 to 126). The key property of ROT47 is that encryption and decryption are identical operations.

The reference alphabet in the script includes a range of printable ASCII characters:
```python
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
```

The function iterates through each character in `secret`, finds its position in `alphabet`, and shifts it by 47 places cyclically.

### Deciphering the Secret

The `bezos_cc_secret` variable is given as:
```
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0cdhb52g2N"
```
By passing this through the `decode_secret()` function, we can obtain the original, unencrypted string.

### Exploiting the ROT47 Function
Since ROT47 encoding and decoding are the same, we can use the function as is to retrieve the hidden information:
```python
decode_secret("A:4@r%uL`M-^M0c0AbcM-MFE0cdhb52g2N")
```
This will output the original hidden message.


