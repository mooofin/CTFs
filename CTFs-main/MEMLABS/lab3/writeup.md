Starting off like any lab , we will do imageinfo or kdgbscan to see info about the OS 

<img width="1900" height="348" alt="image" src="https://github.com/user-attachments/assets/5e2cc211-1499-4ee3-83dd-049eeec365f7" />


we can see that there are multiple window profiles ? so we might need to check for all the profiles ig 

Moving onto to see what processes were running might give us more insight 

<img width="1869" height="936" alt="image" src="https://github.com/user-attachments/assets/e678f017-0dbf-4602-86b1-5421b7ce6cbc" />



Also we see dump it .exe running , and its used to make the memory dump . A intuitive way to think about this is that whatever was running before dumpit.exe should be our focus and here we see 2 notepad.exe 's running . 


Now the workflow for any DFIR challenge is to dump the info that you see might be worth looking into , so lets do that 

<img width="1899" height="282" alt="image" src="https://github.com/user-attachments/assets/8b293c14-a499-4437-95c2-b0ba4bd1b08d" />

After running comndscan i got this 

<img width="1916" height="943" alt="image" src="https://github.com/user-attachments/assets/5ab8b2de-a9a1-47ef-94f1-71c00c69dd54" />


seems like no lead .

tehn i looked at the clues , which was about steghide ?? So i started searching for png , jpeg and jpg in the dump ..

And there was one actually :) jpeg 


<img width="1899" height="146" alt="image" src="https://github.com/user-attachments/assets/722aecbd-cbbc-4dec-acca-04144cd0b8ee" />


After dumping it and opening it i saw 

<img width="1407" height="686" alt="image" src="https://github.com/user-attachments/assets/6844b03e-94af-4ea0-9f32-15d5a0536452" />


So this image might have been steghided with a password and we'll need a password to uncover ig .

The way i thought was since steghide is a cmd line tool , the person who made the dump should run it on the commands line to steghide it . So the location or any insight could be that of getting the cmdline stdin .

<img width="1919" height="874" alt="image" src="https://github.com/user-attachments/assets/3a4f670d-dcd9-4334-a348-7914d5fd33ec" />

So yea , earlier we say two things running on notepad.exe that might have been this python encryption texts , 
```bash
notepad.exe pid:   3736
Command line : "C:\Windows\system32\NOTEPAD.EXE" C:\Users\hello\Desktop\evilscript.py
************************************************************************
notepad.exe pid:   3432
Command line : "C:\Windows\system32\NOTEPAD.EXE" C:\Users\hello\Desktop\vip.txt
```
<img width="1906" height="228" alt="image" src="https://github.com/user-attachments/assets/9fda83be-07d8-46a5-8266-d03c0830d789" />

Dumping them 

we get 


```
C:\Users\SIDDHARTH U\Downloads\volatility_2.6_win64_standalone\volatility_2.6_win64_standalone>type vip.txt
am1gd2V4M20wXGs3b2U=

C:\Users\SIDDHARTH U\Downloads\volatility_2.6_win64_standalone\volatility_2.6_win64_standalone>type evilscript.py
import sys
import string

def xor(s):

        a = ''.join(chr(ord(i)^3) for i in s)
        return a


def encoder(x):

        return x.encode("base64")


if __name__ == "__main__":

        f = open("C:\\Users\\hello\\Desktop\\vip.txt", "w")

        arr = sys.argv[1]

        arr = encoder(xor(arr))

        f.write(arr)

        f.close()
```
vip.txt  contained the base64 string `am1gd2V4M20wXGs3b2U=` and `evilscript.py` revealed the encoding routine: it XORs each character with the value 3 and then encodes the result with base64. Knowing this, I reversed the process by base64-decoding the `vip.txt` payload and XORing each byte with 3, which yielded the recovered secret: `inctf{0n3_h4lf}` :)



Since the description said , you need to use the first part to get the 2nd part i used the flag part 1 was a password to extract the info .

<img width="1895" height="366" alt="image" src="https://github.com/user-attachments/assets/a5d5939c-dc81-4cf1-9de7-0d6c6f44375a" />

and we got the 2nd half 

<img width="1236" height="72" alt="image" src="https://github.com/user-attachments/assets/a0296bea-0e0a-4b2f-9e89-b07fe4b64c7d" />


```bash
inctf{0n3_h4lf_1s_n0t_3n0ugh}
```
