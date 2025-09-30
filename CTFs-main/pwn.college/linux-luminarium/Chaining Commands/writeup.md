# Chaining Commands 

## Chaining with semicolons

<img width="1333" height="232" alt="screenshot-1759053946" src="https://github.com/user-attachments/assets/b6664c9a-dcad-4755-bb3b-79f518149409" />

## Building on success 

<img width="1323" height="233" alt="screenshot-1759054074" src="https://github.com/user-attachments/assets/841cf634-5a45-46a4-b3a5-a519e7a411c2" />

## Handling failures 

<img width="1311" height="269" alt="screenshot-1759054206" src="https://github.com/user-attachments/assets/89e1b23b-0fa3-486b-88ce-fc636b26e7bb" />

## First shell script 

<img width="1295" height="332" alt="screenshot-1759054302" src="https://github.com/user-attachments/assets/2969f2da-c2a0-43b9-b792-a3791838e058" />

## Redirecting script output 
<img width="1306" height="318" alt="screenshot-1759216726" src="https://github.com/user-attachments/assets/1d37a4cb-48ea-4acd-a9ab-d4f5b1825920" />


## Executable shell scripts 

<img width="1299" height="321" alt="screenshot-1759216873" src="https://github.com/user-attachments/assets/1b57f3f9-d4b3-4e4a-b3f1-f98bd8a5e651" />

## Understanding shebangs 

<img width="1301" height="531" alt="screenshot-1759216977" src="https://github.com/user-attachments/assets/c54e7c08-f3b5-4744-a0d1-3dc1c918f299" />

Note -  In Linux, when you run a file, the system doesn’t use the file extension to decide how to execute it. Instead, it checks the first line of the file. If the file begins with `#!`, called a **shebang**, Linux uses the path that follows (like `/bin/bash`) as the interpreter to run the script.

The shebang must be the **first line** with no spaces or blank lines before it. For example:

```bash
#!/bin/bash
echo "Hello Hackers!"
```

When you make this script executable (`chmod +x script.sh`) and run it (`./script.sh`), Linux reads the shebang and effectively runs `/bin/bash ./script.sh`.

This allows scripts to run directly  even when called by other programs — without needing to explicitly type `bash script.sh`. Common shebangs include `#!/bin/bash` for Bash, `#!/usr/bin/python3` for Python, and `#!/bin/sh` for POSIX shell.

## Scripting with arguments 


<img width="1292" height="563" alt="screenshot-1759217299" src="https://github.com/user-attachments/assets/835e269f-48ae-47b0-8fd1-2020eb67af2c" />

## Scripting with conditionals 


<img width="1319" height="717" alt="screenshot-1759217415" src="https://github.com/user-attachments/assets/f05d044d-b89f-44ea-8ce7-1db349bdbd93" />


note - 
| Command / Syntax   |                                         What it does | Example                            |                                                     |       |   |       |
| ------------------ | ---------------------------------------------------: | ---------------------------------- | --------------------------------------------------- | ----- | - | ----- |
| `if`               |                           Starts a conditional block | `if [ "$1" = "pwn" ]`              |                                                     |       |   |       |
| `then`             |             Begins commands to run when `if` is true | `then echo "yes"`                  |                                                     |       |   |       |
| `else`             |           (Optional) Commands when the test is false | `else echo "no"`                   |                                                     |       |   |       |
| `elif`             |    "else if" — another test if the first `if` failed | `elif [ "$1" = "test" ]`           |                                                     |       |   |       |
| `fi`               |                 Ends the `if` block (`if` backwards) | `fi`                               |                                                     |       |   |       |
| `[ ... ]` / `test` |      Evaluates a condition (strings, numbers, files) | `[ -f file.txt ]`                  |                                                     |       |   |       |
| `"$1"`, `"$2"`     |         Positional parameters (1st, 2nd script args) | `echo "$2 $1"`                     |                                                     |       |   |       |
| `&&`               | Run next command only if previous succeeded (exit 0) | `cmd1 && cmd2`                     |                                                     |       |   |       |
| `                  |                                                      | `                                  | Run next command only if previous failed (non‑zero) | `cmd1 |   | cmd2` |
| `chmod +x file`    |                               Make `file` executable | `chmod +x solve.sh`                |                                                     |       |   |       |
| `#!/bin/bash`      |      Shebang — tells kernel which interpreter to use | `#!/bin/bash` at top of script     |                                                     |       |   |       |
| `./script`         |        Run an executable script in current directory | `./solve.sh arg`                   |                                                     |       |   |       |
| `echo` / `printf`  |                                 Print text to stdout | `echo "hi"` / `printf "%s\n" "$1"` |                                                     |       |   |       |





