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


USER32.dll manages windows and user input, while GDI32.dll handles graphics rendering. SHELL32.dll is particularly significant as it provides shell and file operation functions, including the ability to execute other programs. This explains how scvhost.exe was able to spawn the notepad.exe process. SHLWAPI.dll provides additional shell utility functions for path and file operations.


Running strings on the binary revealed a lot , Privilege escalation capabilities are evident through the AdjustTokenPrivileges, OpenProcessToken, and LookupPrivilegeValueA imports. These functions allow the malware to manipulate security tokens and potentially elevate its privileges . The malware imports RegOpenKeyExA, RegDeleteKeyA, RegDeleteKeyW, RegDeleteTreeA, RegDeleteTreeW, RegDeleteValueA, and RegDeleteValueW. While these functions can delete registry entries, they are typically paired with registry writing functions to establish autorun keys that would cause the malware to execute on system startup.




Enough bs lets run it on ghidra . 


<img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/20af38e4-1500-4eb6-aa2a-cbfea81289d9" />


The dissasembly seems to be a mess , then on the program trees , it showed that the exe has been packed with UPX , so lets unpack and load it again 


<img width="888" height="399" alt="image" src="https://github.com/user-attachments/assets/28fb474e-fa61-4cd7-9c5a-06cb08e9b099" />

I wasted a lot of time trying to dump this , but got a error with UPX .

Malware sometimes alters its UPX headers in memory to block unpacking, so using `procdump` can produce a tampered binary that UPX refuses to decompress. In this case, `dumpfiles` from Volatility pulled the untouched executable from the Windows file cache instead of process memory, allowing UPX to successfully unpack it. When UPX fails with a “possibly modified/hacked” error on a memory dump, always try retrieving the file from cache.

<img width="1079" height="197" alt="image" src="https://github.com/user-attachments/assets/8c686274-048d-47d7-b11f-1df4a89ac77b" />

Now that the procdump version is working let's move onto reversing this . 


I am using ghidra because idk ida 

<img width="1919" height="1011" alt="image" src="https://github.com/user-attachments/assets/45b12e87-508d-499c-862e-cec01b4b2825" />


We see some sus strings 


Also i spotted a starnge env called AZRAEL

<img width="1908" height="750" alt="image" src="https://github.com/user-attachments/assets/b91ee514-eea4-4bc0-b70f-bebf05cea8e9" />

Let's try to understand what this malware is doing  .



This is a lot , ill try to explain the important parts 


<img width="1023" height="808" alt="image" src="https://github.com/user-attachments/assets/96554c5a-26da-4162-a677-1d5356a04863" />


Checks if running with admin privileges, If not elevated, uses ShellExecuteExA() with "runas" to relaunch "scvhost.exe" with admin rights , Exits if user cancels UAC prompt (error 0x4c7)



I spotted the malware using  a function  for privilage escalation  . 

<img width="1078" height="835" alt="image" src="https://github.com/user-attachments/assets/dc0a1dfd-cfa8-41bd-914c-da62161d9052" />


This function enables SeDebugPrivilege for the current process by opening the process token, looking up the SeDebugPrivilege LUID, and calling AdjustTokenPrivileges to turn it on. Enabling that privilege lets the program open and manipulate other processes, including system-owned ones, which malware commonly uses to inject code, read memory (for credential theft), or tamper with protected processes. The sequence is a classic first step in process injection and privilege escalation.

<img width="1918" height="862" alt="image" src="https://github.com/user-attachments/assets/89b079a2-48d2-484b-ac76-28ad0c388097" />

In short this does - K32EnumProcesses() → K32EnumProcessModules() → K32GetModuleFileNameExA()
MultiByteToWideChar() → FUN_140031c70(L"Notepad.exe") , im guessing this is to store , its process ID for later injection . 


<img width="804" height="449" alt="image" src="https://github.com/user-attachments/assets/0f062d7a-4132-406b-95ce-1afbfe969bb2" />


