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


