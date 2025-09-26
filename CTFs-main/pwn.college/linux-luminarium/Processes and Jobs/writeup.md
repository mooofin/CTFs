<img width="1082" height="721" alt="screenshot-1758894247" src="https://github.com/user-attachments/assets/87872c20-9aaa-4a3c-bf2b-74c8c3b19df6" /># Processes and Jobs 

## Listing processes 


<img width="1099" height="396" alt="screenshot-1758874149" src="https://github.com/user-attachments/assets/59b5fb69-5965-4b68-963d-2299d73d049a" />


Note - Found the running `/challenge` process in `ps`, copied its full path, ran that binary to reveal the flag 

## Killing processes 

<img width="1083" height="319" alt="screenshot-1758874375" src="https://github.com/user-attachments/assets/fa40037e-6202-4c9b-8a01-748470604da2" />

Note  - first lists all running processes with full, untruncated command lines using ps -efww, then filters for any process whose command contains /challenge/dont_run while excluding the grep command itself. 

## Interrupting challenges 

<img width="1116" height="385" alt="screenshot-1758893686" src="https://github.com/user-attachments/assets/09caa256-9d04-49c2-baee-84524d5e4964" />

Note - Ctrl + C while running   sends an interrupt signal (SIGINT) to the process

## Killing misbehaving processes 

<img width="1099" height="760" alt="screenshot-1758894093" src="https://github.com/user-attachments/assets/e0ccba49-3faa-4fce-85dd-f6ea564ffdba" />

Note - In this challenge, a decoy process was blocking access to a named pipe (`/tmp/flag_fifo`), preventing `/challenge/run` from writing the real flag. To solve it, I listed all running processes using `ps aux`, found the decoy process (`/challenge/decoy`), and noted its PID. I then terminated it with `kill <PID>`. After removing the decoy, running `/challenge/run` successfully wrote the flag to `/tmp/flag_fifo`, which I retrieved by reading it with `cat /tmp/flag_fifo`.



## Suspending processes 


<img width="1082" height="721" alt="screenshot-1758894247" src="https://github.com/user-attachments/assets/3f28ffa8-c014-4db1-b880-f6769500814c" />



Note - I ran `/challenge/run`, suspended it with **Ctrl+Z** so it stayed paused in the background, then started a second `/challenge/run` in the same terminal. Because one copy was suspended and another was active, the challenge detected the two instances and printed the flag.

## Resuming proccess 

<img width="1090" height="479" alt="screenshot-1758894389" src="https://github.com/user-attachments/assets/c83d86b3-fe3c-44a7-a23c-957061486cab" />


note  -  I started `/challenge/run`, suspended it with **Ctrl+Z** to pause it in the background, then used `fg` to bring it back to the foreground—when it resumed it printed the flag and I pressed Enter to exit.


You shell keeps a table of currently executing jobs and can be displayed with jobs command. You need to use bg command to restart a stopped background process. The fg command moves a background job in the current shell environment into the foreground

ALSO -  You cannot use fg and bg with a pid. They are shell builtin-s which require a jobspec, not a pid

ALSO x2 - 

The job control section of Greg's Bash Guide describes this as follows:

    A job specification or "jobspec" is a way of referring to the processes that make up a job. A jobspec may be:

        %n to refer to job number n.
        %str to refer to a job which was started by a command beginning with str. It is an error if there is more than one such job.
        %?str to refer to a job which was started by a command containing str. It is an error if there is more than one such job.
        %% or %+ to refer to the current job: the one most recently started in the background, or suspended from the foreground. fg and bg will operate on this job if no jobspec is given.
        %- for the previous job (the job that was %% before the current one).


## Backgrounding proccess 


<img width="809" height="717" alt="screenshot-1758894910" src="https://github.com/user-attachments/assets/c020b852-9667-47f9-a47a-96a7f342128e" />


## foregrounding proccess 

<img width="1080" height="610" alt="screenshot-1758896435" src="https://github.com/user-attachments/assets/0eb9ce9c-7a53-4047-9023-b9c30fe32f28" />

Note - Suspend with Ctrl-Z, background it with `bg`, then bring it to the foreground with `fg`.











