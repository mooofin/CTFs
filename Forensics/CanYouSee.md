# Writeup: Extracting Hidden Data from Image Metadata

## Challenge Description
We are given a ZIP file (`unknown.zip`). After extracting it, we find an image file named `ukn_reality.jpg`. The goal is to analyze the image for hidden information.

## Solution Steps

### Step 1: Extract the ZIP File
After downloading the `unknown.zip`, I extracted its contents and found an image file:

```sh
┌──(sid㉿kali)-[~/Downloads]
└─$ dir
ukn_reality.jpg  unknown.zip
```

### Step 2: Check Image Metadata with `exiftool`
Using `exiftool`, I examined the metadata of `ukn_reality.jpg`:

```sh
exiftool ukn_reality.jpg
```

This revealed various metadata fields, including an interesting `Attribution URL` field containing a base64-encoded string:

```
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==
```

### Step 3: Decode the Hidden Base64 String
To decode the base64 string, I used:

```sh
echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==" | base64 -d
```

This returned the flag:

```
picoCTF{ME74D47A_HIDD3N_d8c381fd}
```

### Conclusion
The flag was hidden in the image metadata as a base64-encoded string. By using `exiftool` to extract metadata and `base64 -d` to decode it, I successfully retrieved the flag.

**Flag:** `picoCTF{ME74D47A_HIDD3N_d8c381fd}`

