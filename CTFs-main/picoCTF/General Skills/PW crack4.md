The objective is to recover the flag by identifying the correct password from a list of 100 possibilities. The program begins by reading two files: one containing an encrypted version of the flag (`level4.flag.txt.enc`) and the other containing the hash of the correct password (`level4.hash.bin`). The code then prompts the user to enter a password, hashes it using the MD5 algorithm, and compares it to the stored hash. If the hashes match, it decrypts the flag using a function called `str_xor`, which XORs the characters of the encrypted flag with the provided password (extended to match the flag's length). Because manually trying 100 passwords is inefficient, I automated this process. By iterating through the given list of potential passwords, I hashed each candidate and compared it to the correct hash. Once the match was found, I used the XOR decryption function to reveal the flag. This method demonstrates a basic hash-matching brute-force approach, which becomes feasible when the password space is small and the hash is known. Upon running the script, the correct password (`7dd6`) successfully decrypted the flag: `picoCTF{fl45h_5pr1ng1ng_d770d48c}`.

---

### Full Script with Automation

```python
import hashlib

# XOR-based decryption function
def str_xor(secret, key):
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key += key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(sc) ^ ord(kc)) for sc, kc in zip(secret, new_key)])

# Read encrypted flag and password hash
flag_enc = open('level4.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level4.hash.bin', 'rb').read()

# MD5 hashing function
def hash_pw(pw_str):
    m = hashlib.md5()
    m.update(pw_str.encode())
    return m.digest()

# List of candidate passwords
pos_pw_list = ["8c86", "7692", "a519", "3e61", "7dd6", "8919", "aaea", "f34b", "d9a2", "39f7", "626b", "dc78", "2a98", "7a85", "cd15", "80fa", "8571", "2f8a", "2ca6", "7e6b", "9c52", "7423", "a42c", "7da0", "95ab", "7de8", "6537", "ba1e", "4fd4", "20a0", "8a28", "2801", "2c9a", "4eb1", "22a5", "c07b", "1f39", "72bd", "97e9", "affc", "4e41", "d039", "5d30", "d13f", "c264", "c8be", "2221", "37ea", "ca5f", "fa6b", "5ada", "607a", "e469", "5681", "e0a4", "60aa", "d8f8", "8f35", "9474", "be73", "ef80", "ea43", "9f9e", "77d7", "d766", "55a0", "dc2d", "a970", "df5d", "e747", "dc69", "cc89", "e59a", "4f68", "14ff", "7928", "36b9", "eac6", "5c87", "da48", "5c1d", "9f63", "8b30", "5534", "2434", "4a82", "d72c", "9b6b", "73c5", "1bcf", "c739", "6c31", "e138", "9e77", "ace1", "2ede", "32e0", "3694", "fc92", "a7e2"]

# Brute-force function
def level_4_pw_check():
    for pw in pos_pw_list:
        if hash_pw(pw) == correct_pw_hash:
            decrypted_flag = str_xor(flag_enc.decode(), pw)
            print(f"Correct password found: {pw}")
            print(f"Decrypted flag: {decrypted_flag}")
            return

# Run the function
level_4_pw_check()
```

When executed, this script identifies the correct password and prints the decrypted flag.
