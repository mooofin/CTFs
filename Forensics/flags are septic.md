

## **The Challenge**  
We’re given a website filled with fake flags. Scrolling down, there’s an image of a "fake country" (`upz.png`). Our goal? Extract the real flag hidden inside it.  

### **First Attempt: Basic Checks**  
Before diving deep, I ran some quick checks:  
1. **`strings upz.png | grep "picoCTF"`** → Nothing.  
2. **`exiftool upz.png`** → No suspicious metadata.  
3. **`binwalk upz.png`** → No embedded files.  
4. **`steghide extract -sf upz.png`** → No password, no data.  



---

## **Discovering the Hidden Data**  
Since basic tools failed, I turned to **LSB steganography**—a common way to hide data in images.  

### **Trying `stepic` (Python LSB Tool)**  
I installed `stepic` (since it wasn’t available by default):  
```bash
sudo apt install stepic
```  

Then ran:  
```bash
stepic -d -i upz.png -o flag.txt
```  

**Boom!** A warning appeared:  
```
DecompressionBombWarning: Image size (150,658,990 pixels) exceeds limit of 89,478,485 pixels
```  

This means the image is **massive** (likely intentional to deter analysis).  

### **Fixing the Error**  
To bypass the size limit, I could:  
1. **Increase PIL’s pixel limit** (temporarily risky, but fine for a CTF).  
2. **Use `zsteg` instead** (better for PNGs).  

I tried `zsteg`:  
```bash
zsteg upz.png
```  

But still nothing.  

### **Final Success with `stepic`**  
I ignored the warning (since it’s a CTF, not a real attack) and ran:  
```bash
stepic -d -i upz.png -o flag.txt && cat flag.txt
```  

**Flag extracted!**  
```
picoCTF{fl4g_h45_fl4g57f48d94}
```  

---

## **Why This Worked**  
- The flag was hidden using **LSB steganography** (changing the least significant bits of pixels).  
- `stepic` decoded these subtle changes into the hidden message.  
- The giant image size was a **red herring**—meant to slow down analysis, but didn’t stop extraction.  

---
