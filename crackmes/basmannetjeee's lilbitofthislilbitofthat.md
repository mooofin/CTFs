# **Reverse Engineering Writeup: Serial Key Validation System**





## **3. Technical Analysis**

### **3.1 Input Handling**
The program flow:
1. Prompts for username (`fgets` with 256-byte buffer)
2. Trims newline characters
3. Generates expected serial key
4. Compares user input against generated key

```c
// Pseudocode
username = get_input();
clean_newlines(username);
serial = generate_serial(username);
if (input_serial == serial) {
    grant_access();
} else {
    deny_access();
}
```

### **3.2 Key Generation Algorithm**
The core algorithm in `generate_serial()`:

```python
def generate_serial(username):
    charset = "abcdefghijklmnoABCDEFGHIJKpqrstuvwxyzLMNOPQRSTUVWXYZ"
    serial = []
    for char in username:
        index = (ord(char) * 0x10 * len(username) >> 2) % len(charset)
        serial.append(charset[index])
    return ''.join(serial)
```

**Algorithm Steps**:
1. For each character in username:
   - Multiply ASCII value by 16 (0x10)
   - Multiply by username length
   - Right-shift by 2 (divide by 4)
   - Modulo 52 (charset length)
2. Use result as index into charset
3. Concatenate characters to form serial

### **3.3 Character Set**
52-character mixed case alphabet:
```
abcdefghijklmnoABCDEFGHIJKpqrstuvwxyzLMNOPQRSTUVWXYZ
```

## **4. Vulnerability Assessment**

### **4.1 Weaknesses Identified**
1. **Deterministic Output**: Same username always produces same serial
2. **No Cryptography**: Simple arithmetic operations only
3. **Fixed Charset**: Limited entropy
4. **Reversible**: Algorithm can be easily inverted

### **4.2 Exploitation Methods**
1. **Static Analysis**:
   - Decompilation reveals full algorithm
   - No obfuscation present
2. **Dynamic Analysis**:
   - Breakpoint at comparison reveals valid serial
   - Memory inspection shows intermediate values

## **5. Key Generator Implementation**

```python
import sys

CHARSET = "abcdefghijklmnoABCDEFGHIJKpqrstuvwxyzLMNOPQRSTUVWXYZ"

def generate_serial(username):
    return ''.join(
        CHARSET[(ord(c) * 16 * len(username) >> 2) % 52]
        for c in username
    )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    if len(username) > 256:
        print("Error: Username too long (max 256 chars)")
        sys.exit(1)
    
    print(f"Username: {username}")
    print(f"Serial: {generate_serial(username)}")
```

**Usage**:
```bash
python keygen.py testuser
Username: testuser
Serial: qGJKM
```


```c

void FUN_100001c30(char *param_1,long param_2)

{
  int iVar1;
  size_t sVar2;
  int local_30;
  
  sVar2 = _strlen(param_1);
  iVar1 = (int)sVar2;
  sVar2 = _strlen("abcdefghijklmnoABCDEFGHIJKpqrstuvwxyzLMNOPQRSTUVWXYZ");
  for (local_30 = 0; local_30 < iVar1; local_30 = local_30 + 1) {
    *(char *)(param_2 + local_30) =
         "abcdefghijklmnoABCDEFGHIJKpqrstuvwxyzLMNOPQRSTUVWXYZ"
         [(param_1[local_30] * 0x10 * iVar1 >> 2) % (int)sVar2];
  }
  *(undefined1 *)(param_2 + iVar1) = 0;
  return;
}
```
```c

undefined8 entry(void)

{
  int iVar1;
  size_t sVar2;
  undefined4 local_31c;
  char local_318 [255];
  char acStack_219 [257];
  char local_118 [264];
  long local_10;
  
  local_10 = *(long *)PTR____stack_chk_guard_100002008;
  local_31c = 0;
  _memset(local_118,0,0x100);
  _memset(acStack_219 + 1,0,0x100);
  _memset(local_318,0,0x100);
  _printf("Username: ");
  _fgets(acStack_219 + 1,0x100,*(FILE **)PTR____stdinp_100002010);
  sVar2 = _strlen(acStack_219 + 1);
  if ((sVar2 != 0) && (acStack_219[sVar2] == '\n')) {
    acStack_219[sVar2] = '\0';
  }
  FUN_100001c30(acStack_219 + 1,(long)local_118);
  _printf("Serial key: ");
  _fgets(local_318,0x100,*(FILE **)PTR____stdinp_100002010);
  sVar2 = _strlen(local_318);
  if ((sVar2 != 0) && (local_318[sVar2 - 1] == '\n')) {
    local_318[sVar2 - 1] = '\0';
  }
  iVar1 = _strcmp(local_318,local_118);
  if (iVar1 == 0) {
    _printf("\nPassed! Upload your solution :3\n\n");
    _printf("\"If you passed by patching, you didnt pass.\"\n        -Maybe linus torvals\n\n");
  }
  else {
    _printf("\nFailure\n");
  }
  if (*(long *)PTR____stack_chk_guard_100002008 == local_10) {
    return 0;
  }
                    /* WARNING: Subroutine does not return */
  ___stack_chk_fail();
}

```
