# **CTF Writeup: Decrypting the Encrypted Blockchain**

## **Challenge Name:** Block Decryption  
## **Category:** Cryptography  
## **Difficulty:** Medium  

---

## **Challenge Description**  
We were provided with an encrypted blockchain string along with an encryption key. Our goal was to **decrypt the data** and extract the hidden flag.

---

## **Step 1: Understanding the Encryption Scheme**  
The encryption used in this challenge appeared to follow a simple **XOR-based block cipher** with padding. The encryption script revealed that:  
- The plaintext blockchain data was **modified** by inserting additional text before encryption.  
- The encryption key was **SHA-256 hashed** before being applied.  
- Blocks of 16 bytes were XORed against the hashed key to generate the ciphertext.

---

## **Step 2: Given Information**  
We were provided with:
1. **The encryption key (32 bytes)**
2. **The encrypted blockchain data (ciphertext)**

Example of given key and ciphertext:
```python
key = b'\xe8\xa6\xde\xcf\\\xbe\xf8\xd8\x81\xc4y\x19\xa5\x92E\x0e\x1f\xa6\xb4\n\xcbY\x1dI\x891\x0e\x8c\xcd\x8f\r\x80'

ciphertext = b'x\xa9\xcaR^\'J\x86\xdd\xb7\x00]...'
```

---

## **Step 3: Decrypting the Blockchain**  
We used a **reverse XOR operation** with the same hashed key to decrypt the data. The process involved:
1. **Extracting the encryption key**
2. **Hashing it using SHA-256**
3. **Performing XOR on the ciphertext**
4. **Removing the padding and inserted text to retrieve the original blockchain**

Python script for decryption:
```python
import hashlib

def xor_bytes(a, b):
    """Perform XOR operation between two byte sequences."""
    return bytes(x ^ y for x, y in zip(a, b))

def unpad(data):
    """Remove padding from decrypted data."""
    if len(data) == 0:
        return data
    padding_length = data[-1]
    return data[:-padding_length]

def decrypt(ciphertext, key):
    """Decrypt the given ciphertext using XOR decryption."""
    key_hash = hashlib.sha256(key).digest()  # Generate SHA-256 hash of the key
    block_size = 16
    decrypted = b''

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        decrypted += xor_bytes(block, key_hash)

    # Try to remove padding
    try:
        decrypted = unpad(decrypted)
    except:
        pass  # Ignore if no padding was used

    return decrypted.decode('utf-8', errors='ignore')

# Given Key and Encrypted Blockchain Data
key = b'\xe8\xa6\xde\xcf\\\xbe\xf8\xd8\x81\xc4y\x19\xa5\x92E\x0e\x1f\xa6\xb4\n\xcbY\x1dI\x891\x0e\x8c\xcd\x8f\r\x80'
ciphertext = b"x\xa9\xcaR^'J\x86\xdd\xb7\x00]\x07\xd3\xb4ip\xf8\x9b\x08_p\x1a\xd7\xdc\xb2W\x00\x01\x86\xb4<,\xaf\xcaRW\"K\xd3\xda\xb5\x07TZ\x86\xe4;\x7f\xaf\xcfWTuN\x83\xdb\xe2\x03\x04T\xd7\xe3oe\xad\xca\x05V\"J\xd3\xd2\xe6VS\x06\x8a\xefi*\xa8\x9f\x01\x04\"O\x8b\xd3\xb4TRR\x8a\xe2o\x7f\xf9\xc9\x05\x07u\x18\xd3\xd9\xe1SVV\x82\xe2k}\xa8\xc8P\x00sM\x87\x8b\xb2QU\x00\x83\xe0h)\xb0\xca\x01\x02'K\x80\x8e\xb4UP\x00\x81\xe0i|\xfe\x9b\x04\x02sL\xd4\xdc\xe2[WZ\xd1\xe0<)\xa5\x8aX\x05.?\xe6\xac\xfc\x00\t\x0c\xd1\xbd\x01{\xce\xa8Y0(.\xd0\xbe\xb6\x13\x06;\xed\x8e\x0b\"\xd0\xcaCRx\x1f\xfa\xb5\xf6!\x1f\x0e\xf8\x8c$\n\xd6\xa5R^r\x19\xd3\x8f\xe2Q\x18V\x8a\xb2nx\xa8\xcd\t\x02vD\x84\xde\xb4\x04\x06R\xd0\xe3kp\xfb\x99\x04Wy\x18\xd1\xdb\xe5Z]N\x82\xe6i)\xaa\x98\x01^\"H\x84\xdf\xe3\x04PS\x8a\xef8q\xac\xcdRR\"J\x85\xdc\xe4R\x07Z\x85\xb0=+\xa4\xc2SVs\x1e\x80\xd2\xb2P\x06\x06\x80\xeff~\xaa\xc3\x06\x00$I\x83\x8b\xe5P\x06S\x9f\xe6np\xa8\xcc\x05Q\"\x1f\x87\xdf\xb3\x01U\x01\x83\xe5l~\xa5\xca\x03S%D\xd7\xdc\xb2W\x06\x01\xd3\xe0j+\xa5\xcd\x02\x00 J\x84\xd2\xb7[VU\xd3\xb0h.\xaf\xcc\x02Q#D\xd7\x89\xe3R\x00\x05\x80\xd4\\"

#  Decrypt the blockchain
decrypted_text = decrypt(ciphertext, key)
print("Decrypted Blockchain:", decrypted_text)
```

---

## **Step 4: Extracting the Flag**  
After decryption, we found a **flag in the decrypted blockchain data**:  
```
Decrypted Blockchain: 040c8f6470b8dab78ea991fe655eb4bbd20c1c7a02e1942e725f24211eaa7e51-0040c6a8a46e897b5e0bc39936718417d34a4da3f135045552af215a530c166a-00df72d375c3674ca5d20f6e929c6ba8picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_c83eaee3}58d00578d78643fc1b558fc518dc1b88-007a7b08c465df5089f917c4c676c0b97fcc98b02b2852ce2986797fe51ab2c0-0085647cc554c0b13268025d8e655cba64c873fa6680936af6f2637b8ecd0ef2
                             
picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_c83eaee3}
```
This confirmed that our decryption was successful!

---

## **Conclusion**  
🔹 **Key Takeaways:**  
✅ XOR encryption can be reversed using the same key.  
✅ Hashing the key before encryption adds a layer of complexity.  
✅ Padding and inserted data must be carefully removed post-decryption.  

---

## **Final Flag:**  
```
picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_c83eaee3}
```

