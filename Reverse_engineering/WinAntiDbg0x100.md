

## Introduction
In this challenge, we’re dealing with a binary that tries to detect if it’s being debugged. If it detects a debugger, it stops us from getting the flag. Our job? **Bypass this anti-debugging trick and grab the flag!**

We'll use **x32dbg** to step through the program, modify values, and trick the binary into thinking we’re not debugging it.

---

## Step 1: Open the Binary in x32dbg
1. Open **x32dbg** and load the executable.
2. Run the program until it hits the **EntryPoint** (you’ll see the main code appear).

---

## Step 2: Look for the Flag
1. Open the **Strings Window** (**Ctrl + F9** or **Search → Find Strings**).
2. Look for anything that resembles a flag (like **picoCTF** or similar).
3. Double-click the string’s memory location to jump to its reference in the code.

---

## Step 3: Finding the Anti-Debugging Check
1. As we step through the code, we find a call to **`IsDebuggerPresent`**.
2. This function checks if a debugger is attached. If it returns `1`, the program knows we’re debugging and blocks us.
3. Set a **breakpoint** on this function by pressing **F2** and then continue execution with **F9**.

---

## Step 4: Bypassing `IsDebuggerPresent`
1. Once the program stops at the **IsDebuggerPresent** function, step through it using **F8 (Step Over)**.
2. Check the **EAX** register:
   - If **EAX = 1**, the program detected the debugger.
   - If **EAX = 0**, no debugger is detected.
3. **Modify EAX to 0**:
   - Right-click **EAX** in the register window.
   - Select **Modify**, and change the value to `00000000`.
4. Alternatively, you can **force the jump to be taken** by modifying the **Zero Flag (ZF)** manually.

---

## Step 5: Extracting the Flag
1. Press **F9** to continue execution.
2. The program now skips the anti-debugging check and proceeds to decrypt the flag.
3. The flag should now be visible in memory or the program’s output! 🎉

---

## Conclusion
By using **x32dbg**, we easily bypassed the debugger check and retrieved the flag. This is a common trick used in reverse engineering, and now you know how to handle it!

### Key Takeaways I Learnt :
✅ Use **Ctrl + F9** to search for important strings.  
✅ Step through execution using **F8** and find anti-debugging checks.  
✅ Modify **EAX = 0** to trick the program into thinking no debugger is present.  
✅ **F9** to continue and grab the flag.  


