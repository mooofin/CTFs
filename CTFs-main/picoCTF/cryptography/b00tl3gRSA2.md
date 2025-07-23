[muffin@ACERNITO-15 SIDDHARTH U]$ nc jupiter.challenges.picoctf.org 19566
c: 101075261492647475705846882143621410443026811190678427222532866933371984262548164523645264267253856991907352197925213132058116378604272268395133469301692386484064618846083603801095424969199351218800226330109533792918848970359842924206187108394486491858256129703232722617125640212888515738556414408925568280762
n: 132847373125156259932343977635213915972524928132955252710410171244689055967119882856046023959651646927338693050193272682139920378340271136389431658564018642137286490852116205053671657412777270050936464045458875730428028665814808049069929473660859698912728903517964543052019124326697341054167448599169227608613
e: 2140574423915727153952046025646366102613582008764526097657706956900554543254628626516084063985109772422748369028245051685914154134722772174912489608062676987320181086404724288233769590009987778482359516050167752765409541050860172300116518519576688152723889824107418059472615069253363466734513277374279115137
![image](https://github.com/user-attachments/assets/20aa2e53-7d11-4f28-b5e1-99b309192beb)

---

# RSA Encryption, Decryption, and Key Generation – Technical Reference

## Overview

RSA is a widely used public-key cryptosystem based on number theory and modular arithmetic. It uses a pair of keys: a public key for encryption and a private key for decryption.

---

## RSA Encryption

### Process:

1. Convert the message to a numeric form $M$ using a consistent encoding scheme (e.g., ASCII, Unicode, or A1Z26).
2. Use the recipient’s public key, which consists of two integers $n$ and $e$.
3. Compute the ciphertext $C$ using the formula:

   $$
   C \equiv M^e \mod n
   $$

### Example:

* Message: "RSA"
* Encoded as ASCII: `0x525341` → Decimal: `5395265`
* Public key: $n = 6199931$, $e = 101$
* Encrypted:

  $$
  C = 5395265^{101} \mod 6199931 = 4331034
  $$

If the value of $M$ is larger than $n$, split the message into smaller numeric blocks, each less than $n$, and encrypt each block separately.

---

## RSA Decryption

### Process:

1. Use the private key $d$ along with the public modulus $n$.
2. Given ciphertext $C$, compute the plaintext message $M$ using:

   $$
   M \equiv C^d \mod n
   $$

### Example:

* Ciphertext: $C = 4331034$
* Public modulus: $n = 1022117$
* Private key: $d = 5029565$
* Decrypted:

  $$
  M = 4331034^{5029565} \mod 1022117 = 5395265
  $$
* Interpreting 5395265 as hexadecimal: `0x525341` → ASCII: "RSA"

---

## RSA Key Generation

### Steps:

1. Choose two distinct large prime numbers $p$ and $q$.
2. Compute the modulus:

   $$
   n = p \times q
   $$
3. Compute Euler's totient function:

   $$
   \varphi(n) = (p - 1)(q - 1)
   $$
4. Choose an integer $e$ such that:

   * $1 < e < \varphi(n)$
   * $\gcd(e, \varphi(n)) = 1$
5. Compute the modular multiplicative inverse of $e$ modulo $\varphi(n)$ to find $d$:

   $$
   d \equiv e^{-1} \mod \varphi(n)
   $$

   (Use the extended Euclidean algorithm for this step.)

The public key is $(n, e)$, and the private key is $d$.

### Example:

* $p = 1009$, $q = 1013$
* $n = 1009 \times 1013 = 1022117$
* $\varphi(n) = (1009 - 1)(1013 - 1) = 1020096$
* Choose $e = 101$ (coprime with 1020096)
* Compute $d = 767597$, such that:

  $$
  (101 \times 767597) \mod 1020096 = 1
  $$

---



