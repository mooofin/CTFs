```python
def str_xor(secret, key):
    # Extend key to match the length of the secret
    new_key = ""
    i = 0
    while len(new_key) < len(secret):
        new_key += key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(s) ^ ord(k)) for s, k in zip(secret, new_key)])


flag_enc = (
    chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) +
    chr(0x15) + chr(0x5a) + chr(0x07) + chr(0x00) + chr(0x46) + chr(0x0b) + chr(0x1a) +
    chr(0x5a) + chr(0x1d) + chr(0x1d) + chr(0x2a) + chr(0x06) + chr(0x1c) + chr(0x5a) +
    chr(0x5c) + chr(0x55) + chr(0x40) + chr(0x3a) + chr(0x5f) + chr(0x53) + chr(0x5b) +
    chr(0x57) + chr(0x41) + chr(0x57) + chr(0x08) + chr(0x5c) + chr(0x14)
)

flag = str_xor(flag_enc, 'enkidu')
print("That is correct! Here's your flag: " + flag)
```
```bash
picoCTF{1nd3nt1ty_cr1515_182342f7}
```
