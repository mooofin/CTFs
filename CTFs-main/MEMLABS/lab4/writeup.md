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

Ok uhm there's a wierd proccess called StikyNot i can see . 

and 2 proccess which were hidden 

```
0x000000003ff67960 csrss.exe               376 True   True   True     True   False True    True
0x000000003ee57b30 csrss.exe               328 True   True   True     True   False True    True

```

My idea for now is to see what commands did these proccess run ?


for that cmdsline will help us 


<img width="927" height="647" alt="image" src="https://github.com/user-attachments/assets/6455e1c4-faec-4d25-bf4d-097df2158932" />


After that , we can see that , it spwaned stickey note program .

<img width="1919" height="324" alt="image" src="https://github.com/user-attachments/assets/c40d34db-1f60-4695-9e62-7dd972d6e2aa" />


We'll dump the exe and see it later .


Moving onto to finding interesting stuff , a focus should be on identifying what kind of files are in the memory dump . 


There are a lot of files now , but the user of the PC is called slim shady , so i'll search what files is under him or related to slimshady .
```
Volatility Foundation Volatility Framework 2.6
0x000000003e839710      2      2 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_256.db
0x000000003e83b2d0      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\Videos\desktop.ini
0x000000003e88a8c0      1      1 -W-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Temp\FXSAPIDebugLogFile.txt
0x000000003e88ba20      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Themes\slideshow.ini
0x000000003e89b070     15      0 RW-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Local\GDIPFONTCACHEV1.DAT
0x000000003e8a85b0      2      0 RW-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Recent\Flag not here.lnk
0x000000003e8a9610     16      0 RW-r-- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\1b4dd67f29cb1962.automaticDestinations-ms
0x000000003e8aa6f0      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Recent\desktop.ini
0x000000003e8ab250      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_256.db
0x000000003e8acc40     17      1 RW-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Cookies\index.dat
0x000000003e8ad250     14      0 R--r-- \Device\HarddiskVolume2\Users\eminem\Desktop\galf.jpeg
0x000000003e8af4a0     17      1 RW-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5\index.dat
0x000000003e8b04e0     15      0 RW-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\History\History.IE5\index.dat
0x000000003e8b1a50      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\History\desktop.ini
0x000000003e8b2a80      1      1 RW-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\History\History.IE5\index.dat
0x000000003e8bbf20      4      1 RWD--- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Temp\~PID8EC.tmp
0x000000003e8c01a0      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_idx.db
0x000000003e8cdb20     15      0 RW-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\History\History.IE5\MSHist012019062920190630\index.dat
0x000000003e8ce500      8      1 RWD--- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Temp\~PIDAB5.tmp
0x000000003e8ce650      1      1 RW-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\History\History.IE5\MSHist012019062920190630\index.dat
0x000000003e8d19e0     16      0 R--r-- \Device\HarddiskVolume2\Users\eminem\Desktop\Screenshot1.png
0x000000003e8d1c80      2      0 RW-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Recent\galf.lnk
0x000000003e8d7dd0      2      0 R--r-- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations\337ed59af273c758.customDestinations-ms
0x000000003e8da350      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_sr.db
0x000000003e8da630      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\Desktop\DumpIt
0x000000003e8e5a50      8      1 RWD--- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Temp\~PIE007.tmp
0x000000003e8e5ba0      2      0 RW-rw- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Recent\Screenshot1.lnk
0x000000003e8e83c0      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\Links
0x000000003e8ecc80      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_32.db
0x000000003e8ecdd0      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_idx.db
0x000000003e8f1aa0      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\Links\desktop.ini
0x000000003e8fc590      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Network Shortcuts
0x000000003e9058a0      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_1024.db
0x000000003e905b80      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_96.db
0x000000003e912190      6      0 R--r-d \Device\HarddiskVolume2\Users\eminem\Desktop\DumpIt\DumpIt.exe
0x000000003e915070      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\Links
0x000000003e9189d0     10      0 R--r-d \Device\HarddiskVolume2\Users\eminem\Desktop\DumpIt\DumpIt.exe
0x000000003e921a30     16      0 R--r-- \Device\HarddiskVolume2\Users\eminem\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content\94308059B57B3142E455B38A6EB92015
0x000000003e922070      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\Desktop\DumpIt
0x000000003e925ab0      2      2 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_sr.db
0x000000003ea20070      1      1 RW-rwd \Device\clfs\Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\UsrClass.dat{a96b97fe-96f7-11e9-9a46-0800275e72bc}.TM
0x000000003ea28c10      2      1 RW-r-- \Device\HarddiskVolume2\Users\eminem\NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms
0x000000003ea34c10      1      1 RW---- \Device\HarddiskVolume2\Users\eminem\NTUSER.DAT
0x000000003ea35ac0      1      1 RW---- \Device\HarddiskVolume2\Users\eminem\ntuser.dat.LOG1
0x000000003ea35f20      1      1 RW---- \Device\HarddiskVolume2\Users\eminem\ntuser.dat.LOG2
0x000000003ea366b0      2      1 RW-r-- \Device\HarddiskVolume2\Users\eminem\NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms
0x000000003ea37ad0      1      1 RW-rwd \Device\clfs\Device\HarddiskVolume2\Users\eminem\NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TM
0x000000003ea38dd0      2      1 RW-r-- \Device\HarddiskVolume2\Users\eminem\NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf
0x000000003ea41960      2      1 RW-rw- \Device\clfs\Device\HarddiskVolume2\Users\eminem\NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TM
0x000000003ea44dd0      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Printer Shortcuts
0x000000003ea60640      1      1 RW---- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\UsrClass.dat
0x000000003ea64850      1      1 RW---- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\UsrClass.dat.LOG2
0x000000003ea64f20      1      1 RW---- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\UsrClass.dat.LOG1
0x000000003ea66dc0      2      1 RW-r-- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\UsrClass.dat{a96b97fe-96f7-11e9-9a46-0800275e72bc}.TM.blf
0x000000003ea6cf20      2      1 RW-r-- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\UsrClass.dat{a96b97fe-96f7-11e9-9a46-0800275e72bc}.TMContainer00000000000000000001.regtrans-ms
0x000000003ea6d070      2      1 RW-r-- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\UsrClass.dat{a96b97fe-96f7-11e9-9a46-0800275e72bc}.TMContainer00000000000000000002.regtrans-ms
0x000000003ea75370      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Credentials
0x000000003ea7ea70     16      0 R--rw- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Caches\cversions.1.db
0x000000003ea83890      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Credentials
0x000000003eaa4d00      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Libraries\Pictures.library-ms
0x000000003eaa8ea0      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_32.db
0x000000003eae05d0      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\Pictures\desktop.ini
0x000000003eafe3c0     14      0 R--r-- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Caches\{AFBF9F1A-8EE8-4C77-AF34-C647E37CA0D9}.1.ver0x0000000000000006.db
0x000000003eb04f20      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_32.db
0x000000003eb219e0      8      0 R--r-- \Device\HarddiskVolume2\Users\eminem\AppData\Local\IconCache.db
0x000000003eb27070      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Libraries\Videos.library-ms
0x000000003eb5ad10      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\Desktop
0x000000003eb78f20      2      0 R--rw- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Google Chrome.lnk
0x000000003eb89790      2      2 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_96.db
0x000000003eb8ab30     16      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Burn\Burn\desktop.ini
0x000000003eb8bc90      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\desktop.ini
0x000000003eb914f0      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Burn
0x000000003eb91820     16      0 R--rwd \Device\HarddiskVolume2\Users\eminem\Desktop\desktop.ini
0x000000003eb91970      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Burn
0x000000003eb94a20     16      0 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_32.db
0x000000003eb95070     10      0 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_96.db
0x000000003eb95bb0      2      0 R--rw- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Internet Explorer.lnk
0x000000003eba2070      2      0 R--rw- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Windows Media Player.lnk
0x000000003eba33b0      2      0 R--rw- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Windows Explorer.lnk
0x000000003eba3e60      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\Desktop
0x000000003eba4d00     16      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Start Menu\desktop.ini
0x000000003eba84b0     16      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\desktop.ini
0x000000003eba9d10     15      0 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_256.db
0x000000003ebaaf20      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Desktop.ini
0x000000003ebab1e0      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Accessibility\Desktop.ini
0x000000003ebab650      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Maintenance\Desktop.ini
0x000000003ebac710      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Administrative Tools\desktop.ini
0x000000003ebaee50     16      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini
0x000000003ebafa90      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\System Tools\Desktop.ini
0x000000003ebb1070     16      0 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_idx.db
0x000000003ebb36c0     16      0 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_1024.db
0x000000003ebb5440      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned
0x000000003ebb91f0      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Start Menu
0x000000003ebb99c0     16      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Libraries\desktop.ini
0x000000003ebbaea0      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Start Menu
0x000000003ebbca20      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned
0x000000003ebbfa70      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\desktop.ini
0x000000003ebc0690      8      0 R--r-- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper.jpg
0x000000003ebc1670     16      0 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_sr.db
0x000000003ebccdd0      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Libraries\Documents.library-ms
0x000000003ebcd590      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\Documents\desktop.ini
0x000000003ebd05e0      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Libraries
0x000000003ebd1070      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Libraries
0x000000003ebd2570      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Libraries\Music.library-ms
0x000000003ebdc890      2      0 R--rwd \Device\HarddiskVolume2\Users\eminem\Music\desktop.ini
0x000000003ebe2a20      1      1 RW-rw- \Device\HarddiskVolume2\Users\eminem\Desktop\DumpIt\2PAC-20190629-072925.raw
0x000000003ebe38e0      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_256.db
0x000000003ebeedc0      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Printer Shortcuts
0x000000003ec36d80      2      2 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_32.db
0x000000003ec45300      2      2 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_idx.db
0x000000003ecd4070      2      0 R--r-- \Device\HarddiskVolume2\Users\eminem\AppData\LocalLow\Microsoft\CryptnetUrlCache\MetaData\94308059B57B3142E455B38A6EB92015
0x000000003edeb470      2      1 RW-rw- \Device\clfs\Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\UsrClass.dat{a96b97fe-96f7-11e9-9a46-0800275e72bc}.TM
0x000000003eeb97d0      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_96.db
0x000000003eebb430      2      2 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_1024.db
0x000000003ef033f0      2      1 R--rwd \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Network Shortcuts
0x000000003ef47f20      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_idx.db
0x000000003eff6f20     16      0 R--r-- \Device\HarddiskVolume2\Users\eminem\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations\5afe4de1b92fc382.customDestinations-ms
0x000000003f602590      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_1024.db
0x000000003f7daa90      4      1 RWD--- \Device\HarddiskVolume2\Users\eminem\AppData\Local\Temp\~PID92B.tmp
0x000000003f9ccf20      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_sr.db
0x000000003f9ce930      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_1024.db
0x000000003f9cea80      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_256.db
0x000000003f9cebd0      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_96.db
0x000000003f9ffcb0      1      1 R--rw- \Device\HarddiskVolume2\Users\eminem\Desktop\DumpIt
0x000000003fc48070      1      1 RW-rwd \Device\HarddiskVolume2\Users\eminem\AppData\Local\Microsoft\Windows\Explorer\thumbcache_sr.db

C:\Users\SIDDHARTH U\Downloads\volatility_2.6_win64_standalone\volatility_2.6_win64_standalone>volatility_2.6_win64_standalone.exe -f "C:\Users\SIDDHARTH U\Downloads\MemLabs-Lab4\MemoryDump_Lab4.raw" --profile=Win7SP1x64 filescan | findstr "SlimShady"
Volatility Foundation Volatility Framework 2.6
0x000000003e900e60      2      1 RW-r-- \Device\HarddiskVolume2\Users\SlimShady\NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms
0x000000003e90df20      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\History\desktop.ini
0x000000003ed01740      1      1 RW-rwd \Device\clfs\Device\HarddiskVolume2\Users\SlimShady\NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TM
0x000000003ed382c0      2      1 RW-r-- \Device\HarddiskVolume2\Users\SlimShady\NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms
0x000000003ee47750      2      1 RW-rw- \Device\clfs\Device\HarddiskVolume2\Users\SlimShady\NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TM
0x000000003ee49c40      2      1 RW-r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\UsrClass.dat{8381e871-9808-11e9-b1e1-0800275e72bc}.TM.blf
0x000000003ee4b480      1      1 RW---- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\UsrClass.dat.LOG1
0x000000003ee4b5d0      1      1 RW---- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\UsrClass.dat
0x000000003ee4cb20      2      1 RW-r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\UsrClass.dat{8381e871-9808-11e9-b1e1-0800275e72bc}.TMContainer00000000000000000002.regtrans-ms
0x000000003ee4cc70      1      0 R--r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations\337ed59af273c758.customDestinations-ms
0x000000003ee4cf20      1      1 RW---- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\UsrClass.dat.LOG2
0x000000003ee8e8c0      1      1 RW---- \Device\HarddiskVolume2\Users\SlimShady\ntuser.dat.LOG1
0x000000003ee9b590     16      0 RW-r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\9b9cdc69c1c24e2b.automaticDestinations-ms
0x000000003eeb6950      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Printer Shortcuts
0x000000003eeb7bb0     16      0 RW-r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\1b4dd67f29cb1962.automaticDestinations-ms
0x000000003eed64e0     16      0 R--rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Caches\cversions.1.db
0x000000003eeec530     15      0 RW-rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\History\History.IE5\MSHist012019062920190630\index.dat
0x000000003eeef070     17      1 RW-rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5\index.dat
0x000000003f631070      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Printer Shortcuts
0x000000003f633d50      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Recent\desktop.ini
0x000000003f666aa0      1      1 RW---- \Device\HarddiskVolume2\Users\SlimShady\ntuser.dat.LOG2
0x000000003f939720      2      0 RW-rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Recent\Important.lnk
0x000000003f9ff6d0      1      1 RW---- \Device\HarddiskVolume2\Users\SlimShady\NTUSER.DAT
0x000000003f9ff8e0      2      1 RW-r-- \Device\HarddiskVolume2\Users\SlimShady\NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf
0x000000003fc398d0     16      0 R--rw- \Device\HarddiskVolume2\Users\SlimShady\Desktop\Important.txt
0x000000003fc39a20     17      1 RW-rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\History\History.IE5\index.dat
0x000000003fc39cd0      2      1 RW-r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\UsrClass.dat{8381e871-9808-11e9-b1e1-0800275e72bc}.TMContainer00000000000000000001.regtrans-ms
0x000000003fc39f20      1      1 RW-rwd \Device\clfs\Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\UsrClass.dat{8381e871-9808-11e9-b1e1-0800275e72bc}.TM
0x000000003fc3c910      2      1 RW-rw- \Device\clfs\Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\UsrClass.dat{8381e871-9808-11e9-b1e1-0800275e72bc}.TM
0x000000003fc3dbb0      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Credentials
0x000000003fc3dd00      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Credentials
0x000000003fcbd070      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Burn\Burn\desktop.ini
0x000000003fcc5140     13      0 R--r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\IconCache.db
0x000000003fce9640     15      0 R--r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Caches\{AFBF9F1A-8EE8-4C77-AF34-C647E37CA0D9}.1.ver0x0000000000000003.db
0x000000003fcedca0      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Accessibility\Desktop.ini
0x000000003fcee070      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Maintenance\Desktop.ini
0x000000003fcee1e0      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Administrative Tools\desktop.ini
0x000000003fcf0a20      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\desktop.ini
0x000000003fcf9690     16      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\Desktop\desktop.ini
0x000000003fcfa070      2      0 R--rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Internet Explorer.lnk
0x000000003fcfb240      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Burn
0x000000003fcfba20      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\desktop.ini
0x000000003fcfc7c0      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Burn
0x000000003fcfd320      2      0 R--rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Google Chrome.lnk
0x000000003fcfd5c0      1      1 RW-rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\History\History.IE5\MSHist012019062920190630\index.dat
0x000000003fcfd920      2      0 R--rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Windows Media Player.lnk
0x000000003fcfdb00      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\Desktop
0x000000003fcfe810      2      0 R--rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Windows Explorer.lnk
0x000000003fcfeac0      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\Desktop
0x000000003fcfef20      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Desktop.ini
0x000000003fd00280      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Start Menu\desktop.ini
0x000000003fd0a970      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Libraries\Documents.library-ms
0x000000003fd0b070      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Libraries\desktop.ini
0x000000003fd0b480      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini
0x000000003fd13850      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\Documents\desktop.ini
0x000000003fd15800      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Libraries\Pictures.library-ms
0x000000003fd17c80      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Libraries
0x000000003fd17dd0      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Libraries
0x000000003fd1a340      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\Pictures\desktop.ini
0x000000003fd1bd50     11      0 R--r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper.jpg
0x000000003fd1c490     18      2 RW-rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Explorer\thumbcache_32.db
0x000000003fd1c5e0      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Libraries\Music.library-ms
0x000000003fd214d0     18      2 RW-rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Explorer\thumbcache_256.db
0x000000003fd22d90     18      2 RW-rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Explorer\thumbcache_idx.db
0x000000003fd23d10      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\desktop.ini
0x000000003fd24c70     18      2 RW-rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Explorer\thumbcache_96.db
0x000000003fd252e0      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\Music\desktop.ini
0x000000003fd25bc0     18      2 RW-rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Explorer\thumbcache_1024.db
0x000000003fd26840     18      2 RW-rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Local\Microsoft\Windows\Explorer\thumbcache_sr.db
0x000000003fd276c0      2      0 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\System Tools\Desktop.ini
0x000000003fd32070      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Start Menu
0x000000003fd32740      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned
0x000000003fd32890      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned
0x000000003fd32c80      2      1 R--rwd \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Start Menu
0x000000003fd3d6d0     17      1 RW-rw- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Cookies\index.dat
0x000000003fd40910     17      1 RW-r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Sticky Notes\StickyNotes.snt
0x000000003ff3dca0      1      0 R--r-- \Device\HarddiskVolume2\Users\SlimShady\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations\5afe4de1b92fc382.customDestinations-ms
```
