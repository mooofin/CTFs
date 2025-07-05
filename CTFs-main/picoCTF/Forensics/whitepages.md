![image](https://github.com/user-attachments/assets/12c3aa0a-d5fe-47a5-9733-8af4b8a9d105)


In this challenge, we were given a file named `whitepages.txt` that appeared to be empty. Opening it in a standard text editor showed no visible content, leading to the initial assumption that it might be a blank file. However, in the context of CTFs, "nothing" is rarely just nothing. The challenge name "Whitepages" hinted that the content could be hidden within whitespace.

Suspecting steganography, I examined the file in a hex editor. This revealed two different types of space characters: the standard ASCII space (`0x20`) and the three-byte UTF-8 sequence `0xE2 0x80 0x83`, which corresponds to the Unicode EM SPACE character (U+2003). This discrepancy suggested that these two types of spaces were being used to encode binary data.

The likely encoding was simple but clever: use the regular space (`0x20`) to represent the binary digit `1`, and the EM SPACE (`0xE2 0x80 0x83`) to represent `0`. With this mapping, the entire file was actually a binary message disguised as a wall of invisible whitespace.

To extract the hidden message, I wrote the following Python script:

```python
def convertSpacesToBinary():
    with open('whitepages.txt', 'rb') as f:
        result = f.read()
    result = result.replace(b'\xe2\x80\x83', b'0')  # EM SPACE -> 0
    result = result.replace(b'\x20', b'1')          # ASCII Space -> 1
    result = result.decode()
    return result

def convertFromBinaryToASCII(binaryValues):
    binary_int = int(binaryValues, 2)
    byte_number = (binary_int.bit_length() + 7) // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode('ascii')
    print(ascii_text)

convertFromBinaryToASCII(convertSpacesToBinary())
```

The first function, `convertSpacesToBinary`, reads the file in binary mode to ensure we are working with raw byte data. It then replaces each EM SPACE byte sequence with the character `'0'` and each regular space with `'1'`. This yields a binary string that can be processed further.

The second function, `convertFromBinaryToASCII`, takes this binary string and interprets it as a base-2 integer. It calculates how many bytes are needed to store that integer, converts it into a byte array, and decodes the result into an ASCII string. The final output is the original hidden message.

When I ran the script, it successfully revealed a plaintext message encoded in the file. In typical CTF scenarios, this message would be a flag or a key.

This challenge demonstrates a classic steganographic technique that hides data using subtle differences in characters that appear visually identical. Unicode-based whitespace steganography is especially effective because many text editors and viewers treat these characters the same as regular spaces, making them hard to detect without inspecting the file at the byte level.
![image](https://github.com/user-attachments/assets/6ee6daea-1763-49d8-8cbe-a4e7bf6c15f6)

