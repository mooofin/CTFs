I started by downloading the files—either manually or using `wget`. After placing them in the same directory, I ran the Python script, which asked for a password to decrypt the flag.

I checked the code. It reads an encrypted flag and a stored MD5 hash of the correct password. The function `hash_pw()` hashes input, and `str_xor()` decrypts the flag using XOR if the password is correct.

Seven possible passwords were given. Instead of entering them manually, I modified the `level_3_pw_check()` function to loop through the list. For each password, I hashed it and compared it to the stored hash.

Once the correct one matched, I used it to decrypt the flag and print it. 
<img width="942" height="865" alt="screenshot-1752313520" src="https://github.com/user-attachments/assets/ac0bbc60-fd9d-48be-9329-29c4e5c5c0dd" />
<img width="943" height="1020" alt="screenshot-1752313549" src="https://github.com/user-attachments/assets/6dd761f6-cce9-43b0-8e48-f37b9834325e" />
<img width="359" height="73" alt="screenshot-1752313832" src="https://github.com/user-attachments/assets/981519b8-4faa-4157-a71e-e986ded92beb" />
