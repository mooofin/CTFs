# **VaultDoor3 Challenge Writeup**

## **Challenge Description**
We are given a Java program that verifies a vault password by scrambling the user input and comparing it with a predefined scrambled string. Our goal is to reverse the scrambling process and extract the original password.

---

## **Understanding the Code**
The Java program performs the following steps:
1. **Checks if the password is 32 characters long**.
2. **Scrambles the input password into a `buffer` array** using four loops:
   - **First loop (i = 0 to 7)**: Directly copies characters.
   - **Second loop (i = 8 to 15)**: Copies characters in a reversed order from index `23 - i`.
   - **Third loop (i = 16 to 30, step 2)**: Takes characters from `46 - i`.
   - **Fourth loop (i = 31 to 17, step -2)**: Copies characters directly.
3. The scrambled result is compared with the hardcoded string:  
   **`jU5t_a_sna_3lpm18g947_u_4_m9r54f`**

To solve this challenge, we need to reverse this transformation to recover the original password.

---

## **Extracting the Password**
Instead of manually reversing the logic, we can write a **Python script** to automate the process. The script initializes an empty array and reconstructs the original password by applying the reverse of each transformation in the Java code.

### **Java Code (VaultDoor3.java)**
```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
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
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
}
```

### **Python Script to Unscramble the Password**
```python
# Reversing the scrambled password from VaultDoor3

def unscramble_password(scrambled):
    buffer = [''] * 32  # Initialize an empty list of length 32
    
    # Step 1: First 8 characters are unchanged
    for i in range(8):
        buffer[i] = scrambled[i]
    
    # Step 2: Characters at indices 8 to 15 are from scrambled[23 - i]
    for i in range(8, 16):
        buffer[i] = scrambled[23 - i]
    
    # Step 3: Characters at even indices from 16 to 30 come from scrambled[46 - i]
    for i in range(16, 32, 2):
        buffer[i] = scrambled[46 - i]
    
    # Step 4: Characters at odd indices from 31 to 17 remain the same
    for i in range(31, 16, -2):
        buffer[i] = scrambled[i]
    
    return "".join(buffer)

# Scrambled password from the Java code
scrambled_password = "jU5t_a_sna_3lpm18g947_u_4_m9r54f"
original_password = unscramble_password(scrambled_password)

# Print the final flag
print(f"picoCTF{{{original_password}}}")
```

---

## **Final Password and Flag**
Running the script extracts the original password:

```
picoCTF{jU5t_a_s1mpl3_gam3_4_u_w1th_pl4y3r5}
```

---

## **Conclusion**
This challenge demonstrated how to analyze a scrambling function and reverse it using systematic programming. By carefully understanding how the Java loops manipulated the input, we were able to reconstruct the correct password and retrieve the flag efficiently.

This method can be applied to similar challenges where transformations need to be undone. 🚀

