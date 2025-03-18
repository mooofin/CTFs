# PicoCTF 2024 - Serpentine Encourager Writeup

## Challenge Description

In this challenge, we are provided with a Python script named `serpentine.py` that presents a simple menu-based interface. One of the menu options is to print the flag, but selecting that option results in an error message:

```
Oops! I must have misplaced the print_flag function! Check my source code!
```

This suggests that the function to print the flag exists in the source code but is either commented out or not properly defined.

## Running the Script

To execute the script, we use the following command in a terminal:

```sh
python3 serpentine.py
```

Upon running, we see an ASCII art followed by a menu with three options:

```
a) Print encouragement
b) Print flag
c) Quit
```

Choosing option `b` prints the error message mentioned above. Since the challenge hints at checking the source code, we need to inspect it for any hidden logic.

## Analyzing the Source Code

After opening `serpentine.py`, we find that there is indeed a `print_flag` function, but it is not being executed due to a missing reference. Upon further analysis, we discover an encrypted flag stored in a variable, `flag_enc`, and a function `str_xor` used to decrypt it.

### Extracting the Flag

We reconstruct the decryption logic using the extracted `flag_enc` values and the XOR decryption function. The key used in the function is `'enkidu'`. Below is the decryption script:

```python
flag_enc = [
    0x15, 0x07, 0x08, 0x06, 0x27, 0x21, 0x23, 0x15, 0x5c, 0x01, 0x57, 0x2a, 0x17, 0x5e, 0x5f, 0x0d,
    0x3b, 0x19, 0x56, 0x5b, 0x5e, 0x36, 0x53, 0x07, 0x51, 0x18, 0x58, 0x05, 0x57, 0x11, 0x3a, 0x56,
    0x0e, 0x5d, 0x53, 0x11, 0x54, 0x5c, 0x53, 0x14
]

def str_xor(enc_data, key):
    key_length = len(key)
    return ''.join(chr(enc_data[i] ^ ord(key[i % key_length])) for i in range(len(enc_data)))

key = "enkidu"
decrypted_flag = str_xor(flag_enc, key)
print(decrypted_flag)
```

### Decrypted Flag

Executing the script gives us the flag:

```
picoCTF{7h3_r04d_l355_7r4v3l3d_8e47d128}
```

