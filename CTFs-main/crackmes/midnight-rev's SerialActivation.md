![image](https://github.com/user-attachments/assets/aea05e30-f803-4e47-b48d-b090e1a2e211)




## Serial Key Validation Breakdown

### 1. Input Requirements

* Format: `XXXX-XXXX` (4 characters, hyphen, 4 characters)
* Total length: **9 characters**

### 2. Key Validation Process

#### a. Length Check

```c
if (strlen(serial) != 9) ExitProcess(1);
```

* If the input is not exactly 9 characters, the program exits immediately.

#### b. Mathematical Transformations

The program performs 100 iterations of calculations involving the serial’s characters.

```c
local_20 = (serial[0] + serial[5] ^ (serial[2] | serial[6])) & 0xF + local_20;
local_24 = (serial[1] + serial[7] + serial[8] ^ local_20) & 0xF0 + local_24;
```

* `local_20` uses serial characters 0, 2, 5, 6
* `local_24` uses characters 1, 7, 8 and depends on `local_20`

The result then branches based on a parity check:

```c
if (local_24 % 2 == 0) {
    local_2c = serial[8] + local_24 + (serial[4] >> (local_20 & 1));
} else {
    local_2c = (serial[4] << (local_20 & 2)) + 2 + serial[8] | local_24;
}
```

* `local_2c` depends on character 4, 8, and the previously computed values.

#### c. Final Check

```c
if (local_20 + local_24 + local_2c == 0) {
    printf("Access granted.");
}
```

* Only if the **sum of `local_20`, `local_24`, and `local_2c` equals zero**, access is granted.

 Python script to automate the process
```python
from itertools import product

# Brute-force all possible ASCII characters from 32 (' ') to 126 ('~') for each serial position
for A, B, C, D, E, F, G, H in product(range(32, 127), repeat=8):
    # Compute local_20 using given formula
    local_20 = (A + E ^ (C | F)) & 0xF
    
    #
    local_24 = (B + G + H ^ local_20) & 0xF0

  
    if local_24 % 2 == 0:
        local_2c = H + local_24 + (D >> (local_20 & 1))
    else:
        local_2c = (D << (local_20 & 2)) + 2 + H | local_24

    
    if local_20 + local_24 + local_2c == 0:
        serial = f"{chr(A)}{chr(B)}{chr(C)}{chr(D)}-{chr(E)}{chr(F)}{chr(G)}{chr(H)}"
        print(f"Valid serial found: {serial}")
        break

```

![image](https://github.com/user-attachments/assets/d7f07048-0372-4d0f-a9d8-74a93ce4c420)
