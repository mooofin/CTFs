![image](https://github.com/user-attachments/assets/55971d85-8ded-45a8-81a0-0c62939eec16)


---



When running the `bininst1.exe` binary, it prints some initial output and then enters an indefinite sleep state. According to the challenge description, the flag is revealed only after this delay, which appears to be intentionally long to slow down analysis.

To bypass the delay, I used **Frida**, a dynamic instrumentation toolkit, to hook and neutralize the `Sleep` function from `kernel32.dll`. Instead of letting the function pause execution, the hook intercepts the call and immediately returns—effectively skipping the sleep and allowing the program to continue.

Here's the Frida script used (`hook.js`):

```js
var k32 = Module.findExportByName("kernel32.dll", "Sleep");

if (k32) {
    Interceptor.replace(k32, new NativeCallback(function(ms) {
        console.log("Sleep intercepted!");
        return; // Skip the sleep
    }, "void", ["uint32"]));
}
```
The Frida script works by intercepting the `Sleep` function in `kernel32.dll`, which the binary uses to pause execution. Using `Module.findExportByName`, it locates the memory address of the exported `Sleep` function. If found, the script replaces it at runtime with a custom native function using `Interceptor.replace`. This replacement function, defined via `NativeCallback`, takes the same argument as `Sleep` (a 32-bit unsigned integer representing milliseconds) but does nothing—effectively skipping the delay. When the binary attempts to call `Sleep`, the call is redirected to this empty function, allowing the program to continue immediately without waiting. This manipulation ensures that the binary executes past the sleep call and reveals the flag without unnecessary delay.

To execute the binary with the script applied, the following command was used:

```bash
frida -f bininst1.exe -l hook.js
```

This allowed the program to run without delay and print the flag immediately.

