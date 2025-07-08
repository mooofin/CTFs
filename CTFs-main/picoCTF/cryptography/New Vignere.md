![screenshot-1751988898](https://github.com/user-attachments/assets/0cd2c1af-7a27-4944-8be4-7b711b269254)



The challenge hint pointed toward the Vigenère cipher Wikipedia page, especially the section on how to break it. There, I learned about the **Kasiski examination**, a technique to estimate the length of the key. I used an online tool (like dCode), and it suggested that the key length could be **3**, **6**, or **9**, with **9** being the most likely.

In a normal Vigenère cipher, once you know the key length, you break the ciphertext into groups — each group uses its own Caesar-like shift. You’d then figure out the shift for each group and recover the key. But in this challenge, that method doesn’t work cleanly because of a twist in the encoding.

The encoding here uses a `b16_encode()` function, which splits each flag character into two smaller characters from a custom 16-letter alphabet. This breaks the usual column structure and makes it harder to analyze letter frequency the normal way.

Still, I used a similar idea. I wrote code to try out different key pairs and see which ones decode cleanly using `b16_decode()`. If the decoded text only contains valid flag characters (like `abcdef0123456789`), there’s a good chance the key part is correct.

For the key parts that didn’t give clear results, I brute-forced all the remaining possibilities using Python’s `itertools.permutations`, while keeping the earlier guesses fixed. When a key produced clean, valid output that passed the checks, I knew I had found the right one.
![screenshot-1751967988](https://github.com/user-attachments/assets/8bf7fb2a-6c45-4288-ac90-b21b43575e3e)

```python
# import string
import string

# constants
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# see caesar cipher for what these are
def b16_decode(cipher):
    dec = ""

    for c in range(0, len(cipher), 2):

        b = ""
        b += "{0:b}".format(ALPHABET.index(cipher[c])).zfill(4)
        b += "{0:b}".format(ALPHABET.index(cipher[c+1])).zfill(4)

        dec += chr(int(b,2))
    
    return dec

def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

# tries to decrypt
def get_key(s, matrix):
    # if we can't go further down
    if len(matrix) == 1:
        # add the last value
        for a in ALPHABET:
            k = str(s) + str(a)
            pt = ""
            for i,c in enumerate(enc):
                pt += unshift(c, k[i%len(k)])

            pt = b16_decode(pt)

            # if the plain text is good then print it
            if all(c in "abcdef0123456789" for c in pt):
                print(pt)
        return
    
    # recursively build key string
    for x in matrix[0]:
        s2 = str(s) + str(x)
        get_key(s2, matrix[1:len(matrix)])

# encrypted text
enc = "bgjpchahecjlodcdbobhjlfadpbhgmbeccbdefmacidbbpgioecobpbkjncfafbe"


keys = []

# create array
[keys.append([]) for i in range(0,32)]

# loop through alphabet twice
for a in ALPHABET:
    for b in ALPHABET:
        # generate key pair
        key = str(a) + str(b)
        
        # store plain text      
        pt = ""

        # unshift all values with key pair
        for i,c in enumerate(enc):
            pt += unshift(c, key[i%len(key)])

        # decode
        pt = b16_decode(pt)

        # loop through decrypted plaintext
        for cur in range(0, len(pt)):

            # check each plaintext char to see if its valid, if it is then add the arrays
            if pt[cur] in "abcdef0123456789":
                keys[cur].append(key)

# print the possible key pairs
for key in keys:
    print(key)

# decrypt the code
get_key("", keys[0:5])
```
