# Practising piping 


## Redirecting output 

<img width="1442" height="328" alt="screenshot-1758634966" src="https://github.com/user-attachments/assets/a0fdbe1a-3ab1-4a63-be31-270443e4f6e3" />

Note - > redirects that output into a file (stdout)

## Appending output 

<img width="1160" height="748" alt="screenshot-1758637103" src="https://github.com/user-attachments/assets/842f84e9-826f-430b-940d-10c90f131191" />

Note - `>` overwrites a file with new output, while `>>` appends the output to the end of the file.

## Redirecting errors


<img width="1196" height="449" alt="screenshot-1758637674" src="https://github.com/user-attachments/assets/3dedddc2-6f5f-4155-84c5-62efe3c8f466" />

Note - 
    FD 0: Standard Input
    FD 1: Standard Output
    FD 2: Standard Error

## Redirecting input 

<img width="1189" height="333" alt="screenshot-1758637879" src="https://github.com/user-attachments/assets/849a43c6-ee35-4467-916a-e29983103d25" />

Note - > overwrites PWN (or creates it if it doesn’t exist)

## Grepping stored results 

<img width="1018" height="345" alt="screenshot-1758638074" src="https://github.com/user-attachments/assets/d57b3b70-7743-4c48-91ab-c3a2851d55bf" />


## Grepping live output 


<img width="1164" height="407" alt="screenshot-1758638205" src="https://github.com/user-attachments/assets/6e824d8c-c754-4266-9ed4-26294346348c" />


## Greppinng erros


<img width="1168" height="381" alt="screenshot-1758638531" src="https://github.com/user-attachments/assets/803819bf-d2f4-49cf-87ae-ef21acd9d4c9" />


## Filter with grep-v 

<img width="1203" height="345" alt="screenshot-1758638687" src="https://github.com/user-attachments/assets/6b321109-0d38-449b-ad51-fce647f3c004" />

Note - grep  -v inverts the match, meaning it filters out any line containing the word

## Duplicating piped data with tee 

<img width="1204" height="302" alt="screenshot-1758638954" src="https://github.com/user-attachments/assets/f256a9a4-6ab3-4687-8968-328f69bcedb0" />


Note - /challenge/pwn generates a secret code, and /challenge/college expects that code as input. Piping pwn directly into college works but leaves you unable to see the secret. Using tee splits the stream: one copy goes to a file (or terminal) so you can inspect the secret, while the other continues to college. By running /challenge/pwn | tee /tmp/intercepted | /challenge/college, you both forward the output and capture it for inspection

## Process subsitituion for input 

Process substitution <(...) is a bash feature that treats the output of a command as if it were a file:
```
<(<command>)
```

 <command> runs the command.

 Bash gives diff a temporary “file” that contains the command’s output.

This allows diff (or any file-based program) to compare command outputs without creating actual files on disk.


``` diff <(/challenge/print_decoys) <(/challenge/print_decoys_and_flag) ```

<img width="1190" height="277" alt="screenshot-1758639156" src="https://github.com/user-attachments/assets/adfda209-8244-4266-8ce1-fe71249d6840" />


Note  - How it works under the hood Bash creates a named pipe (FIFO) in /dev/fd/ or /proc/self/fd/.The command runs, writing its output into the pipe



## Writing to multiple programs 

Normally, a pipe (|) sends output to a single command, but by combining tee with >(command), you can treat a command’s stdin as a “file” and write to it. For example, /challenge/hack | tee >( /challenge/the ) >( /challenge/planet ) runs /challenge/hack once, and tee duplicates its output to both commands simultaneously. Bash sets up named pipes for each process substitution, so when tee writes to them, the connected commands receive the same input

<img width="1191" height="376" alt="screenshot-1758639683" src="https://github.com/user-attachments/assets/f89ac63d-1bd6-43f7-bf8e-27b4385f2548" />

## Split piping stderr and  stdout 

`/challenge/hack` produces two streams: **stdout** (normal output, fd 1) and **stderr** (error messages, fd 2). Using `> >( /challenge/planet )` redirects stdout into a process substitution running `/challenge/planet`, while `2> >( /challenge/the )` redirects stderr into a process substitution running `/challenge/the`. This way, both streams are handled **separately and simultaneously**, so `/challenge/planet` receives only stdout and `/challenge/the` receives only stderr.

<img width="1160" height="472" alt="screenshot-1758639937" src="https://github.com/user-attachments/assets/125c8ae5-9845-46f6-969c-7cd64cb47c02" />








