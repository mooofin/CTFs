

In this challenge, I was provided with a Python script that implemented a modified version of the **Playfair cipher** using a 6×6 matrix instead of the traditional 5×5. The key for generating the matrix was read from a file named `key`, and the message to be encrypted came from a file named `msg`. To solve the challenge, I examined the encryption logic and wrote a corresponding decryption script by reversing the Playfair rules: if both characters in a pair were in the same row, I moved left instead of right; if in the same column, I moved up instead of down; and if neither, I swapped the columns. After hardcoding the given alphabet (`lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9`) and the encrypted message (`1x5hqlod8x7oa88h0de1b5r6xja5sd`) into my script, the decryption function revealed the plaintext: `lhxm62i5lwoi0rljor647xq9wh7wie`. I then connected to the remote service using `nc mercury.picoctf.net 19860`, provided the decrypted plaintext as input, and successfully received the flag: `f391b621282ef5063ab2de93ab9e4bff`.
![image](https://github.com/user-attachments/assets/8250f99e-f1ae-4c38-84d6-6a66de21ee52)

![image](https://github.com/user-attachments/assets/18b10db4-e8db-47f4-bec9-aba07b25da50)

