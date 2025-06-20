![image](https://github.com/user-attachments/assets/9e3f9db9-2225-4603-bcf4-8522300fd846)


While reversing the binary, I encountered anti-debugging logic embedded in the function `sub_4016e0`. This function is responsible for detecting the presence of a debugger and printing corresponding debug messages using Windows API functions. Specifically, the function calls `IsDebuggerPresent`, which returns a non-zero value if a debugger is attached to the process. The result of this call is then tested using the `test eax, eax` instruction, followed by a conditional jump.

The binary performs a `jne` (jump if not equal) to skip over a debug warning message if a debugger is detected. This message is printed using `OutputDebugStringW`, and the string indicates that the debugger was caught. To prevent this behavior and allow the program to execute as if no debugger were present, I patched this `jne` instruction.

Originally, the instruction at address `0x401830` was `jne 0x401847`, which would jump past the debug message when `eax` was non-zero (i.e., when a debugger was detected). 




![image](https://github.com/user-attachments/assets/7074134e-cf32-481a-84ba-4ccf20a1d754)
![image](https://github.com/user-attachments/assets/b948227c-7daa-446f-972a-39b24b1076fd)

