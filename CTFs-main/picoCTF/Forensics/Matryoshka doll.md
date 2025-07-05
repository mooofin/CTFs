

In this challenge, I was given a series of image files beginning with `1_c.jpg`, which at first appeared to be normal JPEG images. However, based on experience with CTF steganography techniques, I suspected that these images might contain embedded ZIP data. A common trick involves appending a ZIP archive to the end of an image file — something standard image viewers ignore, but ZIP tools can still recognize and extract.

Starting with `1_c.jpg`, I ran `unzip 1_c.jpg`. Despite a warning about "extra bytes at beginning or within zipfile," the file extracted successfully and produced `2_c.jpg`. This confirmed the suspicion that `1_c.jpg` contained a ZIP archive hidden behind its image data.

I continued this pattern, running `unzip 2_c.jpg`, which extracted `3_c.jpg`, then `unzip 3_c.jpg`, which extracted `4_c.jpg`. Each file generated the next in the chain using the same embedded-archive trick. Finally, running `unzip 4_c.jpg` extracted a file named `flag.txt`.

Reading `flag.txt` revealed the hidden flag:
`picoCTF{bf6acf878dcbd752f4721e41b1b1b66b}`
![image](https://github.com/user-attachments/assets/0748a9cd-29d6-41bd-84b2-0422ffb2ad42)

