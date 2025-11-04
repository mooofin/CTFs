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

```
PS D:\DFIR-LABS\bi0sctfchall1> vol2 -f .\Damian.mem --profile=Win7SP1x64 pslist | Select-String "2320"
Volatility Foundation Volatility Framework 2.6

0xfffffa800398f660 notepad.exe            2320   1924      2       57      1      0 2023-05-06 16:44:54 UTC+0000


PS D:\DFIR-LABS\bi0sctfchall1> vol2 -f .\Damian.mem --profile=Win7SP1x64 pslist | Select-String "1924"
Volatility Foundation Volatility Framework 2.6

0xfffffa8003967b30 scvhost.exe            1924   1532      5       55      1      0 2023-05-06 16:44:54 UTC+0000
0xfffffa800398f660 notepad.exe            2320   1924      2       57      1      0 2023-05-06 16:44:54 UTC+0000

```

Okie so The process name is scvhost.exe which is a typo/misspelling of the legitimate Windows process svchost.exe 

This could be a malware and we'll use malfind next for more investigation later  . 


coming back to see what the commands were 

```

PS D:\DFIR-LABS\bi0sctfchall1> vol2 -f .\Damian.mem --profile=Win7SP1x64 cmdline -p 1924              
Volatility Foundation Volatility Framework 2.6
************************************************************************
scvhost.exe pid:   1924
Command line : "C:\Users\EdwardNygma7\Downloads\windows-patch-update\scvhost.exe"

```

Also edward nygma is riddler which might be a clue ? 


Now that we;ve made sure that this was a malware pretending to be a legitimate process lets run malfind .


