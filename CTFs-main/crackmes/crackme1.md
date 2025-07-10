<img width="1605" height="752" alt="screenshot-1752173720" src="https://github.com/user-attachments/assets/a0699a67-d7d3-4bce-9667-23d9c7c89db1" />
In the given disassembly snippet starting at `LAB_001013da`, the logic flow is precise and deliberate. The program first accesses a value located at `[RBP - 0x40]` (likely a local variable, given the offset) and moves it into `RAX`. It then adds `0x8` to this value, dereferences the resulting pointer, and stores the content in `RSI`. At this point, `RSI` contains some value likely intended to be copied—this is confirmed by the subsequent `LEA` loading the address of a global buffer (denoted `[PASS]`) into `RDI`. The standard library function `strcpy` is then called, copying the content from `RSI` to `RDI`. The copied string likely represents an identifier or password.

After copying, the code zeroes out `EAX` and proceeds to call the function `check_id_xor()`. The result of this function is stored back into `EDI` and immediately passed to another function, `check_id_sum()`. Following this, a `TEST` is performed on the return value in `EAX`, and if it is non-zero, the control jumps to a later code block (`LAB_00101413`). Otherwise, it moves `0` into `EAX` again and calls the `error()` function, likely indicating a failed verification.

This structure strongly implies that two checks—`check_id_xor()` and `check_id_sum()`—are both critical validation steps for the copied string. 
```c

undefined8 main(int param_1,long param_2)

{
  undefined4 uVar1;
  int iVar2;
  size_t sVar3;
  size_t sVar4;
  long in_FS_OFFSET;
  char local_2a [10];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  if (param_1 != 2) {
    puts("Usage: ./crackme <key>");
                    /* WARNING: Subroutine does not return */
    exit(-1);
  }
  sVar3 = strlen(*(char **)(param_2 + 8));
  if (4 < sVar3) {
    sVar3 = strlen(*(char **)(param_2 + 8));
    if (sVar3 < 0xff) goto LAB_00101387;
  }
  error();
LAB_00101387:
  builtin_strncpy(local_2a,"0123456789",10);
  sVar3 = strlen(*(char **)(param_2 + 8));
  sVar4 = strspn(*(char **)(param_2 + 8),local_2a);
  if (sVar3 != sVar4) {
    error();
  }
  strcpy(&PASS,*(char **)(param_2 + 8));
  uVar1 = check_id_xor();
  iVar2 = check_id_sum(uVar1);
  if (iVar2 == 0) {
    error();
  }
  puts("The password was correct");
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
The `main` function strictly validates a user-provided key. It requires exactly one argument and checks that its length is between 5 and 254 characters. It then verifies that the key consists only of digits using `strspn`. If any of these checks fail, it calls `error()` and exits. On success, the key is copied into a global `PASS` buffer. Two verification functions, `check_id_xor()` and `check_id_sum()`, are called in sequence. If both pass, the program prints a success message; otherwise, it terminates. The flow is tight, minimal, and leaves no room for incorrect input.
<img width="557" height="286" alt="screenshot-1752174166" src="https://github.com/user-attachments/assets/2b79a02c-6e49-47b5-a1b9-7a4f75527c0c" />



The `check_id_xor` function validates the password by combining its first character with a hidden byte from a static buffer. It selects a byte based on the password's length, subtracts `'0'` from both values to get integers, and XORs them. If the result is smaller than either of the original numbers, it returns `0xffffffff`, signaling failure. Otherwise, it returns the XOR result. This introduces a tight dependency between the first character and the length of the password, making it resistant to naive guessing.



<img width="511" height="554" alt="screenshot-1752174224" src="https://github.com/user-attachments/assets/7cae49ef-95f7-4231-901e-722065d1094c" />

The `check_id_sum` function performs an alternating sum over the digits of the password, excluding the first and last characters. It iterates from index 1 to `len - 2`, adding digits at odd indices and subtracting those at even indices. The final result is compared to the value produced by `check_id_xor`. If the computed sum matches this value and the XOR result is not -1, the function returns success; otherwise, it fails. This introduces a numeric dependency between the middle digits of the password and the XOR of its endpoints.

The binary enforces a strict length requirement on the input string: it must be greater than 4 characters. This is checked explicitly in `main()` using a call to `strlen`, followed by a conditional that immediately invokes the `error()` function if the length is 4 or less. 


Keygen 


```python3
 from itertools import permutations

def check_id_xor(pass_str):
    rax_2 = int(pass_str[0])
    rax_6 = int(pass_str[len(pass_str) - 1])
    rax_8 = rax_2 ^ rax_6
    return rax_8 if rax_8 >= rax_2 and rax_8 >= rax_6 else -1

def check_id_sum(pass_str, xor_val):
    if xor_val == -1:
        return False
    var_20 = 0
    for i in range(1, len(pass_str) - 1):
        if i % 2 == 1:
            var_20 += int(pass_str[i])
        else:
            var_20 -= int(pass_str[i])
    return var_20 == xor_val

for i in range(5, 10):
    for perm in permutations("1234567890", i):
        pass_str = "".join(perm)
        xor_val = check_id_xor(pass_str)
        if check_id_sum(pass_str, xor_val):
            print("A password was found: ", pass_str)
            break
```

The keygen script is designed to reverse the logic implemented in the binary's validation functions, specifically `check_id_xor` and `check_id_sum`. It aims to generate a valid numeric password that satisfies both conditions. The script systematically generates digit-only strings using permutations of `"1234567890"` with lengths ranging from 5 to 9. These lengths are chosen to comply with the binary’s requirement that the input must be strictly longer than 4 characters.

The `check_id_xor` function takes the first and last digits of the candidate password, computes their bitwise XOR, and accepts the result only if it is greater than or equal to both operands. If this condition fails, the XOR result is rejected. The `check_id_sum` function then validates the middle portion of the password. It calculates an alternating sum: adding digits at odd indices and subtracting those at even indices. The result must match the XOR value obtained earlier.

The script runs these checks over each permutation and prints the first password that passes both. The use of permutations ensures each digit is unique in a given attempt, which reduces redundancy but also limits the search space. 














