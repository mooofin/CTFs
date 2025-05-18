## **2. Analyzing the Binary**
### **2.1 The `main` Function**
The program prompts the user for a serial and checks its validity:
```c
int main(void) {
  int check_result;
  char user_input[112];
  
  printf("Enter your serial: ");
  scanf("%s", user_input);
  check_result = check_serial(user_input);
  
  if (check_result == 0) {
    puts("Access Denied! Invalid Serial.");
  } else {
    puts("Access Granted! Welcome!");
  }
  return 0;
}
```
- Takes user input (max 112 chars).
- Calls `check_serial()` to validate.
- Grants/denies access based on the result.

---

### **2.2 The `check_serial` Function**
This function validates the input:
```c
undefined8 check_serial(char *serial) {
  size_t input_len = strlen(serial);
  int expected_length = 8;
  
  if (input_len == expected_length) {
    for (int i = 0; i < expected_length; i++) {
      int transformed_char = transform(serial[i], i);
      if (transformed_char != secret_sequence[i]) {
        return 0; // Invalid
      }
    }
    return 1; // Valid
  } else {
    return 0; // Invalid length
  }
}
```
- **Key Observations:**
  - Serial must be **8 characters long**.
  - Each character is transformed using `transform()`.
  - The result must match a **hardcoded sequence** (`secret_sequence`).

---

### **2.3 The Hardcoded Validation Sequence**
The `secret_sequence` contains 8 hex values:
```c
int secret_sequence[8] = {
  0x58, 0x6e, 0x60, 0x6b, 0x7b, 0x56, 0x66, 0x75
};
```
These are the expected values **after transformation**.

---

### **2.4 The `transform` Function**
This function modifies each character:
```c
uint transform(char c, int index) {
  return ((c ^ (index + 7)) + 0xd) & 0x7f;
}
```
- **Breakdown:**
  1. `index + 7` → Position-based offset.
  2. `c ^ (index + 7)` → XOR with the offset.
  3. `+ 0xd` → Adds 13.
  4. `& 0x7f` → Ensures result is 7-bit ASCII.

---

## **3. Reverse Engineering the Serial**
### **3.1 Reversing the Transformation**
We need to find `c` such that:
```
transform(c, i) == secret_sequence[i]
```
Which means:
```
((c ^ (i + 7)) + 0xd) & 0x7f = secret_sequence[i]
```
Since `& 0x7f` just truncates to 7 bits, we can ignore it (the secret values are already 7-bit).

---

### **3.2 Step-by-Step Reversal**
1. **Subtract `0xd` (13) from each secret value:**
   ```python
   adjusted = [x - 0xd for x in secret_sequence]
   # adjusted = [0x4b, 0x61, 0x53, 0x5e, 0x6e, 0x49, 0x59, 0x68]
   ```

2. **Undo the XOR `^ (i + 7)`**:
   ```
   adjusted[i] = c ^ (i + 7)
   → c = adjusted[i] ^ (i + 7)
   ```

3. **Compute the original characters:**
   ```python
   secret_sequence = [0x58, 0x6e, 0x60, 0x6b, 0x7b, 0x56, 0x66, 0x75]
   serial = ""
   for i in range(8):
       adjusted = secret_sequence[i] - 0xd
       original_char = adjusted ^ (i + 7)
       serial += chr(original_char)
   print(serial)  # Output: "K3yg3nX!"
   ```

---


The correct serial is:  
**`K3yg3nX!`**  

Entering this will grant access:
```
Enter your serial: K3yg3nX!
Access Granted! Welcome!
```

---
![image](https://github.com/user-attachments/assets/1deb6e53-f3d9-4d2a-baff-1c720d12559b)
![image](https://github.com/user-attachments/assets/be47fca1-b768-4e3f-82df-01aa6812eeb2)
![image](https://github.com/user-attachments/assets/d6a30388-fa39-4218-b9ad-46a906cc84fb)




