In this challenge, I performed a **Chosen Plaintext Attack (CPA)** on textbook RSA encryption. I was given the public key components: the modulus `n`, the exponent `e`, and the ciphertext `c`. Using the `RSHack` toolkit, I selected option 6 for the Chosen Plaintext Attack and entered the provided values. The tool calculated a modified ciphertext `c′ = c × 2^e mod n` and instructed me to send it to the challenge server acting as a decryption oracle.

I connected to the server and submitted the modified ciphertext. In return, the server gave me a decrypted value, which I knew to be `2 × plaintext`. I entered this result back into RSHack, which then divided it by 2 to recover the original message. The final integer value decoded cleanly into a UTF-8 string, revealing the flag:
**`picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_4005534}`**.



