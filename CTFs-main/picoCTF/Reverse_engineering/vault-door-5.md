**Title:** Vault Door 5 - PicoCTF 2024 Writeup

**Challenge Overview:**
In this challenge, we are given a Java program that validates a password. The password undergoes two encoding transformations before being compared with an expected encoded value. Our goal is to reverse the process and extract the original password.

---

**Understanding the Code:**
The Java program follows these key steps:
1. It asks the user for input in the format `picoCTF{<password>}` and extracts the part inside the curly braces.
2. The extracted password is first URL-encoded.
3. The URL-encoded string is then Base64-encoded.
4. The result is compared to a predefined encoded string.

```java
import java.net.URLDecoder;
import java.util.*;

class VaultDoor5 {
    public static void main(String args[]) {
        VaultDoor5 vaultDoor = new VaultDoor5();
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

    public String base64Encode(byte[] input) {
        return Base64.getEncoder().encodeToString(input);
    }

    public String urlEncode(byte[] input) {
        StringBuffer buf = new StringBuffer();
        for (int i=0; i<input.length; i++) {
            buf.append(String.format("%%%2x", input[i]));
        }
        return buf.toString();
    }

    public boolean checkPassword(String password) {
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2";
        return base64Encoded.equals(expected);
    }
}
```

---

**Reversing the Encoding Process:**
To retrieve the original password, we need to:
1. Decode the given Base64-encoded string.
2. Decode the resulting URL-encoded string.

**Python Code to Reverse the Encoding:**
```python
import base64
import urllib.parse

# Base64-encoded expected password
encoded_password = ("JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                    "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                    "JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2")

# Step 1: Decode from Base64
decoded_base64 = base64.b64decode(encoded_password).decode()

# Step 2: URL Decode
decoded_url = urllib.parse.unquote(decoded_base64)

print("Decoded Password:", decoded_url)
```

**Output:**
```
Decoded Password: c0nv3rt1ng_fr0m_ba5e_64_0b957c4f
```

**Final Flag:**
```
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_0b957c4f}
```

---

**Conclusion:**
This challenge introduced encoding techniques used in web security: Base64 encoding and URL encoding. By understanding how these transformations work, we were able to reverse-engineer the process and extract the original password. This knowledge is useful for decoding obfuscated data in real-world applications.

