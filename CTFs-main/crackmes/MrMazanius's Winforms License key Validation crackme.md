![image](https://github.com/user-attachments/assets/9c0698f4-5395-4519-bd6d-4315936cd730)

We were provided with a simple CrackMe challenge consisting of two files: `Crackme.exe` and `Crackme.dll`. The objective was to find the correct license key that, when entered into the application, would display the message: *"Correct license key!"* Otherwise, the application would respond with *"Invalid license key. Please try again."*

Upon launching the application, a GUI appeared prompting the user to input a license key. At first, we attempted to analyze `Crackme.exe` using dnSpy, a popular .NET reverse engineering tool. However, we quickly noticed that `Crackme.exe` only displayed PE headers and section data, with no decompiled .NET code or methods. This indicated that the executable was likely a native wrapper or launcher and that the actual license-checking logic resided elsewhere.

We then turned our attention to `Crackme.dll`, which, when opened in dnSpy, revealed a fully decompilable .NET assembly. Navigating through the module, we located the `Form1` class and the `button1_Click` method — the event handler triggered when the license validation button was pressed. Inside this method, we found a simple conditional check that compared the contents of `textBox1` (the license input field) to a hardcoded string.


![image](https://github.com/user-attachments/assets/dbdd5e39-b5d2-41f2-b7eb-26ed1a1c3358)


The relevant code was straightforward: if `textBox1.Text` equaled `"YouFoundTheLicenseKey"`, the program would display a success message. Otherwise, it would indicate failure. From this, it was immediately clear that the correct license key was simply the hardcoded string: `YouFoundTheLicenseKey`.

To verify our findings, we ran the application again and entered `YouFoundTheLicenseKey` into the license field. As expected, the application responded with the success message, confirming that the key was correct. This concluded the challenge.

![image](https://github.com/user-attachments/assets/7ce7eec9-ece0-4de2-892d-849e98d213a1)

dnSpy is often preferred over Ghidra for analyzing .NET applications because it is specifically built for working with .NET assemblies. While Ghidra is a powerful general-purpose reverse engineering suite capable of analyzing both native and managed code, it lacks the deep .NET-specific features that dnSpy offers out of the box. dnSpy can decompile .NET assemblies directly into readable C# code, preserving high-level constructs like classes, methods, properties, and even Windows Forms UI components. It allows users to browse, edit, and debug .NET code in its original structure with minimal effort, something Ghidra would require additional plugins or manual IL analysis to achieve.
