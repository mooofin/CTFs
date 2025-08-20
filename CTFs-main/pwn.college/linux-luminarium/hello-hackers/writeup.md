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

__________________________________

# Pwn College Challenge Write-up: Intro to Arguments

## Objective

The objective of this challenge is to execute a command with a specific argument to retrieve the flag.

## Challenge Analysis

This challenge introduces the concept of command-line arguments. When a command is executed, the shell parses the input line, identifying the first word as the command and subsequent words as its arguments. These arguments provide additional data or options to the command.

For example, with `echo Hello Hackers!`, the command is `echo`, and it receives two arguments: `Hello` and `Hackers!`.

For this specific level, the task is to run the `hello` command, passing `hackers` as a single argument.

## Solution

Execution requires typing the command followed by its argument at the prompt and pressing **Enter**.

1.  At the prompt, input the command and its argument:
    ```bash
    hello hackers
    ```
2.  Press **Enter** to execute.

The `hello` program is designed to check for the `hackers` argument and, upon successful validation, print the flag to the terminal.

## Flag

The flag obtained from this challenge is:

`pwn.college{AtBtvnMYqW8B-Cxv6G3WnLXBQqw.dhjNyUDL0ATO0czW}`







