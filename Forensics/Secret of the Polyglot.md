

### 1. **Download the File**
Create a separate folder for the challenge and use the `wget` command to download the file:
```bash
$ wget -O flag2of2-final.pdf 
```

### 2. **Inspect the File**
Use the `cat` command to view the file's content:
```bash
$ cat flag2of2-final.pdf
```
If the content doesn't appear to be a valid PDF, check its actual format using:
```bash
$ file flag2of2-final.pdf
```

### 3. **Rename and Convert File**
If the file is identified as a PNG image despite having a `.pdf` extension, rename it:
```bash
$ mv flag2of2-final.pdf flag2of2-final.png
```
View the image using:
```bash
$ eog flag2of2-final.png
```
This may reveal part of the flag.

### 4. **Analyze Metadata**
Extract metadata from the image using `exiftool`:
```bash
$ exiftool flag2of2-final.png
```
Look for clues about hidden data or embedded files.

### 5. **Inspect Hex Data**
Use a hex editor like `ghex` to analyze the file and locate any embedded data:
```bash
$ ghex flag2of2-final.png
```
Search for the PDF header signature (`%PDF`, hex: `25 50 44 46`) within the PNG file.

### 6. **Extract Embedded PDF**
Copy all hex data starting from `%PDF` to the end of the embedded PDF and save it as a new file, e.g., `embedded.pdf`.

### 7. **Convert PDF to Text**
Convert the extracted PDF into text format using:
```bash
$ pdftotext embedded.pdf
```
Read the resulting text file to retrieve additional parts of the flag.

### 8. **Combine Flag Parts**
Combine all parts of the flag (from both image content and extracted metadata) to form the complete solution.

For example, if one part of the flag is visible in the image and another is extracted from metadata or embedded files, combine them as follows:
```
picoCTF{f1u3n7_1n_pn9_&_pdf_53b741d6}
```

This process demonstrates techniques like metadata analysis, steganography, and hex editing commonly used in forensic challenges.

---
