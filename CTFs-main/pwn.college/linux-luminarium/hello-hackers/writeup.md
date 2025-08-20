# Pwn College Challenge Write-up: Your First Command

## Objective

The objective of this challenge is to execute a specific command within the provided shell environment to retrieve the flag.

## Challenge Analysis

The pwn.college dojo environment presents a standard Linux shell prompt (`hacker@dojo:~$`). The core task is command invocation. As per the instructions, commands entered into the terminal are executed upon pressing the **Enter** key, with their output printed to standard output.

The specific command for this level is `hello`. It is crucial to note that command-line environments in Linux are case-sensitive, meaning `hello` is a distinct command from `HELLO` or any other capitalization.

## Solution

Execution requires typing the `hello` command at the prompt and pressing **Enter**.

1.  At the prompt, input the command:
    ```bash
    hello
    ```
2.  Press **Enter** to execute.

The command's successful execution results in the flag being printed to the terminal.

## Flag

The flag obtained from this challenge is:

`pwn.college{8AI1t5NJHM22TkWzIhgUFY8OKa9.ddjNyUDL0ATO0czW}`


