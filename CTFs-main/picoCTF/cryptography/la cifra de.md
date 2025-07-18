
In this CTF challenge, I was given a block of encrypted text served over a network connection via `nc jupiter.challenges.picoctf.org 58295`. The ciphertext exhibited patterns typical of a classical Vigenère cipher, a polyalphabetic substitution technique. To decrypt it, I used the Guballa Vigenère Cipher Solver, an online tool capable of performing automated frequency and key-length analysis. Upon inputting the encrypted message, the tool successfully revealed a historical passage discussing the origins of the cipher itself. Interestingly, the decrypted text clarified that the Vigenère Cipher was not originally invented by Blaise de Vigenère, as commonly believed, but rather by Giovan Battista Bellaso in 1553. It also referenced other cryptographic pioneers like Leon Battista Alberti and Johannes Trithemius, who contributed key concepts such as the tabula recta. Embedded within the plaintext was the flag: `picoCTF{b311a50_0r_v1gn3r3_c1ph3ra966878a}`.
![image](https://github.com/user-attachments/assets/ef1a50f4-03bd-45f6-ae19-b603c76ef96e)
![image](https://github.com/user-attachments/assets/f08a1b55-5b1e-4204-a31e-95a1ebc00598)


