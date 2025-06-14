# Writeup: Extracting Hidden Data from a QR Code using ZBar

## Challenge Description
After unzipping the provided file, I found an image. Suspecting it might contain hidden information, I decided to scan it for any embedded data.

## Solution Steps

### Step 1: Inspect the Unzipped File
After extracting the contents of the provided archive, I noticed an image file (`flag.png`). Given that QR codes are commonly used in CTF challenges, I suspected the image might contain a scannable QR code.

### Step 2: Use `zbarimg` to Scan the QR Code
Since the `zbarimg` tool is designed to extract information from barcodes and QR codes, I used the following command in Kali Linux:

```sh
zbarimg flag.png
```

### Step 3: Extract the Flag
Running the command produced the following output:

```
QR-Code:picoCTF{p33k_@_b00_d4ca652e}
scanned 1 barcode symbols from 1 images in 0 seconds
```

This output revealed the hidden flag embedded in the QR code.

## Conclusion
By using the `zbarimg` tool, I was able to quickly extract the flag from the QR code image. This challenge highlighted the importance of recognizing QR codes as a method of encoding information in CTF challenges.

**Flag:** `picoCTF{p33k_@_b00_d4ca652e}`

