# **Writeup: Modular Message Decryption**

## **Challenge Overview**
We are given a sequence of numbers and a decryption scheme to convert them into a readable message. The goal is to decrypt the numbers and wrap the result in the `picoCTF{}` flag format.

### **Given Data**
- **Numbers:**  
  `165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138`  
- **Decryption Scheme:**  
  1. Take each number **modulo 37** (find the remainder when divided by 37).  
  2. Map the result to a character:  
     - `0-25` → Uppercase letters (`A-Z`, where `0=A`, `1=B`, ..., `25=Z`)  
     - `26-35` → Digits (`0-9`, where `26=0`, `27=1`, ..., `35=9`)  
     - `36` → Underscore (`_`)  

## **Step-by-Step Solution**

### **Step 1: Compute Each Number Modulo 37**
We calculate the remainder of each number when divided by 37.

| Number | Calculation | Mod 37 |
|--------|-------------|-------|
| 165    | 165 ÷ 37 = 4 R **17** | 17 |
| 248    | 248 ÷ 37 = 6 R **26** | 26 |
| 94     | 94 ÷ 37 = 2 R **20**  | 20 |
| 346    | 346 ÷ 37 = 9 R **13** | 13 |
| 299    | 299 ÷ 37 = 8 R **3**   | 3  |
| 73     | 73 ÷ 37 = 1 R **36**   | 36 |
| 198    | 198 ÷ 37 = 5 R **13**  | 13 |
| 221    | 221 ÷ 37 = 5 R **36**  | 36 |
| 313    | 313 ÷ 37 = 8 R **17**  | 17 |
| 137    | 137 ÷ 37 = 3 R **26**  | 26 |
| 205    | 205 ÷ 37 = 5 R **20**  | 20 |
| 87     | 87 ÷ 37 = 2 R **13**   | 13 |
| 336    | 336 ÷ 37 = 9 R **3**   | 3  |
| 110    | 110 ÷ 37 = 2 R **36**  | 36 |
| 186    | 186 ÷ 37 = 5 R **1**   | 1  |
| 69     | 69 ÷ 37 = 1 R **32**   | 32 |
| 223    | 223 ÷ 37 = 6 R **1**   | 1  |
| 213    | 213 ÷ 37 = 5 R **28**  | 28 |
| 216    | 216 ÷ 37 = 5 R **31**  | 31 |
| 216    | (Same as above)        | 31 |
| 177    | 177 ÷ 37 = 4 R **29**  | 29 |
| 138    | 138 ÷ 37 = 3 R **27**  | 27 |

### **Step 2: Map Modulo Results to Characters**
Using the given mapping:

| Mod 37 | Character |
|--------|-----------|
| 0-25   | A (0) to Z (25) |
| 26-35  | 0 (26) to 9 (35) |
| 36     | _ |

Applying this to our results:

| Mod 37 | Mapped Character |
|--------|-------------------|
| 17     | R |
| 26     | 0 |
| 20     | U |
| 13     | N |
| 3      | D |
| 36     | _ |
| 13     | N |
| 36     | _ |
| 17     | R |
| 26     | 0 |
| 20     | U |
| 13     | N |
| 3      | D |
| 36     | _ |
| 1      | B |
| 32     | 6 (since 32 - 26 = 6) |
| 1      | B |
| 28     | 2 (28 - 26 = 2) |
| 31     | 5 (31 - 26 = 5) |
| 31     | 5 |
| 29     | 3 (29 - 26 = 3) |
| 27     | 1 (27 - 26 = 1) |

### **Step 3: Combine Characters into the Final Message**
Putting it all together in order:
```
R 0 U N D _ N _ R 0 U N D _ B 6 B 2 5 5 3 1
```
Removing spaces:
```
R0UND_N_R0UND_B6B25531
```

### **Step 4: Wrap in Flag Format**
The final flag is:
```
picoCTF{R0UND_N_R0UND_B6B25531}
```

## **Conclusion**
By applying modular arithmetic (`mod 37`) and a simple character mapping, we decrypted the given numbers into the flag:
**`picoCTF{R0UND_N_R0UND_B6B25531}`**  

