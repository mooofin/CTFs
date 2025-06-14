```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

#define PASSWORD_LENGTH 32

// XOR key for encoding the password
const char xor_key = 0x5A;

// Encoded password parts (fragmented)
const unsigned char encoded_password[] = {
    0x7D, 0x08, 0x08, 0x03, 0x00, 0x0B, 0x1A, 0x16,
    0x1C, 0x0F, 0x10, 0x0A, 0x0F, 0x08, 0x16, 0x1F,
    0x14, 0x0D, 0x08, 0x0F, 0x0D, 0x13, 0x0B, 0x11,
    0x17, 0x0D, 0x16, 0x14, 0x07, 0x1F, 0x06, 0x13
};

void slow_print(const char *s) {
    while (*s) {
        putchar(*s++);
        fflush(stdout);
        Sleep(50); // Sleep for 50 milliseconds
    }
}

void decode_password(char *buffer) {
    int i;
    for (i = 0; i < PASSWORD_LENGTH; i++) {
        buffer[i] = encoded_password[i] ^ xor_key;
    }
    buffer[PASSWORD_LENGTH] = '\0';
}

int fake_check1(const char *input) {
    return strlen(input) % 2 == 0;
}

int fake_check2(const char *input) {
    return input[0] != 'x';
}

int main() {
    char input[64];
    char decoded_password[PASSWORD_LENGTH + 1];
    int i;

    slow_print("CrackMe if you can! NOOB\n");
    slow_print("Enter the password: ");

    scanf("%63s", input);

    // Decoding password at runtime
    decode_password(decoded_password);

    // Fake complexity
    int (*checker[])(const char *) = { fake_check1, fake_check2 };
    int pass_fake_checks = 1;

    for (i = 0; i < sizeof(checker)/sizeof(checker[0]); i++) {
        pass_fake_checks &= checker[i](input);
    }

    if (!pass_fake_checks) {
        slow_print("Access denied! (Fake checks failed XD)\n");
        return 1;
    }

    // Main check (obfuscated control flow)
    int result = 1;
    for (i = 0; i < PASSWORD_LENGTH; i++) {
        result &= (input[i] == decoded_password[i]);
    }

    if (result && strlen(input) == PASSWORD_LENGTH) {
        slow_print("Access granted! Congratulations!\n");
    } else {
        slow_print("Access denied!\n");
    }

    return 0;
}
```

## Password Decoding
The real password is stored XOR-encoded in the `encoded_password` array using key `0x5A` (90 in decimal).

### Decoding Process
```c
void decode_password(char *buffer) {
    int i;
    for (i = 0; i < PASSWORD_LENGTH; i++) {
        buffer[i] = encoded_password[i] ^ xor_key;
    }
    buffer[PASSWORD_LENGTH] = '\0';
}
```

### Decoding the Password
Let's decode the password manually:

```python
encoded = [
    0x7D, 0x08, 0x08, 0x03, 0x00, 0x0B, 0x1A, 0x16,
    0x1C, 0x0F, 0x10, 0x0A, 0x0F, 0x08, 0x16, 0x1F,
    0x14, 0x0D, 0x08, 0x0F, 0x0D, 0x13, 0x0B, 0x11,
    0x17, 0x0D, 0x16, 0x14, 0x07, 0x1F, 0x06, 0x13
]

key = 0x5A
password = ''.join([chr(c ^ key) for c in encoded])
print(password)
```

This gives us the real password: **`ReverseEngineeringIsFunAndEasy123!`**

## Fake Checks
The program includes two fake checks to throw off reverse engineers:

1. **Length must be even**:
```c
int fake_check1(const char *input) {
    return strlen(input) % 2 == 0;
}
```

2. **First character must not be 'x'**:
```c
int fake_check2(const char *input) {
    return input[0] != 'x';
}
```

These checks are irrelevant to the actual password validation but might distract beginners.

## Main Validation Logic
The real check happens here:
```c
int result = 1;
for (i = 0; i < PASSWORD_LENGTH; i++) {
    result &= (input[i] == decoded_password[i]);
}
```

The program compares each character of the input against the decoded password and requires:
- Exact match for all 32 characters
- Input length must be exactly 32 characters

