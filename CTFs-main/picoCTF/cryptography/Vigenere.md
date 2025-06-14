# Writeup: Decrypting a Vigenère Cipher

## Challenge Overview
In this challenge, we were given a ciphertext and a key, and our task was to decrypt it using the Vigenère cipher. The provided key for decryption was **CYLAB**.

### Given Ciphertext
```
rgn0DVD{00NU_WQ3_G1G303T3_A1AH3S_cc82272b}
```

## Decryption Process
The Vigenère cipher is a method of encrypting text by using a series of Caesar ciphers based on the letters of a key. To decrypt the message, we reverse this process using the given key.

### Tools Used
We used an online Vigenère cipher decoder to perform the decryption:
- **Cipher Type**: Standard Vigenère cipher
- **Key**: CYLAB
- **Key Mode**: Repeat
- **Alphabet**: a-z (maintaining case sensitivity)

### Decryption Output
Upon decrypting the given ciphertext using the key "CYLAB," we obtained the following plaintext:
```
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}
```


