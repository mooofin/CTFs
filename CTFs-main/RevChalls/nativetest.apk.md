The challenge began with a single Android application package, `nativetest.apk`. Using JADX, a popular Java decompiler, i tried to explore the application's Java layer. my initial looks were onto `com.example.nativetest.UIORHTG`, which immediately stood out due to its declaration of a native Java Native Interface (JNI) method, a common technique for hiding core logic in pre-compiled C++ code ? (first 

Within the `UIORHTG` activity, the `onCreate` method laid out a standard Android application flow. It referenced an `EditText` for user input and a `Button` to trigger an action. The button's `OnClickListener` was programmed to take the string from the `EditText`, pass it to the native function `stringFromJNI`, and then display the returned string back in the same `EditText`. 

<img width="1875" height="1010" alt="image" src="https://github.com/user-attachments/assets/dae24c56-a046-41ba-bbe3-f206b62c565d" />

 After extracting `libnative-lib.so` from the APK, i  loaded it into IDA Pro. The primary entry point was the JNI function `Java_com_example_nativetest_UIORHTG_stringFromJNI`. Decompilation revealed that this function acted as a dispatcher, orchestrating a sequence of calls to five internal C++ functions. The input string was passed through this chain, with the output of one function becoming the input for the next, before being returned to the Java layer.
 
<img width="1919" height="835" alt="image" src="https://github.com/user-attachments/assets/5e52afc5-1876-47be-9634-2e673342b840" />

 The first function, `f16pvq5m`, performed a straightforward conversion, iterating through the input `std::string` and populating a `std::vector<int>` with the ASCII value of each character. The second function, `taha5qd5`, contained the most significant logic. It processed the vector of integers in pairs, applying a bit-packing algorithm defined by the expression `(char1_ascii << 10) + char2_ascii`. This operation multiplies the first integer by 1024 and adds the second, effectively merging two 8-bit ASCII values into a single, larger integer. An important detail was a conditional check ensuring that if the input vector had an odd number of elements, the final, unpaired integer was discarded. The subsequent functions, `ntp05jxq` and `n2dyo835`, handled post-processing by converting these packed integers into their string representations and concatenating them into a single numeric string.

<img width="1919" height="994" alt="image" src="https://github.com/user-attachments/assets/0dc51f70-936a-40c3-b2fe-5251ca8f8d04" />

