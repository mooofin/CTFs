First lets run imageinfo using KDGB

<img width="1918" height="391" alt="image" src="https://github.com/user-attachments/assets/e0af3b2c-ebde-4ff4-b0f1-7c44b7fed9e3" />


Then lets see what proccess are there 

<img width="1236" height="919" alt="image" src="https://github.com/user-attachments/assets/cb439154-ce60-46a2-8a72-772d4333f388" />

Next , wel'll have to use a plugin called psxview :3 

<img width="1156" height="340" alt="image" src="https://github.com/user-attachments/assets/0b5ae541-b50f-48cb-bc61-b64f80a87198" />


It  cross-checks multiple methods (pslist, pstree, thrdproc, etc.) to find processes that might be hidden by rootkits.

```
C:\Users\SIDDHARTH U\Downloads\volatility_2.6_win64_standalone\volatility_2.6_win64_standalone>volatility_2.6_win64_standalone.exe -f "C:\Users\SIDDHARTH U\Downloads\MemLabs-Lab4\MemoryDump_Lab4.raw" --profile=Win7SP1x64 psxview
Volatility Foundation Volatility Framework 2.6
Offset(P)          Name                    PID pslist psscan thrdproc pspcid csrss session deskthrd ExitTime
------------------ -------------------- ------ ------ ------ -------- ------ ----- ------- -------- --------
0x000000003e920350 conhost.exe            2636 True   True   True     True   True  True    True
0x000000003f1c1b30 services.exe            472 True   True   True     True   True  True    False
0x000000003fc62b30 dwm.exe                3000 True   True   True     True   True  True    True
0x000000003e930060 winlogon.exe           2728 True   True   True     True   True  True    True
0x000000003ec1b890 svchost.exe             220 True   True   True     True   True  True    True
0x000000003e8f0610 GoogleCrashHan         2272 True   True   True     True   True  True    False
0x000000003eaa4420 DumpIt.exe             2624 True   True   True     True   True  True    True
0x000000003efb9b30 svchost.exe             840 True   True   True     True   True  True    False
0x000000003ecaab30 spoolsv.exe            1132 True   True   True     True   True  True    True
0x000000003fceeb30 VBoxTray.exe           2384 True   True   True     True   True  True    True
0x000000003efacb30 svchost.exe             804 True   True   True     True   True  True    True
0x000000003eec1b30 lsm.exe                 488 True   True   True     True   True  True    False
0x000000003eaf7b30 explorer.exe           1944 True   True   True     True   True  True    True
0x000000003e86e910 SearchProtocol         1696 True   True   True     True   True  True    True
0x000000003fcaeb30 explorer.exe           3012 True   True   True     True   True  True    True
0x000000003ed81b30 taskhost.exe           1804 True   True   True     True   True  True    True
0x000000003ef30b30 VBoxService.ex          640 True   True   True     True   True  True    False
0x000000003eeb5940 lsass.exe               480 True   True   True     True   True  True    False
0x000000003eff1060 audiodg.exe             952 True   True   True     True   True  True    True
0x000000003e892b30 dllhost.exe            2076 True   True   True     True   True  True    True
0x000000003ec45630 svchost.exe             484 True   True   True     True   True  True    True
0x000000003fc54b30 taskhost.exe           2976 True   True   True     True   True  True    True
0x000000003efc6850 svchost.exe             864 True   True   True     True   True  True    True
0x000000003e8f6b30 GoogleCrashHan         2284 True   True   True     True   True  True    False
0x000000003edf9630 taskeng.exe            1824 True   True   True     True   True  True    False
0x000000003ecd7b30 svchost.exe            1176 True   True   True     True   True  True    True
0x000000003ed452e0 svchost.exe            1276 True   True   True     True   True  True    True
0x000000003fd18b30 StikyNot.exe           2432 True   True   True     True   True  True    True
0x000000003ee6f760 wininit.exe             384 True   True   True     True   True  True    True
0x000000003e879890 SearchFilterHo         1688 True   True   True     True   True  True    True
0x000000003ebabab0 VBoxTray.exe           1592 True   True   True     True   True  True    True
0x000000003eabbb30 dwm.exe                1908 True   True   True     True   True  True    True
0x000000003ee751f0 winlogon.exe            412 True   True   True     True   True  True    True
0x000000003ef43a70 svchost.exe             708 True   True   True     True   True  True    True
0x000000003e801ab0 SearchIndexer.         1068 True   True   True     True   True  True    False
0x000000003ef02b30 svchost.exe             580 True   True   True     True   True  True    False
0x000000003ff67960 csrss.exe               376 True   True   True     True   False True    True
0x000000003ee57b30 csrss.exe               328 True   True   True     True   False True    True
0x000000003ff5f040 System                    4 True   True   True     True   False False   False
0x000000003f6af950 smss.exe                256 True   True   True     True   False False   False
0x000000003eeac460 csrss.exe              2700 True   True   True     True   False True    True
0x000000003edfab30 LogonUI.exe            2148 False  True   False    False  False False   False    2019-06-29 07:29:59 UTC+0000
0x000000003ea94630 csrss.exe              2672 False  True   False    False  False False   False    2019-06-29 07:29:59 UTC+0000
0x000000003fc5ab30 dllhost.exe            2572 False  True   False    False  False False   False    2019-06-29 07:30:07 UTC+0000

```

