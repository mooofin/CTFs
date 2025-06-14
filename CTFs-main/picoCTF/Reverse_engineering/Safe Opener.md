# SafeOpener Challenge Write-Up

## Challenge Description
We are given a Java program that asks for a password to open a safe. If the password is correct, it prints "Sesame open"; otherwise, it gives us three attempts before terminating.

The program encodes the user-inputted password using Base64 and compares it to a stored Base64-encoded string.

## Code Analysis
Examining the `openSafe` function, we find that it checks the entered password (after Base64 encoding) against a predefined encoded key:

```java
public static boolean openSafe(String password) {
    String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
    
    if (password.equals(encodedkey)) {
        System.out.println("Sesame open");
        return true;
    }
    else {
        System.out.println("Password is incorrect\n");
        return false;
    }
}
```

The encoded key provided is:
```
cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz
```

## Solution
Since Base64 encoding is reversible, we can decode the stored key to retrieve the original password.

### Decoding the Key
Using Python, we can decode the Base64 string:

```python
import base64

encoded_key = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"
decoded_key = base64.b64decode(encoded_key).decode("utf-8")
print(decoded_key)
```

### Output
```
pl3as3_l3t_m3_1nt0_th3_saf3
```

## Flag Submission
The challenge specifies using the picoCTF flag format:
```
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```


