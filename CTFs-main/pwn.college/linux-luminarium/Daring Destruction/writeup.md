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




