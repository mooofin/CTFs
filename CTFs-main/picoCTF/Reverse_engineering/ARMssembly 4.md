

```m
# ARM Assembly Challenge Writeup

## Challenge Overview
We need to determine what the program prints when executed with the argument `3459413018`. The program consists of multiple nested functions written in ARMv8 assembly.

## Key Functions
The call graph for our input follows this path:
```
main → func1 → func2 → func5 → func8
```

## Step-by-Step Execution

### 1. Initial Call (main)
- Argument: `3459413018`
- Calls: `func1(3459413018)`

### 2. func1 Analysis
```asm
cmp w0, 100          ; Compare input with 100
bls .L2              ; If <=100, jump to func3
add w0, w0, 100      ; Else add 100 (3459413018 → 3459413118)
bl func2             ; Call func2(3459413118)
```
- Our input (3459413018) > 100 → calls `func2(3459413118)`

### 3. func2 Analysis
```asm
cmp w0, 499          ; Compare input with 499
bhi .L5              ; If >499, jump to func5
sub w0, w0, #86      ; Else subtract 86 (not taken)
bl func4             ; Would call func4 (not taken)
```
- Our input (3459413118) > 499 → calls `func5(3459413131)` (added 13)

### 4. func5 Analysis
```asm
bl func8             ; Calls func8(input)
```
- Calls `func8(3459413131)`

### 5. func8 Analysis
```asm
add w0, w0, 2        ; Adds 2 to input (3459413131 → 3459413133)
ret                  ; Returns final value
```

## Final Calculation
Original input: `3459413018`  
Transformations:
1. `+100` = 3459413118
2. `+13` = 3459413131
3. `+2` = 3459413133

Total added: `100 + 13 + 2 = 115`

## Result Conversion
Decimal `3459413133` → 32-bit hexadecimal `ce32748d`

## Final Answer
The program prints:  
**`picoCTF{ce32748d}`**
```

