

Challenge Overview
------------------
Challenge Name: Information
Category: Forensics
Description: Explore the hidden secrets in seemingly simple files by analyzing metadata and encoded information.

------------------

Solution Walkthrough
--------------------

1. Initial File Analysis
------------------------
After downloading the file `cat.jpg`, we verify its type using the following commands:

file cat.jpg
hexdump -C cat.jpg | head
binwalk cat.jpg

This confirms that `cat.jpg` is a valid JPEG file without any obvious embedded files.

--------------------

2. Metadata Inspection
-----------------------
When working with images in CTF challenges, it’s always a good idea to inspect their metadata. Use `exiftool` to analyze the metadata of the image:

exiftool cat.jpg

Key fields to examine include:
- Author
- Copyright
- License
- Comment
- GPS Coordinates

Upon inspection, we find something interesting in the License field:
cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9

This string looks suspicious and resembles Base64 encoding.

--------------------

3. Base64 Decoding
------------------
To decode the Base64 string, we use the following command:

echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d

This outputs:
picoCTF{the_m3tadata_1s_modified}

--------------------

4. Capturing the Flag
---------------------
The decoded string reveals the flag for the challenge:
picoCTF{the_m3tadata_1s_modified}

------------------

Key Learning Points
-------------------
1. Metadata Analysis: Always check EXIF data first when dealing with image-related CTF challenges.
2. Encoding Patterns: Recognize common encoding formats like Base64 for suspicious strings.
3. Flag Structure: PicoCTF flags often contain self-referential hints about the solved problem.
4. Tool Familiarity: Master CLI tools like `exiftool`, `base64`, and `binwalk` for efficient analysis.

------------------


------------------
