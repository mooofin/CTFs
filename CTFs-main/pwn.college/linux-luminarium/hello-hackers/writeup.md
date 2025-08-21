# Pwn College Write-up: Initial Challenges

---

## Challenge 1: Your First Command

### Objective
The objective of this challenge is to execute a specific command within the provided shell environment to retrieve the flag.

### Challenge Analysis
The pwn.college dojo environment presents a standard Linux shell prompt (`hacker@dojo:~$`). The core task is command invocation. As per the instructions, commands entered into the terminal are executed upon pressing the **Enter** key, with their output printed to standard output.

The specific command for this level is `hello`. It is crucial to note that command-line environments in Linux are case-sensitive, meaning `hello` is a distinct command from `HELLO` or any other capitalization.

### Solution
Execution requires typing the `hello` command at the prompt and pressing **Enter**.

1.  At the prompt, input the command:
    ```bash
    hello
    ```
2.  Press **Enter** to execute.

### Flag
`pwn.college{8AI1t5NJHM22TkWzIhgUFY8OKa9.ddjNyUDL0ATO0czW}`

---

## Challenge 2: Intro to Arguments

### Objective
The objective of this challenge is to execute a command with a specific argument to retrieve the flag.

### Challenge Analysis
This challenge introduces the concept of command-line arguments. When a command is executed, the shell parses the input line, identifying the first word as the command and subsequent words as its arguments. These arguments provide additional data or options to the command.

For this specific level, the task is to run the `hello` command, passing `hackers` as a single argument.

### Solution
Execution requires typing the command followed by its argument at the prompt and pressing **Enter**.

1.  At the prompt, input the command and its argument:
    ```bash
    hello hackers
    ```
2.  Press **Enter** to execute.

### Flag
`pwn.college{AtBtvnMYqW8B-Cxv6G3WnLXBQqw.dhjNyUDL0ATO0czW}`

---

## Challenge 3: Command History

### Objective
The objective of this challenge is to retrieve a flag from the shell's command history.

### Challenge Analysis
Modern shells maintain a history of previously executed commands to improve user efficiency. This history can be navigated using the **up** and **down arrow keys**, allowing for the quick recall and re-execution of commands without retyping them.

In this challenge, the flag is not obtained by running a command, but by accessing a pre-populated entry in the command history.

### Solution
To retrieve the flag, the user simply needs to recall the last entry from the command history.

1. At the prompt, press the **up arrow key** once.
2. The shell will populate the command line with the most recent history entry, which is the flag.
3. Copy the flag from the terminal.

### Flag
`pwn.college{UpPYmnzvrIeXVsFzKNTVYuIwXXm.QX2MTM3EDL0ATO0czW}`
