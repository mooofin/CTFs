

### 1. Using zsteg
The `zsteg` tool analyzes PNG files for hidden data in LSB (Least Significant Bit):
```bash
zsteg buildings.png
```

### 2. Found Flag
The tool revealed the flag in the RGB LSB channel:
```
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"
```

## Final Answers
1. SVG file flag:
```
picoCTF{3nh4nc3d_d0a757bf}
```

2. PNG file flag:
```
picoCTF{h1d1ng_1n_th3_b1t5}
```

## Key Takeaways
- **SVG files**: Can contain hidden text in XML elements. Use `strings` or inspect the source.
- **PNG files**: May hide data in pixel values. Tools like `zsteg` can reveal LSB steganography.
- Always check multiple analysis methods when searching for hidden flags.
