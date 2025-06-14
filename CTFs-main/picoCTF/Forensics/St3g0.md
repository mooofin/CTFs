

---

# Writeup: Hidden Flag in PNG (Steganography)

**Challenge Name:** Hidden Flag in PNG  
**Category:** Steganography  
**Difficulty:** Easy  

## Challenge Description
The challenge provides a PNG file named `pico.flag.png`. The task is to extract a hidden flag embedded within the image using steganography techniques.

## Tools Used
- **zsteg**: A tool for detecting steganography in PNG and BMP files.

## Approach
1. **Initial Analysis**:  
   First, I checked the file type to confirm it was indeed a PNG image:
   ```bash
   file pico.flag.png
   ```
   Output:
   ```
   pico.flag.png: PNG image data, 800 x 600, 8-bit/color RGB, non-interlaced
   ```

2. **Steganography Analysis with `zsteg`**:  
   Since the challenge likely involves hidden data, I used `zsteg` to analyze the image for embedded information. The `-a` flag ensures all known steganography methods are tested, and `-v` provides verbose output:
   ```bash
   zsteg -a -v pico.flag.png
   ```

## Findings
The `zsteg` output revealed two notable sections:
1. **First Output** (`b1,r,lsb,xy`):  
   A seemingly random string `~__B>VG?G@` was found, but this was not the flag.
   ```
   b1,r,lsb,xy         .. text: "~__B>VG?G@"
   ```

2. **Second Output** (`b1,rgb,lsb,xy`):  
   The flag was discovered in the RGB channel, using LSB (Least Significant Bit) steganography. The flag was embedded in the pixel data from left to right (`xy` order).
   ```
   b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_a9a181eb}$t3g0"
   ```

## Extracted Flag
The flag was successfully extracted from the image:
```
picoCTF{7h3r3_15_n0_5p00n_a9a181eb}
```

## Explanation of Techniques
- **LSB Steganography**:  
  The flag was hidden in the least significant bits of the RGB channels of the image. This technique alters the least noticeable bits of pixel data to embed information without visibly affecting the image.
  
- **zsteg**:  
  The tool automates the process of checking common steganography methods, including LSB analysis across different color channels and bit orders.

## Conclusion
This challenge demonstrates a basic steganography technique where data is hidden in the LSB of an image. Tools like `zsteg` simplify the extraction process by automating the search for embedded data.

---

### Additional Notes
- The `$t3g0` at the end of the extracted text is likely an artifact or a signature from the steganography tool/process and is not part of the actual flag.
- Always verify the flag format (e.g., `picoCTF{...}`) to avoid false positives.
