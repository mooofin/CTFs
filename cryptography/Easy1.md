

## Challenge Description
This PicoCTF challenge requires us to decrypt a cipher using a one-time pad (OTP). While OTP encryption is theoretically unbreakable, it becomes solvable if the key is known. We are provided with an encrypted flag `UFJKXQZQUNB` and a key `SOLVECRYPTO`. Additionally, the challenge provides a table for decryption.

### Given Data:
- **Encrypted Flag:** `UFJKXQZQUNB`
- **Key:** `SOLVECRYPTO`
- **Table:** `table.txt` (provided below)

## Understanding the One-Time Pad (OTP)
A one-time pad encrypts a message by pairing each character of the plaintext with a corresponding key character using modular addition. The modular addition follows the modulo 26 system (since the alphabet consists of 26 letters). The decryption process involves reversing this operation using modular subtraction.

### Decryption Process
To decrypt the message, we perform modular subtraction:
- Subtract the ASCII values of the corresponding key and ciphertext characters.
- Adjust the result to stay within the valid range of capital letters ('A' to 'Z').
- Convert the resulting numbers back to characters.

### Python Script for Decryption
We can automate the decryption process using the following Python script:

```python
#!/usr/bin/env python

"""
This script decrypts the encrypted flag using modular subtraction
from the one-time pad (OTP) encryption.

Usage: python3 script.py
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "SOLVECRYPTO"
encrypted_flag = "UFJKXQZQUNB"

def modular_subtraction(encrypted_flag):
    res = ""
    for i in range(len(encrypted_flag)):
        if (ord(encrypted_flag[i]) - ord(key[i])) >= 0:
            res += chr(ord(encrypted_flag[i]) - ord(key[i]) + 65)
        else:
            res += chr(ord(encrypted_flag[i]) - ord(key[i]) + 91)
    return res

print("And the flag is: picoCTF{" + modular_subtraction(encrypted_flag) + "}")
```

### Explanation of the Script
1. **Modular Subtraction:** The script iterates over each character in the encrypted flag and its corresponding key character. It subtracts their ASCII values.
2. **Wrap-Around Logic:** If the result is negative, it adjusts using `+91` to ensure it remains within the alphabet's range.
3. **Final Output:** The decrypted message is returned in the format `picoCTF{decrypted_text}`.

### Table for Decryption
The provided table is a traditional Vigenère cipher table, where each row represents a shifted version of the alphabet:

```
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
   +----------------------------------------------------
A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```

## Conclusion
This challenge demonstrates a fundamental cryptographic weakness: **OTP encryption is only secure if the key is used once and remains secret**. By knowing the key, we were able to reverse the encryption using modular subtraction. The provided Python script automates the decryption, revealing the original flag in the required format.

