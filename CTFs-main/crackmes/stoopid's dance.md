

### **First Impressions**  
I started by running the crackme—a simple Windows console app—and saw this prompt:  

```
WELCOME!  
PASS: 12345678  
You made a mistake. Try again!!  
Press any key to continue . . .  
```  

Hmm, the failure message wasn’t in the binary’s strings. That meant it was probably **encrypted or obfuscated**. Time to dig deeper.  

---

### **Reverse Engineering the Binary**  
I opened the executable in **Ghidra** and looked at `main()`. Here’s what stood out:  

1. **Password Input**  
   - The program reads input using `std::cin` into a `std::string`.  
   - It then calls `checkFlag()` to validate the password.  

2. **The `checkFlag` Function**  
   - Inside `checkFlag`, there’s a mysterious function `jio()` that checks the password.  
   - Depending on `jio()`’s result, it either:  
     - Decrypts `_c` (success message)  
     - Decrypts `_d` (failure message)  

3. **Hidden Encoded Strings**  
   - Looking in the `.rdata` section, I found these weird number sequences:  
     ```  
     _c: "99 222 330 412 570 582 812 936..."  
     _d: "89 222 351 128 545 582 700 808..."  
     _e: "49 98 162 128 250 288 392 256..."  
     _f: "112 194 351 460 505"  
     ```  
   - These had to be **encrypted strings**—but how?  

---

### **Cracking the Encryption**  
I noticed that `_d` decrypted to the failure message I saw earlier. That meant:  
- **`_c`** → Success message (`"congratulations! you did it successfully!"`)  
- **`_d`** → Failure message (`"You made a mistake. Try again!!"`)  
- **`_e` and `_f`** → Unknown (but probably important)  

#### **Experimenting with Patching**  
Since `checkFlag` used `_d` for failures, I wondered: *What if I forced it to use `_e` instead?*  

I patched the binary to replace references to `_d` with `_e` and ran it again:  

```
WELCOME!  
PASS: 12345678  
116 208 291 464 510 648 679 824 945 1150 1265 1404 1495 714  
```  

**Bingo!** That looked like another encoded string.  

I added this sequence to the binary’s data section and patched `_d` to point to it. When I ran the program again, it decrypted to:  

```
thatflagissus3  
```  

#### **Testing the Password**  
I ran the **unpatched** version and entered `thatflagissus3`:  

```
WELCOME!  
PASS: thatflagissus3  
congratulations! you did it successfully!  
Press any key to continue . . .  
```  

**Success!** I had found the correct password.  

As for `_f`, it decrypted to `"pause"`—probably used in `system("pause")`.  

---

### **How the Encryption Worked**  
The crackme stored strings as **space-separated numbers**, which were decoded at runtime.  

#### **Possible Decoding Methods**  
1. **Direct ASCII Mapping**  
   - `116` → `'t'`  
   - `208` → `'h'`  
   - `291` → `'a'` (likely modulo 256)  
   - ...and so on.  

2. **Mathematical Transform**  
   - Maybe subtracting a fixed value (e.g., `208 - 100 = 108 = 'h'`).  

Since `thatflagissus3` worked, I didn’t need to reverse the exact math—but if I had to, I’d check the `de()` function for the decoding logic.  

---

### **Final Answer**  
**Password:** `thatflagissus3`  
