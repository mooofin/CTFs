
---

# Flag Hunters – picoCTF 2025 Writeup

**Category**: Reverse Engineering  
**Points**: Easy  


---

## Challenge Overview

The challenge presents a Python program that prints stylized song lyrics, prompting the user with `Crowd:` at various points. Embedded within the code is a hidden `secret_intro` containing the flag, which is not displayed during normal execution.

---

## Initial Analysis

Upon examining the source code, we identify the following key components:

```python
secret_intro = '''Pico warriors rising...''' + flag + '\n'
song_content = secret_intro + '''[REFRAIN]...'''

def reader(song, startLabel):
    # Parses the song and interprets embedded commands
```

- `secret_intro` contains the flag prepended to the song but is skipped in regular output.
- The `reader` function processes the song line-by-line and handles special commands like `REFRAIN` and `RETURN`.

---

## Vulnerability Discovery

### Observed Weaknesses

1. **Unsanitized Input Handling**  
   - The program accepts direct user input at `Crowd:` and incorporates it into the lyric processing without validation.

2. **Command Injection via Semicolons**  
   - The parser allows multiple commands separated by semicolons (`;`), enabling injection of unintended behavior such as jumps via `RETURN`.

---

## Exploitation Strategy

### Objective

Reveal the hidden flag embedded in the third line of the song (index `3` in a zero-indexed list).

### Technique

Inject the command `;RETURN 3` during the `Crowd:` prompt. This forces the reader to jump directly to the line containing the flag.

---

## Exploitation Steps

1. Connect to the remote challenge server:
   ```bash
   nc verbal-sleep.picoctf.net 59014
   ```

2. At the `Crowd:` prompt, enter:
   ```
   ;RETURN 3
   ```

3. The program responds by displaying the line containing the flag.

---

## Live Interaction Output

```text
└─$ nc verbal-sleep.picoctf.net 59014
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: ;RETURN 3

Echoes in memory, packets in trace,
Digging through the remnants to uncover with haste.
Hex and headers, carving out clues,
Resurrect the hidden, it's forensics we choose.
Disk dumps and packet dumps, follow the trail,
Buried deep in the noise, but we will prevail.

We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd:
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_05182f4f}
```

---

## Explanation

- The user input is interpreted as part of the song script.
- Semicolon (`;`) acts as a command separator.
- `RETURN 3` jumps the execution to line 3, which contains the flag.

---

## Mitigation Recommendations

To prevent such vulnerabilities in similar applications:

1. **Input Sanitization**  
   Disallow or escape control characters such as `;`:
   ```python
   if ';' in user_input:
       print("Invalid input.")
       continue
   ```

2. **Strict Command Parsing**  
   Ensure only a predefined set of commands is allowed:
   ```python
   allowed_commands = {'REFRAIN', 'END'}
   if command not in allowed_commands:
       print("Command not recognized.")
   ```

---

## Flag

```
picoCTF{70637h3r_f0r3v3r_05182f4f}
```

---

