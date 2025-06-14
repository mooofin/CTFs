# CrackMe Writeup - Simple Password Check Binary

## Initial Analysis

This CrackMe binary prompts the user for a password and validates it against a hardcoded value.

### First Attempt: Static Analysis with Ghidra

* Loaded the binary into Ghidra.
* Initial scan revealed no obvious strings or logic.
* Suspected anti-decompilation techniques or debug protection.

### Dynamic Analysis with GDB

* Ran the binary with `gdb ./crackme`.
* Used `info functions` and `strings` to identify interesting sections.
* Located the welcome message: `"Welcome to your first Crack Me program!"`
* Traced cross-references to locate the password validation logic.

## Targeted Analysis in Ghidra

* Using the string's memory address, located the main function.
* Identified a function named `FUN_140018060` that contains the primary logic.

### Decompilation Summary (Relevant Sections):

```c
void FUN_140018060(void)
{
  // ... (stack setup and debug checks) ...

  thunk_FUN_1400152c0(local_170, "QuiteEasyRight"); // Hardcoded password
  thunk_FUN_140015360(local_130);

  // Display messages
  thunk_FUN_1400138e0(cout_exref, "Welcome to your first Crack Me program!");
  thunk_FUN_1400138e0(cout_exref, "What is the password?: ");
  thunk_FUN_1400134a0(cin_exref, local_130); // Get user input

  // Compare user input with hardcoded password
  cVar1 = thunk_FUN_140013d80(local_130, local_170);

  if (cVar1 == '\0') {
    thunk_FUN_1400138e0(cout_exref, "Authentication Failed.");
  } else {
    thunk_FUN_1400138e0(cout_exref, "Authentication Successful.");
  }

  // Cleanup and exit prompts
  thunk_FUN_1400138e0(cout_exref, "Press ENTER to exit!");
  // ... (final input waits and cleanups) ...
}
```

## Password Check Logic

The program performs a simple string comparison:

```c
thunk_FUN_1400152c0(local_170, "QuiteEasyRight"); // Hardcoded password
cVar1 = thunk_FUN_140013d80(user_input, local_170);
```

If the user input matches the hardcoded string, access is granted.

## Conclusion

Combining static and dynamic analysis was necessary to fully understand the binary:

* Ghidra alone did not immediately reveal the password.
* GDB helped locate key strings in memory.
* Tracing back from the string reference led to the exact comparison logic.

**Recovered Password:** `QuiteEasyRight`

![image](https://github.com/user-attachments/assets/640a5bf7-de37-4da4-a60c-9304608eea35)
![image](https://github.com/user-attachments/assets/eadca60d-0040-4499-8be4-cd25df311030)