Retrieves encryption key from environment variable "AZRAEL" , XORs the key with 0x33

<img width="885" height="525" alt="image" src="https://github.com/user-attachments/assets/3637e2fa-513a-450b-83dc-6300e99edf03" />


Opens C:\confidential.bin for reading -> Creates C:\Windows\windowsupdate.bin for output

Im not sure right now about whats being done next but an XOR is happening tho and it's doing twice ? 


<img width="949" height="483" alt="image" src="https://github.com/user-attachments/assets/1dc858e9-0530-4651-af9a-5a315ece671b" />

Classic DLL injection ah . Opens Notepad process with full access ->Allocates memory in Notepad's address space->Writes path to malicious DLL: Msrct.dll->Creates remote thread to load the DLL


Then the malware tries to hide itself by deleating everything 
```c

                CloseHandle(pvVar10);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002ba6;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002bc6;
                FUN_1400a8620((longlong *)(&stack0x000003a0 + lVar3),
                              "C:\\Windows\\AppCompat\\Programs\\amcache.hve");
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002bd5;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002be4;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x000003a0 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002bec;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002bfb;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002c1b;
                FUN_1400a8620((longlong *)(&stack0x00000380 + lVar3),
                              "C:\\Windows\\AppCompat\\Programs\\ShimCache.sys");
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002c2a;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002c39;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x00000380 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002c41;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002c50;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002c70;
                FUN_1400a8620((longlong *)(&stack0x00000360 + lVar3),"C:\\Windows\\Prefetch");
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002c7f;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002c8e;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x00000360 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002c96;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002ca5;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002cc5;
                FUN_1400a8620((longlong *)(&stack0x00000340 + lVar3),
                              "C:\\Windows\\System32\\winevt\\Logs");
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002cd4;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002ce3;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x00000340 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002ceb;
                remove(pcVar12);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x00000338 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002d1d;
                RegOpenKeyExA((HKEY)0xffffffff80000002,
                              "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution  Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x00000338 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002d43;
                RegDeleteKeyExA(pHVar2,"notepad.exe",0x100,0);
                pHVar2 = *(HKEY *)(&stack0x00000338 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002d69;
                RegDeleteKeyExA(pHVar2,"notepad.exe",0x200,0);
                pHVar2 = *(HKEY *)(&stack0x00000338 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002d7c;
                RegCloseKey(pHVar2);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002d81;
                FUN_140001e00();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002d86;
                FUN_140001eed();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002d8b;
                FUN_140001fd0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002d9a;
                remove("C:\\confidential.bin");
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x00000330 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002dcc;
                RegOpenKeyExW((HKEY)0xffffffff80000002,
                              L"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Executio n Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x00000330 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002df2;
                RegDeleteKeyExW(pHVar2,L"notepad.exe",0x100,0);
                pHVar2 = *(HKEY *)(&stack0x00000330 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002e18;
                RegDeleteKeyExW(pHVar2,L"notepad.exe",0x200,0);
                pHVar2 = *(HKEY *)(&stack0x00000330 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002e2b;
                RegCloseKey(pHVar2);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x00000328 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002e5d;
                RegOpenKeyExA((HKEY)0xffffffff80000002,
                              "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution  Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x00000328 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002e77;
                RegDeleteKeyA(pHVar2,"notepad.exe");
                pHVar2 = *(HKEY *)(&stack0x00000328 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002e8a;
                RegCloseKey(pHVar2);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x00000320 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002ebc;
                RegOpenKeyExW((HKEY)0xffffffff80000002,
                              L"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Executio n Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x00000320 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002ed6;
                RegDeleteKeyW(pHVar2,L"notepad.exe");
                pHVar2 = *(HKEY *)(&stack0x00000320 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002ee9;
                RegCloseKey(pHVar2);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x00000318 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002f1b;
                RegOpenKeyExA((HKEY)0xffffffff80000002,
                              "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution  Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x00000318 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002f35;
                RegDeleteValueA(pHVar2,"notepad.exe");
                pHVar2 = *(HKEY *)(&stack0x00000318 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002f48;
                RegCloseKey(pHVar2);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x00000310 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002f7a;
                RegOpenKeyExW((HKEY)0xffffffff80000002,
                              L"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Executio n Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x00000310 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002f94;
                RegDeleteValueW(pHVar2,L"notepad.exe");
                pHVar2 = *(HKEY *)(&stack0x00000310 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002fa7;
                RegCloseKey(pHVar2);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x00000308 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002fd9;
                RegOpenKeyExA((HKEY)0xffffffff80000002,
                              "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution  Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x00000308 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140002ff3;
                RegDeleteTreeA(pHVar2,"notepad.exe");
                pHVar2 = *(HKEY *)(&stack0x00000308 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003006;
                RegCloseKey(pHVar2);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x00000300 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003038;
                RegOpenKeyExW((HKEY)0xffffffff80000002,
                              L"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Executio n Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x00000300 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003052;
                RegDeleteTreeW(pHVar2,L"notepad.exe");
                pHVar2 = *(HKEY *)(&stack0x00000300 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003065;
                RegCloseKey(pHVar2);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x000002f8 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003097;
                RegOpenKeyExA((HKEY)0xffffffff80000002,
                              "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution  Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x000002f8 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400030b1;
                RegDeleteTreeA(pHVar2,"notepad.exe");
                pHVar2 = *(HKEY *)(&stack0x000002f8 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400030c4;
                RegCloseKey(pHVar2);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400030d3;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400030f3;
                FUN_1400a8620((longlong *)(&stack0x000002d0 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Temp\\* "
                             );
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003102;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003111;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x000002d0 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003119;
                remove(pcVar12);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x000002c8 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000314b;
                RegOpenKeyExA((HKEY)0xffffffff80000002,
                              "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Comp atibility Assistant\\Store"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x000002c8 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003165;
                RegDeleteValueA(pHVar2,"BAM");
                pHVar2 = *(HKEY *)(&stack0x000002c8 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003178;
                RegCloseKey(pHVar2);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x000002c0 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400031aa;
                RegOpenKeyExA((HKEY)0xffffffff80000002,
                              "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Comp atibility Assistant\\Store"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x000002c0 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400031c4;
                RegDeleteValueA(pHVar2,"DAM");
                pHVar2 = *(HKEY *)(&stack0x000002c0 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400031d7;
                RegCloseKey(pHVar2);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400031e6;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003206;
                FUN_1400a8620((longlong *)(&stack0x000002a0 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Microso ft\\Windows\\History\\History.IE5\\ActivitiesCache.db"
                             );
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003215;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003224;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x000002a0 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000322c;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000323b;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000325b;
                FUN_1400a8620((longlong *)(&stack0x00000280 + lVar3),
                              "C:\\Windows\\System32\\SRUM\\SRUM.DAT");
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000326a;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003279;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x00000280 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003281;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003290;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400032b0;
                FUN_1400a8620((longlong *)(&stack0x00000260 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Microso ft\\Windows\\UsrClass.dat"
                             );
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400032bf;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400032ce;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x00000260 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400032d6;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400032e5;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003305;
                FUN_1400a8620((longlong *)(&stack0x00000240 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Microso ft\\Windows\\Explorer\\ComDlg32.dll.mui"
                             );
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003314;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003323;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x00000240 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000332b;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000333a;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000335a;
                FUN_1400a8620((longlong *)(&stack0x00000220 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Microso ft\\Windows\\Explorer\\RunMRU"
                             );
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003369;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003378;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x00000220 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003380;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000338f;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400033af;
                FUN_1400a8620((longlong *)(&stack0x00000200 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Microso ft\\Windows\\Explorer\\AutomaticDestinations"
                             );
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400033be;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400033cd;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x00000200 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400033d5;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400033e4;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003404;
                FUN_1400a8620((longlong *)(&stack0x000001e0 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Microso ft\\Windows\\Explorer\\RecentPlaces"
                             );
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003413;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003422;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x000001e0 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000342a;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003439;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003459;
                FUN_1400a8620((longlong *)(&stack0x000001c0 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Microso ft\\Windows\\Explorer\\WindowsSearch"
                             );
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003468;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003477;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x000001c0 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000347f;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000348e;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400034ae;
                FUN_1400a8620((longlong *)(&stack0x000001a0 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Microso ft\\Windows\\Explorer\\WindowsSearch"
                             );
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400034bd;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400034cc;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x000001a0 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400034d4;
                remove(pcVar12);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400034e3;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003503;
                FUN_1400a8620((longlong *)(&stack0x00000180 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Microso ft\\Windows\\Explorer\\thumbs.db"
                             );
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003512;
                FUN_1400736b0();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003521;
                pcVar12 = (char *)FUN_140031060((undefined8 *)(&stack0x00000180 + lVar3));
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003529;
                remove(pcVar12);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x00000178 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x14000355b;
                RegOpenKeyExA((HKEY)0xffffffff80000002,
                              "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution  Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x00000178 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003575;
                RegDeleteValueA(pHVar2,"confidential.bin");
                pHVar2 = *(HKEY *)(&stack0x00000178 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003588;
                RegCloseKey(pHVar2);
                *(undefined1 **)(&stack0xffffffffffffffe0 + lVar4 + lVar3) =
                     &stack0x00000170 + lVar3;
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400035ba;
                RegOpenKeyExW((HKEY)0xffffffff80000002,
                              L"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Executio n Options"
                              ,0,0xf003f,*(PHKEY *)(&stack0xffffffffffffffe0 + lVar4 + lVar3));
                pHVar2 = *(HKEY *)(&stack0x00000170 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400035d4;
                RegDeleteValueW(pHVar2,L"confidential.bin");
                pHVar2 = *(HKEY *)(&stack0x00000170 + lVar3);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400035e7;
                RegCloseKey(pHVar2);
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x1400035f6;
                FUN_140073680();
                *(undefined8 *)((longlong)&uStack_48 + lVar4 + lVar3) = 0x140003616;
                FUN_1400a8620((longlong *)(&stack0x00000150 + lVar3),
                              "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Temp\\* "
                             );
```


