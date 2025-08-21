

## The Root 

### Objective
The objective of this challenge is to execute a program using its absolute path.

### Challenge Analysis
The Linux filesystem is structured as a hierarchy starting from the root directory, denoted by `/`. A path that begins from the root directory is called an "absolute path." This provides an exact, unambiguous location for a file or program regardless of the current working directory.

In this level, a program named `pwn` is located in the root directory. Attempts to read the flag directly (e.g., `cat /flag`) fail due to insufficient permissions. The intended solution is to execute the `/pwn` program.

### Solution
To get the flag, the program must be invoked by providing its absolute path on the command line.

1.  At the prompt, input the program's absolute path:
    ```bash
    /pwn
    ```
2.  Press **Enter** to execute.

### Flag
`pwn.college{EnjLZxQwe6Cqv_vzV-l8XDISgy1.dhzN5QDL0ATO0czW}`


------------------------------

# Pwn College Challenge Write-up: Programs and Absolute Paths

## Objective
The objective of this challenge is to execute a specific program located outside the current working directory by using its absolute path.

## Challenge Analysis
This challenge builds on the concept of absolute paths. The current working directory (`~/program-and-absolute-paths`) contains numerous files, which can serve as a distraction. However, the target executable, `run`, is not located here.

The challenge requires understanding that an absolute path provides a direct reference to a file or program's location, starting from the root (`/`) of the filesystem. Therefore, the contents of the current directory are irrelevant to solving the challenge. The program we need to execute is located at `/challenge/run`.

## Solution
To obtain the flag, we must invoke the `run` program by specifying its full, absolute path in the terminal.

1.  At the prompt, input the program's absolute path:
    ```bash
    /challenge/run
    ```
2.  Press **Enter** to execute the program.

## Flag
`pwn.college{0uKsuZvvZQ07TJOj5bzZr1IPoQu.dVDN1QDL0ATO0czW}`
