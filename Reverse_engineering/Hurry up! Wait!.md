

## Analysis
After analyzing the binary in Ghidra, I observed that:
- The main function at `0x0010298a` calls several `FUN_00*` functions
- Each `FUN_00*` function contains one character of the flag at offset `+0x9`

![Ghidra Disassembly View](https://github.com/user-attachments/assets/fd7cde22-82fb-4fab-887d-7a86fb063a8d)  
*Main function calling `FUN_00*` routines*

## Automated Solution
I used Ghidra's Python scripting to extract the flag:

```python
from ghidra.program.model.listing import Function
from ghidra.program.model.scalar import Scalar

def get_called_functions(func):
    for instr in currentProgram.getListing().getInstructions(func.getBody(), True):
        if instr.getFlowType().isCall():
            for ref in instr.getReferencesFrom():
                called_func = getFunctionAt(ref.getToAddress())
                if called_func and called_func.getName().startswith("FUN_00"):
                    yield called_func.getEntryPoint()

def get_flag_char(address):
    target_address = address.add(0x9)
    instruction = currentProgram.getListing().getInstructionAt(target_address)
    operand = instruction.getOpObjects(1)[0]
    if isinstance(operand, Scalar):
        char_addr = toAddr(operand.getValue())
        return chr(currentProgram.getMemory().getByte(char_addr))

main_function = getFunctionAt(toAddr(0x0010298a))
flag = [get_flag_char(addr) for addr in get_called_functions(main_function)]
print(''.join(filter(None, flag)))
```

**Output**:  
`picoCTF{d15a5m_ftw_eab78e4}`

## Key Steps
1. Identified flag storage pattern in `FUN_00*` functions
2. Used Ghidra's API to:
   - Trace function calls
   - Extract operand values
   - Convert memory bytes to ASCII
3. Automated with Script Manager

## Resources
- [![Laurie's Tutorial](https://img.shields.io/badge/Video-Ghidra_Scripting-blue)](https://youtu.be/z7SO6CF3guE?si=O11BTkBMb6Owz0Ul)
- [Ghidra API Docs](https://ghidra.re/ghidra_docs/api/overview-summary.html)
