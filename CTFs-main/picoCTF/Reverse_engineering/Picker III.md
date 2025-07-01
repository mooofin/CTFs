Upon reviewing the code, I noticed that the `write_variable` function uses Python’s `exec()` function to assign values to global variables. This is dangerous because it allows us to overwrite existing functions in memory — even those listed in the function table. I also discovered a hidden function named `win()` that was not exposed through the menu, but if called, would read and print the contents of a file called `flag.txt` — encoded in hexadecimal format.

To exploit this, I used the `write_variable` option (menu number 3) to overwrite the `getRandomNumber` function with `win`. Since `getRandomNumber` was one of the allowed options (menu number 4), this allowed me to trick the program into calling `win()` when I selected option 4. I entered `getRandomNumber` as the variable name and `win` as the new value. After that, choosing option 4 caused the program to execute `win()` and print the flag — but in hex format.

The output appeared as a long string of hexadecimal values like `0x70 0x69 0x63 ...`. To decode this, I wrote a simple Python script that converted each hex number into its corresponding ASCII character. The script split the hex string by spaces, converted each piece from hex to an integer, then to a character, and finally joined the characters into a readable string. The result was the final flag:

```
picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_c20f5222}
```


![screenshot-1751373965](https://github.com/user-attachments/assets/7a2ec9b2-c71b-476d-b9b6-064e9812a216)
