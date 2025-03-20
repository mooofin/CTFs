# **VaultDoor1 Challenge Writeup**

## **Challenge Description**
The challenge presents us with a Java program that verifies a vault password using a method called `checkPassword`. Our task is to determine the correct password to gain access.

---

## **Understanding the Code**
The Java program reads user input and extracts a substring from it, specifically removing the prefix `picoCTF{` and the closing `}` before passing it to the `checkPassword` function. This function then verifies whether the extracted password meets a set of predefined character conditions.

### **Key Observations**
1. The password must be **32 characters long**.
2. The function checks specific characters at fixed positions.
3. If all conditions match, access is granted.

---

## **Extracting the Password**
The `checkPassword` function uses a series of conditions to verify individual characters in the password. By analyzing these conditions, we can reconstruct the password by placing the specified characters in their respective positions.

Below is the character mapping extracted from the function:

| Index | Character |
|--------|-----------|
| 0      | d         |
| 1      | 3         |
| 2      | 5         |
| 3      | c         |
| 4      | r         |
| 5      | 4         |
| 6      | m         |
| 7      | b         |
| 8      | l         |
| 9      | 3         |
| 10     | _         |
| 11     | t         |
| 12     | H         |
| 13     | 3         |
| 14     | _         |
| 15     | c         |
| 16     | H         |
| 17     | 4         |
| 18     | r         |
| 19     | 4         |
| 20     | c         |
| 21     | T         |
| 22     | 3         |
| 23     | r         |
| 24     | 5         |
| 25     | _         |
| 26     | 7         |
| 27     | 5         |
| 28     | 0         |
| 29     | 9         |
| 30     | 2         |
| 31     | e         |

### **Reconstructing the Password**
By arranging the extracted characters in order, we obtain:

```
d35cr4mbl3_tH3_cH4r4cT3r5_75092e
```

Since the program expects the input in the format `picoCTF{<password>}`, we append the prefix and suffix:

```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}
```

This is the final flag.

---

## **Conclusion**
This challenge involved reverse-engineering a password validation function by carefully analyzing how characters were checked. By systematically reconstructing the password, we successfully determined the correct input to unlock the vault. This exercise demonstrates the importance of avoiding hardcoded verification methods in security-sensitive applications.

