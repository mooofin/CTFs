
# Shell Variables

## Printing variables 

<img width="645" height="315" alt="screenshot-1758802158" src="https://github.com/user-attachments/assets/cac00a15-fe7a-4d61-8c5e-bb79b40ba259" />
Note - The shell performed parameter expansion ($FLAG → the variable’s value)


## Setting variables


<img width="628" height="354" alt="screenshot-1758802366" src="https://github.com/user-attachments/assets/4a06c1b9-ee0c-49a2-8a4f-7b1f74b752a0" />

Note - PWN=COLLEGE is a shell variable assignment. It sets the variable named PWN to the string COLLEGE

## Multi-word Variables

<img width="622" height="395" alt="screenshot-1758802530" src="https://github.com/user-attachments/assets/ae1a9eb6-cbbd-4728-8622-60375b9db71f" />



Note - Set the shell variable PWN to the multi-word string COLLEGE YEAH using quotes (PWN="COLLEGE YEAH")

## Exporting Variables 

<img width="641" height="526" alt="screenshot-1758802761" src="https://github.com/user-attachments/assets/9d0052d3-f7cf-4276-8bf1-92315e0224dd" />

Note-The key idea is that the child process sees the exported PWN=COLLEGE in its environment, while the parent shell still holds COLLEGE=PWN without exporting it


## Printing exported variables 

<img width="614" height="732" alt="screenshot-1758802845" src="https://github.com/user-attachments/assets/91771fa7-16fa-42b0-a470-d815268a1a22" />

## Storing command output

<img width="742" height="631" alt="screenshot-1758803244" src="https://github.com/user-attachments/assets/d8fb0e91-9b57-4f1f-bc70-6899dfe50481" />

Note - variables set inside a child process do not automatically appear in the parent shell , I didn’t get the flag because i tried to read a variable as a file
