Lets check the profile info 

<img width="1919" height="646" alt="image" src="https://github.com/user-attachments/assets/005c153a-890d-456e-a80a-fa5f5bcf6ccc" />


This came from a 64-bit Windows 7 SP1 machine . 


<img width="1912" height="954" alt="image" src="https://github.com/user-attachments/assets/53753f06-b31a-4709-b13b-2bf0fdfc5403" />


cmd.exe (PID 880) — suggests manual command-line activity.

chrome.exe instances (PIDs 2124, 2132, 2168, 2340, etc.) — multiple browser tabs 

firefox.exe cluster (PIDs 2080–3316) — another browser session, possibly used concurrently

WinRAR.exe (PID 3716) — indicates file compression/extraction activity like before 


Lets dump wintrar , it should be a direct indication of something 

<img width="1914" height="174" alt="image" src="https://github.com/user-attachments/assets/f4e9b2e8-b120-46d7-851e-9301c990ae7c" />

Yes and now let's dump it

<img width="1893" height="340" alt="image" src="https://github.com/user-attachments/assets/f884f393-975b-4ea7-aba5-d0095530cf87" />


AFter trying to unrar it , well it needs a password :((


```
C:\Users\SIDDHARTH U\Downloads\volatility_2.6_win64_standalone\volatility_2.6_win64_standalone>volatility_2.6_win64_standalone.exe --plugins=plugins/ -f "C:\Users\SIDDHARTH U\Downloads\MemLabs-Lab6\MemoryDump_Lab6.raw" --profile=Win7SP1x64 consoles
Volatility Foundation Volatility Framework 2.6
**************************************************
ConsoleProcess: conhost.exe Pid: 916
Console: 0xff086200 CommandHistorySize: 50
HistoryBufferCount: 2 HistoryBufferMax: 4
OriginalTitle: %SystemRoot%\system32\cmd.exe
Title: C:\Windows\system32\cmd.exe
AttachedProcess: cmd.exe Pid: 880 Handle: 0x60
----
CommandHistory: 0x1fedc0 Application: whoami.exe Flags:
CommandCount: 0 LastAdded: -1 LastDisplayed: -1
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x0
----
CommandHistory: 0x1feab0 Application: cmd.exe Flags: Allocated, Reset
CommandCount: 2 LastAdded: 1 LastDisplayed: 1
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x60
Cmd #0 at 0x1fd530: whoami
Cmd #1 at 0x1fdde0: env
----
Screen 0x1e0f80 X:80 Y:300
Dump:
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Jaffa>whoami
virus-pc\jaffa

C:\Users\Jaffa>env
'env' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Jaffa>
**************************************************
ConsoleProcess: conhost.exe Pid: 4092
Console: 0xff086200 CommandHistorySize: 50
HistoryBufferCount: 1 HistoryBufferMax: 4
OriginalTitle: C:\Users\Jaffa\Desktop\DumpIt.exe
Title: C:\Users\Jaffa\Desktop\DumpIt.exe
AttachedProcess: DumpIt.exe Pid: 4084 Handle: 0x60
----
CommandHistory: 0x30eab0 Application: DumpIt.exe Flags: Allocated
CommandCount: 0 LastAdded: -1 LastDisplayed: -1
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x60
----
Screen 0x2f0f80 X:80 Y:300
Dump:
  DumpIt - v1.3.2.20110401 - One click memory memory dumper
  Copyright (c) 2007 - 2011, Matthieu Suiche <http://www.msuiche.net>
  Copyright (c) 2010 - 2011, MoonSols <http://www.moonsols.com>


    Address space size:        1610547200 bytes (   1535 Mb)
    Free space size:           9889345536 bytes (   9431 Mb)

    * Destination = \??\C:\Users\Jaffa\Desktop\VIRUS-PC-20190819-144155.raw

    --> Are you sure you want to continue? [y/n] y
    + Processing...
```


Jaffa tried running envars before dumpit.exe so that's a lead for us 

From pervious lab refrence , lets try runnning envars for all the sus proccess we saw earlier .

```
Volatility Foundation Volatility Framework 2.6
Pid      Process              Block              Variable                       Value
-------- -------------------- ------------------ ------------------------------ -----
    2124 chrome.exe           0x00000000003453f0 ALLUSERSPROFILE                C:\ProgramData
    2124 chrome.exe           0x00000000003453f0 APPDATA                        C:\Users\Jaffa\AppData\Roaming
    2124 chrome.exe           0x00000000003453f0 CHROME_CRASHPAD_PIPE_NAME      \\.\pipe\crashpad_2124_HYPTHIKRKHINVSMY
    2124 chrome.exe           0x00000000003453f0 CHROME_RESTART                 Google Chrome|Whoa! Google Chrome has crashed. Relaunch now?|LEFT_TO_RIGHT
    2124 chrome.exe           0x00000000003453f0 CommonProgramFiles             C:\Program Files\Common Files
    2124 chrome.exe           0x00000000003453f0 CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files
    2124 chrome.exe           0x00000000003453f0 CommonProgramW6432             C:\Program Files\Common Files
    2124 chrome.exe           0x00000000003453f0 COMPUTERNAME                   VIRUS-PC
    2124 chrome.exe           0x00000000003453f0 ComSpec                        C:\Windows\system32\cmd.exe
    2124 chrome.exe           0x00000000003453f0 FP_NO_HOST_CHECK               NO
    2124 chrome.exe           0x00000000003453f0 HOMEDRIVE                      C:
    2124 chrome.exe           0x00000000003453f0 HOMEPATH                       \Users\Jaffa
    2124 chrome.exe           0x00000000003453f0 LOCALAPPDATA                   C:\Users\Jaffa\AppData\Local
    2124 chrome.exe           0x00000000003453f0 LOGONSERVER                    \\VIRUS-PC
    2124 chrome.exe           0x00000000003453f0 NUMBER_OF_PROCESSORS           1
    2124 chrome.exe           0x00000000003453f0 OS                             Windows_NT
    2124 chrome.exe           0x00000000003453f0 Path                           C:\Program Files (x86)\Google\Chrome\Application;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\
    2124 chrome.exe           0x00000000003453f0 PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
    2124 chrome.exe           0x00000000003453f0 PROCESSOR_ARCHITECTURE         AMD64
    2124 chrome.exe           0x00000000003453f0 PROCESSOR_IDENTIFIER           Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
    2124 chrome.exe           0x00000000003453f0 PROCESSOR_LEVEL                6
    2124 chrome.exe           0x00000000003453f0 PROCESSOR_REVISION             9e0a
    2124 chrome.exe           0x00000000003453f0 ProgramData                    C:\ProgramData
    2124 chrome.exe           0x00000000003453f0 ProgramFiles                   C:\Program Files
    2124 chrome.exe           0x00000000003453f0 ProgramFiles(x86)              C:\Program Files (x86)
    2124 chrome.exe           0x00000000003453f0 ProgramW6432                   C:\Program Files
    2124 chrome.exe           0x00000000003453f0 PSModulePath                   C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
    2124 chrome.exe           0x00000000003453f0 PUBLIC                         C:\Users\Public
    2124 chrome.exe           0x00000000003453f0 RAR password                   easypeasyvirus
    2124 chrome.exe           0x00000000003453f0 SESSIONNAME                    Console
    2124 chrome.exe           0x00000000003453f0 SystemDrive                    C:
    2124 chrome.exe           0x00000000003453f0 SystemRoot                     C:\Windows
    2124 chrome.exe           0x00000000003453f0 TEMP                           C:\Users\Jaffa\AppData\Local\Temp
    2124 chrome.exe           0x00000000003453f0 TMP                            C:\Users\Jaffa\AppData\Local\Temp
    2124 chrome.exe           0x00000000003453f0 USERDOMAIN                     VIRUS-PC
    2124 chrome.exe           0x00000000003453f0 USERNAME                       Jaffa
    2124 chrome.exe           0x00000000003453f0 USERPROFILE                    C:\Users\Jaffa
    2124 chrome.exe           0x00000000003453f0 windir                         C:\Windows
    2124 chrome.exe           0x00000000003453f0 windows_tracing_flags          3
    2124 chrome.exe           0x00000000003453f0 windows_tracing_logfile        C:\BVTBin\Tests\installpackage\csilogfile.log
    2132 chrome.exe           0x0000000000561320 ALLUSERSPROFILE                C:\ProgramData
    2132 chrome.exe           0x0000000000561320 APPDATA                        C:\Users\Jaffa\AppData\Roaming
    2132 chrome.exe           0x0000000000561320 CommonProgramFiles             C:\Program Files\Common Files
    2132 chrome.exe           0x0000000000561320 CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files
    2132 chrome.exe           0x0000000000561320 CommonProgramW6432             C:\Program Files\Common Files
    2132 chrome.exe           0x0000000000561320 COMPUTERNAME                   VIRUS-PC
    2132 chrome.exe           0x0000000000561320 ComSpec                        C:\Windows\system32\cmd.exe
    2132 chrome.exe           0x0000000000561320 FP_NO_HOST_CHECK               NO
    2132 chrome.exe           0x0000000000561320 HOMEDRIVE                      C:
    2132 chrome.exe           0x0000000000561320 HOMEPATH                       \Users\Jaffa
    2132 chrome.exe           0x0000000000561320 LOCALAPPDATA                   C:\Users\Jaffa\AppData\Local
    2132 chrome.exe           0x0000000000561320 LOGONSERVER                    \\VIRUS-PC
    2132 chrome.exe           0x0000000000561320 NUMBER_OF_PROCESSORS           1
    2132 chrome.exe           0x0000000000561320 OS                             Windows_NT
    2132 chrome.exe           0x0000000000561320 Path                           C:\Program Files (x86)\Google\Chrome\Application;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\
    2132 chrome.exe           0x0000000000561320 PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
    2132 chrome.exe           0x0000000000561320 PROCESSOR_ARCHITECTURE         AMD64
    2132 chrome.exe           0x0000000000561320 PROCESSOR_IDENTIFIER           Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
    2132 chrome.exe           0x0000000000561320 PROCESSOR_LEVEL                6
    2132 chrome.exe           0x0000000000561320 PROCESSOR_REVISION             9e0a
    2132 chrome.exe           0x0000000000561320 ProgramData                    C:\ProgramData
    2132 chrome.exe           0x0000000000561320 ProgramFiles                   C:\Program Files
    2132 chrome.exe           0x0000000000561320 ProgramFiles(x86)              C:\Program Files (x86)
    2132 chrome.exe           0x0000000000561320 ProgramW6432                   C:\Program Files
    2132 chrome.exe           0x0000000000561320 PSModulePath                   C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
    2132 chrome.exe           0x0000000000561320 PUBLIC                         C:\Users\Public
    2132 chrome.exe           0x0000000000561320 RAR password                   easypeasyvirus
    2132 chrome.exe           0x0000000000561320 SESSIONNAME                    Console
    2132 chrome.exe           0x0000000000561320 SystemDrive                    C:
    2132 chrome.exe           0x0000000000561320 SystemRoot                     C:\Windows
    2132 chrome.exe           0x0000000000561320 TEMP                           C:\Users\Jaffa\AppData\Local\Temp
    2132 chrome.exe           0x0000000000561320 TMP                            C:\Users\Jaffa\AppData\Local\Temp
    2132 chrome.exe           0x0000000000561320 USERDOMAIN                     VIRUS-PC
    2132 chrome.exe           0x0000000000561320 USERNAME                       Jaffa
    2132 chrome.exe           0x0000000000561320 USERPROFILE                    C:\Users\Jaffa
    2132 chrome.exe           0x0000000000561320 windir                         C:\Windows
    2132 chrome.exe           0x0000000000561320 windows_tracing_flags          3
    2132 chrome.exe           0x0000000000561320 windows_tracing_logfile        C:\BVTBin\Tests\installpackage\csilogfile.log
    2168 chrome.exe           0x0000000000421320 ALLUSERSPROFILE                C:\ProgramData
    2168 chrome.exe           0x0000000000421320 APPDATA                        C:\Users\Jaffa\AppData\Roaming
    2168 chrome.exe           0x0000000000421320 CHROME_CRASHPAD_PIPE_NAME      \\.\pipe\crashpad_2124_HYPTHIKRKHINVSMY
    2168 chrome.exe           0x0000000000421320 CommonProgramFiles             C:\Program Files\Common Files
    2168 chrome.exe           0x0000000000421320 CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files
    2168 chrome.exe           0x0000000000421320 CommonProgramW6432             C:\Program Files\Common Files
    2168 chrome.exe           0x0000000000421320 COMPUTERNAME                   VIRUS-PC
    2168 chrome.exe           0x0000000000421320 ComSpec                        C:\Windows\system32\cmd.exe
    2168 chrome.exe           0x0000000000421320 FP_NO_HOST_CHECK               NO
    2168 chrome.exe           0x0000000000421320 HOMEDRIVE                      C:
    2168 chrome.exe           0x0000000000421320 HOMEPATH                       \Users\Jaffa
    2168 chrome.exe           0x0000000000421320 LOCALAPPDATA                   C:\Users\Jaffa\AppData\Local
    2168 chrome.exe           0x0000000000421320 LOGONSERVER                    \\VIRUS-PC
    2168 chrome.exe           0x0000000000421320 NUMBER_OF_PROCESSORS           1
    2168 chrome.exe           0x0000000000421320 OS                             Windows_NT
    2168 chrome.exe           0x0000000000421320 Path                           C:\Program Files (x86)\Google\Chrome\Application;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\
    2168 chrome.exe           0x0000000000421320 PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
    2168 chrome.exe           0x0000000000421320 PROCESSOR_ARCHITECTURE         AMD64
    2168 chrome.exe           0x0000000000421320 PROCESSOR_IDENTIFIER           Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
    2168 chrome.exe           0x0000000000421320 PROCESSOR_LEVEL                6
    2168 chrome.exe           0x0000000000421320 PROCESSOR_REVISION             9e0a
    2168 chrome.exe           0x0000000000421320 ProgramData                    C:\ProgramData
    2168 chrome.exe           0x0000000000421320 ProgramFiles                   C:\Program Files
    2168 chrome.exe           0x0000000000421320 ProgramFiles(x86)              C:\Program Files (x86)
    2168 chrome.exe           0x0000000000421320 ProgramW6432                   C:\Program Files
    2168 chrome.exe           0x0000000000421320 PSModulePath                   C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
    2168 chrome.exe           0x0000000000421320 PUBLIC                         C:\Users\Public
    2168 chrome.exe           0x0000000000421320 RAR password                   easypeasyvirus
    2168 chrome.exe           0x0000000000421320 SESSIONNAME                    Console
    2168 chrome.exe           0x0000000000421320 SystemDrive                    C:
    2168 chrome.exe           0x0000000000421320 SystemRoot                     C:\Windows
    2168 chrome.exe           0x0000000000421320 TEMP                           C:\Users\Jaffa\AppData\Local\Temp
    2168 chrome.exe           0x0000000000421320 TMP                            C:\Users\Jaffa\AppData\Local\Temp
    2168 chrome.exe           0x0000000000421320 USERDOMAIN                     VIRUS-PC
    2168 chrome.exe           0x0000000000421320 USERNAME                       Jaffa
    2168 chrome.exe           0x0000000000421320 USERPROFILE                    C:\Users\Jaffa
    2168 chrome.exe           0x0000000000421320 windir                         C:\Windows
    2168 chrome.exe           0x0000000000421320 windows_tracing_flags          3
    2168 chrome.exe           0x0000000000421320 windows_tracing_logfile        C:\BVTBin\Tests\installpackage\csilogfile.log
    2340 chrome.exe           0x0000000000551320 ALLUSERSPROFILE                C:\ProgramData
    2340 chrome.exe           0x0000000000551320 APPDATA                        C:\Users\Jaffa\AppData\Roaming
    2340 chrome.exe           0x0000000000551320 CHROME_CRASHPAD_PIPE_NAME      \\.\pipe\crashpad_2124_HYPTHIKRKHINVSMY
    2340 chrome.exe           0x0000000000551320 CommonProgramFiles             C:\Program Files\Common Files
    2340 chrome.exe           0x0000000000551320 CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files
    2340 chrome.exe           0x0000000000551320 CommonProgramW6432             C:\Program Files\Common Files
    2340 chrome.exe           0x0000000000551320 COMPUTERNAME                   VIRUS-PC
    2340 chrome.exe           0x0000000000551320 ComSpec                        C:\Windows\system32\cmd.exe
    2340 chrome.exe           0x0000000000551320 FP_NO_HOST_CHECK               NO
    2340 chrome.exe           0x0000000000551320 HOMEDRIVE                      C:
    2340 chrome.exe           0x0000000000551320 HOMEPATH                       \Users\Jaffa
    2340 chrome.exe           0x0000000000551320 LOCALAPPDATA                   C:\Users\Jaffa\AppData\Local
    2340 chrome.exe           0x0000000000551320 LOGONSERVER                    \\VIRUS-PC
    2340 chrome.exe           0x0000000000551320 NUMBER_OF_PROCESSORS           1
    2340 chrome.exe           0x0000000000551320 OS                             Windows_NT
    2340 chrome.exe           0x0000000000551320 Path                           C:\Program Files (x86)\Google\Chrome\Application;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\
    2340 chrome.exe           0x0000000000551320 PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
    2340 chrome.exe           0x0000000000551320 PROCESSOR_ARCHITECTURE         AMD64
    2340 chrome.exe           0x0000000000551320 PROCESSOR_IDENTIFIER           Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
    2340 chrome.exe           0x0000000000551320 PROCESSOR_LEVEL                6
    2340 chrome.exe           0x0000000000551320 PROCESSOR_REVISION             9e0a
    2340 chrome.exe           0x0000000000551320 ProgramData                    C:\ProgramData
    2340 chrome.exe           0x0000000000551320 ProgramFiles                   C:\Program Files
    2340 chrome.exe           0x0000000000551320 ProgramFiles(x86)              C:\Program Files (x86)
    2340 chrome.exe           0x0000000000551320 ProgramW6432                   C:\Program Files
    2340 chrome.exe           0x0000000000551320 PSModulePath                   C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
    2340 chrome.exe           0x0000000000551320 PUBLIC                         C:\Users\Public
    2340 chrome.exe           0x0000000000551320 RAR password                   easypeasyvirus
    2340 chrome.exe           0x0000000000551320 SESSIONNAME                    Console
    2340 chrome.exe           0x0000000000551320 SystemDrive                    C:
    2340 chrome.exe           0x0000000000551320 SystemRoot                     C:\Windows
    2340 chrome.exe           0x0000000000551320 TEMP                           C:\Users\Jaffa\AppData\Local\Temp
    2340 chrome.exe           0x0000000000551320 TMP                            C:\Users\Jaffa\AppData\Local\Temp
    2340 chrome.exe           0x0000000000551320 USERDOMAIN                     VIRUS-PC
    2340 chrome.exe           0x0000000000551320 USERNAME                       Jaffa
    2340 chrome.exe           0x0000000000551320 USERPROFILE                    C:\Users\Jaffa
    2340 chrome.exe           0x0000000000551320 windir                         C:\Windows
    2340 chrome.exe           0x0000000000551320 windows_tracing_flags          3
    2340 chrome.exe           0x0000000000551320 windows_tracing_logfile        C:\BVTBin\Tests\installpackage\csilogfile.log
    2080 firefox.exe          0x00000000005f1320 ALLUSERSPROFILE                C:\ProgramData
    2080 firefox.exe          0x00000000005f1320 APPDATA                        C:\Users\Jaffa\AppData\Roaming
    2080 firefox.exe          0x00000000005f1320 CommonProgramFiles             C:\Program Files\Common Files
    2080 firefox.exe          0x00000000005f1320 CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files
    2080 firefox.exe          0x00000000005f1320 CommonProgramW6432             C:\Program Files\Common Files
    2080 firefox.exe          0x00000000005f1320 COMPUTERNAME                   VIRUS-PC
    2080 firefox.exe          0x00000000005f1320 ComSpec                        C:\Windows\system32\cmd.exe
    2080 firefox.exe          0x00000000005f1320 FP_NO_HOST_CHECK               NO
    2080 firefox.exe          0x00000000005f1320 HOMEDRIVE                      C:
    2080 firefox.exe          0x00000000005f1320 HOMEPATH                       \Users\Jaffa
    2080 firefox.exe          0x00000000005f1320 LOCALAPPDATA                   C:\Users\Jaffa\AppData\Local
    2080 firefox.exe          0x00000000005f1320 LOGONSERVER                    \\VIRUS-PC
    2080 firefox.exe          0x00000000005f1320 NUMBER_OF_PROCESSORS           1
    2080 firefox.exe          0x00000000005f1320 OS                             Windows_NT
    2080 firefox.exe          0x00000000005f1320 Path                           C:\Program Files (x86)\Mozilla Firefox;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\
    2080 firefox.exe          0x00000000005f1320 PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
    2080 firefox.exe          0x00000000005f1320 PROCESSOR_ARCHITECTURE         AMD64
    2080 firefox.exe          0x00000000005f1320 PROCESSOR_IDENTIFIER           Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
    2080 firefox.exe          0x00000000005f1320 PROCESSOR_LEVEL                6
    2080 firefox.exe          0x00000000005f1320 PROCESSOR_REVISION             9e0a
    2080 firefox.exe          0x00000000005f1320 ProgramData                    C:\ProgramData
    2080 firefox.exe          0x00000000005f1320 ProgramFiles                   C:\Program Files
    2080 firefox.exe          0x00000000005f1320 ProgramFiles(x86)              C:\Program Files (x86)
    2080 firefox.exe          0x00000000005f1320 ProgramW6432                   C:\Program Files
    2080 firefox.exe          0x00000000005f1320 PSModulePath                   C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
    2080 firefox.exe          0x00000000005f1320 PUBLIC                         C:\Users\Public
    2080 firefox.exe          0x00000000005f1320 RAR password                   easypeasyvirus
    2080 firefox.exe          0x00000000005f1320 SESSIONNAME                    Console
    2080 firefox.exe          0x00000000005f1320 SystemDrive                    C:
    2080 firefox.exe          0x00000000005f1320 SystemRoot                     C:\Windows
    2080 firefox.exe          0x00000000005f1320 TEMP                           C:\Users\Jaffa\AppData\Local\Temp
    2080 firefox.exe          0x00000000005f1320 TMP                            C:\Users\Jaffa\AppData\Local\Temp
    2080 firefox.exe          0x00000000005f1320 USERDOMAIN                     VIRUS-PC
    2080 firefox.exe          0x00000000005f1320 USERNAME                       Jaffa
    2080 firefox.exe          0x00000000005f1320 USERPROFILE                    C:\Users\Jaffa
    2080 firefox.exe          0x00000000005f1320 windir                         C:\Windows
    2080 firefox.exe          0x00000000005f1320 windows_tracing_flags          3
    2080 firefox.exe          0x00000000005f1320 windows_tracing_logfile        C:\BVTBin\Tests\installpackage\csilogfile.log
    3716 WinRAR.exe           0x00000000002a1320 ALLUSERSPROFILE                C:\ProgramData
    3716 WinRAR.exe           0x00000000002a1320 APPDATA                        C:\Users\Jaffa\AppData\Roaming
    3716 WinRAR.exe           0x00000000002a1320 CommonProgramFiles             C:\Program Files\Common Files
    3716 WinRAR.exe           0x00000000002a1320 CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files
    3716 WinRAR.exe           0x00000000002a1320 CommonProgramW6432             C:\Program Files\Common Files
    3716 WinRAR.exe           0x00000000002a1320 COMPUTERNAME                   VIRUS-PC
    3716 WinRAR.exe           0x00000000002a1320 ComSpec                        C:\Windows\system32\cmd.exe
    3716 WinRAR.exe           0x00000000002a1320 FP_NO_HOST_CHECK               NO
    3716 WinRAR.exe           0x00000000002a1320 HOMEDRIVE                      C:
    3716 WinRAR.exe           0x00000000002a1320 HOMEPATH                       \Users\Jaffa
    3716 WinRAR.exe           0x00000000002a1320 LOCALAPPDATA                   C:\Users\Jaffa\AppData\Local
    3716 WinRAR.exe           0x00000000002a1320 LOGONSERVER                    \\VIRUS-PC
    3716 WinRAR.exe           0x00000000002a1320 NUMBER_OF_PROCESSORS           1
    3716 WinRAR.exe           0x00000000002a1320 OS                             Windows_NT
    3716 WinRAR.exe           0x00000000002a1320 Path                           C:\Program Files\WinRAR;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\
    3716 WinRAR.exe           0x00000000002a1320 PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
    3716 WinRAR.exe           0x00000000002a1320 PROCESSOR_ARCHITECTURE         AMD64
    3716 WinRAR.exe           0x00000000002a1320 PROCESSOR_IDENTIFIER           Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
    3716 WinRAR.exe           0x00000000002a1320 PROCESSOR_LEVEL                6
    3716 WinRAR.exe           0x00000000002a1320 PROCESSOR_REVISION             9e0a
    3716 WinRAR.exe           0x00000000002a1320 ProgramData                    C:\ProgramData
    3716 WinRAR.exe           0x00000000002a1320 ProgramFiles                   C:\Program Files
    3716 WinRAR.exe           0x00000000002a1320 ProgramFiles(x86)              C:\Program Files (x86)
    3716 WinRAR.exe           0x00000000002a1320 ProgramW6432                   C:\Program Files
    3716 WinRAR.exe           0x00000000002a1320 PSModulePath                   C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
    3716 WinRAR.exe           0x00000000002a1320 PUBLIC                         C:\Users\Public
    3716 WinRAR.exe           0x00000000002a1320 RAR password                   easypeasyvirus
    3716 WinRAR.exe           0x00000000002a1320 SESSIONNAME                    Console
    3716 WinRAR.exe           0x00000000002a1320 SystemDrive                    C:
    3716 WinRAR.exe           0x00000000002a1320 SystemRoot                     C:\Windows
    3716 WinRAR.exe           0x00000000002a1320 TEMP                           C:\Users\Jaffa\AppData\Local\Temp
    3716 WinRAR.exe           0x00000000002a1320 TMP                            C:\Users\Jaffa\AppData\Local\Temp
    3716 WinRAR.exe           0x00000000002a1320 USERDOMAIN                     VIRUS-PC
    3716 WinRAR.exe           0x00000000002a1320 USERNAME                       Jaffa
    3716 WinRAR.exe           0x00000000002a1320 USERPROFILE                    C:\Users\Jaffa
    3716 WinRAR.exe           0x00000000002a1320 windir                         C:\Windows
    3716 WinRAR.exe           0x00000000002a1320 windows_tracing_flags          3
    3716 WinRAR.exe           0x00000000002a1320 windows_tracing_logfile        C:\BVTBin\Tests\installpackage\csilogfile.log
```


oh we actually got the rar password and it wasnt the flag of the 2nd one ..

Now let's extrcat it 


and we get a 2nd'part of the flag? 

<img width="564" height="576" alt="image" src="https://github.com/user-attachments/assets/d18ac950-40c7-4b96-b17d-c188a99e3866" />

Since the  clues mentioned , a link to and we saw some chrome and firefox running mhmm lets try to see history . 

I found a amazing volatilyt plugin repo which helped [![Volatility Plugins](https://img.shields.io/badge/Volatility-Plugins-blue?logo=github)](https://github.com/superponible/volatility-plugins)

AFter spending a lot of time and clicking a lot of dead ends , i spotted a pastebin link which lead to

<img width="1229" height="449" alt="image" src="https://github.com/user-attachments/assets/520ec6e4-c310-4311-8f6f-7fea7c48d94f" />

mhm 

<img width="1861" height="867" alt="image" src="https://github.com/user-attachments/assets/fb4e084c-5637-418a-9928-c9851f35abbd" />

<img width="1862" height="886" alt="image" src="https://github.com/user-attachments/assets/736a9a85-326d-4045-9b60-f2dd11c16478" />

And it had a mega link which needed a mhmm , 

<img width="1847" height="868" alt="image" src="https://github.com/user-attachments/assets/a4e9568a-4d4c-43ee-a08a-b469f5fb2428" />


This needs a password and i spend a lot of time looking for what to do next as there wasnt anything explicit mentioned ..


