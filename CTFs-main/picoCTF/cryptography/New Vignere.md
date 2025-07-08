![screenshot-1751988898](https://github.com/user-attachments/assets/0cd2c1af-7a27-4944-8be4-7b711b269254)



The challenge hint pointed toward the Vigenère cipher Wikipedia page, especially the section on how to break it. There, I learned about the **Kasiski examination**, a technique to estimate the length of the key. I used an online tool (like dCode), and it suggested that the key length could be **3**, **6**, or **9**, with **9** being the most likely.

In a normal Vigenère cipher, once you know the key length, you break the ciphertext into groups — each group uses its own Caesar-like shift. You’d then figure out the shift for each group and recover the key. But in this challenge, that method doesn’t work cleanly because of a twist in the encoding.

The encoding here uses a `b16_encode()` function, which splits each flag character into two smaller characters from a custom 16-letter alphabet. This breaks the usual column structure and makes it harder to analyze letter frequency the normal way.

Still, I used a similar idea. I wrote code to try out different key pairs and see which ones decode cleanly using `b16_decode()`. If the decoded text only contains valid flag characters (like `abcdef0123456789`), there’s a good chance the key part is correct.

For the key parts that didn’t give clear results, I brute-forced all the remaining possibilities using Python’s `itertools.permutations`, while keeping the earlier guesses fixed. When a key produced clean, valid output that passed the checks, I knew I had found the right one.
![screenshot-1751967988](https://github.com/user-attachments/assets/8bf7fb2a-6c45-4288-ac90-b21b43575e3e)

