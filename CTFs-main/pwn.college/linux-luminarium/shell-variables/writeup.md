# Shell Variables

## SUMMARYY : ) 



| **Concept**                | **Command / Example**                             | **Explanation**                                                               |                                              |
| -------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------- |
| **Printing variables**     | `echo $FLAG`                                      | Expands the variable `FLAG` and prints its value.                             |                                              |
| **Setting variables**      | `PWN=COLLEGE`                                     | Assigns the string `COLLEGE` to the shell variable `PWN`.                     |                                              |
| **Multi-word variables**   | `PWN="COLLEGE YEAH"`                              | Quotes let you assign values with spaces to a single variable.                |                                              |
| **Exporting variables**    | `COLLEGE=PWN; export PWN=COLLEGE; /challenge/run` | `export` makes a variable available to child processes.                       |                                              |
| **Printing exported vars** | `printenv PWN` or `env                            | grep PWN`                                                                     | Shows environment variables (exported ones). |
| **Storing output**         | `PWN=$(/challenge/run)`                           | Captures stdout of a command and assigns it to the variable `PWN`.            |                                              |
| **Reading input**          | `read PWN` → then type `COLLEGE`                  | Reads user input from stdin into the variable `PWN`.                          |                                              |
| **Reading files**          | `read PWN < /challenge/read_me`                   | Redirects file contents into stdin for `read`, storing in the variable `PWN`. |                                              |

---


## Printing Variables

<p align="center">
  <img width="700" height="350" alt="screenshot-printing" src="https://github.com/user-attachments/assets/cac00a15-fe7a-4d61-8c5e-bb79b40ba259" />
</p>  

**Note:** The shell performed parameter expansion (`$FLAG` → the variable’s value).

---

## Setting Variables

<p align="center">
  <img width="700" height="350" alt="screenshot-setting" src="https://github.com/user-attachments/assets/4a06c1b9-ee0c-49a2-8a4f-7b1f74b752a0" />
</p>  

**Note:** `PWN=COLLEGE` is a shell variable assignment. It sets the variable named `PWN` to the string `COLLEGE`.

---

## Multi-word Variables

<p align="center">
  <img width="700" height="350" alt="screenshot-multiword" src="https://github.com/user-attachments/assets/ae1a9eb6-cbbd-4728-8622-60375b9db71f" />
</p>  

**Note:** Set the shell variable `PWN` to the multi-word string `"COLLEGE YEAH"` using quotes (`PWN="COLLEGE YEAH"`).

---

## Exporting Variables

<p align="center">
  <img width="700" height="350" alt="screenshot-exporting" src="https://github.com/user-attachments/assets/9d0052d3-f7cf-4276-8bf1-92315e0224dd" />
</p>  

**Note:** The child process sees the exported `PWN=COLLEGE` in its environment, while the parent shell still holds `COLLEGE=PWN` without exporting it.

---

## Printing Exported Variables

<p align="center">
  <img width="700" height="350" alt="screenshot-printing-exported" src="https://github.com/user-attachments/assets/91771fa7-16fa-42b0-a470-d815268a1a22" />
</p>  

---

## Storing Command Output

<p align="center">
  <img width="700" height="350" alt="screenshot-storing" src="https://github.com/user-attachments/assets/d8fb0e91-9b57-4f1f-bc70-6899dfe50481" />
</p>  

**Note:** Variables set inside a child process do not automatically appear in the parent shell. I didn’t get the flag because I tried to read a variable as a file.

---

## Reading Input

<p align="center">
  <img width="700" height="350" alt="screenshot-reading" src="https://github.com/user-attachments/assets/6aca93f8-8a81-4728-863a-22224c6d2445" />
</p>  

**Note:** `read PWN` tells the shell to wait for input and store it in the variable.

---

## Reading Files

<p align="center">
  <img width="700" height="350" alt="screenshot-reading-file" src="https://github.com/user-attachments/assets/1c7ae866-4cd1-42aa-8ea1-0075da433d09" />
</p>  

**Note:** `read PWN < /challenge/read_me` feeds the file as stdin to `read` in the current shell.

