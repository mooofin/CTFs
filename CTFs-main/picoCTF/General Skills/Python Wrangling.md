In this picoCTF challenge, we were provided with a Python script named `ende.py` along with two files: `pw.txt` and `flag.txt (1).en`. The goal was to decrypt the encrypted flag file using the provided script and retrieve the hidden flag.

Initially, running the script with a placeholder filename like `pole.txt` resulted in a `FileNotFoundError`. This indicated that the expected input file did not exist under that name. Upon reviewing the download history, it became clear that the actual encrypted file was named `flag.txt (1).en`, a common filename pattern when files are downloaded more than once. This filename included spaces and parentheses, which required careful handling in the terminal using quotation marks to ensure correct parsing by the shell.

After resolving the filename issue, the script was successfully executed using:

```bash
python3 ende.py -d "flag.txt (1).en"
```

The script also prompted for a password, which was stored in the `pw.txt` file. After supplying the password, the script proceeded with decryption and revealed the flag.

The final output of the script was the following flag:

```
picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}
```

![image](https://github.com/user-attachments/assets/c1db7180-5a44-4ed0-924d-58ab9582eb24)

