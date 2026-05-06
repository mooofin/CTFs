# Aurora License Validator - Solution

First things first lets try running the binary 


<img width="1892" height="727" alt="image" src="https://github.com/user-attachments/assets/2cd50323-bd9c-4108-9b9e-25736faecfbe" />

When we run aurora_license_validator.exe without any arguments, the program prints a usage message telling us that it expects a license file as input, specifically a file with the .auroralic extension. This already tells us that the program works as a license checker rather than doing anything automatically on launch . So that out of the way let's look at the binary. 

<img width="1917" height="980" alt="image" src="https://github.com/user-attachments/assets/88266846-a62d-4087-8900-d4c67afe05b6" />




What we are seeing here is the raw unpacked code blob exactly as it existed in memory at runtime. Because the original import table and section layout were not fully reconstructed, IDA cannot properly identify function boundaries, library calls, or high-level constructs.The downside is that, without proper imports and symbols, IDA has very little context, so everything looks much lower level and harder to read. From here, instead of trying to understand all the messy code at once, we focus on finding important parts like license parsing and validation by following jumps, checking referenced strings, and looking for comparison instructions, while ignoring IDA warnings caused by the dumped nature of the binary.

<img width="566" height="158" alt="image" src="https://github.com/user-attachments/assets/45299281-25b8-4374-a4ab-5ac0c59376ae" />


Looking further down in the control-flow graph, we can see a large amount of junk code made up of repetitive jumps, register shuffling, and unnecessary arithmetic that does not contribute to the actual license logic 

<img width="1527" height="643" alt="image" src="https://github.com/user-attachments/assets/a2ea40cc-6a20-4513-b524-02b0f9e0107a" />


Looking back at first principles lets look at the strings ; 

<img width="960" height="749" alt="image" src="https://github.com/user-attachments/assets/dd5f032d-65a8-41ec-a1f4-eef57f79e39f" />

Here we see a packer signature - .MPRESS1 and .MPRESS20 . 

You can confirm this using Detect it -

<img width="1919" height="1011" alt="image" src="https://github.com/user-attachments/assets/5bfe5081-3836-4598-b4c5-97ed94216e49" />


The entropy reveals the area with .MPRESS packed . So that out lets start unpacking using x64xdg

<img width="1919" height="1008" alt="image" src="https://github.com/user-attachments/assets/3f6b52a5-6cfe-4d9a-bcaa-6bba3d164cda" />

Most of the time, x64dbg will automatically stop at your EXE entry point 

When you first hit the program’s entry point, press F8 only once or twice. Don’t spam it. This tiny pause lets the stack pointer (RSP) stabilize so it’s pointing to the real stack and not mid-chaos from loader stuff. Then, look at the Registers panel and find RSP. Right-click on it, set a hardware breakpoint, and choose Write.The debugger will instantly stop the moment the unpacker writes to the stack. That write usually happens exactly when control is being handed from the unpacking stub to the real, unpacked code .


While single-stepping with **F8**, the objective is to identify the transfer of execution from the unpacking stub to the original program code.

As you step, watch closely for a **JMP instruction** that transfers control to a **new address range**. This jump usually stands out because the destination code looks significantly cleaner and more structured compared to the unpacker stub. Junk instructions, heavy stack manipulation, and opaque control flow typically disappear at this point.

A common indicator that you have landed in real program code is the presence of a standard function prologue, such as:

```
push rbp
mov rbp, rsp
```

When you step into this jump and execution lands in clean, conventional code with a normal prologue, you have reached the **Original Entry Point (OEP)**.


On x64 Windows, packed executables often transition through several system layers before reaching the unpacked user code. As you single-step, execution typically flows like this:

```
ntdll → kernel32 → ntdll → EXE
```

This happens because the loader and unpacking stub rely on Windows APIs to allocate memory, resolve imports, and transfer execution. Each `ret` or indirect jump moves execution one layer closer to your program.


<img width="1919" height="1007" alt="image" src="https://github.com/user-attachments/assets/320b8e3f-97ef-40d6-93f8-453b05b18fa9" />

Finally - x64dbg is directly reading the PE header of the loaded image and resolving the AddressOfEntryPoint field. In other words, the debugger is stating, based on the executable’s own metadata 

