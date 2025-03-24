# Writeup: Understanding Fork Logic and Finding the Flag

## Analyzing the Program

We are given an ELF 32-bit binary and need to determine the last integer value passed to the function `doNothing()`. The main function is as follows:

```c
/* WARNING: Function: __x86.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx */

undefined4 main(void)
{
    int *piVar1;
    
    piVar1 = (int *)mmap((void *)0x0,4,3,0x21,-1,0);
    *piVar1 = 1000000000;
    fork();
    fork();
    fork();
    fork();
    *piVar1 = *piVar1 + 0x499602d2;
    doNothing(*piVar1);
    return 0;
}
```

The function `doNothing()` does nothing significant but takes an integer argument. Our goal is to determine the last integer value that gets passed to `doNothing()`.

---

## Understanding `fork()`

The `fork()` function creates a new child process. Each time `fork()` is called, the process count doubles.

- **First fork()** → 2 processes (1 parent, 1 child)
- **Second fork()** → 4 processes
- **Third fork()** → 8 processes
- **Fourth fork()** → 16 processes

So, after executing all `fork()` calls, there will be **16 processes** in total.

---

## Identifying the Passed Integer Value

The program initializes `*piVar1 = 1000000000` (or `0x3B9ACA00` in hex).
After the `fork()` calls, each of the **16 processes** adds `0x499602D2` (or `1234567890` in decimal) to `*piVar1`.

Thus, the final value passed to `doNothing()` is:

```python
import numpy as np

# Initial value
initial_value = np.int32(1000000000)

# Increment value
increment = np.int32(0x499602D2)

# Number of processes created (2^4 = 16)
num_processes = np.int32(16)

# Final value after all processes add the increment
final_value = initial_value + (num_processes * increment)

# Result
print(final_value)  # -721750240
```

Since we are working with **signed 32-bit integers**, integer overflow occurs, and the final value becomes **-721750240**.

### Flag:

```
picoCTF{-721750240}
```

---

## How to Identify Fork Logic in Ghidra

To analyze `fork()` logic in Ghidra:

1. **Open the Binary in Ghidra**
   - Load the ELF binary into Ghidra and let it analyze the functions.
   
2. **Find the `main()` Function**
   - Look for `fork()` calls in the decompiled output. Each `fork()` doubles the number of processes.
   
3. **Count the Number of Forks**
   - If `fork()` is called `n` times, the number of processes created is `2^n`.
   - In this case, `fork()` is called **4 times**, leading to `2^4 = 16` processes.
   
4. **Track Memory Modifications**
   - Look for a global or shared memory (like `mmap()`) that stores and modifies values across forked processes.
   - `piVar1` is modified in each child process, affecting the final value.

---

## Conclusion
By understanding `fork()`, tracking memory modifications, and handling integer overflow, we determined that the final integer value passed to `doNothing()` is **-721750240**, leading to the flag **picoCTF{-721750240}**.

