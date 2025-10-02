# Daring Destruction 

## The FORK  BOMB 

<img width="1316" height="645" alt="screenshot-1759345747" src="https://github.com/user-attachments/assets/adb4772a-aea4-4fed-bfd4-627c9ef9eda4" />

<img width="1293" height="635" alt="screenshot-1759345736" src="https://github.com/user-attachments/assets/a9fbc537-af7b-45dd-b6a9-bab8143db5be" />

### Fork bomb (DDOS kinda attack ) 
The :(){ :|:& };: is nothing but a bash function. This function gets executed recursively. It is often used by sysadmin to test user process limitations on server. Linux process limits can be configured via /etc/security/limits.conf and PAM to avoid bash fork() bomb 

The :() – Defined the function called :. This function accepts no arguments. The syntax for bash function is as follows:
```
foo(){
 arg1=$1
 arg2=$2
 echo 'Bar..'
 #do_something on $arg argument
}
```
fork() bomb is defined as follows:
```
:(){
 :|:&
};:
```
:|: – Next it will call itself using programming technique called recursion and pipes the output to another call of the function ‘:’. The worst part is function get called two times to bomb your system.

& – Puts the function call in the background so child cannot die at all and start eating system resources.

; – Terminate the function definition.

: – Call (run) the function aka set the fork() bomb.


### Preventing fork bomb on Linux

<img width="898" height="1008" alt="screenshot-1759345938" src="https://github.com/user-attachments/assets/7ccd6876-43e1-4cd1-819f-a6f698e182ec" />


The number 62166 means that , you can rum upto that many proccesses , 

To prevent getting fork bombed  lower that amount by using 

```ulimit -S -u 5000 ```

<img width="499" height="595" alt="image" src="https://github.com/user-attachments/assets/2c60b85b-3ee2-477f-82e0-eb98fd7cf411" />


 -----

## Disk-space DOOMSDAY

<img width="1312" height="604" alt="screenshot-1759348504" src="https://github.com/user-attachments/assets/4533bd1d-b72f-437a-99ae-f45e1a473968" />

In this challenge, the goal was to intentionally fill up the available disk space in the `/home/hacker` directory until even a small 1 MB file could no longer be created. Although the filesystem itself had plenty of capacity, the system imposed a per-user quota of 1 GB. To reach this limit, we used the `yes` command, which continuously outputs the letter `y`. By redirecting this output into a file using `yes > junkfile.txt`, the file grew rapidly until the message `Disk quota exceeded` appeared, indicating that our quota was fully used. Without deleting the file, we then ran `/challenge/check`, which attempted to create a temporary file and failed, confirming that the quota was exhausted. This completed the first stage of the challenge. Next, we removed the large file with `rm junkfile.txt` to free up the used space and ran `/challenge/check` again.

## rm -rf / 

<img width="774" height="288" alt="screenshot-1759385325" src="https://github.com/user-attachments/assets/8e1f21e9-3417-4e71-b5b3-c604d7dab201" />

<img width="1112" height="424" alt="screenshot-1759387088" src="https://github.com/user-attachments/assets/fa361341-42bd-47e5-80b2-0205515d26f3" />
The rm utility is invoked with the -r (recursive) flag to traverse the entire directory tree starting from the root (/) and the -f (force) flag to suppress most prompts and error messages, allowing the process to proceed with minimal interruption. On modern GNU/Linux systems, rm includes a default safeguard (--preserve-root) to prevent this exact operation

## Life after -rm rf 

<img width="779" height="320" alt="screenshot-1759387728" src="https://github.com/user-attachments/assets/ee5151eb-09c9-4e7c-b2a0-2a80dbe082c8" />


<img width="846" height="557" alt="screenshot-1759387724" src="https://github.com/user-attachments/assets/dacfcce6-39a2-4958-9003-ae4e65c8293a" />

