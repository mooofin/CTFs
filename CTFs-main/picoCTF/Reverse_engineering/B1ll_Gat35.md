
## Challenge
Windows executable that validates a key before printing the flag.




Decompiled in Ghidra - found validation check at `0x00408114`:

<img width="1919" height="999" alt="image" src="https://github.com/user-attachments/assets/6bc1caff-2cc7-4964-8971-1ea6f1f84c7e" />

```asm
00408112  TEST  EAX, EAX
00408114  JNZ   LAB_00408125    ; Jump to success if key is correct
```


Change conditional jump to unconditional:
- **File offset:** `0x7514`
- **Change:** `0x75` (JNZ) → `0xEB` (JMP)




```powershell
echo "1" | .\win-exec-1-patched.exe
```

### Flag
```
PICOCTF{These are the access codes to the vault: 1063340}
```
