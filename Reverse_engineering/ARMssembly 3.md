

##  Challenge Description

We're given an ARM64 assembly file (`chall_3.S`) and an input value: `597130609`. The program prints an integer, and we need to convert that integer into the flag format:

```
Flag format: picoCTF{XXXXXXXX}
→ where XXXXXXXX is the lowercase 32-bit hex representation of the integer (padded to 8 digits).
```

---

##  Reversing the Assembly

We start with the two core functions in the `.S` file: `func1` and `func2`.

### `func2` - Simple Addition

```asm
func2:
    ...
    add w0, w0, 3
    ...
```

This is a simple function that returns `x + 3`.

###  `func1` - Bitwise Loop

```asm
func1:
    result = 0
    while (input != 0) {
        if (input & 1) {
            result = func2(result); // +3
        }
        input >>= 1;
    }
    return result;
```

Every time it finds a 1-bit in `input`, it applies `func2`, which adds 3 to the result.

---

## Simulating the Behavior

```python
def func1(n):
    result = 0
    while n != 0:
        if n & 1:
            result += 3
        n >>= 1
    return result
```

Running this with input `597130609` gives:

```python
func1(597130609) = 54
```

We also verified this by counting the number of 1s in the binary:

```
bin(597130609) = 0b1000111010101111000111000001
popcount = 18
result = 3 * 18 = 54
```

---

##  Final Step: Convert to Flag

```
54 in hex = 0x36 → padded to 32-bit: 00000036
```

---

##  Final Flag

```
picoCTF{00000036}
```

---

##  Lessons Learned

- Understand ARM64 calling conventions and memory layout
- Simulating bitwise loops is super helpful in reverse engineering
- `result = result + 3` per set bit is a common obfuscation trick

