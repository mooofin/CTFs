

# Reverse Engineering DLLs

This document provides an overview of how Dynamic-Link Libraries (DLLs) work and how they can be analyzed, debugged, or reverse-engineered. Understanding DLLs is essential when reverse engineering Windows software.

---

## What is a DLL?

- A **Dynamic-Link Library (DLL)** is a binary file that contains executable code.
- A DLL cannot be run directly; it must be loaded by a host process.
- When loaded, the function `DllMain()` is executed within the context of the host process.
- DLLs are widely used in Windows for code reuse and memory efficiency.

---

## Executing a DLL for Analysis

### DLL Injection

One method of executing code inside a DLL is to inject it into a running process:

```cpp
HMODULE dll = LoadLibraryA("DLL.DLL");
````

This causes the `DllMain()` function to be executed.

### Using rundll32.exe

Windows provides a utility called `rundll32.exe`, which can load DLLs and execute specific exported functions. While this is intended for legitimate use, it is rarely used in reverse engineering workflows due to its limitations.

### Writing a Custom Loader

For targeted analysis of a specific function within a DLL, a custom loader can be written:

```cpp
HMODULE dll = LoadLibraryA("DLL.DLL");

// Define the function signature
typedef void(WINAPI* Add_TypeDef)(int, int);

// Get a pointer to the function
Add_TypeDef Add = (Add_TypeDef)GetProcAddress(dll, "Add_MangledName");

// Call the function
Add(1, 2);
```

Note: Without access to a header file or library file, the function signature must be reverse engineered.

---

## Imports, Exports, and Modules

* **Imports:** Functions that an executable or DLL uses from other DLLs.
* **Exports:** Functions that a DLL exposes to other modules.
* **Modules:** Executables and DLLs loaded into a process. For example, running `Loop.exe` will also load modules such as `kernel32.dll` and `ntdll.dll`.

Reverse engineering tools such as IDA Pro can identify known library functions using:

* **FLIRT (Fast Library Identification and Recognition Technology):** A signature-based system for identifying standard library functions by matching known byte patterns.

---

## Name Mangling and Decoration

C++ supports function overloading, where multiple functions can share the same name but have different parameters. This requires unique naming at the binary level, which is accomplished through **name mangling** (also called **function decoration**).

Example of a mangled name:

```
??0?$_Yarn@D@std@@QEAA@PEBD@Z
```

Tools such as IDA and Ghidra can demangle these names to recover the original function signatures.

### C Linkage

To avoid name mangling, developers can use `extern "C"` in C++:

```cpp
extern "C" void MyFunction(); // Prevents name mangling
```

Note: This disables function overloading for that function.

---

## Summary

* DLLs are often easier to reverse engineer than executables because function names are often preserved and debug symbols may be included.
* Use `LoadLibrary()` and `GetProcAddress()` to load and call functions in a DLL.
* Understanding FLIRT, name mangling, and the import/export system is critical for effective reverse engineering.



