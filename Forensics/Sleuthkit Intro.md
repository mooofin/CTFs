

## **Challenge Details**
- **Author:** LT 'syreal' Jones
- **Category:** Forensics
- **Description:**
  - Download the disk image and use `mmls` to find the size of the Linux partition.
  - Connect to the remote checker service to verify the answer and get the flag.
  - If using the webshell, extract the disk image into `/tmp` instead of the home directory.

## **Solution Steps**

### **Step 1: Download and Extract the Disk Image**
1. Download the disk image from the challenge.
2. Move to the `Downloads` directory or `/tmp` (if using the webshell):
   ```sh
   cd ~/Downloads   # Or cd /tmp
   ```
3. If the file is compressed, extract it:
   ```sh
   tar -xvf disk_image.tar  # If it's a tar archive
   unzip disk_image.zip      # If it's a zip file
   ```

### **Step 2: Analyze the Disk Image Using `mmls`**
`mmls` (from The Sleuth Kit) is used to analyze the partition structure:
```sh
mmls disk.img
```
#### **Output:**
```
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```
- The **Linux partition (0x83)** has a **length of 2,027,752 sectors**.
- Each sector is **512 bytes**, but the challenge asks for the sector count.

### **Step 3: Submit the Answer to the Remote Checker**
Connect to the provided checker service using `nc`:
```sh
nc challenge_host challenge_port
```
_(Replace `challenge_host` and `challenge_port` with the values from the challenge.)_

The prompt asks:
```
Enter the partition size:
```
Enter the **Linux partition size (in sectors):**
```
0000202752
```

### **Step 4: Get the Flag**
If correct, the server responds with the flag:
```
Great work!
picoCTF{mm15_f7w!}
```

## **Alternative Verification Using `fdisk`**
If `mmls` is unavailable, you can also use:
```sh
fdisk -l disk.img
```
It will display partition details, from which you can extract the Linux partition size.

## **Flag**
```
picoCTF{mm15_f7w!}
```

---

### **Final Notes**
- The **partition size was directly available in the `mmls` output** under the "Length" column.
- If the challenge required the size in bytes, we would multiply sectors by 512:
  ```sh
  echo $((202752 * 512))  # Convert to bytes
  ```
- Using `mmls` is an efficient way to analyze partitions in forensic challenges.

This concludes the solution write-up for the challenge! 🚀

