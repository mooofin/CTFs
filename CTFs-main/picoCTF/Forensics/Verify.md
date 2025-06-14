![image](https://github.com/user-attachments/assets/7d1d5806-88d0-4ce8-8bd8-bb460d2ca738)


The challenge provided three items:

* `checksum.txt` containing the SHA-256 hash of the correct flag file,
* `decrypt.sh` script to decrypt files,
* a `files` directory containing multiple encrypted files.

My task was to find the correct encrypted file that matched the checksum and then decrypt it to get the flag.

---

### Step 1: Find the Correct Encrypted File

First, I checked the hash inside `checksum.txt` using:

```bash
cat /home/ctf-player/drop-in/checksum.txt
```

It contained the hash:

```
fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7
```

Then, I compared the SHA-256 hash of all files inside the `files` directory:

```bash
sha256sum /home/ctf-player/drop-in/files/* | grep fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7
```

This showed me the file that matched the hash:

```
/home/ctf-player/drop-in/files/87590c24
```

---

### Step 2: Decrypt the File

Using the provided `decrypt.sh` script as reference, I saw that it used `openssl enc` with AES-256-CBC encryption. I ran the following command to decrypt the file:

```bash
openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in /home/ctf-player/drop-in/files/87590c24 -k picoCTF
```

This decrypted the file successfully and revealed the flag.

---

### Notes

* OpenSSL is a command-line tool for encryption and decryption that supports many cryptographic algorithms.
* AES-256-CBC is a secure symmetric encryption algorithm that uses a 256-bit key and Cipher Block Chaining mode.
* `sha256sum` is used to verify file integrity by computing and comparing SHA-256 hashes.

---

### Reference

I referred to another writeup to better understand the process of verifying SHA-256 hashes and decrypting files using OpenSSL.

---

### Final Result

The decrypted output revealed the flag in plaintext.

---
