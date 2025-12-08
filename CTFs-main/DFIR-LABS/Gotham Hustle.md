
## Initial Analysis

First, I ran `imageinfo` to identify the memory profile and basic system details.

<img width="1425" height="394" alt="image" src="https://github.com/user-attachments/assets/6e32d06b-92fb-4693-a22f-d1955b5adbf8" />

**System Information**
- OS Profile: Win7SP1x64
- Processors: 6 CPUs
- Image Date/Time: 2024-08-06 18:37:19 UTC
- Memory Size: 4.6 GB



## Process Enumeration

Next, I ran `pslist` to observe active processes.

```text

cmd.exe (PID 3944)
notepad.exe (PID 2592)
mspaint.exe (PID 2516)
multiple chrome.exe processes
````

### Notable Processes

* `cmd.exe` (PID 3944): Command prompt activity
* `notepad.exe` (PID 2592): Notepad open
* `mspaint.exe` (PID 2516): Paint running
* Multiple `chrome.exe`: Browser activity



## Command History

To check user activity, I ran `cmdscan`.

<img width="1427" height="489" alt="image" src="https://github.com/user-attachments/assets/d7789d80-4ffe-4422-80b0-6f106dc07a48" />

```text
Cmd #4: Ymkwc2N0Znt3M2xjMG0zXw==
Cmd #5: azr43ln1ght.github.io
Cmd #6: Azr43lKn1ght
Cmd #7: did you find flag1?
```

The base64 string decodes to:

```
bi0sctf{w3lc0m3_
```



## Notepad & Memory Strings

Dumping Notepad directly failed due to Volatility version mismatch.
I dumped process memory and ran `strings`, which mostly yielded DLL data.
One extracted link led to the following page:

<img width="1156" height="319" alt="image" src="https://github.com/user-attachments/assets/f7ac2ee8-d44d-427e-a062-aa8edf9715a2" />

This contained another base64 string, decoding to:

```
h0p3_th15_
```



## File Extraction

From `filescan`, I noticed `flag5.rar` on the Desktop and dumped it:

```powershell
vol -f gotham.raw --profile=Win7SP1x64 dumpfiles -Q 0x000000011fdaff20 --dump-dir=D:\DFIR
```

<img width="624" height="354" alt="image" src="https://github.com/user-attachments/assets/1123e858-4c29-4ac8-9668-fb8f34b2cb99" />

The archive was password-protected.



## Credential Dump

Using `hashdump`:

```text
bruce:1001:...:b7265f8cc4f00b58f413076ead262720:::
```

<img width="1342" height="490" alt="image" src="https://github.com/user-attachments/assets/b5cce846-70ed-4ad0-9399-35a0d45601df" />

The password was **`batman`**.

Extracting the archive revealed another base64 string:

<img width="906" height="161" alt="image" src="https://github.com/user-attachments/assets/d80b3467-1dbc-442d-aa92-394d3e8a5276" />

Decoded:

```
m0r3_13337431}
```



## Flag 4

Dumping Notepad with `procdump` showed a search for `flag4`.
Running `strings` revealed:

```
YjNuM2YxNzVfeTB1Xw==
```

<img width="313" height="519" alt="image" src="https://github.com/user-attachments/assets/61645293-1932-49d8-b819-7a6469e13d9d" />



## Flag 2 (MS Paint)

From `pslist`, `mspaint.exe` was active.
I dumped the process memory, renamed it to `.data`, and opened it in GIMP.

<img width="720" height="763" alt="image" src="https://github.com/user-attachments/assets/3fc6f1e4-7ac4-4b0b-b5e7-463fc906725e" />



I had to use **Unsigned Integer** because I was loading raw process memory, not a real image file. The pixel values in memory are stored as normal positive numbers, especially for RGB 16-bit, which expects values between 0 and 65535. When I tried signed or floating point, the same bytes were misinterpreted and the image completely fell apart into noise. Unsigned was the only option that kept the colors stable and readable. Since MSPaint stores its canvas as raw pixel data in memory without headers, I had to manually line everything up.

After inspecting and tweaking values for hours, I finally managed to align a base64 string in the image:

```
dDBfZGYxcl9sNGl1Xw==
```

The data appeared flipped in the output, so I rotated and flipped the image to make the text readable.

<img width="331" height="513" alt="image" src="https://github.com/user-attachments/assets/a787c105-52c3-4c74-9c94-58c6ca5109f1" />

Decoding the base64 revealed the final combined flag:

```
bi0sctf{w3lc0m3_t0_df1r_l4b5_h0p3_th15_b3n3f175_y0u_m0r3_13337431}
```


