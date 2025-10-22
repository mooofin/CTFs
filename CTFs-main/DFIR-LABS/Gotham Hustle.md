First i ran imageinfo :) to see what we are working with 

<img width="1425" height="394" alt="image" src="https://github.com/user-attachments/assets/6e32d06b-92fb-4693-a22f-d1955b5adbf8" />


System Information:

OS Profile: Win7SP1x64 (Windows 7 SP1 64-bit)
Processors: 6 CPUs
Image Date/Time: 2024-08-06 18:37:19 UTC (11:37:19 AM Pacific Time)
Memory Size: 4.6 GB

Like always lets run pslist and see 

```
Volatility Foundation Volatility Framework 2.6
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa80036d4040 System                    4      0    113      573 ------      0 2024-08-07 04:19:36 UTC+0000
0xfffffa8004969040 smss.exe                312      4      2       34 ------      0 2024-08-07 04:19:36 UTC+0000
0xfffffa80064e2b00 csrss.exe               400    388      9      524      0      0 2024-08-07 04:19:42 UTC+0000
0xfffffa8006433360 wininit.exe             452    388      3       81      0      0 2024-08-07 04:19:42 UTC+0000
0xfffffa80063c7b00 csrss.exe               460    444     12      535      1      0 2024-08-07 04:19:42 UTC+0000
0xfffffa8006685280 winlogon.exe            516    444      5      123      1      0 2024-08-07 04:19:43 UTC+0000
0xfffffa8006682b00 services.exe            552    452      7      228      0      0 2024-08-07 04:19:43 UTC+0000
0xfffffa80066d7060 lsass.exe               568    452      9      745      0      0 2024-08-07 04:19:44 UTC+0000
0xfffffa80066d5b00 lsm.exe                 576    452     10      154      0      0 2024-08-07 04:19:44 UTC+0000
0xfffffa8006714b00 svchost.exe             680    552     11      375      0      0 2024-08-07 04:19:45 UTC+0000
0xfffffa80048eb8e0 VBoxService.ex          744    552     13      124      0      0 2024-08-07 04:19:45 UTC+0000
0xfffffa80064de5c0 svchost.exe             804    552      8      305      0      0 2024-08-06 15:49:46 UTC+0000
0xfffffa80065c8750 svchost.exe             896    552     23      593      0      0 2024-08-06 15:49:46 UTC+0000
0xfffffa80067c4860 svchost.exe             936    552     27      610      0      0 2024-08-06 15:49:46 UTC+0000
0xfffffa80067d0b00 svchost.exe             968    552     20      651      0      0 2024-08-06 15:49:46 UTC+0000
0xfffffa80067e43e0 svchost.exe            1004    552     36     1041      0      0 2024-08-06 15:49:46 UTC+0000
0xfffffa8006816b00 svchost.exe            1064    552     18      494      0      0 2024-08-06 15:49:47 UTC+0000
0xfffffa8006905590 spoolsv.exe            1280    552     14      323      0      0 2024-08-06 15:49:48 UTC+0000
0xfffffa800691a280 svchost.exe            1308    552     16      320      0      0 2024-08-06 15:49:48 UTC+0000
0xfffffa800688cb00 svchost.exe            1400    552     10      156      0      0 2024-08-06 15:49:49 UTC+0000
0xfffffa80069a8b00 svchost.exe            1428    552     20      366      0      0 2024-08-06 15:49:50 UTC+0000
0xfffffa80038c4b00 dwm.exe                1556    936      3      110      1      0 2024-08-06 15:49:58 UTC+0000
0xfffffa8006bbeb00 explorer.exe           1172   2024     32     1017      1      0 2024-08-06 15:49:58 UTC+0000
0xfffffa80067b0b00 taskhost.exe           1328    552      8      216      1      0 2024-08-06 15:49:58 UTC+0000
0xfffffa8006c5f780 VBoxTray.exe           2240   1172     17      165      1      0 2024-08-06 15:50:00 UTC+0000
0xfffffa8006bc0b00 SearchIndexer.         2460    552     13      664      0      0 2024-08-06 15:50:06 UTC+0000
0xfffffa80038ce060 wmpnetwk.exe           2784    552     33      462      0      0 2024-08-06 15:50:32 UTC+0000
0xfffffa8006d90b00 svchost.exe            2888    552     10      372      0      0 2024-08-06 15:50:33 UTC+0000
0xfffffa8004887410 sppsvc.exe              912    552      7      157      0      0 2024-08-06 15:52:00 UTC+0000
0xfffffa800673bb00 svchost.exe            1080    552     13      385      0      0 2024-08-06 15:52:01 UTC+0000
0xfffffa8004587060 GoogleCrashHan         3044   4908      5       92      0      1 2024-08-06 16:36:44 UTC+0000
0xfffffa80039c5b00 GoogleCrashHan          408   4908      5       85      0      0 2024-08-06 16:36:44 UTC+0000
0xfffffa80044c3b00 chrome.exe             4456   4464     32     1296      1      0 2024-08-06 16:36:45 UTC+0000
0xfffffa8004463060 chrome.exe             4432   4456      8      119      1      0 2024-08-06 16:36:45 UTC+0000
0xfffffa8003daeb00 chrome.exe             4928   4456     13      234      1      0 2024-08-06 16:36:47 UTC+0000
0xfffffa8004511b00 chrome.exe             4872   4456      8      155      1      0 2024-08-06 16:36:47 UTC+0000
0xfffffa8003ff9060 chrome.exe             4612   4456     17      229      1      0 2024-08-06 16:36:55 UTC+0000
0xfffffa8004846060 taskhost.exe           3620    552      5       96      1      0 2024-08-06 16:37:06 UTC+0000
0xfffffa8004412060 chrome.exe             4204   4456     11      191      1      0 2024-08-06 16:37:16 UTC+0000
0xfffffa8004403b00 cmd.exe                3944   1172      1       20      1      0 2024-08-06 16:45:56 UTC+0000
0xfffffa8006d58060 conhost.exe            4188    460      2       53      1      0 2024-08-06 16:45:56 UTC+0000
0xfffffa8003c9c4f0 notepad.exe            2592   1172      1       58      1      0 2024-08-06 16:47:20 UTC+0000
0xfffffa8003f3cb00 chrome.exe             3764   4456     17      253      1      0 2024-08-06 17:24:44 UTC+0000
0xfffffa8003cebb00 chrome.exe             2608   4456     17      250      1      0 2024-08-06 17:24:45 UTC+0000
0xfffffa800447c060 chrome.exe             3612   4456     17      253      1      0 2024-08-06 17:24:48 UTC+0000
0xfffffa800446a9a0 chrome.exe             3172   4456     17      258      1      0 2024-08-06 17:24:52 UTC+0000
0xfffffa800443e060 chrome.exe             3704   4456     17      253      1      0 2024-08-06 17:24:55 UTC+0000
0xfffffa80047c5060 chrome.exe             4452   4456     17      270      1      0 2024-08-06 17:25:33 UTC+0000
0xfffffa8004031290 chrome.exe             4836   4456     17      241      1      0 2024-08-06 17:26:01 UTC+0000
0xfffffa8003d47860 chrome.exe             2168   4456     17      231      1      0 2024-08-06 17:27:52 UTC+0000
0xfffffa8004a7fb00 chrome.exe             3808   4456     21      254      1      0 2024-08-06 18:15:29 UTC+0000
0xfffffa800437b4d0 chrome.exe             3740   4456     12      164      1      0 2024-08-06 18:32:47 UTC+0000
0xfffffa8003e86060 taskeng.exe            4196   1004      4       89      0      0 2024-08-06 18:33:18 UTC+0000
0xfffffa80039c2490 mspaint.exe            2516   1172      7      142      1      0 2024-08-06 18:35:09 UTC+0000
0xfffffa8003d94060 svchost.exe            1648    552      7      112      0      0 2024-08-06 18:35:09 UTC+0000
0xfffffa80044d6700 SearchProtocol         4436   2460      9      285      0      0 2024-08-06 18:36:43 UTC+0000
0xfffffa80040403e0 SearchFilterHo         1496   2460      6      105      0      0 2024-08-06 18:36:43 UTC+0000
0xfffffa800491c600 audiodg.exe            4028    896      6      132      0      0 2024-08-06 18:37:14 UTC+0000
0xfffffa8003bcf420 DumpItog.exe           4960   1172      5       56      1      1 2024-08-06 18:37:17 UTC+0000
0xfffffa80045dca30 conhost.exe            4140    460      2       53      1      0 2024-08-06 18:37:17 UTC+0000

```