```
PS D:\DFIR-LABS\bi0sctfchall1> vol2 -f .\Damian.mem --profile=Win7SP1x64 malfind        
Volatility Foundation Volatility Framework 2.6
Process: explorer.exe Pid: 1532 Address: 0x3dc0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x03dc0000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x03dc0010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x03dc0020  00 00 dc 03 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x03dc0030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................

0x03dc0000 0000             ADD [EAX], AL
0x03dc0002 0000             ADD [EAX], AL
0x03dc0004 0000             ADD [EAX], AL
0x03dc0006 0000             ADD [EAX], AL
0x03dc0008 0000             ADD [EAX], AL
0x03dc000a 0000             ADD [EAX], AL
0x03dc000c 0000             ADD [EAX], AL
0x03dc000e 0000             ADD [EAX], AL
0x03dc0010 0000             ADD [EAX], AL
0x03dc0012 0000             ADD [EAX], AL
0x03dc0014 0000             ADD [EAX], AL
0x03dc0016 0000             ADD [EAX], AL
0x03dc0018 0000             ADD [EAX], AL
0x03dc001a 0000             ADD [EAX], AL
0x03dc001c 0000             ADD [EAX], AL
0x03dc001e 0000             ADD [EAX], AL
0x03dc0020 0000             ADD [EAX], AL
0x03dc0022 dc03             FADD QWORD [EBX]
0x03dc0024 0000             ADD [EAX], AL
0x03dc0026 0000             ADD [EAX], AL
0x03dc0028 0000             ADD [EAX], AL
0x03dc002a 0000             ADD [EAX], AL
0x03dc002c 0000             ADD [EAX], AL
0x03dc002e 0000             ADD [EAX], AL
0x03dc0030 0000             ADD [EAX], AL
0x03dc0032 0000             ADD [EAX], AL
0x03dc0034 0000             ADD [EAX], AL
0x03dc0036 0000             ADD [EAX], AL
0x03dc0038 0000             ADD [EAX], AL
0x03dc003a 0000             ADD [EAX], AL
0x03dc003c 0000             ADD [EAX], AL
0x03dc003e 0000             ADD [EAX], AL

Process: explorer.exe Pid: 1532 Address: 0x4180000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 16, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x04180000  41 ba 80 00 00 00 48 b8 38 a1 ee fd fe 07 00 00   A.....H.8.......
0x04180010  48 ff 20 90 41 ba 81 00 00 00 48 b8 38 a1 ee fd   H...A.....H.8...
0x04180020  fe 07 00 00 48 ff 20 90 41 ba 82 00 00 00 48 b8   ....H...A.....H.
0x04180030  38 a1 ee fd fe 07 00 00 48 ff 20 90 41 ba 83 00   8.......H...A...

0x04180000 41               INC ECX
0x04180001 ba80000000       MOV EDX, 0x80
0x04180006 48               DEC EAX
0x04180007 b838a1eefd       MOV EAX, 0xfdeea138
0x0418000c fe07             INC BYTE [EDI]
0x0418000e 0000             ADD [EAX], AL
0x04180010 48               DEC EAX
0x04180011 ff20             JMP DWORD [EAX]
0x04180013 90               NOP
0x04180014 41               INC ECX
0x04180015 ba81000000       MOV EDX, 0x81
0x0418001a 48               DEC EAX
0x0418001b b838a1eefd       MOV EAX, 0xfdeea138
0x04180020 fe07             INC BYTE [EDI]
0x04180022 0000             ADD [EAX], AL
0x04180024 48               DEC EAX
0x04180025 ff20             JMP DWORD [EAX]
0x04180027 90               NOP
0x04180028 41               INC ECX
0x04180029 ba82000000       MOV EDX, 0x82
0x0418002e 48               DEC EAX
0x0418002f b838a1eefd       MOV EAX, 0xfdeea138
0x04180034 fe07             INC BYTE [EDI]
0x04180036 0000             ADD [EAX], AL
0x04180038 48               DEC EAX
0x04180039 ff20             JMP DWORD [EAX]
0x0418003b 90               NOP
0x0418003c 41               INC ECX
0x0418003d ba               DB 0xba
0x0418003e 83               DB 0x83
0x0418003f 00               DB 0x0

Process: SearchFilterHo Pid: 1580 Address: 0xc50000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 2, PrivateMemory: 1, Protection: 6

0x00c50000  00 00 00 00 00 00 00 00 09 83 17 8f 1c e3 00 01   ................
0x00c50010  ee ff ee ff 00 00 00 00 28 01 c5 00 00 00 00 00   ........(.......
0x00c50020  28 01 c5 00 00 00 00 00 00 00 c5 00 00 00 00 00   (...............
0x00c50030  00 00 c5 00 00 00 00 00 80 00 00 00 00 00 00 00   ................

0x00c50000 0000             ADD [EAX], AL
0x00c50002 0000             ADD [EAX], AL
0x00c50004 0000             ADD [EAX], AL
0x00c50006 0000             ADD [EAX], AL
0x00c50008 0983178f1ce3     OR [EBX-0x1ce370e9], EAX
0x00c5000e 0001             ADD [ECX], AL
0x00c50010 ee               OUT DX, AL
0x00c50011 ff               DB 0xff
0x00c50012 ee               OUT DX, AL
0x00c50013 ff00             INC DWORD [EAX]
0x00c50015 0000             ADD [EAX], AL
0x00c50017 0028             ADD [EAX], CH
0x00c50019 01c5             ADD EBP, EAX
0x00c5001b 0000             ADD [EAX], AL
0x00c5001d 0000             ADD [EAX], AL
0x00c5001f 0028             ADD [EAX], CH
0x00c50021 01c5             ADD EBP, EAX
0x00c50023 0000             ADD [EAX], AL
0x00c50025 0000             ADD [EAX], AL
0x00c50027 0000             ADD [EAX], AL
0x00c50029 00c5             ADD CH, AL
0x00c5002b 0000             ADD [EAX], AL
0x00c5002d 0000             ADD [EAX], AL
0x00c5002f 0000             ADD [EAX], AL
0x00c50031 00c5             ADD CH, AL
0x00c50033 0000             ADD [EAX], AL
0x00c50035 0000             ADD [EAX], AL
0x00c50037 008000000000     ADD [EAX+0x0], AL
0x00c5003d 0000             ADD [EAX], AL
0x00c5003f 00               DB 0x0

Process: iexplore.exe Pid: 2668 Address: 0xf60000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 2, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x00f60000  b0 00 eb 70 b0 01 eb 6c b0 02 eb 68 b0 03 eb 64   ...p...l...h...d
0x00f60010  b0 04 eb 60 b0 05 eb 5c b0 06 eb 58 b0 07 eb 54   ...`...\...X...T
0x00f60020  b0 08 eb 50 b0 09 eb 4c b0 0a eb 48 b0 0b eb 44   ...P...L...H...D
0x00f60030  b0 0c eb 40 b0 0d eb 3c b0 0e eb 38 b0 0f eb 34   ...@...<...8...4

