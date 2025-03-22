**Title:** Vault Door 6 - PicoCTF 2024 Writeup

**Challenge Overview:**
In this challenge, we are given a Java program that checks a password by performing an XOR operation on each character and comparing it to a predefined byte array. Our goal is to reverse this process to extract the original password.

---

**Understanding the Code:**
The Java program follows these key steps:
1. It asks the user for input in the format `picoCTF{<password>}` and extracts the part inside the curly braces.
2. The extracted password must be exactly **32 characters long**.
3. Each character's ASCII value is XORed with `0x55` (decimal 85).
4. The result is compared to a predefined byte array (`myBytes[]`).
5. If all 32 conditions hold, the password is correct.

```java
import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        VaultDoor6 vaultDoor = new VaultDoor6();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0x0A, 0x38, 0x00, 0x36, 0x1D,
            0x0A, 0x3D, 0x61, 0x27, 0x11, 0x66, 0x27, 0x0A,
            0x21, 0x1D, 0x61, 0x3B, 0x0A, 0x2D, 0x65, 0x27,
            0x0A, 0x6C, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}
```

---

**Reversing the Encoding Process:**
To retrieve the original password, we need to:
1. Extract the predefined `myBytes` array.
2. Reverse the XOR operation using:
   
   ```plaintext
   password[i] = myBytes[i] ^ 0x55
   ```
3. Convert the resulting bytes back to characters.

**Python Code to Reverse the Encoding:**
```python
import base64

# Given byte array from the Java program
my_bytes = [
    0x3b, 0x65, 0x21, 0x0A, 0x38, 0x00, 0x36, 0x1D,
    0x0A, 0x3D, 0x61, 0x27, 0x11, 0x66, 0x27, 0x0A,
    0x21, 0x1D, 0x61, 0x3B, 0x0A, 0x2D, 0x65, 0x27,
    0x0A, 0x6C, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36
]

# Apply XOR operation with 0x55 to retrieve the original characters
password = ''.join(chr(b ^ 0x55) for b in my_bytes)

# Full flag format
flag = f"picoCTF{{{password}}}"
print(flag)
```

**Output:**
```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc}
```

**Final Flag:**
```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc}
```

---

**Conclusion:**
This challenge reinforced XOR-based encryption techniques. By understanding that XOR is a reversible operation, we successfully extracted the original password. This method is commonly used in cryptography and binary data obfuscation.

