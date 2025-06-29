In this challenge, I was presented with an encryption service claiming to use a one-time pad (OTP). Upon connecting to the server, I was greeted with a message showing a ciphertext — the encrypted flag — and a prompt asking what data I’d like to encrypt. This immediately suggested the possibility of a chosen-plaintext attack, where I could send inputs of my choice and observe how they were encrypted.

The first thing to note is that a one-time pad is only secure under strict conditions: the key must be truly random, as long as the message, and — most importantly — it must never be reused. If the same portion of the key is ever used twice, the OTP becomes trivially breakable. This challenge revolved around the failure of that last condition.
![screenshot-1751183097](https://github.com/user-attachments/assets/30b7980f-5b00-4807-ae11-ba0642ecb1e0)

Internally, the challenge had a bug in the way it managed key usage. Specifically, if you sent enough data to exhaust the key’s length, the system would wrap around and reuse the beginning of the key again. This is because of a modulo operation in the indexing logic — once the internal key pointer exceeded the key length, it reset to zero. That meant I could send a long filler string to roll the key pointer forward, and then send a message of the same length as the flag, which would now be encrypted using the same key segment as the flag was.

To exploit this, I first connected to the server and retrieved the hex-encoded encrypted flag. I calculated the number of bytes in the flag by halving the length of the hex string. Then I sent a long filler input (`"a"` repeated `50000 - flag_len` times) to advance the internal key pointer to the end. My next input — a known plaintext of `"a"` repeated `flag_len` times — would be encrypted using the same key that was used on the flag.

Now that I had a known plaintext and its ciphertext, I XORed them to recover the key segment. With this key segment in hand, I XORed it against the encrypted flag to recover the original plaintext flag. This worked because in OTP: `ciphertext = plaintext XOR key`, so reversing the operation is simply `plaintext = ciphertext XOR key`.


```
picoCTF{7f9da29f40499a98db220380a57746a4}
```
```python
#!/usr/bin/env python3
from pwn import *

# Configuration: remote challenge host and port
host = 'mercury.picoctf.net'
port = 36981

# XOR helper: takes list of ciphertext ints and string message, returns XOR result
def xor_list_str(a, b):
    return ''.join([chr(p ^ ord(k)) for p, k in zip(a, b)])

# Convert hex string to list of decimal bytes
def hex_to_dec_list(hex_str):
    return [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]

# Connect to the server
io = remote(host, port)

# Step 1: Read the encrypted flag from the server
io.recvuntil(b'This is the encrypted flag!\n')
enc_flag = io.recvline().strip().decode()
flag_len = len(enc_flag) // 2
log.info(f"Encrypted flag (hex): {enc_flag}")
log.info(f"Flag length in bytes: {flag_len}")

# Step 2: Send filler to force key pointer wraparound
filler = "a" * (50000 - flag_len)
io.sendlineafter(b"What data would you like to encrypt? ", filler.encode())
log.info("Filler sent to wrap the OTP key pointer")

# Step 3: Send known plaintext of same length as the flag
known_plain = "a" * flag_len
io.sendlineafter(b"What data would you like to encrypt? ", known_plain.encode())
io.recvuntil(b"Here ya go!\n")
enc_known = io.recvline().strip().decode()
log.info(f"Encrypted known plaintext (hex): {enc_known}")

# Step 4: Recover the key by XORing ciphertext with known plaintext
key = xor_list_str(hex_to_dec_list(enc_known), known_plain)
log.success(f"Recovered Key: {key.encode('utf-8', errors='replace')}")

# Step 5: Decrypt the flag
flag = xor_list_str(hex_to_dec_list(enc_flag), key)
log.success(f"Decrypted Flag: picoCTF{{{flag}}}")
```
![screenshot-1751183023](https://github.com/user-attachments/assets/6c9677ea-21c1-4877-9df3-a347335a7e75)





