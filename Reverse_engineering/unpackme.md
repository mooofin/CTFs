# Reverse Engineering the UPX Packed Binary (unpackme-upx)

## **Introduction**
This writeup details the process of reverse engineering a UPX-packed binary named **unpackme-upx** to extract a hidden flag. The goal is to analyze the binary, determine the correct input to unlock the flag, and understand how the program processes user input.

---
## **Step 1: Initial Binary Execution**
Before analyzing the binary, we first execute it to observe its behavior:

```bash
./unpackme-upx
```

### **Observation:**
The binary prompts the user:
```
What's my favorite number?
```
Entering a random number results in:
```
Sorry, that's not it!
```
Since no further information is provided, we must analyze the binary to determine the correct input.

---
## **Step 2: Identifying UPX Packing**
Next, we use the `strings` tool to inspect the binary for readable text:

```bash
strings unpackme-upx | less
```

### **Observation:**
The output contains **UPX** references, indicating that the binary is packed with the Ultimate Packer for Executables (UPX).

To confirm, we use the `upx` command:

```bash
upx -t unpackme-upx
```

If the binary is packed, UPX will confirm it.

---
## **Step 3: Unpacking the Binary**
To extract the original binary, we execute:

```bash
upx -d unpackme-upx
```

### **Output:**
```
Ultimate Packer for eXecutables
Unpacked 1 file.
```

At this point, the binary has been successfully decompressed.

---
## **Step 4: Running the Unpacked Binary**
We rerun the binary to see if any changes occur:

```bash
./unpackme-upx
```

Again, it prompts for a favorite number. We proceed with **reverse engineering** to uncover the correct input.

---
## **Step 5: Analyzing with Ghidra**
To examine the binary in **Ghidra**, we launch it:

```bash
ghidra
```

1. Create a new project and import the **unpackme-upx** binary.
2. Navigate to the **Symbol Tree** section and locate the `main` function under **Functions**.

### **Disassembly Findings**
The decompiled `main` function reveals the following logic:

```c
undefined8 main(void)
{
  long in_FS_OFFSET;
  int iStack_44;
  undefined8 uStack_40;
  undefined8 uStack_38;
  undefined8 uStack_30;
  undefined8 uStack_28;
  undefined4 uStack_20;
  undefined2 uStack_1c;
  long lStack_10;
  
  lStack_10 = *(long *)(in_FS_OFFSET + 0x28);
  uStack_38 = 0x4c75257240343a41;
  uStack_30 = 0x30623e306b6d4146;
  uStack_28 = 0x6865666430486637;
  uStack_20 = 0x36636433;
  uStack_1c = 0x4e;
  printf(&UNK_004b3004);
  __isoc99_scanf(&UNK_004b3020,&iStack_44);
  if (iStack_44 == 754635) {
    uStack_40 = rotate_encrypt(0,&uStack_38);
    fputs(uStack_40,stdout);
    putchar(10);
    free(uStack_40);
  }
  else {
    puts(&UNK_004b3023);
  }
  if (lStack_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

---
## **Step 6: Extracting the Correct Input**
From the decompiled code, we focus on:

```c
if (iStack_44 == 754635) {
```

This line indicates that the correct input to unlock the flag is `754635`.

---
## **Step 7: Extracting the Flag**
We rerun the binary and enter the correct number:

```bash
./unpackme-upx
```
```
What's my favorite number? 754635
picoCTF{up><_m3_f7w_5769b54e}
```

### **Final Flag:**
```
picoCTF{up><_m3_f7w_5769b54e}
```

---


