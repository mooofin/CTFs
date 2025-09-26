# Processes and Jobs 

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
