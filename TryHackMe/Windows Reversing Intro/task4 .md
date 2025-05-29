![image](https://github.com/user-attachments/assets/e63fc3f5-a7c9-4e88-a1a2-45a1c757494d)



sub RSP, 28h at the top. For this function that's the entire prologue. It's setting up the function by moving the stack pointer and creating a new stack frame area


![image](https://github.com/user-attachments/assets/1fbd14ec-1f2a-483c-84fb-e5ca5876a00a)



Inlining
One compiler/linker optimization that makes noticeable changes to the code is inlining. When a function gets inlined it's essentially pasted where the call would be instead of making a call. See the following example.

Without Function Inlining:
```c

int Add(int x, int y){
    return x+y;
}
int main(){
    int x = RandInt();
    int res = Add(x, 5)
}

```

With Function Inlining:
```c

int main(){
    int x = RandInt();
    int res = x + 5;
}

```




### SUMMARY


---

### Summary of Analysis: `HelloWorld.exe`

This analysis involved examining a simple Windows x64 executable (`HelloWorld.exe`) in IDA Pro to understand function calling conventions, stack setup, and compiler optimizations such as function inlining.

#### Program Execution and IDA Configuration

Before beginning the reverse engineering process, the program was executed in a command prompt environment to observe its behavior. When loading the binary into IDA, it was important to avoid downloading debug symbols to simulate a realistic reverse engineering scenario. Debug symbols, if needed, could be loaded manually from the provided directory.

#### Stack Frame Setup and Calling Convention

In the `main()` function, the instruction `sub rsp, 28h` establishes a new stack frame by adjusting the stack pointer. This is a standard part of the function prologue in the Microsoft x64 calling convention. According to this convention, function parameters are passed in the following order:

* First parameter: `RCX`
* Second parameter: `RDX`
* Third parameter: `R8`
* Fourth parameter: `R9`

#### Analysis of `printf()` Call

The first function call in `main()` is a call to `printf()`. Although not explicitly named in IDA, it was identified based on its usage and parameter setup:

* The instruction `lea rcx, Format` sets the first parameter, which is the format string (`"%s\n"`).
* The instruction `lea rdx, aHelloWithPrint` sets the second parameter, the message string (`"Hello with printf()"`).

This matches the signature of `printf(const char *format, ...)`.

#### Analysis of `std::cout` Call

The second call in `main()` involves C++ standard output using `std::cout`. This was inferred from the use of symbols related to `basic_ostream`, `char_traits`, and `std::cout`, despite the presence of C++ name mangling.

Unlike `printf`, the string output associated with `std::cout` is not passed as a parameter. Instead, it is directly embedded within the function due to compiler inlining.

#### Function Inlining

The analysis revealed that the call to `std::cout` was inlined by the compiler. Instead of a direct function call, the corresponding logic is inserted directly into `main()`. This behavior is common when the compiler detects that the function is only called once and meets inlining criteria. If `std::cout` were called multiple times, inlining would typically not occur, and the function call structure would more closely resemble that of `printf()`.



