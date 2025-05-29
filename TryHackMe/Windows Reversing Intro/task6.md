

## Structures and Memory Layout in Reverse Engineering

Modern software, especially on Windows, frequently uses structured data types due to its object-oriented design. Understanding how arrays and classes are laid out in memory is essential for effective reverse engineering.

### Arrays

Arrays consist of sequential memory segments storing elements of the same data type. For example, an integer array of 5 elements, starting at address `0x4000`, occupies 20 bytes (5 × 4 bytes per integer). The location of each element follows predictable offsets (e.g., `0x4000`, `0x4004`, etc.). Arrays are typically straightforward to analyze, such as in the earlier loop-based string inspection task.

### Classes

Classes are more complex structures that can store multiple data types. This heterogeneity, combined with the use of pointers and internal offsets, increases the difficulty of reverse engineering. Identifying the structure of a class typically involves analyzing how various functions access and manipulate its fields.

#### Example: `Human` Class

Consider the following C++ class:

```cpp
class Human {
public:
    int age;
    float height;
    char* name;
    Human(char* newName, int newAge, float newHeight)
        : age(newAge), height(newHeight), name(newName) {}
};
```

This class occupies 16 bytes in memory on a 64-bit system:

* `int age`: 4 bytes
* `float height`: 4 bytes
* `char* name`: 8 bytes (pointer)

Suppose an instance resides at address `0x4000`, and a pointer to it is in `RAX`. The layout in assembly would look like:

```asm
mov RAX, 0x4000     ; RAX = base address (age field)
lea RBX, [RAX+0x4]  ; RBX = address of height
lea RCX, [RAX+0x8]  ; RCX = address of name
mov [RAX], 0x32     ; age = 50
mov [RBX], 0x48     ; height = 72
mov [RCX], 0x424F42 ; name = "BOB"
```

Fields are accessed using offsets from the base address. The `lea` instruction is frequently used to retrieve addresses of internal fields rather than their contents. This is a hallmark of pointer-based access within classes.