Sus Processes !!!


cmd.exe (PID 3944) - Command prompt was used
notepad.exe (PID 2592) - A notepad was open 
mspaint.exe (PID 2516) - Paint was running (hate paint recovery smh)
Multiple chrome.exe processes - Browser activity maybe 


Lets see cmdscan to check if there's anything interesing 

<img width="1427" height="489" alt="image" src="https://github.com/user-attachments/assets/d7789d80-4ffe-4422-80b0-6f106dc07a48" />


```
Cmd #4: Ymkwc2N0Znt3M2xjMG0zXw==
Cmd #5: azr43ln1ght.github.io
Cmd #6: Azr43lKn1ght
Cmd #7: did you find flag1?
```
 Oh thats b64 which translates to - bi0sctf{w3lc0m3_ 


 Next i tried using notepad to see but the version mismatch of vol breaks it . 

 So i tried dumping the memory and tried to strings from it for clues 


there were nothing helpful but loads of data like , dll info but something randoly was a link 
i followed the link and got here 
<img width="1156" height="319" alt="image" src="https://github.com/user-attachments/assets/f7ac2ee8-d44d-427e-a062-aa8edf9715a2" />
this was again a b64 which translates to h0p3_th15_ 

I also noticed in the filescan output there's a flag5.rar file on the Desktop! Let's extract it: : p


```
PS D:\DFIR> Set-Alias vol "C:\Users\SIDDHARTH U\Downloads\volatility_2.6_win64_standalone\volatility_2.6_win64_standalone\volatility_2.6_win64_standalone.exe"; vol -f "D:\DFIR\gotham.raw" --profile=Win7SP1x64 dumpfiles -Q 0x000000011fdaff20 --dump-dir="D:\DFIR"       
Volatility Foundation Volatility Framework 2.6
DataSectionObject 0x11fdaff20   None   \Device\HarddiskVolume2\Users\bruce\Desktop\flag5.rarp\VirtualBox Dropped Files\2024-08-06T18_36_43.522668500Z\flag5.rar
```
