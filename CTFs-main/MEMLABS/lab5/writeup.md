<img width="1919" height="1028" alt="image" src="https://github.com/user-attachments/assets/92283b1a-d49b-420a-b5c4-47872e81aa05" />

First rituals should be running pslist and kDBG scan 

<img width="1914" height="984" alt="image" src="https://github.com/user-attachments/assets/2ff35f7c-401d-461f-ac06-7f208e9efe7e" />

WIntrar !!, flahsbacks to first lab , we'll see if some zip file is there and try to dump it .

Okie so lets see what command was it used to spwan it from (not pstree but cmdline)

<img width="1898" height="129" alt="image" src="https://github.com/user-attachments/assets/b377bb93-d62f-433a-9429-7ed8f9e7ee55" />

we're onto something here . 

nvm it's actually the 2nd part and the password is the first part flag . (Hint: You’ll get the stage 2 flag only when you have the stage 1 flag.) opps


I tried to see deleated files , and then nothing happened .. 


Now lets move onto hidden files and see if filescan can get us something . 

Ok after locking in and reading the clues again , it's related to a network as the attacker is outside , so i started looking for plugins that could uncover this 

<img width="1914" height="924" alt="image" src="https://github.com/user-attachments/assets/4877ec6f-2165-4275-8c50-06123994495d" />

Nothing much here tho . 

AFter exploring more and reading a writeup for this , i came across a plugin which does  
```
iehistory
This plugin recovers fragments of IE history index.dat cache files. It can find basic accessed links (via FTP or HTTP), redirected links ( — REDR), and deleted entries ( — LEAK). It applies to any process which loads and uses the wininet.dll library, not just Internet Explorer. Typically that includes Windows Explorer and even malware samples.
```

<img width="1919" height="312" alt="image" src="https://github.com/user-attachments/assets/99b406e2-a784-4622-9702-ee061a4fa26f" />


Decoding that gives the first flag :))

flag{!!_w3LL_d0n3_St4g3–1_0f_L4B_5_D0n3_!!} and entering that to the zipped wintrar file gives us the 2nd flag in an image 

<img width="1049" height="826" alt="image" src="https://github.com/user-attachments/assets/3d2e376c-4c56-4891-a1b8-56de3215d0d2" />
