# Silly Shenanigans 

## Bashrc backdoor 

<img width="1279" height="575" alt="screenshot-1759311135" src="https://github.com/user-attachments/assets/b70b7356-2ead-4bb0-bef4-e6f9cce47118" />

Note  - I can edit the victim’s `~/.bashrc` because I (the `hacker` user) have write access to `/home/zardus/.bashrc`. When I run the simulator `/challenge/victim`, it logs in as `zardus` and executes that file, so I can inject a harmless, non‑interactive command that copies or prints `/flag` somewhere I can read (for example `/tmp/zardus_flag`) and set its permissions world‑readable. I’ll use absolute paths (e.g. `/bin/cat /flag > /tmp/zardus_flag`) and avoid commands that read stdin or `exit`, then run `/challenge/victim` and `cat /tmp/zardus_flag` to retrieve the flag.

## Sniffing input 

<img width="1067" height="560" alt="screenshot-1759311528" src="https://github.com/user-attachments/assets/0515b008-daf8-4538-a0c0-3e9e5567a651" />



**What the challenge is doing**
I’m pretending to be an attacker (`hacker`) who can edit another user’s startup script: `/home/zardus/.bashrc`. The simulated victim (`/challenge/victim`) will log in as user `zardus` and run whatever is in that `.bashrc`. When `zardus` logs in, he will later run a program called `flag_checker` and manually type the secret flag into it. My job is to make `zardus` unintentionally hand me the flag.

**The trick I use (high level)**
Instead of waiting for `flag_checker` to appear, I create my *own* `flag_checker` program (a small shell script) and make sure the login shell finds *my* script before any real `flag_checker`. I do that by putting my script in a directory I control (e.g. `/tmp/fakebin`) and then prepending that directory to `zardus`’s `PATH` inside `/home/zardus/.bashrc`. When `zardus` later types `flag_checker`, the shell runs *my script* (because it’s first on `PATH`). My script prints the expected prompt so `zardus` doesn’t get suspicious, reads the line he types (the flag), and saves it to a file I can read.

**Why each bit matters**

* `.bashrc` is run on shell startup, so modifying it makes me run code whenever `zardus` logs in.
* Prepending `/tmp/fakebin` to `PATH` ensures `execvp("flag_checker",...)` finds my script first  that’s how command lookup works. If I replaced `PATH` entirely I might break normal commands; prepending is safer.
* My fake `flag_checker` must print the exact prompt (`Type the flag`) because `zardus` checks for that prompt before typing. If it doesn’t appear, he might not type or might become suspicious.
* The script must read from stdin (either `cat` with no args or `read`) to capture what `zardus` types.
* I write the captured flag to `/tmp/zardus_flag` and `chmod 644` it so my `hacker` user can read it  otherwise the file would still be only readable by `zardus`.
* I use absolute paths inside the script (e.g. `/bin/cat`, `/bin/chmod`) so the script works even though I changed `PATH`.
* Make the script executable (`chmod +x`) so the shell can run it.

**Typical one‑liner (what I actually run)**

* Create the fake dir and script:

  ```bash
  mkdir -p /tmp/fakebin
  printf '%s\n' '#!/bin/sh' 'printf "Type the flag\n"' 'read -r FLAG' 'printf "%s\n" "$FLAG" > /tmp/zardus_flag' '/bin/chmod 644 /tmp/zardus_flag' > /tmp/fakebin/flag_checker
  chmod +x /tmp/fakebin/flag_checker
  ```
* Add to `.bashrc` so `zardus` gets my PATH:

  ```bash
  printf '\n# prepend hijack dir to PATH for victim login\nexport PATH=/tmp/fakebin:$PATH\n' >> /home/zardus/.bashrc
  ```
* Run the victim simulator:

  ```bash
  /challenge/victim
  ```

  When `zardus` types the flag at the `Type the flag` prompt, my script captures it into `/tmp/zardus_flag`. After the simulation finishes I read it:

  ```bash
  cat /tmp/zardus_flag
  ```

**Common pitfalls**

* If my fake checker doesn’t print the expected prompt, the victim may not type and the trick fails.
* If my script reads further from stdin or blocks unexpectedly (for example uses `read` incorrectly), the login automation may die  keep the script simple: print the prompt, read one line, save it, exit.
* If I overwrite `PATH` instead of prepending, normal commands `zardus` needs might break and the simulation could fail early.
* Forgetting `chmod +x` means the shell won’t execute my script.
* Not making the captured file world-readable means I (hacker) still can’t read it.


