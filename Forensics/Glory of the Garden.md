# Writeup: Extracting Hidden Data from an Image using a Hex Editor

## Challenge Description
We are given a file that appears to be just a photo of a garden. However, the hint suggests using a hex editor, indicating that hidden data might be embedded in the file.

## Solution Steps

### Step 1: Download the File
First, I downloaded the provided image file and inspected it. At first glance, it seemed like a normal picture, but based on the hint, I suspected there might be hidden data.

### Step 2: Open the File in a Hex Editor
Since the hint mentioned a hex editor, I used an online hex editor to analyze the image. I loaded the image into the editor using the "Open file" button.

### Step 3: Search for the Flag Format
To quickly locate any hidden data, I used the search functionality in the hex editor. I searched for the common CTF flag format (`picoCTF{}`) and pressed Enter.

### Step 4: Extract the Flag
The search function highlighted a part of the hex dump where the flag was embedded. I clicked on the result and successfully retrieved the hidden flag.

## Conclusion
This challenge demonstrated how information can be hidden inside files and how a hex editor can be used to extract it. Always check for embedded data when working with CTF challenges involving files!

**Flag:** `picoCTF{more_than_m33ts_the_3y33dd2eEF5}`