0x00f60000 b000             MOV AL, 0x0
0x00f60002 eb70             JMP 0xf60074
0x00f60004 b001             MOV AL, 0x1
0x00f60006 eb6c             JMP 0xf60074
0x00f60008 b002             MOV AL, 0x2
0x00f6000a eb68             JMP 0xf60074
0x00f6000c b003             MOV AL, 0x3
0x00f6000e eb64             JMP 0xf60074
0x00f60010 b004             MOV AL, 0x4
0x00f60012 eb60             JMP 0xf60074
0x00f60014 b005             MOV AL, 0x5
0x00f60016 eb5c             JMP 0xf60074
0x00f60018 b006             MOV AL, 0x6
0x00f6001a eb58             JMP 0xf60074
0x00f6001c b007             MOV AL, 0x7
0x00f6001e eb54             JMP 0xf60074
0x00f60020 b008             MOV AL, 0x8
0x00f60022 eb50             JMP 0xf60074
0x00f60024 b009             MOV AL, 0x9
0x00f60026 eb4c             JMP 0xf60074
0x00f60028 b00a             MOV AL, 0xa
0x00f6002a eb48             JMP 0xf60074
0x00f6002c b00b             MOV AL, 0xb
0x00f6002e eb44             JMP 0xf60074
0x00f60030 b00c             MOV AL, 0xc
0x00f60032 eb40             JMP 0xf60074
0x00f60034 b00d             MOV AL, 0xd
0x00f60036 eb3c             JMP 0xf60074
0x00f60038 b00e             MOV AL, 0xe
0x00f6003a eb38             JMP 0xf60074
0x00f6003c b00f             MOV AL, 0xf
0x00f6003e eb34             JMP 0xf60074

Process: iexplore.exe Pid: 2668 Address: 0x5fff0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 16, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x5fff0000  64 74 72 52 00 00 00 00 00 02 ff 5f 00 00 00 00   dtrR......._....
0x5fff0010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x5fff0020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x5fff0030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................

0x5fff0000 647472           JZ 0x5fff0075
0x5fff0003 52               PUSH EDX
0x5fff0004 0000             ADD [EAX], AL
0x5fff0006 0000             ADD [EAX], AL
0x5fff0008 0002             ADD [EDX], AL
0x5fff000a ff5f00           CALL FAR DWORD [EDI+0x0]
0x5fff000d 0000             ADD [EAX], AL
0x5fff000f 0000             ADD [EAX], AL
0x5fff0011 0000             ADD [EAX], AL
0x5fff0013 0000             ADD [EAX], AL
0x5fff0015 0000             ADD [EAX], AL
0x5fff0017 0000             ADD [EAX], AL
0x5fff0019 0000             ADD [EAX], AL
0x5fff001b 0000             ADD [EAX], AL
0x5fff001d 0000             ADD [EAX], AL
0x5fff001f 0000             ADD [EAX], AL
0x5fff0021 0000             ADD [EAX], AL
0x5fff0023 0000             ADD [EAX], AL
0x5fff0025 0000             ADD [EAX], AL
0x5fff0027 0000             ADD [EAX], AL
0x5fff0029 0000             ADD [EAX], AL
0x5fff002b 0000             ADD [EAX], AL
0x5fff002d 0000             ADD [EAX], AL
0x5fff002f 0000             ADD [EAX], AL
0x5fff0031 0000             ADD [EAX], AL
0x5fff0033 0000             ADD [EAX], AL
0x5fff0035 0000             ADD [EAX], AL
0x5fff0037 0000             ADD [EAX], AL
0x5fff0039 0000             ADD [EAX], AL
0x5fff003b 0000             ADD [EAX], AL
0x5fff003d 0000             ADD [EAX], AL
0x5fff003f 00               DB 0x0

