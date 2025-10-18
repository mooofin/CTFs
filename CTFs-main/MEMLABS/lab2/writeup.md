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


Moving on 
