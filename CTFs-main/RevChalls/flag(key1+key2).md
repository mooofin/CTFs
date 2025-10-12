Note - always check for UPX , wasted half an hour because i didnt unpack the binary 



```bash
$ file './flag{key1+key2}'
./flag{key1+key2}: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=77c06ef6af332d2e5def19f42f2b60fcf2c5d2e6, not stripped
```

**Key observations:**
- 32-bit ELF binary
- Dynamically linked (requires 32-bit libraries)
- Not stripped (symbols intact - easier to analyze)

### Initial Execution
```bash
$ ./flag\{key1+key2\}
[No output]
```

The binary runs but produces no output. Mybe the key is in the binary itself ? 





### Detecting the Packer
```bash
$ strings './flag{key1+key2}' | grep -i upx
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.91 Copyright (C) 1996-2013 the UPX Team. All Rights Reserved. $
PROT_EXEC|PROT_WRITE failed.
```

The binary is packed with UPX (Ultimate Packer for eXecutables) version 3.91.

### Unpacking with UPX
```bash
$ upx -d './flag{key1+key2}'
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2025
UPX 5.0.2       Markus Oberhumer, Laszlo Molnar & John Reiser   Jul 20th 2025

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
[WARNING] bad b_info at 0x12948
[WARNING] ... recovery at 0x12944
    194808 <-     85996   44.14%   linux/i386    flag{key1+key2}

Unpacked 1 file.
```




### Searching for Key-Related Strings
```bash
$ strings './flag{key1+key2}' | grep -i key
You don't have the first part of key yet
You dont have the entire key yet.... :(
keyjoin.12717834333337631731.tmp.c
mapnode_find_key
map_key_to_index
mapnode_subkeys
map_keys_1
SortedMap_keys
mapnode_remove_key
DenseArray_key
map_keys
```

**Important strings ehe :**
1. `"You don't have the first part of key yet"`
2. `"You dont have the entire key yet.... :("`

These error messages indicate the binary checks for keys and displays messages when conditions aren't met 

### Additional Context Strings
```bash
$ strings './flag{key1+key2}' | head -20
You don't have the first part of key yet
You dont have the entire key yet.... :(
0123456789abcdefghijklmnopqrstuvwxyz
```





### Main Function Analysis
```bash
$ objdump -d -M intel './flag{key1+key2}' | grep -A 50 "<main>:"
```

**Output:**
```assembly
08068f89 <main>:
 8068f89:	8d 4c 24 04          	lea    ecx,[esp+0x4]
 8068f8d:	83 e4 f0             	and    esp,0xfffffff0
 8068f90:	ff 71 fc             	push   DWORD PTR [ecx-0x4]
 8068f93:	55                   	push   ebp
 8068f94:	89 e5                	mov    ebp,esp
 8068f96:	51                   	push   ecx
 8068f97:	83 ec 04             	sub    esp,0x4
 8068f9a:	89 c8                	mov    eax,ecx
 8068f9c:	83 ec 08             	sub    esp,0x8
 8068f9f:	ff 70 04             	push   DWORD PTR [eax+0x4]
 8068fa2:	ff 30                	push   DWORD PTR [eax]
 8068fa4:	e8 f3 93 ff ff       	call   806239c <_vinit>
 8068fa9:	83 c4 10             	add    esp,0x10
 8068fac:	e8 cb 8f ff ff       	call   8061f7c <main__main>
 8068fb1:	b8 00 00 00 00       	mov    eax,0x0
 8068fb6:	8b 4d fc             	mov    ecx,DWORD PTR [ebp-0x4]
 8068fb9:	c9                   	leave
 8068fba:	8d 61 fc             	lea    esp,[ecx-0x4]
 8068fbd:	c3                   	ret
```


- `main` calls `_vinit` for initialization
- Then calls `main__main` at address `0x8061f7c`
- Returns 0


```bash
$ objdump -d -M intel './flag{key1+key2}' | grep -A 50 "8061f7c <main__main>:"
```

