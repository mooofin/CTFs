# 🏴‍☠️ ASCII & Hex - CTF Writeup 🏴‍☠️

## Challenge Overview 📜
We were given a hint that a word starts with `0x70` in hexadecimal and asked to determine what it starts with in ASCII. Sounds simple, right? But as any seasoned CTF player knows, even the easiest-looking challenges can have twists!

## Solution 💡
### Step 1: Understanding Hexadecimal 
Hexadecimal (or "hex") is a base-16 numbering system commonly used in computing. Each hex digit represents 4 bits, and two hex digits together (like `0x70`) represent a single byte.

### Step 2: Converting Hex to ASCII 
The `0x70` notation is a hexadecimal representation of a number. To see what it translates to in ASCII, we can use Python:
```python
print(chr(0x70))
```
Running this gives us:
```
p
```
So, the word starts with **'p'** in ASCII!

## CTF Takeaways 🎯
- Always recognize `0x` as a hex number.
- The `chr()` function in Python is your best friend for converting hex to ASCII.
- ASCII tables can be super handy for quick lookups.

## Final Answer 🏆
The word starts with **'p'**! If this were a CTF challenge, I'd be looking for a flag like:
```
picoCTF{something_cool_here}
```



