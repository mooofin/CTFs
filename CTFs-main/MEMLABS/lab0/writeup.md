# MemLabs Lab 0 - Never Too Late Mister

## Challenge Description

My friend John is an "environmental" activist and a humanitarian. He hated the ideology of Thanos from the Avengers: Infinity War. He sucks at programming. 
He used too many variables while writing any program. One day, John gave me a memory dump and asked me to find out what he was doing while he took the dump. Can you figure it out for me?

## Solution 

First i unizpped it to check whats inside the dump 

```bash
[nix-shell:~/sid/CTF/memlabs]$ tar -xf Challenge.tar.xz
(.venv) 
[nix-shell:~/sid/CTF/memlabs]$ ls
Challenge.raw  Challenge.tar.xz  shell.nix
(.venv)
```


Upon initial inspection of the memory dump Challenge.raw using the Volatility 3 framework, the windows.info command was executed to determine the system's profile. The analysis successfully identified the operating system as a 32-bit Windows 7 Service Pack 1, as indicated by the NTBuildLab string "7601.24260.x86fre.win7sp1_ldr.18". Key memory structure addresses, such as the Kernel Base at 0x82604000, were resolved, and the appropriate debugging symbols were automatically downloaded and parsed. The tool also extracted a crucial timestamp, revealing the system time was set to October 23, 2018, at 08:30:51 UTC, providing an initial temporal baseline for the investigation. .

<img width="1733" height="779" alt="screenshot-1759772865" src="https://github.com/user-attachments/assets/64d93546-efdf-49f9-afd5-63fe8e1f9179" />

Also The cool plugin pslist helps us see what proccesses were running 

<img width="1400" height="884" alt="screenshot-1759772947" src="https://github.com/user-attachments/assets/2ca05fb1-904d-4a47-852e-7efbb9fb7dc0" />



The investigation shows that the user logged in under Session ID 1, with explorer.exe (PID 324) serving as their main shell. From there, they opened a command prompt (cmd.exe, PID 2096) at 08:30:18 UTC.



SO since Cmd.exe was executed , we'll try to find what commands were used in the PS shell , using the plugin  cmdscan


I attempted to retrieve the user’s command-line history directly using Volatility 3’s windows.cmdscan and windows.consoles plugins, both designed to pull command history from memory. Unfortunately, both plugins failed. They returned a NotImplementedError, stating that the Windows version in the memory image (6.1.15.7601) wasn’t supported. This meant I couldn’t access the console buffer or command history using my current Volatility build


Even when a program terminates, traces of its activity can remain in memory, including references to the files it opened. To search for such remnants, I used the windows.filescan plugin, which scans memory for _FILE_OBJECT structures representing files that were recently accessed by the system. At this stage, I didn’t know exactly which file I was looking for  I simply wanted to see what had been opened around the time of the user’s session. As I reviewed the output, one entry immediately stood out: a file object pointing to \Users\hello\Desktop\demon.py.txt at the virtual address 0x3d4d1dc8

switched to volatility 2 : (

At this point, I decided to switch tools and try **Volatility 2**, since some plugins in Volatility 3 weren’t fully supported for this image. Using the `consoles` plugin, I was able to extract the full command-line history from the user’s active session. The output revealed two console processes: one associated with `cmd.exe` (PID 2096) and another with `DumpIt.exe` (PID 2412).

What caught my attention immediately was the command history linked to `cmd.exe`. It showed a single executed command:

```
C:\Python27\python.exe C:\Users\hello\Desktop\demon.py.txt
```

This confirmed that the user had explicitly run the Python interpreter to execute a script named `demon.py.txt` from their desktop. The captured screen buffer even showed the program’s output:

```
335d366f5d6031767631707f
```

This hexadecimal string was likely the key output or result produced by the script ? 



<img width="859" height="928" alt="screenshot-1759775791" src="https://github.com/user-attachments/assets/e75d11a6-c3cf-41f1-9c95-29ea1638f1ba" />


After confirming that the user executed demon.py.txt, I wanted to see if there were any additional clues hidden in the system’s runtime environment. Processes often store useful information in environment variables, including configuration values, keys, or even passwords used during execution. To explore this, I ran the Volatility 2 plugin envars, which lists the environment variables for every process in memory.

While reviewing the output, one particular process stood out svchost.exe (PID 716). Among its environment variables, I discovered entries referencing “Thanos”, “xor”, and “password”. 





After running several Volatility plugins, I decided to look into the environment variables using the `envars` plugin, since processes often store clues like encryption keys, commands, or passwords in memory. When I ran:

```bash
vol2 -f Challenge.raw --profile=Win7SP1x86 envars
```

I came across something interesting. Under the process `svchost.exe` (PID 716), I noticed an environment variable named **Thanos** with the value **xor**. Right next to it, there was also a **password** variable. At first, I didn’t quite understand what it meant, but seeing “xor” immediately made me think that the password might be hidden using a simple XOR cipher. This clue pointed me toward a potential decryption step.

To confirm this, I next decided to check for user credentials stored in memory. Using the `hashdump` plugin, I was able to extract NTLM password hashes from the memory image:

```bash
vol2 -f Challenge.raw --profile=Win7SP1x86 hashdump
```

The output revealed the following users and hashes:

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
hello:1000:aad3b435b51404eeaad3b435b51404ee:101da33f44e92c27835e64322d72e8b7:::
```



Given the earlier **Thanos = xor** clue, I suspected this string might be XOR-encrypted. So, I wrote a simple Python script to brute-force all possible XOR keys (0–255) and print the decrypted results:

```python
a = "335d366f5d6031767631707f".decode("hex")

for i in range(0, 255):
    b = ""
    for j in a:
        b += chr(ord(j) ^ i)
    print(b)
```


Solving the hash and concatenating the xor output gave the flag : ) 

```flag{you_are_good_but1_4m_b3tt3r}```






