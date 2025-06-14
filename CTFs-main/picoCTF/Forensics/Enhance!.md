# Writeup: Finding the Flag in an SVG File

## Challenge Overview
The challenge presents an SVG file named `drawing.flag.svg` that appears to contain a hidden flag. SVG (Scalable Vector Graphics) files are XML-based and can sometimes contain hidden information or clues.

## Step-by-Step Solution

### 1. Initial Inspection
First, I examined the contents of the directory:
```bash
┌──(sid㉿kali)-[~/Downloads]
└─$ dir
drawing.flag.svg  juliascope_1.0.0-1_all.deb
```

### 2. Analyzing the SVG File
I used the `strings` command to extract human-readable text from the SVG file:
```bash
strings drawing.flag.svg
```

### 3. Identifying the Flag
The output revealed several `<tspan>` elements containing parts of what looked like the flag:
```xml
<tspan id="tspan3748">p </tspan>
<tspan id="tspan3754">i </tspan>
<tspan id="tspan3756">c </tspan>
<tspan id="tspan3758">o </tspan>
<tspan id="tspan3760">C </tspan>
<tspan id="tspan3762">T </tspan>
<tspan id="tspan3764">F { 3 n h 4 n </tspan>
<tspan id="tspan3752">c 3 d _ d 0 a 7 5 7 b f }</tspan>
```

### 4. Extracting and Combining the Flag
I combined all the text from the `<tspan>` elements, removing spaces to form the complete flag:
```
picoCTF{3nh4nc3d_d0a757bf}
```

### 5. Verification
To confirm, I used `grep` to specifically extract the `<tspan>` elements:
```bash
strings drawing.flag.svg | grep tspan
```
This confirmed the flag was correctly assembled.

## Final Answer
The flag hidden in the SVG file is:
```
picoCTF{3nh4nc3d_d0a757bf}
```

## Key Takeaways
- SVG files can contain hidden text elements that may not be visible when viewing the image normally.
- The `strings` command is useful for extracting human-readable text from binary or XML-based files.
- When dealing with flags split across multiple elements, carefully combine all parts to reconstruct the complete flag.