Once the Original Entry Point has been confirmed and execution is paused there, the unpacking phase is effectively complete. You should not step further, as doing so risks moving past the clean state you want to capture. This is the ideal moment to extract the fully unpacked image from memory.



<img width="724" height="712" alt="image" src="https://github.com/user-attachments/assets/973d8cd0-0e13-4b44-9331-ca3b1effc825" />

Open Scylla and attach it to the running aurora_license_validator.exe process. After attaching, click Dump and select the option to dump at the current OEP. Because execution is paused exactly at the real entry point, Scylla can correctly identify and use this address as the entry point for the dumped file.

The first step is IAT Autosearch, which you already performed. Scylla located a possible IAT first entry at 000000011E7FDAFA. This address represents the real import table region reconstructed from memory, not from the on-disk headers. This is exactly what we want when dealing with MPRESS.

Next, you must click Get Imports. This is the step many people skip. When clicked, Scylla uses the detected IAT region to resolve imported functions and populate the Imports window. If successful, you should see common system libraries such as kernel32.dll, user32.dll, msvcrt.dll, and others. If the window remains empty, this does not mean failure. It simply means the imports need manual adjustment or rescanning, which can be handled later.


<img width="346" height="142" alt="image" src="https://github.com/user-attachments/assets/4f427fd2-ccce-4e26-a976-fea1160f352b" />

If imports are populated, the next step is cleaning invalid imports, which is critical. Click Show Invalid and remove anything marked in red, unresolved entries, or obvious garbage. MPRESS commonly leaves behind junk import references that must be removed. Leaving invalid imports in place will almost always cause the dumped executable to fail at load time.

Once the import list contains only valid, resolved entries, click Fix Dump. This step writes a correct import table into the dumped executable, repairs PE header inconsistencies, and adjusts the entry point if necessary. Wait for Scylla to report a successful fix. Only after this step is complete should you consider further rebuilding or analysis.

If **Get Imports** returns an empty list, this is a known and common behavior with MPRESS-packed binaries. It does not mean the dump is unusable and it does not indicate a mistake so far. MPRESS often obscures the IAT in a way that prevents automatic detection on the first pass.

In this case, switch to a manual scan. In Scylla, take the IAT address that was already identified and set the **VA** field to `000000011E7FDAFA`. This explicitly tells Scylla where the import table is expected to begin in memory.

Next, increase the **Size** field to a reasonable scan range, starting with `0x1000`. This gives Scylla enough memory space to search for valid import pointers. After setting the VA and Size, click **Get Imports** again. With these parameters in place, Scylla can correctly scan the specified memory region and recover the import table that MPRESS left behind.

<img width="1919" height="1008" alt="image" src="https://github.com/user-attachments/assets/29d4c488-1ace-4ada-b0b0-e0e4fb976d85" />

The database is no longer dominated by opaque loader logic or unresolved code regions. Instead, IDA is correctly identifying structured sections, defined functions, and meaningful data references. This is the expected state after a proper MPRESS unpack.



The key to cracking this challenge is reverse engineering the binary to discover how it validates `.auroralic` files. By analyzing the binary with tools like Ghidra, you'll find that licenses start with magic bytes `AUR0`, followed by a version byte, username length, username, expiry timestamp, and feature flags. The critical part is the SHA-256 checksum at the end, which validates everything. The checksum is calculated by hashing a secret seed (`aurora_ctf_2025_secret_salt`), the username XORed with `0x42`, a timestamp mixed with the magic number `0x5f3759df`, and the feature flags. The endianness is tricky - little-endian for the mixed timestamp but big-endian for the license file structure.

Once you understand the algorithm, building a keygen is straightforward. The included Julia implementation shows how to construct valid licenses by properly formatting the binary data and calculating the correct checksum. Generate a license for any username, run it through the validator, and the binary will reveal your flag. The flag is generated by hashing the license data with a secret prefix, producing a unique flag in the format `FLAG{aurora_<hash>}`. The real challenge is discovering those constants buried in the binary and understanding how they all fit together in the validation process.


## AUR{fb013f8719fe631c1c3fb8641120b134291224d6fa6a52ed66b874019931ce98} 
