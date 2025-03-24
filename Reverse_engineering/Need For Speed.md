text
# Need for Speed: Comprehensive Writeup

## Problem Analysis
**Key Observations:**
- Program terminates with "Not fast enough" message
- Contains SIGALRM signal handling (alarm timer)
- Key generation process is intentionally slowed down
- Goal: Bypass time constraints to reveal the flag

---

## Solution Methods

### 1. SIGALRM Signal Ignorance (Primary Method)
**Steps:**
gdb ./need-for-speed
(gdb) handle SIGALRM ignore
(gdb) run

text

**Mechanism:**
- Prevents SIGALRM (signal 14) from triggering program termination
- Bypasses security check: `if (local_10 != 0) { explode_bomb(); }`

---

### 2. Function Bypass Technique
**Steps:**
(gdb) break set_timer
(gdb) run
(gdb) return # Skip timer setup
(gdb) continue

text

**Assembly Insight (Ghidra):**
0x00000883 <+15>: call 0x700 <set_timer>

text

---

### 3. Direct Function Execution
**Steps:**
(gdb) break main
(gdb) call (int) get_key()
(gdb) call (int) print_flag()

text

**Decompiled Code (Ghidra):**
void main() {
set_timer();
get_key();
print_flag();
}

text

---

### 4. Cryptographic Bypass (Advanced)
**Steps:**
1. Find XOR key in Ghidra: `0xe99d7887`
2. Direct decryption:
(gdb) call (int) decrypt_flag(0xe99d7887)
(gdb) call (int) print_flag()

text

**XOR Encryption Logic:**
encrypted_flag[local_c] ^ (byte)(param_1 >> (local_c % 4) * 8);

text

---

## Technical Concepts

### Signal Handling
- SIGALRM = Timer expiration (Signal 14)
- Default action: Process termination
- Critical functions: `alarm()`, `setitimer()`

### Anti-Debugging Prevention
// Real-world protection example
if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
exit(1); // Debugger detected
}

text

---

## Prevention Techniques
1. **Time Validation**
clock_gettime(CLOCK_MONOTONIC, &end);
if ((end.tv_sec - start.tv_sec) > TIMEOUT) explode();




---

## Flag
`PICOCTF{Good job keeping bus #24c43740 speeding along!}`

---
