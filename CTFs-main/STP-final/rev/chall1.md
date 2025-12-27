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


Also i found this while investiagting 

```c#
// Token: 0x06000006 RID: 6 RVA: 0x00003D18 File Offset: 0x00003118
	internal unsafe static void func6()
	{
		string input = Console.ReadLine();
		Regex regex = new Regex("^bi0s{([a-zA-Z0-9_]+)}$");
		Match match = regex.Match(input);
		if (match.Success)
		{
			string value = match.Groups[1].Value;
			<Module>.func11();
			IntPtr hglobal = Marshal.StringToHGlobalAnsi(value);
			<Module>.strcpy_s((sbyte*)(&<Module>.user_input), 128UL, (sbyte*)hglobal.ToPointer());
			Marshal.FreeHGlobal(hglobal);
			<Module>.func8((sbyte*)(&<Module>.user_input));
			<Module>.func1();
		}
		else
		{
			Environment.Exit(1);
		}
```

And there are a bunch of exception checks which i can see from IDA's graph view , so ill have to resolve or patch them during runtime as this challenge seems way too hard to solve statically .


Also from the CFG it calls this VM dispatcher or initialiser of sorts 

```c#
// Token: 0x0600000B RID: 11 RVA: 0x00003C8C File Offset: 0x0000308C
	internal unsafe static void func1()
	{
		if (<Module>.global_flag != 1)
		{
			Environment.Exit(1);
		}
		<Module>.func27();
		<Module>.func5((byte*)(&<Module>.embedded_instructions), 7889);
		<Module>.func23();
		int num = <Module>.func18();
		if (*(ref <Module>._err_token + 82 + (long)num) == 0)
		{
			<lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7> <lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>;
			initblk(ref <lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>, 0, 1L);
			_err_tok_2<7,0> err_tok_2<7,0>;
			<Module>.printf(<Module>._err_tok_2<7,0>.decrypt(<Module>.func1.<lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>.()((<lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>*)(&<lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>), &err_tok_2<7,0>)));
			<Module>.exit(0);
		}
		<lambda_80864a03a1c3fa5fa295ad64a1df9c07> <lambda_80864a03a1c3fa5fa295ad64a1df9c07>;
		initblk(ref <lambda_80864a03a1c3fa5fa295ad64a1df9c07>, 0, 1L);
		_err_tok_2<9,0> err_tok_2<9,0>;
		<Module>.printf(<Module>._err_tok_2<9,0>.decrypt(<Module>.func1.<lambda_80864a03a1c3fa5fa295ad64a1df9c07>.()((<lambda_80864a03a1c3fa5fa295ad64a1df9c07>*)(&<lambda_80864a03a1c3fa5fa295ad64a1df9c07>), &err_tok_2<9,0>)));
```
So further more the codes look like a VM going on and a dispatcher is being called?


<img width="687" height="117" alt="image" src="https://github.com/user-attachments/assets/439c85e0-9331-467f-a65d-282156cd4329" />
func11 needs more details as it's not in dns spy 


If the regex check passes, functions func11, func8, and func1 are executed ? is my current assumption as the tokens idicate character allotment limits of values 


```c#
internal unsafe static void func8(sbyte* input)
	{
		<Module>.msclr.gcroot<System::String\u0020^>.=(&<Module>.?A0x73b52d52.injectedInput, new string((sbyte*)input));
		<Module>.?A0x73b52d52.injectedIndex = 0;
	}
```
This function takes an unmanaged C-style string passed as an `sbyte*`, converts it into a managed `.NET System.String`, and stores it in a global module-level variable using `msclr::gcroot` so it remains safe from garbage collection. In doing so, it effectively injects external input into the managed runtime for later use. The function also resets a global index variable to zero, indicating that any subsequent logic will begin processing this injected string from the start.


