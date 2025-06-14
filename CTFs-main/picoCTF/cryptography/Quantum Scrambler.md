# **Quantum Scrambler (Crypto – 200 pts) Writeup**  

## **Challenge Description**
We are given a challenge that claims to use **"quantum entanglement"** to scramble the flag. We need to **reverse** the scrambling process to recover the original flag.

### **Challenge Instructions**
We are provided with a netcat (`nc`) command to connect to the challenge server:
```sh
nc verbal-sleep.picoctf.net 60759
```
When we connect, we receive a **scrambled list**, which is a Python object. Our goal is to unscramble it and recover the flag.

We are also given the Python source code used to scramble the flag.

---

## **Step 1: Understanding the Scrambling Code**
The given Python script contains the **scramble** function:

### **Scramble Function Analysis**
```python
def scramble(L):
    A = L
    i = 2
    while (i < len(A)):
        A[i-2] += A.pop(i-1)   # Step 1: Combine elements
        A[i-1].append(A[:i-2]) # Step 2: Store previous elements in a nested list
        i += 1                 # Step 3: Move to the next index
    return L
```

### **Breakdown of What Happens**
- It starts with a **list of hex-encoded characters** representing the flag.
- The function **modifies** the list step by step:
  1. **Adds (`+=`) the (i-1)th element to the (i-2)th element.**
  2. **Stores previous elements in a nested list inside (i-1).**
  3. **Moves to the next index and repeats.**

- This makes **reversing** the process tricky because **information is hidden inside nested lists**.

---

## **Step 2: Getting the Scrambled Data**
To retrieve the scrambled data, **run the following command in a terminal**:

```sh
nc verbal-sleep.picoctf.net 60759 > output.txt
```

This does two things:
1. Connects to the challenge server.
2. **Saves the scrambled output** into a file called `output.txt`.

After running the command, `output.txt` will contain a **long Python list** of scrambled hex values.

---

## **Step 3: Writing the Unscrambling Function**
To reverse the scrambling process, we must **undo each transformation in reverse order**.

### **Unscrambling Strategy**
- Since scrambling **combined** elements and stored previous steps inside nested lists, we must:
  1. **Extract** the stored values from nested lists.
  2. **Undo the additions (`+=`) that were performed.**
  3. **Reinsert the removed elements back into the correct positions.**
  4. **Continue working backward until the original list is restored.**

### **Python Code for Unscrambling**
```python
import sys

def unscramble(L):
    A = L
    i = len(A) - 1  # Start from the last modified index

    while i >= 2:
        # Extract the stored prefix (previous part of the list)
        prefix = A[i-1].pop()

        # Recover the original element in A[i-2]
        original_element = A[i-2][-len(A[i-1]):]
        A[i-2] = A[i-2][:-len(A[i-1])]  # Remove scrambled portion

        # Restore A[i-1] to its original position
        A.insert(i-1, original_element)

        i -= 1  # Move backwards

    return L

def main(file):
    # Read scrambled flag from the file and convert it into a Python list
    scrambled_flag = eval(open(file, 'r').read())

    # Unscramble the flag
    flag_hex = unscramble(scrambled_flag)

    # Convert hex values to characters and print the flag
    for c in flag_hex:
        print(chr(int(c[0], 16)), end='')

if __name__ == '__main__':
    main(sys.argv[1])
```

### **Explanation of the Code**
1. **`unscramble(L)` function**
   - Works **backward** through the scrambled list.
   - **Extracts** the stored parts from nested lists.
   - **Reverses the modifications** made during scrambling.
   - **Restores the original sequence** of hex values.

2. **`main(file)` function**
   - Reads the scrambled list from `output.txt`.
   - Converts it into a Python object using `eval()`.
   - Calls `unscramble()` to recover the original list.
   - Converts **hex values back into characters** to reconstruct the flag.

---

## **Step 4: Running the Unscrambler**
After saving the script as `unscramble.py`, run it using:

```sh
python unscramble.py output.txt
```

This will:
1. **Load the scrambled data from `output.txt`**.
2. **Run the unscramble function to recover the original flag**.
3. **Print the flag as text**.

### **Expected Output**
```
picoCTF{python_is_weirde2a45ca5}
```

---

## **Step 5: Understanding the Recovered Flag**
The final output is:
```
picoCTF{python_is_weirde2a45ca5}
```
This confirms that we **successfully reversed** the scrambling process and retrieved the original flag.

---

## **Summary of Steps**
| **Step** | **What We Did** |
|----------|----------------|
| **1** | Understood how the `scramble()` function modifies the flag. |
| **2** | Retrieved the scrambled flag by running `nc verbal-sleep.picoctf.net 60759 > output.txt`. |
| **3** | Wrote an `unscramble()` function to reverse the scrambling process. |
| **4** | Ran `python unscramble.py output.txt` to decode the flag. |
| **5** | Successfully obtained the flag: `picoCTF{python_is_weirde2a45ca5}`. |

---

## **Final Thoughts**
- This challenge was tricky because of the **nested list structure** hiding information.
- The key insight was **realizing how the scramble function stored previous elements** and **reversing that process** step by step.
- **Running `eval()` on the scrambled data** allowed us to work with it as a **Python object**.
- We worked **backwards** through the scrambled list, recovering the original flag.

This structured approach will **help you understand and recall the solution** when reviewing it later. 🚀