**Output:**
```assembly
08061f7c <main__main>:
 8061f7c:	55                   	push   ebp
 8061f7d:	89 e5                	mov    ebp,esp
 8061f7f:	83 ec 28             	sub    esp,0x28
 8061f82:	c7 45 d8 17 00 00 00 	mov    DWORD PTR [ebp-0x28],0x17
 8061f89:	c7 45 dc 8c 09 00 00 	mov    DWORD PTR [ebp-0x24],0x98c
 8061f90:	83 7d d8 2d          	cmp    DWORD PTR [ebp-0x28],0x2d
 8061f94:	75 07                	jne    8061f9d <main__main+0x21>
 8061f96:	e8 64 00 00 00       	call   8061fff <main__one>
 8061f9b:	eb 29                	jmp    8061fc6 <main__main+0x4a>
 8061f9d:	c7 45 e0 04 a0 06 08 	mov    DWORD PTR [ebp-0x20],0x806a004
 8061fa4:	c7 45 e4 0f 00 00 00 	mov    DWORD PTR [ebp-0x1c],0xf
 8061fab:	c7 45 e8 01 00 00 00 	mov    DWORD PTR [ebp-0x18],0x1
 8061fb2:	83 ec 04             	sub    esp,0x4
 8061fb5:	ff 75 e8             	push   DWORD PTR [ebp-0x18]
 8061fb8:	ff 75 e4             	push   DWORD PTR [ebp-0x1c]
 8061fbb:	ff 75 e0             	push   DWORD PTR [ebp-0x20]
 8061fbe:	e8 43 59 ff ff       	call   8057906 <println>
 8061fc3:	83 c4 10             	add    esp,0x10
 8061fc6:	83 7d dc 4c          	cmp    DWORD PTR [ebp-0x24],0x4c
 8061fca:	75 07                	jne    8061fd3 <main__main+0x57>
 8061fcc:	e8 60 01 00 00       	call   8062131 <main__two>
 8061fd1:	eb 29                	jmp    8061ffc <main__main+0x80>
 8061fd3:	c7 45 ec 04 a0 06 08 	mov    DWORD PTR [ebp-0x14],0x806a004
 8061fda:	c7 45 f0 0f 00 00 00 	mov    DWORD PTR [ebp-0x10],0xf
 8061fe1:	c7 45 f4 01 00 00 00 	mov    DWORD PTR [ebp-0xc],0x1
 8061fe8:	83 ec 04             	sub    esp,0x4
 8061feb:	ff 75 f4             	push   DWORD PTR [ebp-0xc]
 8061fee:	ff 75 f0             	push   DWORD PTR [ebp-0x10]
 8061ff1:	ff 75 ec             	push   DWORD PTR [ebp-0x14]
 8061ff4:	e8 0d 59 ff ff       	call   8057906 <println>
 8061ff9:	83 c4 10             	add    esp,0x10
 8061ffc:	90                   	nop
 8061ffd:	c9                   	leave
 8061ffe:	c3                   	ret
```

So Summing everything up here 

**Line 8061f82:** `mov DWORD PTR [ebp-0x28],0x17`
- Stores value `0x17` (decimal 23) in local variable

**Line 8061f89:** `mov DWORD PTR [ebp-0x24],0x98c`
- Stores value `0x98c` (decimal 2444) in local variable

**Line 8061f90:** `cmp DWORD PTR [ebp-0x28],0x2d`
- Compares first value with `0x2d` (decimal 45)
- Since 23 ≠ 45, the jump at 8061f94 is taken

**Line 8061f96:** `call 8061fff <main__one>`
- **This call is SKIPPED** because the comparison failed

**Line 8061f9d-8061fbe:** Error message print
- Loads address `0x806a004` (points to error string)
- Calls `println` to print the error

**Line 8061fc6:** `cmp DWORD PTR [ebp-0x24],0x4c`
- Compares second value with `0x4c` (decimal 76)
- Since 2444 ≠ 76, this also fails

**Line 8061fcc:** `call 8062131 <main__two>`
- **This call is also SKIPPED**

**Conclusion:** The binary intentionally prevents the key functions from being called by using incorrect comparison values.




Since the binary won't naturally print the keys, we need to analyze the `main__one` and `main__two` functions to extract the keys manually.

### KEY 1: Analyzing main__one

```bash
$ objdump -d -M intel './flag{key1+key2}' | grep -A 150 "8061fff <main__one>:"
```

**Key sections:**

```assembly
08061fff <main__one>:
 8062030:	c7 45 a8 2d 00 00 00 	mov    DWORD PTR [ebp-0x58],0x2d
 8062037:	83 7d a8 1f          	cmp    DWORD PTR [ebp-0x58],0x1f
 806203b:	0f 8f 93 00 00 00    	jg     80620d4 <main__one+0xd5>
```

