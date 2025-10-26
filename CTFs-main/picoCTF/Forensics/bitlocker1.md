We're given a BitLocker encrypted disk image (`bitlocker-1.dd`, 100 MB). Need to decrypt it and get the flag.



I installed the required tools : ) 

```bash

sudo pacman -S git base-devel openssl zlib hashcat wget ntfs-3g
yay -S dislocker


cd ~
git clone https://github.com/openwall/john.git
cd john/src
./configure && make -sj$(nproc)
```



I used `bitlocker2john` to extract the password hash:

```bash
cd ~/john/run
python3 bitlocker2john.py "/mnt/c/Users/SIDDHARTH U/bitlocker-1.dd"
```

This gave me 4 hashes. I saved the user password hashes (type 0 and 1):

```bash
cat > ~/hash.txt << 'EOF'
$bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
$bitlocker$1$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
EOF
```



I downloaded rockyou.txt and cracked the hash with hashcat:

```bash

wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

# Crack with hashcat (BitLocker mode 22100)
hashcat -m 22100 -a 0 hash.txt rockyou.txt -w 3
```

Found the password **`jacqueline`**



I mounted the BitLocker volume using the password:

```bash
# Unlock BitLocker
mkdir -p ~/bitlocker_mount
sudo dislocker -v "/mnt/c/Users/SIDDHARTH U/bitlocker-1.dd" -ujacqueline ~/bitlocker_mount

# Mount NTFS volume
sudo mkdir -p /mnt/bitlocker
sudo mount -t ntfs-3g -o ro ~/bitlocker_mount/dislocker-file /mnt/bitlocker

# Read flag
sudo cat /mnt/bitlocker/flag.txt
```

**Flag:** `picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}`

This challenge involves cracking a BitLocker encrypted disk image. BitLocker is Windows' built-in disk encryption that scrambles data so only someone with the password can access it. The attack works by first extracting the password hash (a scrambled representation of the password) from the encrypted disk using `bitlocker2john`. Then we use `hashcat` to perform a dictionary attack .  Once we crack the password ("jacqueline" in this case), we use `dislocker` to decrypt the volume and mount it like a normal drive to read the flag. 
