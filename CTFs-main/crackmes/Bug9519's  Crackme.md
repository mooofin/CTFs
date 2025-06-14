
**Tools Used**:  
- Static Analysis: Ghidra, IDA Pro (Pseudocode Reconstruction)  
- Dynamic Analysis: x64dbg (Attempted)  
- System Inspection: Dependency Walker  

---

## **1. Executive Summary**  
 The analysis reveals a straightforward string comparison vulnerability, with the correct password hardcoded in plaintext.  

### **Key Findings**  
- Password verification via direct `memcmp()` of user input against `"ThisIsNotThePassword!"`  
- Presence of a decoy string (`"SuperSecretPassword!"`) not used in validation  
- Dependency issue (`STATUS_DLL_NOT_FOUND`) observed during dynamic analysis  

---

## **2. Technical Analysis**  

### **2.1 Binary Overview**  
- **Format**: PE32+ (64-bit Windows executable)  
- **Compiler**: Microsoft Visual C++ (MSVC runtime dependency observed)  
- **Protections**: None (No ASLR, packing, or anti-debug measures)  

### **2.2 Static Analysis Findings**  

#### **Password Verification Routine**  
The core authentication logic is implemented in the function at `0x00402d30`:  

```c
int verify_password() {
  char user_input[32];
  char *correct_password = "ThisIsNotThePassword!";
  
  printf("Password: ");
  scanf("%s", user_input);
  
  if (strlen(user_input) == strlen(correct_password)) {
    if (memcmp(user_input, correct_password, strlen(correct_password)) == 0) {
      puts("Password Correct. CrackMe Solved!");
      return 0;
    }
  }
  puts("Password Incorrect, please try again.");
  return 1;
}
```

#### **Key Observations**  
1. **String Storage**:  
   - Actual password stored at `.rdata:0x405054`  
   - Decoy string at `.rdata:0x40503e` (never referenced in validation)  

2. **Comparison Method**:  
   - Length check followed by `memcmp()`  
   - No hashing or obfuscation  

### **2.3 Dynamic Analysis Challenges**  
Attempted debugging in x64dbg failed with:  
```
STATUS_DLL_NOT_FOUND (0xC0000135)
```  
**Root Cause**: Missing MSVC runtime DLL (`vcruntime140.dll` or similar).  😢💔💔💔(aint working :((  


---

## **3. Solution**  
### **Valid Credentials**  
 **Password**: `ThisIsNotThePassword!`  

### **Verification Method**  
1. **Static String Extraction**:  
   ```bash
   strings Bug9519_First_Crackme.exe | findstr /i password
   ```
   Output:  
   ```
   ThisIsNotThePassword!
   SuperSecretPassword!
   ```

2. **Pseudocode Analysis**: Confirmed password comparison at `0x00402e20`  

---