**Line 8062030:** Sets value to `0x2d` (45)
**Line 8062037:** Compares with `0x1f` (31)
**Line 806203b:** If > 31, jump to error handler

Since 45 > 31, it jumps to the error path. But the important part is the code that WOULD execute:

```assembly
 8062041:	8d 45 c8             	lea    eax,[ebp-0x38]
 8062044:	83 ec 0c             	sub    esp,0xc
 8062047:	6a 00                	push   0x0
 8062049:	6a 04                	push   0x4
 806204b:	6a 0a                	push   0xa
 806204d:	6a 00                	push   0x0
 806204f:	50                   	push   eax
 8062050:	e8 14 3a ff ff       	call   8055a69 <__new_array_with_default>
```

This creates an array with capacity 10.

```assembly
 8062058:	c7 45 a4 02 00 00 00 	mov    DWORD PTR [ebp-0x5c],0x2
 806205f:	eb 1d                	jmp    806207e <main__one+0x7f>
 8062061:	8b 45 a4             	mov    eax,DWORD PTR [ebp-0x5c]
 8062064:	89 45 ec             	mov    DWORD PTR [ebp-0x14],eax
 8062067:	83 ec 08             	sub    esp,0x8
 806206a:	8d 45 ec             	lea    eax,[ebp-0x14]
 806206d:	50                   	push   eax
 806206e:	8d 45 c8             	lea    eax,[ebp-0x38]
 8062071:	50                   	push   eax
 8062072:	e8 43 49 ff ff       	call   80569ba <array_push>
 8062077:	83 c4 10             	add    esp,0x10
 806207a:	83 45 a4 01          	add    DWORD PTR [ebp-0x5c],0x1
 806207e:	83 7d a4 0b          	cmp    DWORD PTR [ebp-0x5c],0xb
 8062082:	7e dd                	jle    8062061 <main__one+0x62>
```

**Loop analysis:**
- **Line 8062058:** Initialize counter to 2
- **Line 8062061-8062072:** Push counter value to array
- **Line 806207a:** Increment counter by 1
- **Line 806207e:** Compare counter with 0xb (11)
- **Line 8062082:** If counter ≤ 11, loop

**Result:** Creates array `[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`

```assembly
 8062084:	8d 45 d8             	lea    eax,[ebp-0x28]
 8062087:	83 ec 04             	sub    esp,0x4
 806208a:	6a 08                	push   0x8
 806208c:	6a 02                	push   0x2
 806208e:	ff 75 d4             	push   DWORD PTR [ebp-0x2c]
 8062091:	ff 75 d0             	push   DWORD PTR [ebp-0x30]
 8062094:	ff 75 cc             	push   DWORD PTR [ebp-0x34]
 8062097:	ff 75 c8             	push   DWORD PTR [ebp-0x38]
 806209a:	50                   	push   eax
 806209b:	e8 d0 43 ff ff       	call   8056470 <array_slice>
```

**Line 806208a:** Push 8 (end index)
**Line 806208c:** Push 2 (start index)
**Call:** `array_slice(array, 2, 8)`

**Result:** Slices array from index 2 to 8 → `[4, 5, 6, 7, 8, 9]`

```assembly
 80620a3:	8d 45 ac             	lea    eax,[ebp-0x54]
 80620a6:	83 ec 0c             	sub    esp,0xc
 80620a9:	ff 75 e4             	push   DWORD PTR [ebp-0x1c]
 80620ac:	ff 75 e0             	push   DWORD PTR [ebp-0x20]
 80620af:	ff 75 dc             	push   DWORD PTR [ebp-0x24]
 80620b2:	ff 75 d8             	push   DWORD PTR [ebp-0x28]
 80620b5:	50                   	push   eax
 80620b6:	e8 fe 70 fe ff       	call   80491b9 <array_int_str>
 80620bb:	83 c4 1c             	add    esp,0x1c
 80620be:	83 ec 04             	sub    esp,0x4
 80620c1:	ff 75 b4             	push   DWORD PTR [ebp-0x4c]
 80620c4:	ff 75 b0             	push   DWORD PTR [ebp-0x50]
 80620c7:	ff 75 ac             	push   DWORD PTR [ebp-0x54]
 80620ca:	e8 37 58 ff ff       	call   8057906 <println>
```

**Call:** `array_int_str` - Converts integer array to string
**Call:** `println` - Prints the result

