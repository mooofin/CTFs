# Exploiting Python's `eval()` for Code Execution

## Overview
In this challenge, the goal was to retrieve the flag from a file named `flag.txt`. However, input filtering was implemented, blocking any input containing the string `'win'`. Upon analyzing the code, I discovered that the `eval()` function was being used, which allowed me to bypass the filter and execute arbitrary Python commands.

## Understanding `eval()` Exploitation
The `eval()` function in Python takes a string as input, evaluates it as a Python expression, and returns the result. For example:

```python
print(eval('4+4'))  # Output: 8
```

The issue with `eval()` is that it can execute any valid Python expression, including file operations, making it a common vulnerability if not properly secured.

## Initial Roadblock - Input Filtering
The challenge had a filter that blocked any input containing `'win'`. This suggested that direct attempts to execute commands like:

```python
eval('open("flag.txt").read()')
```

would not work if `'win'` was present in the payload.

## Bypassing the Filter
Since the filter specifically blocked `'win'`, but `eval()` could still execute other expressions, I used an alternate approach to read the flag:

```python
eval("open('flag.txt', 'r').read()")
```

This command successfully read the contents of `flag.txt` and displayed the flag.

## Lessons Learned
1. **Avoid Using `eval()` Unnecessarily**: If a function allows execution of arbitrary input, it becomes a major security risk.
2. **Implement Strong Input Validation**: Instead of blocking specific keywords like `'win'`, proper input sanitization and whitelisting should be applied.
3. **Use `ast.literal_eval()` Instead**: If evaluating expressions is necessary, `ast.literal_eval()` should be used as it only allows safe operations like numbers, strings, and lists.

## Conclusion
By leveraging Python's built-in functions and carefully analyzing the filtering mechanism, I was able to bypass the restrictions and retrieve the flag. This challenge highlights the importance of secure coding practices and reinforces why dangerous functions like `eval()` should be handled with caution or avoided altogether.

---

_File: `writeup.md`_

