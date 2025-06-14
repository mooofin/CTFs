# PatchMe Flag Challenge Write-Up

## Challenge Description
We are provided with a Python script that requires a password to decrypt an encrypted flag stored in `flag.txt.enc`. Our goal is to analyze the script and extract the flag.

## Code Analysis
The script consists of the following main components:

1. **`str_xor(secret, key)` function:**
   - It takes a `secret` and a `key`, extending the key to match the length of `secret`.
   - It then performs an XOR operation character by character.

2. **Encrypted Flag:**
   - The flag is stored in `flag.txt.enc` and is read in binary mode.

3. **`level_1_pw_check()` function:**
   - Prompts the user for a password.
   - Checks if the input matches a predefined password.
   - If the password is correct, it decrypts the flag using `str_xor()` with the key **`utilitarian`**.

## Finding the Password
The password check is explicitly hardcoded in the script:

```python
if( user_pw == "ak98" + \
               "-=90" + \
               "adfjhgj321" + \
               "sleuth9000"):
```

Concatenating the string fragments, we get the password:

```
ak98-=90adfjhgj321sleuth9000
```

## Extracting the Flag
1. Run the script and enter the password:
   
   ```bash
   python patchme.flag.py
   ```
   
2. Enter the password when prompted:
   
   ```
   Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
   ```

3. The script will decrypt and print the flag:
   
   ```
   Welcome back... your flag, user:
   picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}
   ```

## Flag
```
picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}
```