```c#
// Token: 0x0600000B RID: 11 RVA: 0x00003C8C File Offset: 0x0000308C
	internal unsafe static void func1()
	{
		if (<Module>.global_flag != 1)
		{
			Environment.Exit(1);
		}
		<Module>.func27();
		<Module>.func5((byte*)(&<Module>.embedded_instructions), 7889);
		<Module>.func23();
		int num = <Module>.func18();
		if (*(ref <Module>._err_token + 82 + (long)num) == 0)
		{
			<lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7> <lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>;
			initblk(ref <lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>, 0, 1L);
			_err_tok_2<7,0> err_tok_2<7,0>;
			<Module>.printf(<Module>._err_tok_2<7,0>.decrypt(<Module>.func1.<lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>.()((<lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>*)(&<lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>), &err_tok_2<7,0>)));
			<Module>.exit(0);
		}
		<lambda_80864a03a1c3fa5fa295ad64a1df9c07> <lambda_80864a03a1c3fa5fa295ad64a1df9c07>;
		initblk(ref <lambda_80864a03a1c3fa5fa295ad64a1df9c07>, 0, 1L);
		_err_tok_2<9,0> err_tok_2<9,0>;
		<Module>.printf(<Module>._err_tok_2<9,0>.decrypt(<Module>.func1.<lambda_80864a03a1c3fa5fa295ad64a1df9c07>.()((<lambda_80864a03a1c3fa5fa295ad64a1df9c07>*)(&<lambda_80864a03a1c3fa5fa295ad64a1df9c07>), &err_tok_2<9,0>)));
	}
```
This function is a gated execution routine that first enforces a global state check and aborts immediately if `global_flag` is not set, acting as an anti-misuse or validation guard. Once past that, it initializes internal state, loads a block of embedded instructions into memory, and executes a processing pipeline that culminates in `func18`, which returns an index or status code. That value is then used to index into a global error token table. If the computed slot contains zero, the function decrypts and prints a specific embedded message and exits cleanly. Otherwise, it decrypts and prints a different message without exiting immediately. In effect, this function runs a hidden instruction stream, evaluates the result against an internal token table, and conditionally reveals one of two obfuscated outputs, making it a classic validation-and-dispatch endpoint rather than general logic.


More down the dissassembly 
```c#
// Token: 0x0600000C RID: 12 RVA: 0x00001A20 File Offset: 0x00000E20
	internal unsafe static _err_tok_2<7,0>* ()(<lambda_7b8f7c1aa6b0ebbbec3baa92a10e10b7>* A_0, _err_tok_2<7,0>* A_1)
	{
		_err_tok_2<7,0> err_tok_2<7,0> = 239;
		*(ref err_tok_2<7,0> + 1) = 234;
		*(ref err_tok_2<7,0> + 2) = 125;
		*(ref err_tok_2<7,0> + 3) = 176;
		*(ref err_tok_2<7,0> + 4) = 147;
		*(ref err_tok_2<7,0> + 5) = 86;
		*(ref err_tok_2<7,0> + 6) = 217;
		*(ref err_tok_2<7,0> + 7) = 184;
		*(ref err_tok_2<7,0> + 8) = 152;
		*(ref err_tok_2<7,0> + 9) = 18;
		*(ref err_tok_2<7,0> + 10) = 222;
		*(ref err_tok_2<7,0> + 11) = 244;
		*(ref err_tok_2<7,0> + 12) = 92;
		*(ref err_tok_2<7,0> + 13) = 217;
		cpblk(A_1, ref err_tok_2<7,0>, 14);
		return A_1;
	}

	// Token: 0x0600000D RID: 13 RVA: 0x00001AC0 File Offset: 0x00000EC0
	internal unsafe static _err_tok_2<9,0>* ()(<lambda_80864a03a1c3fa5fa295ad64a1df9c07>* A_0, _err_tok_2<9,0>* A_1)
	{
		_err_tok_2<9,0> err_tok_2<9,0> = 239;
		*(ref err_tok_2<9,0> + 1) = 234;
		*(ref err_tok_2<9,0> + 2) = 125;
		*(ref err_tok_2<9,0> + 3) = 176;
		*(ref err_tok_2<9,0> + 4) = 147;
		*(ref err_tok_2<9,0> + 5) = 86;
		*(ref err_tok_2<9,0> + 6) = 217;
		*(ref err_tok_2<9,0> + 7) = 220;
		*(ref err_tok_2<9,0> + 8) = 55;
		*(ref err_tok_2<9,0> + 9) = 172;
		*(ref err_tok_2<9,0> + 10) = 133;
		*(ref err_tok_2<9,0> + 11) = 15;
		*(ref err_tok_2<9,0> + 12) = 194;
		*(ref err_tok_2<9,0> + 13) = 246;
		*(ref err_tok_2<9,0> + 14) = 53;
		*(ref err_tok_2<9,0> + 15) = 173;
		*(ref err_tok_2<9,0> + 16) = 214;
		*(ref err_tok_2<9,0> + 17) = 55;
		cpblk(A_1, ref err_tok_2<9,0>, 18);
		return A_1;
	}
```

