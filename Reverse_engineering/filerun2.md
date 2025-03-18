# Capture The Flag (CTF) Writeup: Argument-Based Challenge

## Challenge Description
We are provided with an executable file named `run`, which, when executed, prints the following message:

```
Run this file with only one argument.
```

This suggests that the program expects exactly one argument to function correctly.

## Initial Exploration
To understand its behavior, we attempt to execute the file without any arguments:

```bash
./run
```

Output:
```
Run this file with only one argument.
```

This confirms that the program requires an argument.

Next, we run the program with a random argument, such as `Hello!`:

```bash
./run Hello!
```

Output:
```
The flag is: picoCTF{F1r57_4rgum3n7_f65ed63e}
```

## Solution
The program checks if exactly one argument is provided and, if so, returns the flag. The challenge was simply to pass an argument when executing the file.

### Steps to Retrieve the Flag:
1. Download the provided `run` executable.
2. Navigate to the directory where the file is located.
3. Make the file executable if necessary:
   ```bash
   chmod +x run
   ```
4. Run the file with an argument:
   ```bash
   ./run Hello!
   ```
5. The program outputs the flag: `picoCTF{F1r57_4rgum3n7_f65ed63e}`.

