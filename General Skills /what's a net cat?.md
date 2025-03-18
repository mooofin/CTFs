# PicoCTF Writeup: Netcat Challenge

## Challenge Description
Using netcat (nc) is going to be pretty important. Can you connect to `jupiter.challenges.picoctf.org` at port `25103` to get the flag?

## Solution
To retrieve the flag, we need to connect to the given host and port using **netcat (nc)**.

### Step 1: Open a Terminal
Since **netcat** is a command-line tool, open a terminal window on your Linux machine or use a command prompt on Windows with netcat installed.

### Step 2: Connect to the Server
Run the following command:
```bash
nc jupiter.challenges.picoctf.org 25103
```

### Step 3: Retrieve the Flag
- If the connection is successful, the flag might be printed immediately.
- If prompted for input, try pressing **Enter** or sending **"GET FLAG"**.

### Alternative Methods
If `nc` is not installed, you can try using:
```bash
ncat jupiter.challenges.picoctf.org 25103
```
Or, if **telnet** is available:
```bash
telnet jupiter.challenges.picoctf.org 25103
```

## Flag
After executing the command, the flag should be displayed. Copy and submit it as the challenge solution.

---


