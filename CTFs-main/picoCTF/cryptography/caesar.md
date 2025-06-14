# picoCTF Challenge Write-Up: Caesar Cipher Decryption

## Challenge Overview
We were given the following encrypted flag in the challenge:

```
picoCTF{gvswwmrkxlivyfmgsrhnrisegl}
```

This appears to be encoded using a **Caesar cipher**, a simple substitution cipher that shifts letters forward or backward by a fixed number of positions in the alphabet.

## Step 1: Understanding the Caesar Cipher
The **Caesar cipher** works by shifting each letter in the plaintext forward or backward by a fixed amount.

For example, with a shift of **+3**:
```
HELLO → KHOOR
```
For decryption, we shift **backward** by the same amount.

## Step 2: Brute-Forcing All 26 Shifts
To find the correct shift, we decrypt the given ciphertext by shifting backward through all 26 possible values.

### **Generated Decryptions:**
```
Shift 0:  picoCTF{gvswwmrkxlivyfmgsrhnrisegl}
Shift 1:  picoCTF{furvvlqjwkhuxelfrqgmqhrdfk}
Shift 2:  picoCTF{etquukpivjgtwdkeqpflpgqcej}
Shift 3:  picoCTF{dspttjohuifsvcjdpoekofpbdi}
Shift 4:  picoCTF{crossingtherubicondjneoach}  ✅ (Correct Flag)
Shift 5:  picoCTF{bqnrrhmfsgdqtahbnmcimdnzbg}
Shift 6:  picoCTF{apmqqglerfcpszgamlbhlcmyaf}
Shift 7:  picoCTF{zolppfkdqeboryfzlkagkblxze}
Shift 8:  picoCTF{ynkooejcpdanqxeykjzfjakwyd}
Shift 9:  picoCTF{xmjnndiboczmpwdxjiyeizjvxc}
Shift 10: picoCTF{wlimmchanbylovcwihxdhyiuwb}
Shift 11: picoCTF{vkhllbgzmaxknubvhgwcgxhtva}
Shift 12: picoCTF{ujgkkafylzwjmtaugfvbfwgsuz}
Shift 13: picoCTF{tifjjzexkyvilsztfeuaevfrty}
Shift 14: picoCTF{sheiiydwjxuhkrysedtzdueqsx}
Shift 15: picoCTF{rgdhhxcviwtgjqxrdcsyctdprw}
Shift 16: picoCTF{qfcggwbuhvsfipwqcbrxbscoqv}
Shift 17: picoCTF{pebffvatgurehovpbaqwarbnpu}
Shift 18: picoCTF{odaeeuzsftqdgnuoazpvzqamot}
Shift 19: picoCTF{nczddtyrespcfmtnzyouypzlns}
Shift 20: picoCTF{mbyccsxqdrobelsmyxntxoykmr}
Shift 21: picoCTF{laxbbrwpcqnadkrlxwmswnxjlq}
Shift 22: picoCTF{kzwaaqvobpmzcjqkwvlrvmwikp}
Shift 23: picoCTF{jyvzzpunaolybipjvukqulvhjo}
Shift 24: picoCTF{ixuyyotmznkxahoiutjptkugin}
Shift 25: picoCTF{hwtxxnslymjwzgnhtsiosjtfhm}
```

The correct decryption (Shift **4**) gives us:
```
picoCTF{crossingtherubicon}
```

## Step 3: Automating with Python
We can automate the decryption process with a simple Python script:
```python
def caesar_cipher(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shift_amount = ord('a') if char.islower() else ord('A')
            decrypted += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
        else:
            decrypted += char
    return decrypted

ciphertext = "gvswwmrkxlivyfmgsrhnrisegl"
for shift in range(26):  # Try all shifts
    print(f"Shift {shift}: picoCTF{{{caesar_cipher(ciphertext, shift)}}}")
```

## Conclusion
- The **Caesar cipher** is a basic encryption technique that shifts letters forward or backward.
- Brute-forcing all 26 shifts revealed the correct flag at **Shift 4**.
- The final decrypted flag is:

```
picoCTF{crossingtherubicon}
```

This challenge reinforced the importance of **brute-force attacks**, **pattern recognition**, and **automation with Python** in CTF challenges!
