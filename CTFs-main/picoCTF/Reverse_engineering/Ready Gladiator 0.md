# Ready Gladiator 0 - Writeup

## Challenge Overview
In this challenge, we participate in a **Core War** match, a competitive programming game where warriors (programs) battle for control of a virtual computer's memory. Our goal is to modify our warrior (Warrior 1) so that it **loses every round** without any ties.

## Understanding the Given Code
We were given the following **warrior code**:

```assembly
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```

### Explanation:
- This program is an **Imp**, an infinite loop that moves itself forward in memory.
- Since both warriors are identical (`Imp Ex` vs. `Imp Ex`), they **always tie** instead of one losing.

### Challenge Condition:
- Our warrior **must lose every round**, no ties allowed.

## Solution: Making Our Warrior Lose
To always lose, we need to create a warrior that **self-destructs** immediately upon execution. The simplest way to do this is using the `DAT` instruction.

### **Modified Warrior Code (Guaranteed Loss)**
```assembly
;redcode
;name Suicide
;assert 1
dat #0
end
```

### **Why This Works?**
- `DAT #0` immediately terminates the program upon execution.
- Since our opponent (`Imp Ex`) continues running while we terminate, we **lose every round** as required.

## Submitting the Solution
### **Steps to Modify and Submit the Warrior**
1. Open the warrior file in a text editor:
   ```bash
   nano imp.red
   ```
   OR
   ```bash
   vim imp.red
   ```

2. Replace the existing code with the **losing warrior**:
   ```assembly
   ;redcode
   ;name Suicide
   ;assert 1
   dat #0
   end
   ```

3. Save and exit:
   - In `nano`: Press `CTRL + X`, then `Y`, then `Enter`.
   - In `vim`: Press `ESC`, type `:wq`, and press `Enter`.

4. Submit the warrior:
   ```bash
   nc saturn.picoctf.net 63323 < imp.red
   ```

## Expected Output
After submitting, the game should report that our warrior **lost all rounds**, fulfilling the challenge requirements.

## output 
;redcode
;name Suicide
;assert 1
dat #0
end

Submit your warrior: (enter 'end' when done)
```
Warrior1:
;redcode
;name Suicide
;assert 1
dat #0
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_7c030e56}
```


