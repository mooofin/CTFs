# The Numbers - PicoCTF 2024

## Challenge Description
> The numbers... what do they mean?  
>  
> **File Provided:** the_numbers.png  
> **Hint:** The flag is in the format `PICOCTF{}`  

This challenge is a reference to the famous quote from *Call of Duty: Black Ops*, where the character Mason is haunted by mysterious numbers. Our goal is to decode these numbers to retrieve the flag.

---

## Solution

Upon analyzing the challenge, we recognize the format of the numbers provided:

```
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }
```

Each number corresponds to a letter in the alphabet using the **A1Z26 cipher** (also called the Letter Number Cipher), where:

- `A = 1`
- `B = 2`
- `C = 3`
- …
- `Z = 26`

By decoding each number:

```
16 -> P
9  -> I
3  -> C
15 -> O
3  -> C
20 -> T
6  -> F

20 -> T
8  -> H
5  -> E
14 -> N
21 -> U
13 -> M
2  -> B
5  -> E
18 -> R
19 -> S
13 -> M
1  -> A
19 -> S
15 -> O
14 -> N
```

This results in the text:  
`PICOCTF{THENUMBERSMASON}`

---

## Flag
```
PICOCTF{THENUMBERSMASON}
```

---

## References

This challenge references the *Call of Duty: Black Ops* storyline, where protagonist **Alex Mason** is constantly asked, *"The numbers, Mason! What do they mean?"*. The numbers were a subliminal programming technique used in the game's plot.
