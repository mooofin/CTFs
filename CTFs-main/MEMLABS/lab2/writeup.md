Uhm the Challenge description says 
One of the clients of our company, lost the access to his system due to an unknown error. He is supposedly a very popular "environmental" activist. As a part of the investigation, he told us that his go to applications are browsers, his password managers etc. We hope that you can dig into this memory dump and find his important stuff and give it back to us.

Note: This challenge is composed of 3 flags.


Starting on some uhm keywords here , enviormental , browsers and password manager . 


First things first , we have to see profile or image info using KDGB which will tell us info about the dump . This is only for vol 2.6 as vol 3 does this automatically 


<img width="1904" height="391" alt="image" src="https://github.com/user-attachments/assets/373462fb-9d5f-4315-8872-eca8d0620d64" />


next as always we need to see what all was running while the , dump was taken so we'll use pslist 

<img width="1908" height="966" alt="image" src="https://github.com/user-attachments/assets/e01b58ee-5bc7-44c8-a0e4-c599a4c764d0" />


Sus processes that we would need to dump and investigate would be chrome.exe, keypass.exe ig 

Also whats wmpnetwk.exe ?


Moving on next i like to do what was passed onto the consoles ...

<img width="1874" height="197" alt="image" src="https://github.com/user-attachments/assets/922b41c6-3f2b-4a3a-8587-b1fc1035e6ef" />

WOW , hidden kbdx !!!!!


Grepping it , (findstr)


<img width="1889" height="260" alt="image" src="https://github.com/user-attachments/assets/33dc6060-4960-410c-b396-20fb225dd13f" />


so we need a keypass sofware to unlock this and we'll need a password as well . Hopefull and luckily greping for pass gave a good info 

A file called PASSWORD.PNG !!!!

lets dump and open it quickly , hopefully no gimp or offset changing rgb values .

Phew and we got the password :

<img width="1919" height="1025" alt="image" src="https://github.com/user-attachments/assets/118dd16d-7e75-43eb-9e3d-aa4cd0d8351d" />

The the right lower block , 

Now we have the password we can open the keypass software and get out first flag .


<img width="1831" height="889" alt="image" src="https://github.com/user-attachments/assets/4bfd85aa-fbcd-417f-9a74-9cb6d2dc218c" />

The workflow is to open this and see put the .kbdx and use the password we recovered and see if there's a flag 

<img width="906" height="662" alt="image" src="https://github.com/user-attachments/assets/9b98f709-0274-46b6-bea6-089886671db7" />

And we got the first flag : 3 

<img width="631" height="629" alt="image" src="https://github.com/user-attachments/assets/b980112a-f946-4e1d-81f6-b91339942bcd" />

But the flag contents said this is the 2nd flag ? 

Reading the description again , i forgot to check the lead on enviorment variables 



