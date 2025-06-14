# Safe Opener 2 Challenge Write-Up

## Challenge Description
We are provided with a Java program that simulates a safe requiring a password to open. Our task is to analyze the code and retrieve the lost key, which is hidden within the program.

## Code Analysis
The provided Java code includes the following key components:

1. It prompts the user to enter a password.
2. The password is then encoded using Base64.
3. The encoded password is compared against a predefined encoded key.
4. If the encoded key matches the stored key, the safe is unlocked.

### Identifying the Flag
By carefully examining the `openSafe` method:
```java
public static boolean openSafe(String password) {
    String encodedkey = "picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_198203f7}";
    if (password.equals(encodedkey)) {
        System.out.println("Sesame open");
        return true;
    }
    System.out.println("Password is incorrect\n");
    return false;
}
```

We see that the flag is stored directly in the source code as `encodedkey`:
```
picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_198203f7}
```

Since the program does not actually use Base64 decoding to validate input against an encoded version of the password, but instead directly stores the flag, we can extract it without running the program.

## Flag
```
picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_198203f7}
```


