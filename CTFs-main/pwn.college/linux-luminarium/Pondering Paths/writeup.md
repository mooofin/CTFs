

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

