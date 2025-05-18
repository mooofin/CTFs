![image](https://github.com/user-attachments/assets/730821e7-cb41-48c3-bdce-3d3f00b535cd)
![image](https://github.com/user-attachments/assets/23ab0c81-0c7f-4ed5-83e0-af675f28a8ba)
![image](https://github.com/user-attachments/assets/9ec94de7-6579-4278-bfa7-1f505531403e)


### Input Processing Workflow
The verification function follows this operational sequence:

1. **Input Acquisition**
   - The function retrieves user input through standard input operations
   - Input storage utilizes a custom string management system with small-string optimization (SSO)

2. **Memory Management**
   - Strings ≤15 characters employ stack-based storage (SSO)
   - Longer strings trigger heap allocation with:
     ```c
     _Dst = operator_new(uVar7 + 1);
     ```
   - Memory operations include proper alignment handling:
     ```c
     _Dst = (undefined8 ****)((longlong)pppuVar9 + 0x27U & 0xffffffffffffffe0);
     ```

3. **String Comparison Logic**
   - The critical validation occurs through:
     ```c
     iVar6 = memcmp(_Buf1, ppppuVar13, _Size);
     bVar14 = iVar6 == 0;
     ```
   - Successful validation leads to:
     ```c
     MessageBoxA("License Accepted!", "Success");
     ```

### Cryptographic Observation
The validation mechanism compares against the static value `0x5A57494B` (ASCII "ZWIK"). Analysis revealed:

1. **Byte Order Significance**
   - Input "KIWZ" (hex: `0x4B49575A`) matches when interpreted in little-endian format
   - Memory representation converts to `0x5A57494B` ("ZWIK")

2. **Validation Logic Characteristics**
   - No cryptographic hashing present
   - Simple byte comparison with fixed value
   - Length check precedes content verification

## Exploitation Methodology

### Static Analysis Findings
1. **Vulnerability Location**
   - Hardcoded comparison at address containing `0x5A57494B`
   - No dynamic key generation or advanced obfuscation

2. **Bypass Techniques**
   - **Binary Patching**
     - Modify `memcmp` to unconditional return 0
     - Alter conditional jump after comparison
   - **Input Crafting**
     - Supply "KIWZ" for direct validation
     - Any 4-byte input where `input[3] == 0x5A`, `input[2] == 0x57`, etc.

### Dynamic Analysis Approach
1. **Debugging Strategy**
   - Breakpoint at input reception (`FUN_140001bc0`)
   - Memory inspection post-processing
   - Register monitoring during comparison

2. **Validation Process Tracing**
   ```assembly
   mov     [rsp+local_e0], 5A57494Bh  ; Load comparison value
   call    memcmp                      ; Critical validation
   test    eax, eax                    ; Result check
   jz      valid_license               ; Success branch
   ```


### Final  Summary
The license verification employs straightforward comparison logic vulnerable to static analysis. The little-endian interpretation creates an apparent discrepancy between the visible value ("ZWIK") and actual valid input ("KIWZ"), demonstrating how byte ordering affects string validation in compiled software.

## Appendices

### Disassembly Snippets
Key validation logic:
```assembly
.text:000000014000169A     mov     [rsp+local_e0], 5A57494Bh
.text:00000001400016A2     call    memcmp_140001220
.text:00000001400016A7     test    eax, eax
.text:00000001400016A9     jz      loc_140001720
```

### Memory Layout
Input processing stack structure:
```
+---------------------+
| Input Buffer        |
+---------------------+
| Comparison Value    |  ; 0x5A57494B
+---------------------+
| String Length       |
+---------------------+
| Allocation Flag     |  ; 0xF for SSO
+---------------------+
```
### The puedo code from ghidra
```c

void FUN_140001540(void)

{
  int iVar6;
  ulonglong uVar7;
  ulonglong uVar8;
  undefined8 ***pppuVar9;
  undefined8 ****_Dst;
  longlong *plVar10;
  longlong *_Buf1;
  void *pvVar11;
  void *pvVar12;
  undefined8 ****ppppuVar13;
  char *lpText;
  char *lpCaption;
  bool bVar14;
  undefined1 auStack_108 [32];
  longlong *local_e8;
  undefined8 local_e0;
  undefined8 uStack_d8;
  undefined8 local_d0;
  undefined8 local_c8;
  undefined1 local_b8 [32];
  undefined8 ***local_98;
  undefined8 **ppuStack_90;
  size_t local_88;
  ulonglong local_80;
  undefined8 ***local_78;
  undefined8 uStack_70;
  ulonglong local_68;
  ulonglong local_60;
  undefined1 local_58;
  undefined7 uStack_57;
  undefined8 local_48;
  ulonglong local_40;
  ulonglong local_38;
  size_t _Size;
  code *pcVar2;
  undefined8 ***pppuVar4;
  ulonglong uVar1;
  ulonglong uVar3;
  ulonglong uVar5;
  
  local_38 = DAT_140006000 ^ (ulonglong)auStack_108;
  FUN_140001010();
  uStack_70 = 0;
  _Dst = (undefined8 ****)0x0;
  local_68 = 0;
  local_60 = 0xf;
  local_78 = (undefined8 ****)0x0;
  FUN_140001a00(cout_exref);
  FUN_140001bc0(cin_exref,&local_78);
  uVar5 = local_60;
  uVar3 = local_68;
  pppuVar4 = local_78;
  local_98 = (undefined8 ***)0x0;
  ppuStack_90 = (undefined8 ***)0x0;
  local_88 = 0;
  local_80 = 0;
  ppppuVar13 = &local_78;
  if (0xf < local_60) {
    ppppuVar13 = (undefined8 ****)local_78;
  }
  if (0x7fffffffffffffff < local_68) {
    FUN_140001200();
LAB_1400018b6:
    FUN_140001160();
    pcVar2 = (code *)swi(3);
    (*pcVar2)();
    return;
  }
  if (local_68 < 0x10) {
    local_88 = local_68;
    local_80 = 0xf;
    local_98 = *ppppuVar13;
    ppuStack_90 = ppppuVar13[1];
    goto LAB_14000169a;
  }
  uVar7 = local_68 | 0xf;
  if (uVar7 < 0x8000000000000000) {
    if (uVar7 < 0x16) {
      uVar7 = 0x16;
    }
    uVar1 = uVar7 + 1;
    if (uVar1 != 0) {
      if (0xfff < uVar1) {
        uVar8 = uVar7 + 0x28;
        if (uVar8 <= uVar1) goto LAB_1400018b6;
        goto LAB_140001620;
      }
      _Dst = (undefined8 ****)operator_new(uVar1);
    }
  }
  else {
    uVar8 = 0x8000000000000027;
    uVar7 = 0x7fffffffffffffff;
LAB_140001620:
    pppuVar9 = (undefined8 ***)operator_new(uVar8);
    if (pppuVar9 == (undefined8 ***)0x0) {
                    /* WARNING: Subroutine does not return */
      _invalid_parameter_noinfo_noreturn();
    }
    _Dst = (undefined8 ****)((longlong)pppuVar9 + 0x27U & 0xffffffffffffffe0);
    _Dst[-1] = pppuVar9;
  }
  local_88 = uVar3;
  local_98 = _Dst;
  local_80 = uVar7;
  memcpy(_Dst,ppppuVar13,uVar3 + 1);
LAB_14000169a:
  FUN_140001220(&local_58,&local_98);
  plVar10 = (longlong *)FUN_140001350(local_b8,&local_58);
  uStack_d8 = 0;
  local_d0 = 4;
  local_c8 = 0xf;
  local_e0 = 013225644513;
  local_e8 = plVar10;
  FUN_140001220(&local_98,&local_e0);
  uVar3 = local_80;
  pppuVar9 = local_98;
  ppppuVar13 = &local_98;
  if (0xf < local_80) {
    ppppuVar13 = (undefined8 ****)local_98;
  }
  _Buf1 = plVar10;
  if (0xf < (ulonglong)plVar10[3]) {
    _Buf1 = (longlong *)*plVar10;
  }
  _Size = plVar10[2];
  if (_Size == local_88) {
    if (_Size == 0) {
      bVar14 = true;
    }
    else {
      iVar6 = memcmp(_Buf1,ppppuVar13,_Size);
      bVar14 = iVar6 == 0;
    }
  }
  else {
    bVar14 = false;
  }
  if (0xf < uVar3) {
    ppppuVar13 = (undefined8 ****)pppuVar9;
    if ((0xfff < uVar3 + 1) &&
       (ppppuVar13 = (undefined8 ****)pppuVar9[-1],
       0x1f < (ulonglong)((longlong)pppuVar9 + (-8 - (longlong)ppppuVar13)))) {
                    /* WARNING: Subroutine does not return */
      _invalid_parameter_noinfo_noreturn();
    }
    free(ppppuVar13);
  }
  local_88 = 0;
  local_80 = 0xf;
  local_98 = (undefined8 ***)((ulonglong)local_98 & 0xffffffffffffff00);
  if (0xf < (ulonglong)plVar10[3]) {
    pvVar12 = (void *)*plVar10;
    pvVar11 = pvVar12;
    if ((0xfff < plVar10[3] + 1U) &&
       (pvVar11 = *(void **)((longlong)pvVar12 + -8),
       0x1f < (ulonglong)((longlong)pvVar12 + (-8 - (longlong)pvVar11)))) {
                    /* WARNING: Subroutine does not return */
      _invalid_parameter_noinfo_noreturn();
    }
    free(pvVar11);
  }
  plVar10[2] = 0;
  plVar10[3] = 0xf;
  *(undefined1 *)plVar10 = 0;
  if (bVar14) {
    lpCaption = "Success";
    lpText = "License Accepted!";
  }
  else {
    lpCaption = "Error";
    lpText = "Invalid License";
  }
  MessageBoxA((HWND)0x0,lpText,lpCaption,0);
  if (0xf < local_40) {
    pvVar11 = (void *)CONCAT71(uStack_57,local_58);
    pvVar12 = pvVar11;
    if ((0xfff < local_40 + 1) &&
       (pvVar12 = *(void **)((longlong)pvVar11 + -8),
       0x1f < (ulonglong)((longlong)pvVar11 + (-8 - (longlong)pvVar12)))) {
                    /* WARNING: Subroutine does not return */
      _invalid_parameter_noinfo_noreturn();
    }
    free(pvVar12);
  }
  local_48 = 0;
  local_40 = 0xf;
  local_58 = 0;
  if (0xf < uVar5) {
    ppppuVar13 = (undefined8 ****)pppuVar4;
    if ((0xfff < uVar5 + 1) &&
       (ppppuVar13 = (undefined8 ****)pppuVar4[-1],
       0x1f < (ulonglong)((longlong)pppuVar4 + (-8 - (longlong)ppppuVar13)))) {
                    /* WARNING: Subroutine does not return */
      _invalid_parameter_noinfo_noreturn();
    }
    free(ppppuVar13);
  }
  FUN_140001fe0(local_38 ^ (ulonglong)auStack_108);
  return;
}

```
