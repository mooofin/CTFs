# Extracting Hidden Data from red.png Using zsteg

## Overview
In this challenge, we analyze an image file (`red.png`) to extract hidden data using the `zsteg` tool. 

## Steps to Solve

### 1. Listing the Files
```bash
┌──(sid㉿kali)-[~/Downloads]
└─$ dir
red.png  ukn_reality.jpg  unknown.zip
```
The file `red.png` is found among the extracted files.

### 2. Running `zsteg`
We use `zsteg` to analyze `red.png` for hidden messages.
```bash
┌──(sid㉿kali)-[~/Downloads]
└─$ zsteg red.png
```

### 3. Decoding the Output
The tool provides various outputs, including hidden text and encoded data. 

#### Extracted Poem (Metadata):
```
Crimson heart, vibrant and bold,
Hearts flutter at your sight.
Evenings glow softly red,
Cherries burst with sweet life.
Kisses linger with your warmth.
Love deep as merlot.
Scarlet leaves falling softly,
Bold in every stroke.
```

#### Extracted Base64 Data:
```
cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==
```
We decode this using `base64`:
```bash
┌──(sid㉿kali)-[~/Downloads]
└─$ echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```

## Conclusion
By using `zsteg`, we successfully extracted a hidden message from `red.png`, which led to the flag:
```
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```

