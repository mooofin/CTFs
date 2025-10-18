kdbgscan is responsible for locating the Kernel Debugger Block (KDBG) within a memory dump. The KDBG is a core Windows kernel structure that stores critical metadata about the running operating system, including the kernel base address, OS build number,offsets to important kernel structures, and even information about active processes and loaded modules.

The way kdbgscan works is by scanning the memory dump for signatures that match the KDBG structure. Once found, it reports the addresses of the KDBG and other related kernel data. This allows Volatility to map the memory correctly and select the proper kernel symbols (PDBs) for analysis. For example, running vol -f MemoryDump_Lab1.raw windows.kdbgscan will output the kernel base, directory table base, and OS build number, all of which are essential for the other plugins to work properly.

<img width="1633" height="693" alt="image" src="https://github.com/user-attachments/assets/64e66429-b522-4793-8df0-9754b60f52e9" />

After running pslist to see what all ran in the time the PC crashed i used PSlist 


<img width="1073" height="966" alt="image" src="https://github.com/user-attachments/assets/86150cd5-6191-41a6-a7ad-d8bfc050e3d4" />


I could see System and smss.exe at the top, followed by critical processes like csrss.exe, winlogon.exe, and services.exe. Each entry showed the PID, parent PID, number of threads, handles, session IDs, and creation times. It was satisfying to watch the familiar Windows processes appear alongside some user-level programs like explorer.exe, mspaint.exe, and even DumpIt.exe, which hinted at how the memory dump was created

Also  Vol3 automatically reads the KDBG structure from the memory dump and maps the kernel symbols for me.


These processes seem to be very out of place WinRAR.exe, mspaint.exe, wmpnetwk.exe 

So lemme dump these and look more inside .

As a standard practise that i saw on last lab its good to see what all the computer was interacting with before it shut down . So we'll use netscan plugin : (


<img width="1918" height="916" alt="image" src="https://github.com/user-attachments/assets/1952db81-630a-4bfb-a245-947592dd11a2" />


There's a wierd uh name under owner tag called ?J3???? ? 



This might be the hacked process ig . 

moving on to see if that had commmunicated with any console to run any commands to run output , ill use the console plugin .


<img width="1878" height="897" alt="image" src="https://github.com/user-attachments/assets/7cf7a543-2336-426c-a65f-883aeacfd455" />

This was very abnormal and i think one of them is a b64 flag and i see dumpit.exe which was used to make the .raw dump .



 