These functions contain **encrypted strings** that are revealed through a simple XOR operation. Let me explain how this obfuscation works:


Both functions create byte arrays with hardcoded values:

**Function 1 (RID 12) - 14 bytes:**
```python
data1 = [0xEF, 0xEA, 0x7D, 0xB0, 0x93, 0x56, 0xD9, 
         0xB8, 0x98, 0x12, 0xDE, 0xF4, 0x5C, 0xD9]
```

**Function 2 (RID 13) - 18 bytes:**
```python
data2 = [0xEF, 0xEA, 0x7D, 0xB0, 0x93, 0x56, 0xD9, 
         0xDC, 0x37, 0xAC, 0x85, 0x0F, 0xC2, 0xF6, 
         0x35, 0xAD, 0xD6, 0x37]
```

The array is split into **two halves**:
- **First half** = Key
- **Second half** = Encrypted data

Since XOR is **symmetric** (`A ^ B = C` and `C ^ B = A`), you can decrypt by XORing corresponding positions:

```
Decrypted[i] = Array[i] ^ Array[i + length/2]
```



For an 18-byte array:
```
Index:  0   1   2   3   4   5   6   7   8  |  9  10  11  12  13  14  15  16  17
Data:  EF  EA  7D  B0  93  56  D9  DC  37  | AC  85  0F  C2  F6  35  AD  D6  37
       └───────────── Key ─────────────────┘ └────────── Encrypted ──────────┘
       
XOR:   EF ^ AC = 43 ('C')
       EA ^ 85 = 6F ('o')
       7D ^ 0F = 72 ('r')
       ...and so on
```


```python
# Function 2 (RID 13) - 18 bytes
data = [0xEF, 0xEA, 0x7D, 0xB0, 0x93, 0x56, 0xD9, 
        0xDC, 0x37, 0xAC, 0x85, 0x0F, 0xC2, 0xF6, 
        0x35, 0xAD, 0xD6, 0x37]

# XOR first half with second half
decrypted = ''.join([chr(data[i] ^ data[i + len(data)//2]) 
                     for i in range(len(data)//2)])

print(f"Decrypted: {repr(decrypted)}")
# Output: 'Correct\n\x00'
```
func5 

<img width="701" height="524" alt="image" src="https://github.com/user-attachments/assets/65734e0a-e9fb-4cfc-897a-83e8e950ecd2" />

After more going through i found the VM dispatcher by see graphs of all the functions and this function- sub_140001EAC	was the run dispatch 

<img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/9cb8fd62-6be4-4d9e-bf88-acee20abe8d4" />

It's over a few 1000 lines so I dont think this is meant for solving statically :((
<img width="626" height="603" alt="image" src="https://github.com/user-attachments/assets/ba07b534-a52f-4c9b-90f5-ddb0e5350286" />

After loading up xdbg nothing seems to look around worthy and yeah 
<img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/59aff28e-a9e2-48c2-ba28-3aecceacb5b6" />


