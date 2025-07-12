I started by downloading the files—either manually or using `wget`. After placing them in the same directory, I ran the Python script, which asked for a password to decrypt the flag.

I checked the code. It reads an encrypted flag and a stored MD5 hash of the correct password. The function `hash_pw()` hashes input, and `str_xor()` decrypts the flag using XOR if the password is correct.

Seven possible passwords were given. Instead of entering them manually, I modified the `level_3_pw_check()` function to loop through the list. For each password, I hashed it and compared it to the stored hash.

Once the correct one matched, I used it to decrypt the flag and print it. 
