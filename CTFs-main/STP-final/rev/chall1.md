### Entry Point Analysis

Since this is a `.NET` binary, `mainCRTStartup` is the first thing to look at in dnSpy, as it serves as the native entry point that initializes the C runtime environment before transitioning to managed code execution.

<img width="1919" height="1026" alt="image" src="https://github.com/user-attachments/assets/9d4ca242-f0b9-437a-8c3d-1b330e59ba7b" />

---

### RVA vs Virtual Address

RVA is a relative address, so you need to add it to the image base to get the actual virtual address in a disassembler.

While using a decompiler, we need to add the offset to obtain the correct address.

A clear distinction can be made as follows:

**File Offset (0x00003864)**

* Where the code sits on disk (in the `.exe` file)
* If you open the executable in a hex editor, this corresponds to position `0x3864`

**RVA (0x00004464)**

* Where the code sits in memory when loaded (relative to the image base)
* When the program runs, Windows loads it at a base address
* Actual virtual address = `ImageBase + RVA`

---

### Beginning the Reversing Process

<img width="1524" height="671" alt="image" src="https://github.com/user-attachments/assets/59f84b62-3653-4d4e-9dfc-87111809c8e7" />

After `mainCRTStartup` sets up the C runtime environment (initializing `argc`, `argv`, and `envp`), it proceeds to:

* Bootstrap the .NET CLR (Common Language Runtime)
* Transition from native C++ code to managed C# execution

---

### Address Resolution in dnSpy and IDA

While attempting to find the offset in dnSpy, the address appeared to be standard, requiring reference material to confirm the correct image base.

<img width="917" height="573" alt="image" src="https://github.com/user-attachments/assets/6e5c6f4a-80de-4a51-8af1-3376c43cfaf6" />

