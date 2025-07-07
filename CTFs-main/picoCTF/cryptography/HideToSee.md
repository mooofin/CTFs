During a steganography challenge, I was provided with an image file named `atbash.jpg`. Suspecting that it might contain hidden data, I used the tool `steghide` to analyze the image. Running the command `steghide info atbash.jpg` revealed that an embedded file named `encrypted.txt` was hidden within the image. The output also showed that the data was encrypted using the rijndael-128 cipher in CBC mode, and it was compressed.

To retrieve the hidden file, I used the command `steghide extract -sf atbash.jpg -xf encrypted.txt`. After entering the passphrase, `steghide` successfully extracted the hidden text file and saved it as `encrypted.txt`. Viewing the contents with `cat encrypted.txt` displayed a seemingly encrypted string: `krxlXGU{zgyzhs_xizxp_8z0uvwwx}`.
![image](https://github.com/user-attachments/assets/e287030f-1f5d-402d-8297-88b268770dbf)

Recognizing the pattern and structure, I identified it as an Atbash cipher — a classic substitution cipher where letters are mapped in reverse (A ↔ Z, B ↔ Y, etc.). Applying Atbash decoding to the string revealed the actual flag: `picoCTF{atbash_crack_8a0feddc}`.


![image](https://github.com/user-attachments/assets/64fdb543-63bd-4918-92ff-d1b6fa7da617)


