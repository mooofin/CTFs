In this challenge, I used the Pollard's p-1 factorization method to break RSA and recover a hidden flag. The modulus n and ciphertext c were provided, and I suspected that one of the primes (p or q) used in generating n was weak in the sense that p-1 or q-1 was composed mostly of small prime factors (B-smooth), making it vulnerable to Pollard’s p-1 attack. I implemented the attack using Python and the gmpy2 library for efficient number-theoretic operations, along with tqdm to track progress. The attack works by choosing a bound B (determined by how many small primes I use), exponentiating a base with a product of these primes modulo n, and checking for a non-trivial greatest common divisor between n and the result minus one. After increasing the number of primes (num_primes) to 7000 to widen the factor base, the algorithm successfully factored n into two large primes p and q. With these, I calculated φ(n) using the least common multiple of p-1 and q-1, and then derived the private key d as the modular inverse of the public exponent e. I decrypted the ciphertext using modular exponentiation and finally extracted the plaintext message, which revealed the flag: picoCTF{p0ll4rd_f4ct0r1z4at10n_FTW_376ebfe7}
```python
import binascii
import gmpy2
import math
from tqdm import tqdm


def _primes_yield_gmpy(n):
    p = i = 1
    while i <= n:
        p = gmpy2.next_prime(p)
        yield p
        i += 1


def primes(n):
    return list(_primes_yield_gmpy(n))


def pollard_P_1(n, progress=True, num_primes=2000):
    """Pollard P1 implementation"""
    z = []
    logn = math.log(int(gmpy2.isqrt(n)))
    prime = primes(num_primes)

    for j in range(0, len(prime)):
        primej = prime[j]
        logp = math.log(primej)
        for i in range(1, int(logn / logp) + 1):
            z.append(primej)

    try:
        for pp in tqdm(prime, disable=(not progress)):
            i = 0
            x = pp
            while 1:
                x = gmpy2.powmod(x, z[i], n)
                i = i + 1
                y = gmpy2.gcd(n, x - 1)
                if y != 1 and y != n:
                    p = y
                    q = n // y
                    return p, q
                if i >= len(z):
                    return 0, None
    except TypeError:
        return 0, None


# New RSA values
e = 0x10001

n = int(
    "b03ea698ce2b51fb00e11e6fbaf1e5373dc5b0c70eb2b14a36d21e8667be8774"
    "eee51f6050a10237f6b24f21204fc8013681e7ed72ed051188f3274aae8f1de0"
    "d39389b514c196fa82c98a270bfabefd044da8c687b0e114ebbde82536c0709a"
    "c5ad81bfe0077e9d9b798ad5abecee52767e68f8060c45936521fd93893102eb"
    "1676f2ff41324a7a6b3dff2e830538e06d25934e9f14bf6b40ab5674fe648e31"
    "4bf06f84282f5ef52bc1401de3a42eb66e64bcdadd2674348e5bdb7016feda44"
    "d719af387a948ad81cbaed10213dd930fc7bc7677d8c4cdab0645d0ff15e6ad6"
    "ca37135942c3be08f23e7be0992c8b3370dcdc31045e086d823107fb2e443dc9",
    16
)

c = int(
    "a913a96e215b5aa79c702d27fa375c73d06787639c4131fb32877cafefaa8faf"
    "70e15f6a17ef2a9a6f5310b157cb287b740e77cb5385081d1853a9104bc16357"
    "b259fa2d146bd87398d4ef6f1c078289812952c67792cf9cd745049aeb9d4ab4"
    "dff2825a9c0b3381f19b2a67164f9d4de33c25f98bc2f224feb5507b531e1a1c"
    "7be5ed2d8ddd01f3fae37245e8cf99c75a21848993d445e1d6d69d555a3e6cc8"
    "055704fdde88df9084bda3ea65a9384fa64bf8df4d88946449526320c15d4d2d"
    "871638070489adf3f8c95caffeab40b0d137a9319be20cdf6ebbaf037f62093d"
    "9bd33edd4ffd7e1929b9ab06252956fd85250a0515ef2b4e035017be5702cdd3",
    16
)

# You can adjust this value if it fails
num_primes = 10000
p, q = pollard_P_1(n, num_primes=num_primes)

if q is None:
    print("Pollard p-1 Factorization Attack Failed. Try increasing `num_primes`.")
else:
    print("Success:")
    print("p =", p)
    print("q =", q)

    n = p * q
    m = gmpy2.lcm(p - 1, q - 1)
    d = pow(e, -1, m)
    m = pow(c, d, n)

    try:
        print("Flag:", binascii.unhexlify(hex(m)[2:]).decode())
    except:
        print("Flag (raw):", hex(m))
```
