Starting off like any lab , we will do imageinfo or kdgbscan to see info about the OS 

<img width="1900" height="348" alt="image" src="https://github.com/user-attachments/assets/5e2cc211-1499-4ee3-83dd-049eeec365f7" />


we can see that there are multiple window profiles ? so we might need to check for all the profiles ig 

Moving onto to see what processes were running might give us more insight 

<img width="1869" height="936" alt="image" src="https://github.com/user-attachments/assets/e678f017-0dbf-4602-86b1-5421b7ce6cbc" />



Also we see dump it .exe running , and its used to make the memory dump . A intuitive way to think about this is that whatever was running before dumpit.exe should be our focus and here we see 2 notepad.exe 's running . 


Now the workflow for any DFIR challenge is to dump the info that you see might be worth looking into , so lets do that 
