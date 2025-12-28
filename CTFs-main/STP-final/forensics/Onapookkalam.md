# Onapookkalam Challenge Writeup

## Challenge Overview

While preparing for Onapookkalam, notes were recorded on a mobile device. The phone was suspected to be tampered with, potentially having data modified or deleted.

**Objectives:**
- **Note Retrieval**: Extract specific information from saved notes (flagPart1)
- **Database Analysis**: Identify a specific string that was modified and deleted from Realm DB (flagPart2)

**Required Output Format**: `flag{flagPart1_flagPart2}`

---

## Investigation Process

### Initial File Extraction

After extraction, numerous files were discovered:

![Extracted Files](https://github.com/user-attachments/assets/e1a5f1d0-5f0f-488d-9375-dd48f4fcffb4)

### Notes Recovery

The challenge focused on recovering notes. During the search for notes files, one file was found with a base64-encoded name:

![Base64 Named File](https://github.com/user-attachments/assets/1a215bc4-4671-4a5b-b273-848765ba7706)

This directory contained the following files:

![Directory Contents](https://github.com/user-attachments/assets/27b3aae7-addc-4219-87a2-ad474d6377bf)

### Flutter App Analysis

Further exploration revealed this was about recovering data from a Flutter app:

![Flutter App Evidence 1](https://github.com/user-attachments/assets/609ffe11-3e24-41e1-a236-454dc7a19d34)

![Flutter App Evidence 2](https://github.com/user-attachments/assets/e77da1a7-252d-4064-b778-1506f593c1d1)

### Source Code Discovery
<img width="747" height="356" alt="image" src="https://github.com/user-attachments/assets/8b825b13-aca7-499a-a441-50261371ede8" />

Since Flutter uses Python (via Flet framework), i  searched for Python files containing the APK logic. The main application file was found:

![Python File Location](https://github.com/user-attachments/assets/ae9efd2b-5dac-4e99-a5cb-981491f8d7ee)

### Encryption Implementation

The discovered Python code revealed the notes app's encryption scheme:

```python
import flet as ft
import datetime, random, os, string

def key_scheduling(key):
    sched = [i for i in range(0, 256)]
    i = 0
    for j in range(0, 256):
        i = (i + sched[j] + key[j % len(key)]) % 256
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
    return sched

def stream_generation(sched):
    stream = []
    i = 0
    j = 0
    while True:
        i = (1 + i) % 256
        j = (sched[i] + j) % 256
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        yield sched[(sched[i] + sched[j]) % 256]

def encrypt(text, key):
    text = [ord(char) for char in text]
    key = [ord(char) for char in key]
    sched = key_scheduling(key)
    key_stream = stream_generation(sched)
    ciphertext = ""
    for char in text:
        enc = str(hex(char ^ next(key_stream))).lower()
        ciphertext += enc
    return ciphertext

def storeData(page, content):
    app_data_path = os.getenv("FLET_APP_STORAGE_DATA")
    fileName = f"{datetime.datetime.now().strftime("%d%m%Y%H%M%S%f")}"
    my_file_path = os.path.join(app_data_path, fileName)
    key = "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(16)
    )
    encText = encrypt(content, key)
    page.client_storage.set(fileName, key)
    with open(my_file_path, "w") as f:
        f.write(encText)
    page.open(ft.SnackBar(ft.Text(f"File saved to App Data Storage!")))

def main(page: ft.Page):
    def saveNote(e):
        data = inputBox.value
        if data != "":
            storeData(page, data)
        else:
            page.open(ft.SnackBar(ft.Text("Empty content!")))
    
    appBar = ft.AppBar(title=ft.Text("Notes App"))
    inputBox = ft.TextField(hint_text="Enter some text...", multiline=True, min_lines=3)
    page.appbar = appBar
    page.add(inputBox)
    page.add(
        ft.ElevatedButton(text="Save Note", on_click=saveNote, style=ft.ButtonStyle())
    )

ft.app(main)
```


The application allows users to create and save encrypted notes with the following workflow:
When a user enters text and clicks "Save Note", the application generates a unique filename based on the current timestamp (format: DDMMYYYYHHMMSSμs). It then creates a random 16-character encryption key consisting of letters and digits. The note content is encrypted using a custom implementation of the RC4 stream cipher algorithm, which involves two main phases: key scheduling (which initializes a 256-byte state array based on the encryption key) and stream generation (which produces a pseudo-random keystream). The encryption process XORs each character of the plaintext with the corresponding keystream byte and converts the result to hexadecimal format. The encrypted text is stored in a file within the app's data directory, while the encryption key is separately stored in the client storage using the filename as the identifier. This design means that to decrypt any saved note, you need both the encrypted file and its corresponding encryption key from the client storage, making the encryption key essential for data recovery.


so I wrote a Python script that:
1. Implemented the RC4 decryption algorithm (mirroring the encryption code)
2. Parsed the hex-encoded ciphertext
3. XORed each byte with the keystream to recover plaintext

```python
#!/usr/bin/env python3
"""Simple decryption script for the notes challenge"""

import os

def key_scheduling(key):
    sched = [i for i in range(0, 256)]
    i = 0
    for j in range(0, 256):
        i = (i + sched[j] + key[j % len(key)]) % 256
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
    return sched

def stream_generation(sched):
    i = 0
    j = 0
    while True:
        i = (1 + i) % 256
        j = (sched[i] + j) % 256
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        yield sched[(sched[i] + sched[j]) % 256]

def decrypt(ciphertext, key):
    key = [ord(char) for char in key]
    sched = key_scheduling(key)
    key_stream = stream_generation(sched)
    
    # Parse hex values from format: 0xXX0xYY0xZZ...
    hex_values = []
    i = 0
    while i < len(ciphertext):
        if ciphertext[i:i+2] == '0x':
            j = i + 2
            while j < len(ciphertext) and ciphertext[j:j+2] != '0x':
                j += 1
            hex_val = ciphertext[i:j]
            hex_values.append(int(hex_val, 16))
            i = j
        else:
            i += 1
    
    plaintext = ""
    for encrypted_byte in hex_values:
        decrypted_byte = encrypted_byte ^ next(key_stream)
        plaintext += chr(decrypted_byte)
    
    return plaintext

# Keys from client storage
KEYS = {
    "15052025175732777833": "1OmIyq5YT50YlWB0",
    "15052025175747121993": "oIdeaSz9iySlAmKJ",
    "15052025175936114230": "YKnQqnrzfTIM9HLu",
    "15052025180002742685": "RhjZrO2JGKQLamST",
    "15052025175724299736": "SkZFksurgEq3Tdhe",
    "15052025175950593733": "M52JUgdj9r6kkVg4",
    "15052025175944264611": "lunMORQQjKhX9u5H",
}

print("\n" + "="*70)
print("DECRYPTING ALL NOTES")
print("="*70 + "\n")

for filename, key in KEYS.items():
    if os.path.exists(filename):
        print(f"\n{'='*70}")
        print(f"File: {filename}")
        print(f"Key: {key}")
        print(f"{'='*70}")
        
        with open(filename, 'r') as f:
            ciphertext = f.read()
        
        try:
            plaintext = decrypt(ciphertext, key)
            print(f"Decrypted content:\n{plaintext}")
        except Exception as e:
            print(f"Error decrypting: {e}")
        
        print(f"{'='*70}\n")
    else:
        print(f"File not found: {filename}")

print("\n✓ Decryption complete!\n")
```
```bash
15052025175732777833: "well this was easy"
15052025175747121993: "i'll give you the first part of the flag :)"
15052025175936114230: "first part of the flag: w311_7h47_p4r7_w45_345y"
15052025180002742685: "f4k3_f14g"
15052025175724299736: "hello there"
15052025175950593733: "boop"
15052025175944264611: "hehehe"
```

After an hour of going through all the files i found this snapshots folder  ( i tried organising the files by images , txt , png etc and came across this title 0 

<img width="825" height="161" alt="image" src="https://github.com/user-attachments/assets/cb607acb-6f7a-42ba-a6be-79caa263524b" />

<img width="887" height="986" alt="image" src="https://github.com/user-attachments/assets/242d30cf-a024-42a5-a9a4-b8188a6d7b5f" />

