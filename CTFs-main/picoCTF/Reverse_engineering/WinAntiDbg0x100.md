# Bypassing `IsDebuggerPresent` & Extracting the Flag – Step-by-Step Guide

## Introduction
This challenge involves analyzing a binary that performs an anti-debugging check. If a debugger is detected, the program prevents further execution. The goal is to bypass this check and extract the flag.

The tool used for this analysis is **x32dbg**.

---

## Step 1: Open the Binary in x32dbg
1. Open **x32dbg** and load the executable.
2. Run the program until it reaches the **EntryPoint**, where execution begins.

---

## Step 2: Search for the Flag
1. Open the **Strings Window** (**Ctrl + F9** or **Search → Find Strings**).
2. Look for any relevant strings, such as **picoCTF** or other flag-like text.
3. Double-click the string’s memory location to jump to its reference in the code.

---

## Step 3: Identifying the Anti-Debugging Check
1. Step through the program to locate a call to **`IsDebuggerPresent`**.
2. This function determines whether a debugger is attached.
3. Set a **breakpoint** on this function call by pressing **F2** and then continue execution with **F9**.

---

## Step 4: Bypassing `IsDebuggerPresent`
1. When execution stops at the **IsDebuggerPresent** function, use **F8 (Step Over)** to proceed.
2. Observe the **EAX** register after the function call:
   - If **EAX = 1**, the program detected a debugger.
   - If **EAX = 0**, no debugger is detected.
3. Modify **EAX to 0**:
   - Right-click **EAX** in the register window.
   - Select **Modify**, and change the value to `00000000`.
4. Alternatively, modify the **Zero Flag (ZF)** to ensure the correct jump is taken.

---

## Step 5: Extracting the Flag
1. Continue execution by pressing **F9**.
2. The program now skips the anti-debugging check and proceeds with normal execution.
3. The flag should now be decrypted and visible in memory or output.

---

## Conclusion
By using **x32dbg**, the debugger detection mechanism was bypassed, allowing extraction of the hidden flag. This technique is commonly used in reverse engineering to defeat anti-debugging measures.




