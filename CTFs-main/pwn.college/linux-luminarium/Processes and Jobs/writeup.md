# Processes and Jobs 

## Listing processes 


<img width="1099" height="396" alt="screenshot-1758874149" src="https://github.com/user-attachments/assets/59b5fb69-5965-4b68-963d-2299d73d049a" />


Note - Found the running `/challenge` process in `ps`, copied its full path, ran that binary to reveal the flag 

## Killing processes 

<img width="1083" height="319" alt="screenshot-1758874375" src="https://github.com/user-attachments/assets/fa40037e-6202-4c9b-8a01-748470604da2" />

Note  - first lists all running processes with full, untruncated command lines using ps -efww, then filters for any process whose command contains /challenge/dont_run while excluding the grep command itself. 
