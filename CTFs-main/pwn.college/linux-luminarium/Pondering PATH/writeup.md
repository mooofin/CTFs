# Pondering PATH 


##  The path variable 

<img width="1321" height="455" alt="screenshot-1759306762" src="https://github.com/user-attachments/assets/e34744c4-d26b-42c6-a509-f44064d79b3a" />

Note - When a program runs another command like rm, it needs to know where to find that program on the system. Normally, it uses an environment variable called PATH. This variable contains a list of directories that the system searches through to locate executables. For example, when you type rm in a terminal, your shell looks inside /usr/local/bin, /usr/bin, and /bin (or whatever directories are listed in PATH) until it finds a file named rm.

If a program tries to execute rm without specifying the full path (like /bin/rm), it relies entirely on the PATH variable to locate it. This is important because if PATH points to directories that do not contain rm, the program will fail to find it. In that case, the system call that tries to execute rm will fail with a “command not found” or “No such file or directory” error, and the program won’t be able to run rm at all.

## Setting PATH 

<img width="1051" height="322" alt="screenshot-1759306991" src="https://github.com/user-attachments/assets/b74d094d-90d7-42e1-aada-84030c384bfe" />

Note - execvp is a system call in C that runs another program by replacing the current process with it. The key feature of execvp is that it searches for the program’s executable file using the directories listed in the PATH environment variable. This means that if a program calls execvp("win", args), it doesn’t know where the win program is located it simply looks through every directory in PATH, in order, until it finds an executable file named win. If it finds one, it runs it; if not, it fails with a “No such file or directory” erro

## Finding commands 

<img width="1095" height="278" alt="screenshot-1759307147" src="https://github.com/user-attachments/assets/5a086dbc-5b59-466a-b1ec-0aca52e40a00" />

Note - The which command replicates how your shell searches for executables: it goes through each directory listed in $PATH 

## Adding commands 

<img width="1105" height="541" alt="screenshot-1759307249" src="https://github.com/user-attachments/assets/78c09ec1-abfa-4a72-b59e-2f9b4ad5aed7" />