During the static analysis of the binary, a peculiar string, `yptnk`, was discovered in the `.rodata` section. In the context of a CTF i thought this could a string input .  When the application was installed on a device, the screen was blank, presenting no visible input field or button, directly contradicting the logic found in the decompiled Java code : ((


This discrepancy led me  to use `apktool`, a tool designed to properly decode and disassemble Android application resources. While JADX is excellent for Java code, `apktool` excels at converting binary XML layouts back into human-readable text. Upon decompiling with `apktool d nativetest.apk`, an inspection of `res/layout/activity_uiorhtg.xml` immediately revealed the cause of the invisible UI. The `EditText` was styled with `android:textColor="@android:color/white"` and `android:backgroundTint="@android:color/white"`, camouflaging it against the white background. Furthermore, a large `android:layout_marginTop="304.0dip"` was pushing both the `EditText` and the `Button` entirely off the visible area of a standard phone screen.
<img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/34191a20-d3fb-4821-a8e9-bae0250a3416" />

With the UI elements being programmatically present but physically inaccessible, i turned to the Android Debug Bridge (`adb`) to bypass the UI entirely. By connecting a device with USB debugging enabled, i could issue commands to simulate user interaction. I kinda started the target activity directly, injected the candidate string `yptnk`, and simulated a tap event on the button's off-screen coordinates. The result was not a flag, but a numeric string: `124016118894109578`.  

<img width="720" height="1600" alt="image" src="https://github.com/user-attachments/assets/9359ff1e-dc28-488e-bd8e-5652fffd153a" />

Now  I tried reversing the transformations on this number with all the 5 functons backwards and it actualy gave me the starting string . Now all that was left was what input will give me the flag . I tried seeing all the strings etc but nothing was helpful , so i asked my mentor and he gave me a clue on where to look (my first apk :3 ) 


<img width="929" height="86" alt="image" src="https://github.com/user-attachments/assets/0164b64d-3c29-4603-9c87-c18f69e28446" />
 Also 
 <img width="1001" height="91" alt="image" src="https://github.com/user-attachments/assets/6143ed39-83c2-4124-b2a5-39f7056989c9" />

This was huge ! 


Now i went on to jadx to see if there were any .

<img width="1917" height="1018" alt="image" src="https://github.com/user-attachments/assets/dd6e95c5-b2b0-4864-82f9-87ea9179eaa7" />


Sadly there were no , /res/values

Then i tried to decompile using apk tool 



<img width="991" height="414" alt="image" src="https://github.com/user-attachments/assets/576e4ce1-97e1-45fa-adce-e04797775c72" />


And while scrolling throught i found this : )

<img width="1823" height="556" alt="image" src="https://github.com/user-attachments/assets/05dfaa92-e42d-4761-a407-7141bd5bb7d6" />


Now we can reverse this using the info from IDA 

A step-by-step explanation of how the `packed_string` is decoded into the final flag: `picoCTF{d0ubl3_r3v3rs3_80046660}`.


1.  **Chunking**: The input string is split into 5-digit chunks.
2.  **Reversal**: The list of chunks (as numbers) is reversed. This is the key step to get the data back in the correct logical order.
3.  **Unpacking**: Each number in the reversed list is unpacked into two separate characters using bitwise operations.
4.  **Concatenation**: The resulting characters are joined together to form the final string.




| Packed Value (Integer) | Unpacking `char1` (`val >> 10`) | ASCII `char1` | Character `char1` | Unpacking `char2` (`val & 1023`) | ASCII `char2` | Character `char2` | Resulting Pair |
| :--------------------- | :------------------------------ | :------------ | :---------------- | :------------------------------- | :------------ | :---------------- | :------------- |
| **52349**              | `52349 >> 10 = 51`              | 51            | `p`               | `52349 & 1023 = 105`             | 105           | `i`               | `pi`           |
| **49252**              | `49252 >> 10 = 48`              | 48            | `c`               | `49252 & 1023 = 111`             | 111           | `o`               | `co`           |
| **52323**              | `52323 >> 10 = 51`              | 51            | `C`               | `52323 & 1023 = 83`              | 83            | `T`               | `CT`           |
| **97380**              | `97380 >> 10 = 95`              | 95            | `F`               | `97380 & 1023 = 100`             | 100           | `{`               | `F{`           |
| **56368**              | `56368 >> 10 = 55`              | 55            | `d`               | `56368 & 1023 = 48`              | 48            | `0`               | `d0`           |
| **102495**             | `102495 >> 10 = 100`            | 100           | `u`               | `102495 & 1023 = 95`             | 95            | `b`               | `ub`           |
| **53362**              | `53362 >> 10 = 52`              | 52            | `l`               | `53362 & 1023 = 114`             | 114           | `3`               | `l3`           |
| **97384**              | `97384 >> 10 = 95`              | 95            | `_`               | `97384 & 1023 = 104`             | 104           | `r`               | `_r`           |
| **53301**              | `53301 >> 10 = 52`              | 52            | `3`               | `53301 & 1023 = 53`              | 53            | `v`               | `3v`           |
| **97399**              | `97399 >> 10 = 95`              | 95            | `3`               | `97399 & 1023 = 119`             | 119           | `r`               | `3r`           |
| **112694**             | `112694 >> 10 = 110`            | 110           | `s`               | `112694 & 1023 = 54`             | 54            | `3`               | `s3`           |
| **116785**             | `116785 >> 10 = 114`            | 114           | `_`               | `116785 & 1023 = 49`             | 49            | `8`               | `_8`           |
| **54327**              | `54327 >> 10 = 53`              | 53            | `0`               | `54327 & 1023 = 55`              | 55            | `0`               | `00`           |
| **102495**             | `102495 >> 10 = 100`            | 100           | `4`               | `102495 & 1023 = 95`             | 95            | `6`               | `46`           |
| **102451**             | `102451 >> 10 = 100`            | 100           | `6`               | `102451 & 1023 = 51`             | 51            | `6`               | `66`           |
| **101424**             | `101424 >> 10 = 99`             | 99            | `0`               | `101424 & 1023 = 48`             | 48            | `}`               | `0}`           |
| **52334**              | `52334 >> 10 = 51`              | 51            | ` `               | `52334 & 1023 = 94`              | 94            | ` `               | `  `           |
| **111711**             | `111711 >> 10 = 109`            | 109           | ` `               | `111711 & 1023 = 99`             | 99            | ` `               | `  `           |
| **156368**             | `156368 >> 10 = 152`            | 152           | ` `               | `156368 & 1023 = 848`            | 848           | ` `               | `  `           |
| **111986**             | `111986 >> 10 = 109`            | 109           | ` `               | `111986 & 1023 = 370`            | 370           | ` `               | `  `           |
| **112605**             | `112605 >> 10 = 109`            | 109           | ` `               | `112605 & 1023 = 1021`           | 1021          | ` `               | `  `           |
| **69943**              | `69943 >> 10 = 68`              | 68            | ` `               | `69943 & 1023 = 311`             | 311           | ` `               | `  `           |
| **10455**              | `10455 >> 10 = 10`              | 10            | ` `               | `10455 & 1023 = 215`             | 215           | ` `               | `  `           |

*Note: The last several rows produce non-printable or out-of-range ASCII characters because the original flag string had an even number of characters. The packing algorithm likely padded the end, resulting in these "junk" values that are ultimately ignored when forming the final string.*


By concatenating the `Resulting Pair` column from top to bottom, we reconstruct the flag:

`pi` + `co` + `CT` + `F{` + `d0` + `ub` + `l3` + `_r` + `3v` + `3r` + `s3` + `_8` + `00` + `46` + `66` + `0}`

**Final Result:** `picoCTF{d0ubl3_r3v3rs3_80046660}`