**KEY1 = "456789"**

---

### KEY 2: Analyzing main__two

```bash
$ objdump -d -M intel './flag{key1+key2}' | grep -A 250 "8062131 <main__two>:"
```

**Key sections:**

```assembly
08062131 <main__two>:
 806216e:	c7 85 18 ff ff ff 5a 	mov    DWORD PTR [ebp-0xe8],0x5a
 8062175:	00 00 00 
 8062178:	83 bd 18 ff ff ff 2c 	cmp    DWORD PTR [ebp-0xe8],0x2c
 806217f:	0f 8f 03 02 00 00    	jg     8062388 <main__two+0x257>
```

**Line 806216e:** Sets value to `0x5a` (90)
**Line 8062178:** Compares with `0x2c` (44)

Since 90 > 44, it jumps to error handler. But the code that would execute:

```assembly
 806219f:	c7 85 70 ff ff ff 3d 	mov    DWORD PTR [ebp-0x90],0x806a03d
 80621a6:	a0 06 08 
 80621a9:	c7 85 74 ff ff ff 01 	mov    DWORD PTR [ebp-0x8c],0x1
 80621b0:	00 00 00 
 80621b3:	c7 85 78 ff ff ff 01 	mov    DWORD PTR [ebp-0x88],0x1
 80621ba:	00 00 00 
 80621bd:	c7 85 7c ff ff ff 3f 	mov    DWORD PTR [ebp-0x84],0x806a03f
 80621c4:	a0 06 08 
 80621c7:	c7 45 80 01 00 00 00 	mov    DWORD PTR [ebp-0x80],0x1
 80621ce:	c7 45 84 01 00 00 00 	mov    DWORD PTR [ebp-0x7c],0x1
 80621d5:	c7 45 88 41 a0 06 08 	mov    DWORD PTR [ebp-0x78],0x806a041
 80621dc:	c7 45 8c 01 00 00 00 	mov    DWORD PTR [ebp-0x74],0x1
 80621e3:	c7 45 90 01 00 00 00 	mov    DWORD PTR [ebp-0x70],0x1
 80621ea:	c7 45 94 43 a0 06 08 	mov    DWORD PTR [ebp-0x6c],0x806a043
 80621f1:	c7 45 98 01 00 00 00 	mov    DWORD PTR [ebp-0x68],0x1
 80621f8:	c7 45 9c 01 00 00 00 	mov    DWORD PTR [ebp-0x64],0x1
 80621ff:	c7 45 a0 45 a0 06 08 	mov    DWORD PTR [ebp-0x60],0x806a045
 8062206:	c7 45 a4 01 00 00 00 	mov    DWORD PTR [ebp-0x5c],0x1
 806220d:	c7 45 a8 01 00 00 00 	mov    DWORD PTR [ebp-0x58],0x1
```

**Memory addresses loaded:**
- `0x806a03d`
- `0x806a03f`
- `0x806a041`
- `0x806a043`
- `0x806a045`

Each address is followed by length 1, suggesting single character strings mostly prolly 



```bash
$ objdump -s --start-address=0x806a014 --stop-address=0x806a050 './flag{key1+key2}'
```

**Output:**
```
./flag{key1+key2}:     file format elf32-i386

Contents of section .rodata:
 806a014 596f7520 646f6e27 74206861 76652074  You don't have t
 806a024 68652066 69727374 20706172 74206f66  he first part of
 806a034 206b6579 20796574 004a004b 004c0071   key yet.J.K.L.q
 806a044 00350039 00550031 00330037           .5.9.U.1.3.7
```


```
Offset   Hex     ASCII   Character
------   -----   -----   ---------
806a03d  4a 00   J \0    'J'
806a03f  4b 00   K \0    'K'
806a041  4c 00   L \0    'L'
806a043  71 00   q \0    'q'
806a045  35 00   5 \0    '5'
806a047  39 00   9 \0    '9'
806a049  55 00   U \0    'U'
806a04b  31 00   1 \0    '1'
806a04d  33 00   3 \0    '3'
806a04f  37 00   7 \0    '7'
```

The code references only the first 5 addresses (0x806a03d through 0x806a045), so:

**KEY2 = "JKLq5"**

---

## Solution

### Final Keys
- **KEY1:** `456789`
- **KEY2:** `JKLq5`

### Flag Format
The challenge filename is `flag{key1+key2}`, which means:

```
flag{456789+JKLq5}
```