After passing the debug check we can actually start running the VM and see how it behaves ;

<img width="1919" height="1020" alt="image" src="https://github.com/user-attachments/assets/be66f260-3daa-4027-8f42-91324e69726e" />

Then i tried focrcing it to take a input and attached it back again and we landed in this region ; 

<img width="1919" height="994" alt="image" src="https://github.com/user-attachments/assets/4909630d-ab3a-49ce-9bdf-4998bbcce246" />

After so many attempts at finding the adress for the VM loop , i found the instrcution which is the VM counter and inspected that in IDA 
<img width="767" height="438" alt="image" src="https://github.com/user-attachments/assets/32df10cd-218c-4a94-b2f9-81e0114617c6" />
It starts by calling sub_140001530(&unk_140011030) to initialize the VM state, where unk_140011030 is the VM state structure pointer. The function then enters an infinite while(1) loop that repeatedly reads the current opcode from byte_1400121A8. If the opcode is zero, the loop breaks and execution stops. Otherwise, the code performs several qmemcpy operations through local stack buffers (v1, v2, v3, v4), with sub_140001570 appearing to fetch or process operand data using dword_140019164 as a parameter. Finally, it calls sub_14000F1AC((__int64)&unk_140011030, v3) which is the opcode dispatcher/handler - this function receives the VM state pointer as the first argument and the processed opcode/operand data as the second argument, and is responsible for executing the actual VM instruction

The other function it calls is 
```c#
void *__fastcall sub_140001570(void *a1, __int16 a2)
{
  int i; // [rsp+24h] [rbp-34h]
  unsigned __int8 v4[40]; // [rsp+30h] [rbp-28h] BYREF

  for ( i = 0; ; ++i )
  {
    if ( i >= dword_140019240 )
      exit(1);
    qmemcpy(v4, &byte_1400121B0[7 * i], 7u);
    if ( sub_140001540(v4) == a2 )
      break;
  }
  qmemcpy(a1, &byte_1400121B0[7 * i], 7u);
  return a1;
}
```
`sub_140001570` acts as a VM instruction fetch routine that scans the VM’s bytecode array to locate a specific instruction identified by `a2`. It iterates over the bytecode, treating it as a sequence of fixed-size 7-byte instructions, copying each candidate into a temporary buffer and extracting its instruction ID via `sub_140001540`. When a matching ID is found, the corresponding 7-byte instruction is copied into the output buffer `a1`; if no match exists after scanning all instructions, the function terminates execution with `exit(1)`. This design implies a VM architecture where instructions are addressed or referenced by identifier rather than strictly executed linearly, with `sub_140001540` serving as the decoder for the instruction header within the 7-byte format


```c#
__int16 __fastcall sub_140001540(unsigned __int8 *a1)
{
  return a1[2] | (*a1 << 8);
}
```
This function extracts a 16-bit instruction identifier from a 7-byte VM instruction by combining two specific bytes: it takes the first byte a1[0] as the high byte and the third byte a1[2] as the low byte, forming the value (*a1 << 8) | a1[2]. This implies the VM instruction format is non-contiguous, with the opcode or instruction ID split across bytes 0 and 2 rather than stored sequentially


from this i can make a boilerplate of the VM from the architecture we know ;
```rust
#[repr(C)]
#[derive(Debug, Clone, Copy)]
struct VmInstruction {
    elem1: u8,  // byte_0 - part of instruction ID (high byte)
    elem2: u8,  // byte_1
    elem3: u8,  // byte_2 - part of instruction ID (low byte)
    elem4: u8,  // byte_3
    elem5: u8,  // byte_4
    elem6: u8,  // byte_5
    elem7: u8,  // byte_6
}

impl VmInstruction {
    /// Get the 16-bit instruction ID from elem1 and elem3
    fn get_id(&self) -> u16 {
        (self.elem1 as u16) << 8 | (self.elem3 as u16)
    }
}
```
