# Best Stuff - Cheap Stuff, Buy Buy Buy...

## Challenge Description

**Challenge Name:** Best Stuff - Cheap Stuff, Buy Buy Buy...
**Instance:** `nc mercury.picoctf.net 24851`

The shop is open for business! Can you find a way to get the flag?

---

## Initial Interaction with the Market

Upon connecting to the server, we are presented with a market interface:

```
Welcome to the market!
=====================
You have 40 coins
   Item         Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
```

- We start with 40 coins.
- The flag ("Fruitful Flag") costs 100 coins.
- We do not have enough money to buy it directly.

### Attempting to Buy the Flag

```
Choose an option: 
2
How many do you want to buy?
1
Not enough money.
```

We need to find a way to get more coins.

---

## Finding the Exploit

### Checking the Selling Menu

```
Choose an option: 
3
Your inventory
(0) Quiet Quiches       10      0
(1) Average Apple       15      0
(2) Fruitful Flag       100     0
What do you want to sell? 
2
How many?
1
Hey you don't have that many on your cart! What kind of scam is this?
```

Since we don't own the item, we cannot sell it.

### Trying a Negative Purchase

```
Choose an option: 
0
How many do you want to buy?
1
You have 30 coins
```

- We buy 1 Quiet Quiche for 10 coins, reducing our balance to 30 coins.

```
Choose an option: 
1
How many do you want to buy?
-5
You have 105 coins
```

- Entering a negative number for purchasing **adds coins instead of deducting them!**
- This integer manipulation allows us to gain enough money to buy the flag.

---

## Buying the Flag

```
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 53 51 50 98 99 100 57 56 125]
```

The flag is displayed as an array of ASCII values.

---

## Decoding the Flag

We convert the ASCII values into characters using Python:

```python
ascii_values = [112, 105, 99, 111, 67, 84, 70, 123, 98, 52, 100, 95, 98, 114, 111, 103, 114, 97, 109, 109, 101, 114, 95, 53, 51, 50, 98, 99, 100, 57, 56, 125]
flag = ''.join(chr(i) for i in ascii_values)
print(flag)
```

### Flag Output:

```
picoCTF{b4d_brogrammer_532bcd98}
```

---

## Conclusion

This challenge exploited an **integer manipulation bug** in the purchase system, allowing negative numbers to add coins instead of subtracting them. This classic **integer underflow** bug is common in improperly validated user inputs in CTF challenges and real-world applications.

Lessons learned:
- Always validate user input.
- Prevent negative values where they shouldn't exist.
- Check integer overflows/underflows in financial transactions.

---

## Final Flag:

**`picoCTF{b4d_brogrammer_532bcd98}`**
