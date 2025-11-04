lets first see the profile of the dump 


```
PS D:\DFIR-LABS\bi0sctfchall1> vol2 -f .\Damian.mem imageinfo 
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (D:\DFIR-LABS\bi0sctfchall1\Damian.mem)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf8000280f0a0L
          Number of Processors : 6
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002810d00L
                KPCR for CPU 1 : 0xfffff880009ea000L
                KPCR for CPU 2 : 0xfffff880030a8000L
                KPCR for CPU 3 : 0xfffff8800311d000L
                KPCR for CPU 4 : 0xfffff88003192000L
                KPCR for CPU 5 : 0xfffff880031c7000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2023-05-06 16:45:20 UTC+0000
     Image local date and time : 2023-05-06 22:15:20 +0530
```

Now lets enumerate the pslist 

```
PS D:\DFIR-LABS\bi0sctfchall1> vol2 -f .\Damian.mem --profile=Win7SP1x64 pslist
Volatility Foundation Volatility Framework 2.6
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa80036e2040 System                    4      0     98      469 ------      0 2023-05-06 16:43:35 UTC+0000
0xfffffa8004961300 smss.exe                272      4      2       34 ------      0 2023-05-06 16:43:35 UTC+0000
0xfffffa80062e8a20 csrss.exe               352    332     10      353      0      0 2023-05-06 16:43:38 UTC+0000
0xfffffa80047ca060 wininit.exe             404    332      4       84      0      0 2023-05-06 16:43:39 UTC+0000
0xfffffa80047c8360 csrss.exe               412    396     10      290      1      0 2023-05-06 16:43:39 UTC+0000
0xfffffa800643a740 services.exe            464    404     14      196      0      0 2023-05-06 16:43:39 UTC+0000
0xfffffa8006444060 winlogon.exe            488    396      6      121      1      0 2023-05-06 16:43:39 UTC+0000
0xfffffa800498f260 lsass.exe               516    404     11      581      0      0 2023-05-06 16:43:40 UTC+0000
0xfffffa800644d5b0 lsm.exe                 524    404     10      147      0      0 2023-05-06 16:43:40 UTC+0000
0xfffffa800632a660 svchost.exe             628    464     13      372      0      0 2023-05-06 16:43:40 UTC+0000
0xfffffa80064d2b30 VBoxService.ex          692    464     13      123      0      0 2023-05-06 16:43:40 UTC+0000
0xfffffa800644bb30 svchost.exe             760    464      8      255      0      0 2023-05-06 16:43:41 UTC+0000
0xfffffa800651ab30 svchost.exe             840    464     20      392      0      0 2023-05-06 16:43:41 UTC+0000
0xfffffa800654a7c0 svchost.exe             896    464     21      476      0      0 2023-05-06 16:43:41 UTC+0000
0xfffffa8006552940 svchost.exe             924    464     33      875      0      0 2023-05-06 16:43:41 UTC+0000
0xfffffa8006575b30 audiodg.exe            1000    840      8      136      0      0 2023-05-06 16:43:41 UTC+0000
0xfffffa8004871060 svchost.exe             296    464     13      290      0      0 2023-05-06 16:43:41 UTC+0000
0xfffffa80065cfb30 svchost.exe             348    464     18      387      0      0 2023-05-06 16:43:41 UTC+0000
0xfffffa8006651a30 spoolsv.exe            1140    464     15      315      0      0 2023-05-06 16:43:42 UTC+0000
0xfffffa800656ab30 svchost.exe            1180    464     21      332      0      0 2023-05-06 16:43:42 UTC+0000
0xfffffa80066dbb30 taskhost.exe           1312    464     10      155      1      0 2023-05-06 16:43:43 UTC+0000
0xfffffa8006742b30 dwm.exe                1448    896      6      103      1      0 2023-05-06 16:43:43 UTC+0000
0xfffffa8006783060 explorer.exe           1532   1416     40     1002      1      0 2023-05-06 16:43:43 UTC+0000
0xfffffa800676d490 VBoxTray.exe           2044   1532     15      149      1      0 2023-05-06 16:43:44 UTC+0000
0xfffffa80066e3060 SearchIndexer.          300    464     14      644      0      0 2023-05-06 16:43:51 UTC+0000
0xfffffa8006305b30 SearchProtocol         1756    300      9      382      0      0 2023-05-06 16:43:51 UTC+0000
0xfffffa8006907b30 SearchFilterHo         1580    300      7      143      0      0 2023-05-06 16:43:51 UTC+0000
0xfffffa80062f5300 iexplore.exe           2668   1532     22      477      1      1 2023-05-06 16:44:41 UTC+0000
0xfffffa80038a2b30 iexplore.exe           2752   2668     21      434      1      1 2023-05-06 16:44:41 UTC+0000
0xfffffa8006434b30 iexplore.exe           2892   2668     20      388      1      1 2023-05-06 16:44:47 UTC+0000
0xfffffa8003967b30 scvhost.exe            1924   1532      5       55      1      0 2023-05-06 16:44:54 UTC+0000
0xfffffa800393db30 conhost.exe            2292    412      3       51      1      0 2023-05-06 16:44:54 UTC+0000
0xfffffa800398f660 notepad.exe            2320   1924      2       57      1      0 2023-05-06 16:44:54 UTC+0000
0xfffffa800699e750 RamCapture64.e          596   1532      3       77      1      0 2023-05-06 16:45:18 UTC+0000
0xfffffa8003985060 conhost.exe            1900    412      2       51      1      0 2023-05-06 16:45:18 UTC+0000
0xfffffa800664f1b0 svchost.exe            2168    464      5        0 ------      0 2023-05-06 16:45:49 UTC+0000
```

Ok so notepad running is always an indication to be checked as ive realised from MEMLABS

So lets dump notepad and see any .dat or what started notepad , we'll use pstree to see the parent child process spawn data .


