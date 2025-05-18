# **Modular Cryptography Challenge Writeup**

## **Challenge Overview**
We are given a sequence of numbers and the following instructions:
1. **Modulo Operation**: Take each number modulo 41.
2. **Modular Inverse**: Find the modular inverse of each result modulo 41.
3. **Character Mapping**:
   - Numbers **1-26** correspond to uppercase letters (**A-Z**).
   - Numbers **27-36** correspond to digits (**0-9**).
   - Number **37** corresponds to an underscore (`_`).
4. Wrap the decrypted message in the `picoCTF{...}` flag format.

### **Given Numbers**
```
432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63
```

---

## **Step 1: Compute Each Number Modulo 41**
We calculate `number % 41` for each given number.

| Original Number | Mod 41 Calculation | Result |
|----------------|--------------------|--------|
| 432 | 432 - (41 × 10) = 432 - 410 = **22** | 22 |
| 331 | 331 - (41 × 8) = 331 - 328 = **3** | 3 |
| 192 | 192 - (41 × 4) = 192 - 164 = **28** | 28 |
| 108 | 108 - (41 × 2) = 108 - 82 = **26** | 26 |
| 180 | 180 - (41 × 4) = 180 - 164 = **16** | 16 |
| 50 | 50 - 41 = **9** | 9 |
| 231 | 231 - (41 × 5) = 231 - 205 = **26** | 26 |
| 188 | 188 - (41 × 4) = 188 - 164 = **24** | 24 |
| 105 | 105 - (41 × 2) = 105 - 82 = **23** | 23 |
| 51 | 51 - 41 = **10** | 10 |
| 364 | 364 - (41 × 8) = 364 - 328 = **36** | 36 |
| 168 | 168 - (41 × 4) = 168 - 164 = **4** | 4 |
| 344 | 344 - (41 × 8) = 344 - 328 = **16** | 16 |
| 195 | 195 - (41 × 4) = 195 - 164 = **31** | 31 |
| 297 | 297 - (41 × 7) = 297 - 287 = **10** | 10 |
| 342 | 342 - (41 × 8) = 342 - 328 = **14** | 14 |
| 292 | 292 - (41 × 7) = 292 - 287 = **5** | 5 |
| 198 | 198 - (41 × 4) = 198 - 164 = **34** | 34 |
| 448 | 448 - (41 × 10) = 448 - 410 = **38** | 38 |
| 62 | 62 - 41 = **21** | 21 |
| 236 | 236 - (41 × 5) = 236 - 205 = **31** | 31 |
| 342 | (Same as above) = **14** | 14 |
| 63 | 63 - 41 = **22** | 22 |

**Modulo Results:**
```
[22, 3, 28, 26, 16, 9, 26, 24, 23, 10, 36, 4, 16, 31, 10, 14, 5, 34, 38, 21, 31, 14, 22]
```

---

## **Step 2: Find Modular Inverses (mod 41)**
The modular inverse of `a` modulo `m` is a number `x` such that:
\[ a \times x \equiv 1 \ (\text{mod} \ m) \]

We compute the inverse for each number in the list:

| Number (mod 41) | Modular Inverse (x) | Verification |
|----------------|---------------------|--------------|
| 22 | 28 | \( 22 \times 28 = 616 \equiv 1 \ (\text{mod} \ 41) \) |
| 3 | 14 | \( 3 \times 14 = 42 \equiv 1 \ (\text{mod} \ 41) \) |
| 28 | 22 | \( 28 \times 22 = 616 \equiv 1 \ (\text{mod} \ 41) \) |
| 26 | 30 | \( 26 \times 30 = 780 \equiv 1 \ (\text{mod} \ 41) \) |
| 16 | 18 | \( 16 \times 18 = 288 \equiv 1 \ (\text{mod} \ 41) \) |
| 9 | 32 | \( 9 \times 32 = 288 \equiv 1 \ (\text{mod} \ 41) \) |
| 26 | 30 | (Same as above) |
| 24 | 12 | \( 24 \times 12 = 288 \equiv 1 \ (\text{mod} \ 41) \) |
| 23 | 25 | \( 23 \times 25 = 575 \equiv 1 \ (\text{mod} \ 41) \) |
| 10 | 37 | \( 10 \times 37 = 370 \equiv 1 \ (\text{mod} \ 41) \) |
| 36 | 8 | \( 36 \times 8 = 288 \equiv 1 \ (\text{mod} \ 41) \) |
| 4 | 31 | \( 4 \times 31 = 124 \equiv 1 \ (\text{mod} \ 41) \) |
| 16 | 18 | (Same as above) |
| 31 | 4 | \( 31 \times 4 = 124 \equiv 1 \ (\text{mod} \ 41) \) |
| 10 | 37 | (Same as above) |
| 14 | 3 | \( 14 \times 3 = 42 \equiv 1 \ (\text{mod} \ 41) \) |
| 5 | 33 | \( 5 \times 33 = 165 \equiv 1 \ (\text{mod} \ 41) \) |
| 34 | 35 | \( 34 \times 35 = 1190 \equiv 1 \ (\text{mod} \ 41) \) |
| 38 | 27 | \( 38 \times 27 = 1026 \equiv 1 \ (\text{mod} \ 41) \) |
| 21 | 2 | \( 21 \times 2 = 42 \equiv 1 \ (\text{mod} \ 41) \) |
| 31 | 4 | (Same as above) |
| 14 | 3 | (Same as above) |
| 22 | 28 | (Same as above) |

**Inverse Results:**
```
[28, 14, 22, 30, 18, 32, 30, 12, 25, 37, 8, 31, 18, 4, 37, 3, 33, 35, 27, 2, 4, 3, 28]
```

---

## **Step 3: Map Inverses to Characters**
Using the given mapping:
- **1-26** → **A-Z** (1=A, 2=B, ..., 26=Z)
- **27-36** → **0-9** (27=0, 28=1, ..., 36=9)
- **37** → `_`

| Inverse | Mapped Character |
|---------|------------------|
| 28 | '1' (since 27=0, 28=1, ..., 36=9) |
| 14 | 'N' |
| 22 | 'V' |
| 30 | '3' |
| 18 | 'R' |
| 32 | '5' |
| 30 | '3' |
| 12 | 'L' |
| 25 | 'Y' |
| 37 | '_' |
| 8 | 'H' |
| 31 | '4' |
| 18 | 'R' |
| 4 | 'D' |
| 37 | '_' |
| 3 | 'C' |
| 33 | '6' |
| 35 | '8' |
| 27 | '0' |
| 2 | 'B' |
| 4 | 'D' |
| 3 | 'C' |
| 28 | '1' |

**Decrypted Message:**
```
1 N V 3 R 5 3 L Y _ H 4 R D _ C 6 8 0 B D C 1
→ "1NV3R53LY_H4RD_C680BDC1"
```

---

## **Final Flag**
Wrap the decrypted message in `picoCTF{...}`:
```
picoCTF{1NV3R53LY_H4RD_C680BDC1}
```
