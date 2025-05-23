

## Overview
1. The challenge provides a ZIP file containing:
   - A Windows executable (`main.exe`)
   - A folder (`test`) with 18 BMP images

2. When run, the program requires a `flag.txt` file and appears to modify the images in some way.

## Analysis Steps

### Initial Execution
- Running the program without `flag.txt` gives an error message
- With `flag.txt` present, it completes but doesn't visibly change anything

### Reverse Engineering
Using Ghidra, we analyze the executable and find:

1. **Main Function**:
   - Reads 18 characters from `flag.txt`
   - Initializes global variables including `_folderName` pointing to "./test"
   - Calls `_listdir(0, "./test")` to process files

2. **Listdir Function**:
   - Recursively processes files in the folder
   - For every other file, calls `_hideInFile()`

3. **HideInFile Function**:
   - Uses Windows API calls to get/set file times
   - Encodes flag characters into the file modification times

### Key Insight
- The program hides the flag by encoding it into the **high-precision modification times** of the BMP files
- Windows stores file times with 100-nanosecond precision (more precise than what standard Python APIs can access)
- Each pair of flag characters is encoded into the least significant 2 bytes of a file's modification time

### Solution Approach
1. **Direct Approach**:
   - Found an uncalled function `_decode()` that would extract the flag
   - Used a debugger to jump to this function after initialization

2. **Scripting Approach**:
   - Wrote a Python script using `ctypes` to access Windows API directly
   - Extracted the precise modification times of every other BMP file
   - Decoded the flag from the least significant 2 bytes of each time

## Final Answer
The flag is: `picoCTF{M4cTim35!}`
