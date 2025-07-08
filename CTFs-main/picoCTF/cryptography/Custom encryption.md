
When I first looked at the challenge, I saw that the flag was hidden in a list of large integers. At first glance, it was obvious that the encryption wasn't just a simple substitution or Caesar cipher — something more layered was going on. After reading through the variables, I noticed values labeled `a`, `b`, `g`, and `p`, which immediately made me think of Diffie-Hellman key exchange.
![screenshot-1751962514](https://github.com/user-attachments/assets/a6fd9b7f-c6b1-4534-906c-6833141d68c5)

The values given were `a = 89`, `b = 27`, with a small prime modulus `p = 97` and generator `g = 31`. This suggested that both parties had exchanged keys using modular exponentiation. To reconstruct the shared secret, I first computed $g^b \mod p$, then raised that result to the power of `a`, again modulo `p`. That gave me the shared key used in the next encryption layer.

Once I had the key, I needed to figure out how the large integers were created. Looking at the numbers and some hints in the code, I realized that each character had been multiplied by the shared key and a constant — specifically `311`. So to reverse this part, I divided each number in the list by `key * 311` to recover the ASCII values. This gave me a piece of text, but it was still garbled.
![screenshot-1751962686](https://github.com/user-attachments/assets/e0ccb372-f31e-4fae-a619-d2c2e3c16ba6)

The final step turned out to be a dynamic XOR cipher using the string `"trudeau"` as the key. I XORed each character of the intermediate string with a repeating character from `"trudeau"`, just like a Vigenère cipher but with XOR instead of addition. 


![screenshot-1751962720](https://github.com/user-attachments/assets/07d72e0f-942c-4266-9a62-6a37a7392bde)
