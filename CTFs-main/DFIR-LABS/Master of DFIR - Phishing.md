Master of DFIR - Phishing(🎣)
Difficulty: Hard

  _____  _     _     _     _             
 |  __ \| |   (_)   | |   (_)            
 | |__) | |__  _ ___| |__  _ _ __   __ _ 
 |  ___/| '_ \| / __| '_ \| | '_ \ / _` |
 | |    | | | | \__ \ | | | | | | | (_| |
 |_|    |_| |_|_|___/_| |_|_|_| |_|\__, |
                                    __/ |
                                   |___/ 

Challenge Description

饥渴C猫是一个刚刚入职的员工，但是最近他发现自己的电脑变得越来越奇怪。可能由于是之前他接受的一封奇怪的邮件，于是饥渴C猫找到了你,他希望你作为取证-应急响应大师可以帮忙。你可以完成调查到底发生了什么并且填写相关的调查报告。

GeekCmore is a new employee who recently noticed that his computer has been acting strangely. It might be due to a strange email he received earlier, so GeekCmore turned to you for help. He hopes that, as a forensics and incident response expert, you can assist him in investigating what happened and completing the related investigation report.

Challenge File:

handout.zip

MD5 Hash:

257aba697f91196d06dfd80c29138a9d  handout.zip



Qsns 

task1:
(1).What is the attacker's email address? (Note: MD5 (attacker's email address) is based on cyberchef's) Example: 9b04d152845ec0a378394003c96da594
(2).What is the victim's email address? (Note: MD5 (victim's email address) is based on cyberchef's) Example: 9b04d152845ec0a378394003c96da594


we are given 2 files :

<img width="991" height="131" alt="image" src="https://github.com/user-attachments/assets/aa51263e-5392-4b69-962f-1b79a0187188" />

The email files looks filled with Keys ? 

<img width="1217" height="1017" alt="image" src="https://github.com/user-attachments/assets/aafdc0bc-5670-4fcb-9b96-365842834ae5" />

We can grep for from and to . and we get 

<img width="1298" height="160" alt="image" src="https://github.com/user-attachments/assets/df365bbd-6929-4bf8-a074-980c47170b9c" />


The MD5 hashes of them are 

1. a8cd5b4ba47e185d4a69a583fde84da5
2. b9cae449f959162f0297fa43b458bd66

task2:
(1).What is the md5 of the file dropped by the attacker? (Note: the result of md5sum shall prevail) Example: 33ec9f546665aec46947dca16646d48e
(2).What is the password of the file dropped by the attacker? Example: 000nb

Opening the eml file 

<img width="1129" height="728" alt="image" src="https://github.com/user-attachments/assets/dd3601ed-b501-4b36-a63c-c372b24db81d" />

```