Process: iexplore.exe Pid: 2752 Address: 0xde0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 2, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x00de0000  b0 00 eb 70 b0 01 eb 6c b0 02 eb 68 b0 03 eb 64   ...p...l...h...d
0x00de0010  b0 04 eb 60 b0 05 eb 5c b0 06 eb 58 b0 07 eb 54   ...`...\...X...T
0x00de0020  b0 08 eb 50 b0 09 eb 4c b0 0a eb 48 b0 0b eb 44   ...P...L...H...D
0x00de0030  b0 0c eb 40 b0 0d eb 3c b0 0e eb 38 b0 0f eb 34   ...@...<...8...4

0x00de0000 b000             MOV AL, 0x0
0x00de0002 eb70             JMP 0xde0074
0x00de0004 b001             MOV AL, 0x1
0x00de0006 eb6c             JMP 0xde0074
0x00de0008 b002             MOV AL, 0x2
0x00de000a eb68             JMP 0xde0074
0x00de000c b003             MOV AL, 0x3
0x00de000e eb64             JMP 0xde0074
0x00de0010 b004             MOV AL, 0x4
0x00de0012 eb60             JMP 0xde0074
0x00de0014 b005             MOV AL, 0x5
0x00de0016 eb5c             JMP 0xde0074
0x00de0018 b006             MOV AL, 0x6
0x00de001a eb58             JMP 0xde0074
0x00de001c b007             MOV AL, 0x7
0x00de001e eb54             JMP 0xde0074
0x00de0020 b008             MOV AL, 0x8
0x00de0022 eb50             JMP 0xde0074
0x00de0024 b009             MOV AL, 0x9
0x00de0026 eb4c             JMP 0xde0074
0x00de0028 b00a             MOV AL, 0xa
0x00de002a eb48             JMP 0xde0074
0x00de002c b00b             MOV AL, 0xb
0x00de002e eb44             JMP 0xde0074
0x00de0030 b00c             MOV AL, 0xc
0x00de0032 eb40             JMP 0xde0074
0x00de0034 b00d             MOV AL, 0xd
0x00de0036 eb3c             JMP 0xde0074
0x00de0038 b00e             MOV AL, 0xe
0x00de003a eb38             JMP 0xde0074
0x00de003c b00f             MOV AL, 0xf
0x00de003e eb34             JMP 0xde0074

Process: iexplore.exe Pid: 2752 Address: 0x5fff0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 16, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x5fff0000  64 74 72 52 00 00 00 00 00 05 ff 5f 00 00 00 00   dtrR......._....
0x5fff0010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x5fff0020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x5fff0030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................

0x5fff0000 647472           JZ 0x5fff0075
0x5fff0003 52               PUSH EDX
0x5fff0004 0000             ADD [EAX], AL
0x5fff0006 0000             ADD [EAX], AL
0x5fff0008 0005ff5f0000     ADD [0x5fff], AL
0x5fff000e 0000             ADD [EAX], AL
0x5fff0010 0000             ADD [EAX], AL
0x5fff0012 0000             ADD [EAX], AL
0x5fff0014 0000             ADD [EAX], AL
0x5fff0016 0000             ADD [EAX], AL
0x5fff0018 0000             ADD [EAX], AL
0x5fff001a 0000             ADD [EAX], AL
0x5fff001c 0000             ADD [EAX], AL
0x5fff001e 0000             ADD [EAX], AL
0x5fff0020 0000             ADD [EAX], AL
0x5fff0022 0000             ADD [EAX], AL
0x5fff0024 0000             ADD [EAX], AL
0x5fff0026 0000             ADD [EAX], AL
0x5fff0028 0000             ADD [EAX], AL
0x5fff002a 0000             ADD [EAX], AL
0x5fff002c 0000             ADD [EAX], AL
0x5fff002e 0000             ADD [EAX], AL
0x5fff0030 0000             ADD [EAX], AL
0x5fff0032 0000             ADD [EAX], AL
0x5fff0034 0000             ADD [EAX], AL
0x5fff0036 0000             ADD [EAX], AL
0x5fff0038 0000             ADD [EAX], AL
0x5fff003a 0000             ADD [EAX], AL
0x5fff003c 0000             ADD [EAX], AL
0x5fff003e 0000             ADD [EAX], AL

Process: iexplore.exe Pid: 2892 Address: 0x510000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 2, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x00510000  b0 00 eb 70 b0 01 eb 6c b0 02 eb 68 b0 03 eb 64   ...p...l...h...d
0x00510010  b0 04 eb 60 b0 05 eb 5c b0 06 eb 58 b0 07 eb 54   ...`...\...X...T
0x00510020  b0 08 eb 50 b0 09 eb 4c b0 0a eb 48 b0 0b eb 44   ...P...L...H...D
0x00510030  b0 0c eb 40 b0 0d eb 3c b0 0e eb 38 b0 0f eb 34   ...@...<...8...4

0x00510000 b000             MOV AL, 0x0
0x00510002 eb70             JMP 0x510074
0x00510004 b001             MOV AL, 0x1
0x00510006 eb6c             JMP 0x510074
0x00510008 b002             MOV AL, 0x2
0x0051000a eb68             JMP 0x510074
0x0051000c b003             MOV AL, 0x3
0x0051000e eb64             JMP 0x510074
0x00510010 b004             MOV AL, 0x4
0x00510012 eb60             JMP 0x510074
0x00510014 b005             MOV AL, 0x5
0x00510016 eb5c             JMP 0x510074
0x00510018 b006             MOV AL, 0x6
0x0051001a eb58             JMP 0x510074
0x0051001c b007             MOV AL, 0x7
0x0051001e eb54             JMP 0x510074
0x00510020 b008             MOV AL, 0x8
0x00510022 eb50             JMP 0x510074
0x00510024 b009             MOV AL, 0x9
0x00510026 eb4c             JMP 0x510074
0x00510028 b00a             MOV AL, 0xa
0x0051002a eb48             JMP 0x510074
0x0051002c b00b             MOV AL, 0xb
0x0051002e eb44             JMP 0x510074
0x00510030 b00c             MOV AL, 0xc
0x00510032 eb40             JMP 0x510074
0x00510034 b00d             MOV AL, 0xd
0x00510036 eb3c             JMP 0x510074
0x00510038 b00e             MOV AL, 0xe
0x0051003a eb38             JMP 0x510074
0x0051003c b00f             MOV AL, 0xf
0x0051003e eb34             JMP 0x510074

