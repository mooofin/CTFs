Lets get the profile first 


```
remnux@remnux:~/Downloads/Investigation$ volatility -f windows.vmem imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/remnux/Downloads/Investigation/windows.vmem)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002c560a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002c57d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2020-07-22 09:07:57 UTC+0000
     Image local date and time : 2020-07-22 14:37:57 +0530

```

We have 3 questions to answer 
Question 1: When was the last time Adam entered an incorrect password to login? {:.info}
Question 2 :When was the file 1.jpg opened? {:.info}
Question 3: When did Adam last use the taskbar to launch Chrome? {:.info}


The profile is Win7SP1x64.

PART 1 

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/67c86689-a87d-4e67-90aa-bb794bc370e1" />

Since Windows registry hives store valuable information about user activity (such as usernames, last login, and failed login attempts), we need to locate the hive that records failed logins. For this challenge, we want to find when Adam last entered an incorrect password.

The first step is to identify and list the registry hives present in the memory image using Volatility. This helps us locate the SAM, SYSTEM, and SECURITY hives, since failed logon attempts are typically stored in the SAM hive and time data is mapped using the SYSTEM hive.


```
remnux@remnux:~/Downloads/Investigation$ volatility -f windows.vmem --profile=Win7SP1x64 hivelist
Volatility Foundation Volatility Framework 2.6.1
Virtual            Physical           Name
------------------ ------------------ ----
0xfffff8a00000f010 0x00000000272a4010 [no name]
0xfffff8a000024010 0x000000002736f010 \REGISTRY\MACHINE\SYSTEM
0xfffff8a000053010 0x000000002725e010 \REGISTRY\MACHINE\HARDWARE
0xfffff8a00078a010 0x000000001ed5e010 \Device\HarddiskVolume1\Boot\BCD
0xfffff8a0013c3010 0x000000001f1ec010 \SystemRoot\System32\Config\SOFTWARE
0xfffff8a00164a410 0x000000001d2d8410 \SystemRoot\System32\Config\DEFAULT
0xfffff8a001896010 0x000000001695f010 \SystemRoot\System32\Config\SECURITY
0xfffff8a0018f0410 0x00000000171e5410 \SystemRoot\System32\Config\SAM
0xfffff8a001993010 0x00000000143d2010 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0xfffff8a001a23010 0x0000000015d26010 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0xfffff8a00256d010 0x00000000005dd010 \??\C:\Users\Adam\ntuser.dat
0xfffff8a002571010 0x0000000001002010 \??\C:\Users\Adam\AppData\Local\Microsoft\Windows\UsrClass.dat

```


Let's dump this and see 

```
remnux@remnux:~/Downloads/Investigation$ volatility -f windows.vmem --profile=Win7SP1x64 dumpregistry -o 0xfffff8a0018f0410 -D .
Volatility Foundation Volatility Framework 2.6.1
**************************************************
Writing out registry: registry.0xfffff8a0018f0410.SAM.reg

**************************************************
```
<img width="1920" height="1020" alt="Screenshot from 2025-11-10 07-40-28" src="https://github.com/user-attachments/assets/b5fb2a0e-218f-4447-a269-0d22b61161fb" />

The output included the F value binary field %02%00%01%00...E8%0B%824%07\%D6%01..., where the third 8-byte FILETIME sequence corresponds to the LastFailedLogontimestamp. The bytes for this field wereE8 0B 82 34 07 60 D6 01, which when reversed from little endian and converted from FILETIME produced the value 2020-07-22 09:05:11. Reformatting the timestamp is  22-07-2020_09:05:11


Onto the 2nd qsn when was the file created ?


For this i'll look up MFT-table for info (memlabs taught this pov)

After some looking up i realised there's a much easier way , whenever windows creates a file a .lnl (the icon),lnk files are basically the shortcuts (icons) you use for files etc . So i'll grep it out for 1.lnk and it should be it  .


```
remnux@remnux:~/Downloads/Investigation$ volatility -f windows.vmem --profile=Win7SP1x64 mftparser | grep "1.lnk"
Volatility Foundation Volatility Framework 2.6.1
2020-07-21 18:22:47 UTC+0000 2020-07-21 18:38:33 UTC+0000   2020-07-21 18:38:33 UTC+0000   2020-07-21 18:38:33 UTC+0000   Users\Adam\AppData\Roaming\Microsoft\Windows\Recent\1.lnk
```

Alr this means that 

```
2020-07-21 18:22:47 UTC   <- Created
2020-07-21 18:38:33 UTC   <- Modified
2020-07-21 18:38:33 UTC   <- MFT entry modified
2020-07-21 18:38:33 UTC   <- Accessed
Users\Adam\AppData\Roaming\Microsoft\Windows\Recent\1.lnk
```
Now onto Question 3: When did Adam last use the taskbar to launch Chrome? 

My assumption is to use the reg or to check hive to see if there are any values 