Reference:
[https://medium.com/@boutnaru/the-portable-executable-journey-image-base-2e87095ca18b](https://medium.com/@boutnaru/the-portable-executable-journey-image-base-2e87095ca18b)

After applying the correct image base, the corresponding location was reached in IDA.

<img width="1519" height="704" alt="image" src="https://github.com/user-attachments/assets/035b90c2-0f53-49c6-b090-9ccee7d4ec36" />

---

### Identifying the Relevant Function

The first call, `sub_140004834()`, is almost certainly C runtime initialization, handling tasks such as global constructors and argument setup, and can usually be ignored during reverse engineering.

The second call, `sub_1400042E8()`, is the important one because its return value becomes the program’s exit code and it typically acts as the bridge into the actual application logic.

---

### Decompilation of `sub_1400042E8`

After some exploration:

```c
__int64 __fastcall sub_1400042E8()
{
  unsigned int v0; // ebx
  __int64 v1; // rcx
  char v2; // si
  __int64 v3; // rcx
  __int64 v5; // rcx
  _QWORD *v6; // rax
  __int64 v7; // rcx
  void (__fastcall **v8)(_QWORD, __int64); // rbx
  _tls_callback_type *v9; // rax
  _tls_callback_type *v10; // rbx
  char **initial_narrow_environment; // rdi
  char **v12; // rbx
  int *v13; // rax
  __int64 v14; // rcx
  __int64 v15; // rcx

  if ( !(unsigned __int8)sub_140004630(1) )
  {
    sub_140004954(7);
    goto LABEL_19;
  }
  v2 = 0;
  LOBYTE(v0) = sub_1400045F4(v1);
  v3 = (unsigned int)dword_1400198A0;
  if ( dword_1400198A0 == 1 )
  {
LABEL_19:
    sub_140004954(7);
    goto LABEL_20;
  }
  if ( dword_1400198A0 )
  {
    v2 = 1;
  }
  else
  {
    dword_1400198A0 = 1;
    if ( initterm_e((_PIFV *)&First, (_PIFV *)&Last) )
      return 255;
    initterm((_PVFV *)&qword_140008238, (_PVFV *)&qword_140008248);
    dword_1400198A0 = 2;
  }
  LOBYTE(v3) = v0;
  sub_140004790(v3);
  v6 = (_QWORD *)sub_14000493C(v5);
  v8 = (void (__fastcall **)(_QWORD, __int64))v6;
  if ( *v6 && (unsigned __int8)sub_1400046F8(v6) )
    (*v8)(0, 2);
  v9 = (_tls_callback_type *)sub_140004944(v7);
  v10 = v9;
  if ( *v9 && (unsigned __int8)sub_1400046F8(v9) )
    register_thread_local_exe_atexit_callback(*v10);
  initial_narrow_environment = get_initial_narrow_environment();
  v12 = *_p___argv();
  v13 = _p___argc();
  v0 = sub_140003BA0((unsigned int)*v13, v12, initial_narrow_environment);
  if ( !(unsigned __int8)sub_140004AA4(v14) )
LABEL_20:
    exit(v0);
  if ( !v2 )
    cexit();
  LOBYTE(v15) = 1;
  sub_1400047B4(v15, 0);
  return v0;
}
```

---

### Interpretation

Most of the body consists of standard MSVC C runtime machinery. It guards against double initialization, runs `_initterm_e` and `_initterm` to initialize global constructors, processes TLS callbacks, sets up thread-local exit handlers, and prepares `argc`, `argv`, and the environment.

The key line is the call to:

```c
sub_140003BA0((unsigned int)*_p___argc(), *_p___argv(), get_initial_narrow_environment())
```

This matches the classic `main(argc, argv, envp)` style entry point and marks the transition into the actual program logic.



<img width="1526" height="436" alt="image" src="https://github.com/user-attachments/assets/1239e5cd-a818-4e66-bdbc-eaa1fea881fd" />
This function, `sub_140003BA0`, represents the first piece of real program logic executed after the CRT handoff. It begins by zero-initializing a small stack buffer and then calls `sub_140003DD8`, passing two stack buffers, likely to construct or derive some form of path or data blob. The return value from this function is then passed to `sub_140007070`, which converts it into a C-style string. This string is used as the filename argument to `fopen` with read permissions. The result of `fopen` is checked, and a flag-like value is derived based on whether the file was successfully opened. This value is then passed to `func2`, which likely handles validation, signaling, or branching logic based on the presence or absence of the file. The function itself always returns `0`, indicating that its purpose is not to compute a return value but to perform a side-effect driven check early in execution.


```c
void *__fastcall sub_140003DD8(__int64 a1, void *a2)
{
  _BYTE v3[112]; // [rsp+0h] [rbp-98h] BYREF

  v3[0] = -17;
  v3[1] = -22;
  v3[2] = 125;
  v3[3] = -80;
  v3[4] = -109;
  v3[5] = 86;
  v3[6] = -39;
  v3[7] = -36;
  v3[8] = 55;
  v3[9] = -102;
  v3[10] = -3;
  v3[11] = 72;
  v3[12] = -69;
  v3[13] = 70;
  v3[14] = -127;
  v3[15] = -116;
  v3[16] = -73;
  v3[17] = 10;
  v3[18] = -19;
  v3[19] = 8;
  v3[20] = -109;
  v3[21] = -2;
  v3[22] = 121;
  v3[23] = -100;
  v3[24] = 15;
  v3[25] = -126;
  v3[26] = 61;
  v3[27] = -64;
  v3[28] = 83;
  v3[29] = 110;
  v3[30] = -127;
  v3[31] = 12;
  v3[32] = -49;
  v3[33] = 34;
  v3[34] = -107;
  v3[35] = -72;
  v3[36] = 107;
  v3[37] = 46;
  v3[38] = -55;
  v3[39] = -44;
  v3[40] = 39;
  v3[41] = -126;
  v3[42] = -67;
  v3[43] = 0;
  v3[44] = -93;
  v3[45] = 126;
  v3[46] = 1;
  v3[47] = -36;
  v3[48] = 23;
  v3[49] = -46;
  v3[50] = 101;
  v3[51] = -32;
  v3[52] = -13;
  v3[53] = -26;
  v3[54] = 121;
  v3[55] = -60;
  v3[56] = -64;
  v3[57] = -126;
  v3[58] = 18;
  v3[59] = -35;
  v3[60] = -10;
  v3[61] = 121;
  v3[62] = -83;
  v3[63] = -76;
  v3[64] = 82;
  v3[65] = -76;
  v3[66] = -112;
  v3[67] = 123;
  v3[68] = -40;
  v3[69] = 46;
  v3[70] = -32;
  v3[71] = -30;
  v3[72] = -34;
  v3[73] = 105;
  v3[74] = -62;
  v3[75] = 106;
  v3[76] = -6;
  v3[77] = -50;
  v3[78] = 10;
  v3[79] = -79;
  v3[80] = 108;
  v3[81] = -10;
  v3[82] = 91;
  v3[83] = -19;
  v3[84] = 97;
  v3[85] = 91;
  v3[86] = -82;
  v3[87] = 111;
  v3[88] = -67;
  v3[89] = 67;
  v3[90] = -17;
  v3[91] = -63;
  v3[92] = 70;
  v3[93] = 94;
  v3[94] = -88;
  v3[95] = -96;
  v3[96] = 79;
  v3[97] = -83;
  v3[98] = -43;
  v3[99] = 101;
  v3[100] = -53;
  v3[101] = 27;
  v3[102] = 46;
  v3[103] = -70;
  v3[104] = 123;
  v3[105] = -77;
  v3[106] = 2;
  v3[107] = -50;
  v3[108] = -121;
  v3[109] = -98;
  v3[110] = 13;
  v3[111] = -60;
  qmemcpy(a2, v3, 0x70u);
  return a2;
}
```

<img width="319" height="125" alt="image" src="https://github.com/user-attachments/assets/e0548ca6-2c74-4fd3-a247-dfe592cd5171" />

<img width="1442" height="639" alt="image" src="https://github.com/user-attachments/assets/6e1a6254-fdad-4769-bcf9-aa55a1097b27" />


IDA treats this as an opaque immediate value, but in the context of a mixed-mode .NET binary, this pattern matches a .NET metadata token. By normalizing it to 32 bits (0x06000011) and applying the metadata layout, 0x06 identifies the MethodDef table and 0x000011 the method index. This is why the value can later be resolved in dnSpy under <Module> as a managed method reference rather than a random constant.


<img width="1267" height="288" alt="image" src="https://github.com/user-attachments/assets/e20a59fc-2ccd-4c96-938f-fb8012f80759" />
this routine performs an XOR decryption over the provided byte array and returns the resulting buffer, which is then assigned to v1 and treated as a file path. This path is subsequently passed to fopen in read mode, with the returned file descriptor stored in v5


Also i found this interesting blob of code after lurking around ;

<img width="708" height="213" alt="image" src="https://github.com/user-attachments/assets/193b0616-931a-4720-abda-97b1b27048c4" />
 the decrypted file path gates execution, and the program is structured so that only the “correct” environment allows the congratulatory path to be taken.

Navigating there ;

<img width="1918" height="979" alt="image" src="https://github.com/user-attachments/assets/da7c5d3d-d1dd-41dc-90d3-759fb2fc4569" />
<img width="669" height="329" alt="image" src="https://github.com/user-attachments/assets/95e4c1b0-e00f-4935-884e-87bf4b032103" />


<img width="1918" height="845" alt="image" src="https://github.com/user-attachments/assets/ce7b20c4-d29c-4740-b1c4-ade54fe615fd" />
<img width="1907" height="866" alt="image" src="https://github.com/user-attachments/assets/2afa4af2-6637-4f6d-861d-02dbbfcef8f5" />
