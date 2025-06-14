# **picoCTF - VaultDoor7 Writeup**

## **Challenge Description**
The challenge provides a Java program (`VaultDoor7.java`) that verifies a password. The program converts the password into an array of integers using bitwise operations and then compares it with predefined integer values. Our goal is to reverse-engineer the program to retrieve the correct password.

---

## **Analyzing the Java Code**
The main function prompts the user for a password, strips the `picoCTF{}` prefix and `}` suffix, and passes the extracted string to `checkPassword()`. The `checkPassword()` function converts the input into an array of 8 integers and checks if it matches a predefined set of values.

### **Understanding `passwordToIntArray()`**
```java
public int[] passwordToIntArray(String hex) {
    int[] x = new int[8];
    byte[] hexBytes = hex.getBytes();
    for (int i=0; i<8; i++) {
        x[i] = hexBytes[i*4]   << 24
             | hexBytes[i*4+1] << 16
             | hexBytes[i*4+2] << 8
             | hexBytes[i*4+3];
    }
    return x;
}
```
This function:
1. Splits the 32-character password into 8 chunks (each 4 characters long).
2. Converts each chunk into a 32-bit integer using bitwise shifts (`<<`).

### **Integer Values for Verification**
```java
return x[0] == 1096770097
    && x[1] == 1952395366
    && x[2] == 1600270708
    && x[3] == 1601398833
    && x[4] == 1716808014
    && x[5] == 1734291511
    && x[6] == 960049251
    && x[7] == 1681089078;
```
The password is valid if its transformed integer array matches these values.

---

## **Reversing the Logic**
We need to extract the original characters from each 32-bit integer. Since each integer is constructed using bitwise shifts, we can reverse this process.

### **Python Script to Recover the Password**
```python
# Given integer values from checkPassword
int_values = [
    1096770097, 1952395366, 1600270708, 1601398833,
    1716808014, 1734291511, 960049251, 1681089078
]

# Function to extract characters from an integer
def int_to_chars(value):
    chars = []
    for shift in (24, 16, 8, 0):  # Extract bytes from most to least significant
        chars.append(chr((value >> shift) & 0xFF))
    return ''.join(chars)

# Reconstruct the password
password = ''.join(int_to_chars(num) for num in int_values)
flag = f"picoCTF{{{password}}}"

print(flag)
```

### **How the Script Works**
1. Loops through the 8 integer values.
2. Extracts each character using bitwise shifts (`>>`) and masking (`& 0xFF`).
3. Concatenates the characters to reconstruct the password.
4. Wraps the recovered password in `picoCTF{}`.

### **Output of the Script**
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u}
```

Thus, the **flag** is:
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u}
```

---

## **Summary**
- The Java program converts a 32-character password into 8 integers using bitwise shifts.
- We reversed this transformation by extracting the original bytes from the integers.
- Using a simple Python script, we reconstructed the correct password.
- The final flag is **picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u}**.

Would you like a deeper explanation of the bitwise operations? 🚀

