# Pondering Paths


## summmary :3 

Absolute paths, starting with /, provide an unambiguous location for a file, while relative paths are interpreted from the current working directory, requiring commands like ./program to explicitly run files in the current directory. Some programs also check the current directory before running, teaching us to use cd to meet environmental prerequisites. The ~ shorthand simplifies access to home directories, enabling very short paths like ~/m to satisfy argument constraints, and cd - lets us quickly return to the previous directory



## The Root 




The Linux filesystem is structured as a hierarchy starting from the root directory, denoted by `/`. A path that begins from the root directory is called an "absolute path." This provides an exact, unambiguous location for a file or program regardless of the current working directory.

In this level, a program named `pwn` is located in the root directory. Attempts to read the flag directly (e.g., `cat /flag`) fail due to insufficient permissions. The intended solution is to execute the `/pwn` program.

### Solution
To get the flag, the program must be invoked by providing its absolute path on the command line.

1.  At the prompt, input the program's absolute path:
    ```bash
    /pwn
    ```


### Flag
`pwn.college{EnjLZxQwe6Cqv_vzV-l8XDISgy1.dhzN5QDL0ATO0czW}`


------------------------------

# Programs and Absolute Paths




This challenge builds on the concept of absolute paths. The current working directory (`~/program-and-absolute-paths`) contains numerous files, which can serve as a distraction. However, the target executable, `run`, is not located here.

The challenge requires understanding that an absolute path provides a direct reference to a file or program's location, starting from the root (`/`) of the filesystem. Therefore, the contents of the current directory are irrelevant to solving the challenge. The program we need to execute is located at `/challenge/run`.

## Solution
To obtain the flag, we must invoke the `run` program by specifying its full, absolute path in the terminal.

1.  At the prompt, input the program's absolute path:
    ```bash
    /challenge/run
    ```


## Flag
`pwn.college{0uKsuZvvZQ07TJOj5bzZr1IPoQu.dVDN1QDL0ATO0czW}`


----------
#  Position Thy Self





This challenge introduces a common scenario where a program's execution is conditional on the user's current working directory. Simply running the program `/challenge/run` via its absolute path is insufficient.

Upon the first execution attempt, the program returns an error explicitly stating that the user must be in the `/proc/376` directory. This demonstrates that programs can inspect their environment, including the present working directory (`pwd`), and alter their behavior based on it. The solution requires using the `cd` (change directory) command to navigate to the required location before re-running the executable.

## Solution
The solution is a two-step process: first, navigate to the correct directory, and second, execute the program.

1.  At the prompt, use the `cd` command to change to the required directory:
    ```bash
    cd /proc/376
    ```
2.  Once in the correct directory, execute the program using its absolute path:
    ```bash
    /challenge/run
    ```

## Flag
`pwn.college{0w5bDwvu-xABKjunh6J9Lrm8TOs.dZDN1QDL0ATO0czW}`


-------------------------------
#  Position Elsewhere

## 
The objective of this challenge is to navigate to a different, specified directory and execute a program to retrieve the flag.

## 
Similar to the previous challenge, this level requires the user to be in a specific directory before the target program will execute successfully. The program, `/challenge/run`, performs a check on the current working directory.

The initial execution fails and provides an error message indicating that the user must navigate to `/usr/share/zoneinfo/posix/Asia`. This is another exercise in using the `cd` (change directory) command to meet a program's environmental prerequisites.

## Solution
The solution involves changing to the specified directory and then running the executable.

1.  First, use the `cd` command to navigate to the target directory:
    ```bash
    cd /usr/share/zoneinfo/posix/Asia
    ```
2.  From within the correct directory, execute the program using its absolute path:
    ```bash
    /challenge/run
    ```

## Flag
`pwn.college{Y6cI8SY5XKarww1Vkv7xKv1c6ov.ddDN1QDL0ATO0czW}`

----------


#  Position Yet Elsewhere





This challenge continues the theme of environmental prerequisites for program execution. The executable, located at `/challenge/run`, will only run successfully if the user's current working directory is `/proc/132`.

An initial attempt to run the program from the default directory fails, but the resulting error message provides the exact path required. The core task is to use the `cd` (change directory) command to position the shell within the correct directory before re-executing the program.

## Solution
The solution is a straightforward, two-step process: change the directory, then run the program.

1.  Use the `cd` command to navigate to the directory specified by the error message:
    ```bash
    cd /proc/132
    ```
2.  With the prompt now reflecting the new location, execute the program using its absolute path:
    ```bash
    /challenge/run
    ```

## Flag
`pwn.college{QmoOwK8qXhgFzg3INKMUgvRBR3z.dhDN1QDL0ATO0czW}`

------------



#  Implicit Relative Paths





This challenge introduces the concept of **relative paths**. Unlike an absolute path, which starts from the root (`/`) and provides a full, unambiguous location, a relative path is interpreted from the current working directory (cwd).

- **Absolute Path:** `/challenge/run` (always refers to the same location)
- **Relative Path:** `challenge/run` (path is resolved starting from the cwd)

The challenge requires executing `/challenge/run`. However, the program is designed to fail if invoked with its absolute path. The key is to first change the current directory to `/` and then call the program using a path that is *relative* to `/`.

When the cwd is `/`, the relative path to `/challenge/run` is simply `challenge/run`. The shell looks for a directory named `challenge` within the current directory (`/`) and then for the `run` executable inside it.

## Solution
The solution is to first position the shell at the root of the filesystem and then execute the program with a relative path.

1.  Ensure the current working directory is the root directory. If not, use `cd /`.
2.  Execute the program using its relative path from root:
    ```bash
    challenge/run
## Flag
`pwn.college{8EVoszXXxkJGHXCVIvITYhp1if6.dlDN1QDL0ATO0czW}`    ```

# Explicit Relative Paths, from /



In this challenge, we learned that . refers to the current directory. To run a program there, we use ./program. From /, we ran the challenge with ./challenge/run and got the flag:

pwn.college{I9VxSxDHSpwjMMzeld1ZovOsCE9.dBTN1QDL0ATO0czW}

<img width="1381" height="254" alt="screenshot-1758447829" src="https://github.com/user-attachments/assets/433ef8d5-725a-4b55-b432-d7e6e6fcd4b6" />

The idea was that Linux doesn’t look in the current directory for commands by default, so we use ./run to explicitly tell it to execute the program in the current directory

----

# Implicit Relative Paths

<img width="796" height="304" alt="screenshot-1758448153" src="https://github.com/user-attachments/assets/de70a03f-aa5e-4e14-ac78-6a04794fc1a5" />


We moved to the root `/` directory and then ran the program using `./run` from the `challenge` directory. Using `./` ensured that Linux executed the program located in the current directory, which successfully gave us the flag.

Notes - By default, the shell searches only the directories listed in the $PATH environment variable for executables. The current directory . is usually not included in $PATH for security reasons, preventing accidental execution of local files with the same name as system commands


# Home Sweet Home 

<img width="1241" height="270" alt="screenshot-1758448523" src="https://github.com/user-attachments/assets/4663bc8c-9fc6-42c9-8338-3dc1eff32551" />


The correct solution was to provide a very short name, such as ~/m, which expanded to /home/hacker/m, allowing the command to successfully write

Beyond this, the ~ shorthand can be used to navigate to other users’ home directories using ~username, while cd - lets you jump back to your previous directory, effectively acting as an “undo” for navigation




