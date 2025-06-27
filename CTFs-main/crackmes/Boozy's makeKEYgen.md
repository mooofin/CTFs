```python
def boozhash(s):
    h = 0
    for c in s.encode('ascii').lower():
        h = (h + c) * 0x401
        h = (h ^ (h >> 6)) & 0xFFFFFFFF
    h = (h * 9) ^ ((h * 9) >> 11)
    h = (h * 0x8001) & 0xFFFFFFFF
    return h

def generate_key(username):
    hash_value = boozhash(username)
    return f"{hash_value:08X}"  # 8-digit uppercase hex

if __name__ == "__main__":
    print("Key Generator for boozhash Authentication")
    print("----------------------------------------")
    while True:
        username = input("Enter username (or 'quit' to exit): ").strip()
        if username.lower() == 'quit':
            break
        if not username.isascii():
            print("Error: Only ASCII characters supported")
            continue
        key = generate_key(username)
        print(f"Username: {username}")
        print(f"Password: {key}\n")
```

## Core Hash Algorithm

The `boozhash` function processes input strings through several bit manipulation operations:

```c
int boozhash(byte *param_1) {
  int iVar1;
  byte *ptr;
  uint hash;
  
  hash = 0;
  ptr = param_1;
  while (*ptr != 0) {
    iVar1 = tolower((uint)*ptr);
    hash = (hash + iVar1) * 0x401;
    hash = hash ^ hash >> 6;
    ptr = ptr + 1;
  }
  return (hash * 9 ^ hash * 9 >> 0xb) * 0x8001;
}
```

## Python Implementation

The equivalent Python implementation:

```python
def boozhash(s):
    h = 0
    for c in s.lower().encode('ascii'):
        h = (h + c) * 0x401
        h = (h ^ (h >> 6)) & 0xFFFFFFFF
    h = (h * 9) ^ ((h * 9) >> 11)
    h = (h * 0x8001) & 0xFFFFFFFF
    return h
```

## Key Generator Program

Complete key generator with proper error handling:

```python
import sys

def generate_password(username):
    try:
        username = username.strip()
        if not username.isascii():
            raise ValueError("Only ASCII characters allowed")
            
        hash_val = boozhash(username)
        return f"{hash_val:08X}"
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return None

if __name__ == "__main__":
    print("BOOZHASH Key Generator")
    print("---------------------")
    while True:
        username = input("Enter username (or 'quit' to exit): ")
        if username.lower() == 'quit':
            break
            
        password = generate_password(username)
        if password:
            print(f"Username: {username}")
            print(f"Password: {password}\n")
```

