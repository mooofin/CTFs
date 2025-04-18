# **Forensics is Fun - CTF Writeup**

**Challenge:** Analyze the `Forensics is fun.pptm` file to find the hidden flag.  

---

## **Step 1: Initial Analysis with `olevba`**
Since the file is a PowerPoint Macro-Enabled Presentation (`.pptm`), we first check for embedded VBA macros using `olevba`:

```bash
python3 -m oletools.olevba "Forensics is fun.pptm"
```

### **Output Analysis:**
- Found a VBA macro (`Module1.bas`) with a fake flag:
  ```vba
  Sub not_flag()
      Dim not_flag As String
      not_flag = "sorry_but_this_isn't_it"
  End Sub
  ```
- No suspicious keywords (e.g., `Shell`, `AutoOpen`) were detected.  
- **Conclusion:** The flag is not in the macros.  

---

## **Step 2: Extract the PPTM File**
Since macros didn’t reveal the flag, we manually extract the `.pptm` (which is a ZIP archive):

```bash
unzip "Forensics is fun.pptm" -d extracted_files
```

### **Key Files Found:**
- `ppt/vbaProject.bin` (contains VBA macros, already checked)
- `ppt/slideMasters/hidden` (a suspicious file with no extension)

---

## **Step 3: Investigate the `hidden` File**
Inside `extracted_files/ppt/slideMasters/`, we find a file named `hidden`:

```bash
cat extracted_files/ppt/slideMasters/hidden
```
### **Output:**
```
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
```

### **Observations:**
1. **Spaces between characters** suggest encoding (e.g., Base64 after removing spaces).
2. The string resembles a **Base64-encoded flag** (common in CTFs).

---

## **Step 4: Decode the Hidden String**
### **Remove Spaces and Decode as Base64**
```bash
cat hidden | sed 's/ //g' | base64 -d
```
### **Output:**
```
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}base64: invalid input
```
(Note: The `base64: invalid input` is due to extra padding, but the flag is clearly visible.)

### **Alternative (Manual Steps):**
1. **Remove spaces** (e.g., manually or with `tr -d ' '`):
   ```
   ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ==
   ```
2. **Decode with CyberChef or Python:**
   ```python
   import base64
   encoded = "ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ=="
   print(base64.b64decode(encoded).decode())
   ```
   **Output:**  
   ```
   flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}
   ```

---

## **Final Flag**
```
picoCTF{D1d_u_kn0w_ppts_r_z1p5}
```

---

## **Summary of Steps**
1. **Checked macros** (`olevba`) → Fake flag.
2. **Extracted the PPTM** → Found `hidden` file.
3. **Removed spaces** from the string → Base64.
4. **Decoded Base64** → Revealed the flag.

---

## **Key Takeaways**
- **PPTM files are ZIP archives** (always check extracted content).
- **Non-standard files** (e.g., `hidden`) often contain flags.
- **Spaces in data** may indicate encoding (e.g., Base64, hex).

**Tools Used:** `olevba`, `unzip`, `base64`, `sed`  