Process: iexplore.exe Pid: 2892 Address: 0x5fff0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 16, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x5fff0000  64 74 72 52 00 00 00 00 00 05 ff 5f 00 00 00 00   dtrR......._....
0x5fff0010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x5fff0020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x5fff0030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................

0x5fff0000 647472           JZ 0x5fff0075
0x5fff0003 52               PUSH EDX
0x5fff0004 0000             ADD [EAX], AL
0x5fff0006 0000             ADD [EAX], AL
0x5fff0008 0005ff5f0000     ADD [0x5fff], AL
0x5fff000e 0000             ADD [EAX], AL
0x5fff0010 0000             ADD [EAX], AL
0x5fff0012 0000             ADD [EAX], AL
0x5fff0014 0000             ADD [EAX], AL
0x5fff0016 0000             ADD [EAX], AL
0x5fff0018 0000             ADD [EAX], AL
0x5fff001a 0000             ADD [EAX], AL
0x5fff001c 0000             ADD [EAX], AL
0x5fff001e 0000             ADD [EAX], AL
0x5fff0020 0000             ADD [EAX], AL
0x5fff0022 0000             ADD [EAX], AL
0x5fff0024 0000             ADD [EAX], AL
0x5fff0026 0000             ADD [EAX], AL
0x5fff0028 0000             ADD [EAX], AL
0x5fff002a 0000             ADD [EAX], AL
0x5fff002c 0000             ADD [EAX], AL
0x5fff002e 0000             ADD [EAX], AL
0x5fff0030 0000             ADD [EAX], AL
0x5fff0032 0000             ADD [EAX], AL
0x5fff0034 0000             ADD [EAX], AL
0x5fff0036 0000             ADD [EAX], AL
0x5fff0038 0000             ADD [EAX], AL
0x5fff003a 0000             ADD [EAX], AL
0x5fff003c 0000             ADD [EAX], AL
0x5fff003e 0000             ADD [EAX], AL

PS D:\DFIR-LABS\bi0sctfchall1>
```

Onto some explanation here - What malfind does is to look for memory pages marked for execution AND that don't have an associated file mapped to disk (signs of code injection). You still need to look at each result to find the malicios code (look for the portable executable signature or shell code)

Some notes which are helpful are  - 

PAGE_EXECUTE_READWRITE is suspicious because normal code pages are usually PAGE_EXECUTE_READ, meaning they can run but not be modified. When a page is both executable and writable it often indicates injected or self-modifying shellcode.

VadS with PrivateMemory means the memory region is not mapped from a file. Legitimate code (DLLs, EXEs) is usually file-backed. Private, executable memory is a common sign of code injection via VirtualAlloc or similar APIs.

In the explorer.exe example, the instructions `MOV EDX, 0x80; MOV EAX, 0xfdeea138; JMP [EAX]` look like a hook redirecting execution, and the changing values (0x80, 0x81, 0x82) resemble a syscall or function pointer table hook. In the iexplore.exe processes, repeated patterns like `MOV AL, 0x0 / JMP 0xf60074` and `MOV AL, 0x1 / JMP 0xf60074` across multiple instances point to process injection. Identical injected code in multiple processes strongly suggests malicious activity.


Onto the malware binary , lemme try to dump it and try to reverse it using ghidra . 


Before that lemme check what dll's were being used - 


<img width="1032" height="490" alt="image" src="https://github.com/user-attachments/assets/b4e3b46d-4f2c-45b6-9f37-ff184a15bf59" />



ADVAPI32.dll provides access to the Windows registry, security functions, and service management - this allows the malware to establish persistence by creating registry keys or installing itself as a service. The sechost.dll library enables security-related operations and privilege manipulation. RPCRT4.dll provides Remote Procedure Call functionality, allowing the malware to communicate with other processes on the system.