<img width="1210" height="503" alt="image" src="https://github.com/user-attachments/assets/e8f7f374-28cf-4126-9278-4b0191b47ae0" />

Also this is how the malware enumerates the list : ) 


Azrael was very sus , lets try running envars plugin to see the stuff which the variable uses . 


<img width="1207" height="330" alt="image" src="https://github.com/user-attachments/assets/6670f18a-c0cf-4977-8dd1-f6e42fbd895a" />


Im guessting that this is the key ? 

Now xoring it with 0x33 the value which we found earlier 



Since the malware deleated some stuff , i looked at MFT-table which on memlabs expereicne  has some flag parts or clues related to it ? 


<img width="930" height="61" alt="image" src="https://github.com/user-attachments/assets/986b1632-8212-478c-ab6f-1e1791f31152" />


Onto the next part , i need some explanations - 

The Virtual Address Descriptor (VAD) node is a data structure used by the Windows operating system to manage virtual memory. Each VAD node contains information about a specific virtual memory region, including the starting and ending addresses, the memory protection constants, and other attributes.

To determine the memory protection constants for a specific VAD node, use the “vadinfo” plugin in the Volatility framework.

VAD is a tree structure and like any tree structure it has a root (which is called Vadroot) and nodes/leafs (Vadnodes) that contains all the information related to memory ranges reserved for a specific process by the memory manager. For each chunk of a continuous virtual memory address allocations, memory manager creates a corresponding VAD node that contains the information about this continuous allocations 

<img width="922" height="669" alt="image" src="https://github.com/user-attachments/assets/20a53e98-2a66-450d-91ec-a9660cf00a30" />

<img width="586" height="594" alt="image" src="https://github.com/user-attachments/assets/16cc0c50-ec2c-4acf-a70d-b759d950e860" />

