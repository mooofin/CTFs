

When analyzing the provided file, I discovered a base64-encoded string: `YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyZzBOMm8yYXpZNWZRPT0nCg==`. After decoding it once, I obtained `b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ=='`, which still appeared encoded. Removing the Python byte literal notation (`b''`) and performing a second base64 decode revealed `wpjvJAM{jhlzhy_k3jy9wa3k_h47j6k69}`. Recognizing this as a Caesar cipher, I tested various rotation shifts and found that a ROT15 transformation successfully decoded it to reveal the final flag: `picoCTF{caesar_d3cr9pt3d_a47c6d69}`. 

![image](https://github.com/user-attachments/assets/f40dd782-0812-4ff2-9b46-6b0566fa8d23)
![image](https://github.com/user-attachments/assets/9cfa45a4-6646-4b59-9f44-33d587f5ba3b)
