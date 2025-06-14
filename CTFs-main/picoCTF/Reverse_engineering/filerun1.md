# Write-up: Extracting the Flag from a Provided Program

## Challenge Description
A program has been provided, and the objective is to determine what happens when it is executed via the command line. 

## Steps to Solve the Challenge

### 1. **Downloading the Program**
First, we obtain the provided program and navigate to the directory where it is stored:
```bash
cd Downloads
```

### 2. **Granting Execution Permissions**
To ensure the file can be executed, we modify its permissions using the `chmod` command:
```bash
chmod +x run
```
This allows the program to be run as an executable.

### 3. **Executing the Program**
We attempt to run the program without any arguments:
```bash
./run
```
Upon execution, the program directly outputs the flag:
```
The flag is: picoCTF{U51N6_Y0Ur_F1r57_F113_e5559d46}
```

### 4. **Understanding the Output**
The program seems to be checking if any arguments are provided and then automatically prints the flag when executed correctly.

## Conclusion
The challenge was straightforward as the flag was revealed simply by running the executable file without any arguments. The key takeaway is that sometimes, examining the behavior of an executable before attempting complex reverse engineering can yield quick results.

### **Final Flag:**
```
picoCTF{U51N6_Y0Ur_F1r57_F113_e5559d46}
```
