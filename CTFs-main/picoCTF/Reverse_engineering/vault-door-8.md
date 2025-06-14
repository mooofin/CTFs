**VaultDoor8 Writeup**

### **Challenge Overview**
The VaultDoor8 challenge presents a Java program that verifies a scrambled password. Our goal is to reverse-engineer the scrambling function to recover the original password.

### **Understanding the Code**
The challenge code consists of:
1. **A main function** that reads input and checks if it matches an expected scrambled password.
2. **A scrambling function (`scramble`)** that applies bitwise transformations to each character in the password.
3. **A `switchBits` function** that swaps specific bits of a character.

To solve the challenge, we need to reverse the scrambling process.

### **Reversing the Scrambling Process**
The scrambling process consists of a series of bit swaps. By applying these swaps in reverse order, we can recover the original password.

#### **Bit Manipulations Used**
The scrambling function applies the following swaps:
1. Swap bits **1 and 2**
2. Swap bits **0 and 3**
3. Swap bits **5 and 6**
4. Swap bits **4 and 7**
5. Swap bits **0 and 1**
6. Swap bits **3 and 4**
7. Swap bits **2 and 5**
8. Swap bits **6 and 7**

### **Solution Implementation**
The solution implements an `unscramble` function that reverses the scrambling operations. We apply the bit swaps in the reverse order of their original application.

#### **Java Solution**
```java
import java.util.*;

class VaultDoor8Solver {
    public static void main(String args[]) {
        char[] expected = {
            0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0,
            0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77,
            0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27,
            0xB5, 0x77, 0xD2, 0xD0, 0xB4, 0xE1, 0xC1,
            0xE0, 0xD0, 0xD0, 0xE0
        };
        
        System.out.println("Recovered password: " + String.valueOf(unscramble(expected)));
    }

    public static char[] unscramble(char[] input) {
        char[] a = Arrays.copyOf(input, input.length);
        for (int i = 0; i < a.length; i++) {
            char c = a[i];
            c = switchBits(c, 6, 7);
            c = switchBits(c, 2, 5);
            c = switchBits(c, 3, 4);
            c = switchBits(c, 0, 1);
            c = switchBits(c, 4, 7);
            c = switchBits(c, 5, 6);
            c = switchBits(c, 0, 3);
            c = switchBits(c, 1, 2);
            a[i] = c;
        }
        return a;
    }
    
    public static char switchBits(char c, int p1, int p2) {
        char mask1 = (char) (1 << p1);
        char mask2 = (char) (1 << p2);
        char bit1 = (char) ((c & mask1) >> p1);
        char bit2 = (char) ((c & mask2) >> p2);
        
        c &= ~(mask1 | mask2);
        c |= (bit1 << p2);
        c |= (bit2 << p1);
        
        return (char) (c & 0xFF);
    }
}
```

### **Recovered Password**
When running this program, we obtain the unscrambled password, which can be used to complete the challenge.

### **Conclusion**
The challenge demonstrates how bitwise operations can be used to obfuscate data. By reversing the transformations, we successfully recover the original password. This approach is commonly used in reverse engineering and binary exploitation challenges.

