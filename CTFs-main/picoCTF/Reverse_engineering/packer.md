# **Unpacking and Analyzing a UPX-Packed Binary – CTF Writeup**

## **Overview**
In this challenge, we analyze an **executable file ("out")** that is **packed using UPX (Ultimate Packer for eXecutables)**. Our goal is to **unpack, analyze, and extract the flag**.

---

## **Step 1: Identifying the Packed File**
We start by checking the file type using the `strings` command:

```bash
strings out
```

### **Output:**
```
...
p$mkqui#
-Kin
#sem
5mun
at8V<
ddr%
H1hP)
-1dl
vinit
ZH'BaPa
kfc5
n*qj)!
.b0.
Z4u.
Z/-id%ABI-
a8s,
n`I C
ot +da$
.bssh
?p! _
H_db
UPX!
UPX!
```
🚀 **Key Observation:** The presence of `UPX!` indicates that the file is **packed using UPX**.

---

## **Step 2: Unpacking with UPX**
UPX is an **open-source executable packer**. To **decompress** the packed file, we use:

```bash
upx -d out -o original
```

### **Explanation:**
- `upx -d` → **Decompress the file**.
- `out` → **Packed file**.
- `-o original` → **Output the unpacked file as "original"**.

After unpacking, we notice an **increase in file size**, confirming a successful unpacking.

---

## **Step 3: Analyzing with Ghidra**
Now, we analyze `original` using **Ghidra**, a powerful reverse engineering tool.

### **Steps:**
1. **Load `original` into Ghidra**.
2. **Wait for analysis to complete** (can take time due to file size).
3. **Search for the `main` function**.
4. **Analyze the decompiled code to locate the flag**.

---

## **Step 4: Extracting the Flag**
After locating the **encrypted flag**, we use **CyberChef** to decrypt it.

### **Steps in CyberChef:**
1. Open **[CyberChef](https://gchq.github.io/CyberChef/)**.
2. Use the **"Magic Wand"** feature to **auto-detect** the encryption type.
3. **Decrypt the flag**.

---

## **Final Flag**
After decrypting, we obtain the final **flag!**
