### Binary Overview

Running `file` on the binary shows a standard ELF executable:

![file info](https://github.com/user-attachments/assets/045f0e79-743e-495b-bf71-e659cf48e529)

Nothing unusual here at first glance.


### Runtime Behavior

When executed, the binary asks for user input. Supplying anything incorrect leads to an immediate failure response, with no visible comparison or transformation in plaintext:

![runtime input](https://github.com/user-attachments/assets/22333440-13b2-45dc-b729-17359151a572)



Opening the binary in Binary Ninja reveals that the validation logic is **not normal control flow**. Instead, it looks like a **nested VM / emulator**, where execution is handled through multiple small functions acting like opcode handlers:

![vm view](https://github.com/user-attachments/assets/df9c875f-828a-4de1-9ef1-9524d25f782d)

Rather than direct comparisons, input seems to be processed through this interpreter.




Below the opcode-handling logic are several **hardcoded byte arrays** that resemble Base64-encoded data:

![b64 array 1](https://github.com/user-attachments/assets/fc80bc60-f72f-4c6a-8517-cd48512a9f04)

![b64 array 2](https://github.com/user-attachments/assets/3c5f69b1-5edd-4fee-8873-140500aa47a4)

These are likely VM data or encrypted constants consumed by the interpreter rather than decoded directly in native code.


