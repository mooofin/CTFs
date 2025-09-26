# Processes and Jobs




| **Topic**                       | **Command / Action**                   | **Purpose / Note**                                                                       |                              |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------- |
| **Listing Processes**           | `ps` / `ps -efww`                      | Lists running processes. Full path needed to run `/challenge` directly for the flag.     |                              |
| **Killing Processes**           | `kill <PID>`                           | Terminate misbehaving or blocking processes. Filter using `ps aux                        | grep <process>` to find PID. |
| **Interrupting Processes**      | `Ctrl + C`                             | Sends SIGINT to stop a running process.                                                  |                              |
| **Suspending Processes**        | `Ctrl + Z`                             | Pauses a process and keeps it in the background.                                         |                              |
| **Resuming Processes**          | `fg`                                   | Brings a suspended or background job to the foreground.                                  |                              |
| **Backgrounding Processes**     | `bg`                                   | Resumes a suspended process in the background.                                           |                              |
| **Starting Background Process** | `<command> &`                          | Launch a process directly in the background.                                             |                              |
| **Jobs Table**                  | `jobs`                                 | Displays a table of current jobs in the shell.                                           |                              |
| **Jobspec Usage**               | `%n`, `%str`, `%?str`, `%%`/`%+`, `%-` | Identifiers used with `fg` or `bg` to control jobs (cannot use PID directly).            |                              |
| **Foregrounding Process**       | `fg %<jobspec>`                        | Bring a background or suspended job to the foreground.                                   |                              |
| **Process Exit Codes**          | `$?`                                   | Retrieves the exit status of the last executed process.                                  |                              |
| **Special Challenge Notes**     | `/challenge/decoy`, `/tmp/flag_fifo`   | Sometimes decoy processes block named pipes; terminate decoys to retrieve the real flag. |                              |

---








## Listing Processes

<div align="center">
<img width="1099" height="396" alt="Listing processes" src="https://github.com/user-attachments/assets/59b5fb69-5965-4b68-963d-2299d73d049a" />
</div>

**Note:** Found the running `/challenge` process in `ps`, copied its full path, and ran that binary to reveal the flag.  

---

## Killing Processes

<div align="center">
<img width="1083" height="319" alt="Killing processes" src="https://github.com/user-attachments/assets/fa40037e-6202-4c9b-8a01-748470604da2" />
</div>

**Note:** First list all running processes with full, untruncated command lines using `ps -efww`, then filter for any process whose command contains `/challenge/dont_run` while excluding the grep command itself.  

---

## Interrupting Challenges

<div align="center">
<img width="1116" height="385" alt="Interrupting challenges" src="https://github.com/user-attachments/assets/09caa256-9d04-49c2-baee-84524d5e4964" />
</div>

**Note:** Ctrl + C while running sends an interrupt signal (SIGINT) to the process.  

---

## Killing Misbehaving Processes

<div align="center">
<img width="1099" height="760" alt="Killing misbehaving processes" src="https://github.com/user-attachments/assets/e0ccba49-3faa-4fce-85dd-f6ea564ffdba" />
</div>

**Note:** In this challenge, a decoy process blocked access to a named pipe (`/tmp/flag_fifo`), preventing `/challenge/run` from writing the real flag. To solve it, list all running processes using `ps aux`, find the decoy process (`/challenge/decoy`), note its PID, and terminate it with `kill <PID>`. After removing the decoy, `/challenge/run` successfully wrote the flag to `/tmp/flag_fifo`, retrievable with `cat /tmp/flag_fifo`.  

---

## Suspending Processes

<div align="center">
<img width="1082" height="721" alt="Suspending processes" src="https://github.com/user-attachments/assets/3f28ffa8-c014-4db1-b880-f6769500814c" />
</div>

**Note:** Ran `/challenge/run`, suspended it with **Ctrl+Z**, then started a second `/challenge/run` in the same terminal. Because one copy was suspended and another was active, the challenge detected the two instances and printed the flag.  

---

## Resuming Processes

<div align="center">
<img width="1090" height="479" alt="Resuming processes" src="https://github.com/user-attachments/assets/c83d86b3-fe3c-44a7-a23c-957061486cab" />
</div>

**Note:** Start `/challenge/run`, suspend it with **Ctrl+Z**, then use `fg` to bring it to the foreground. When resumed, it printed the flag.  

**Additional Notes on Job Control:**

- `jobs` displays current jobs.
- `bg` restarts a stopped background process.
- `fg` brings a background job to the foreground.  
- `fg` and `bg` **cannot** be used with a PID—they require a **jobspec**.  

**Jobspec Examples (from Greg's Bash Guide):**  
- `%n` — job number n  
- `%str` — job started by command beginning with str  
- `%?str` — job started by command containing str  
- `%%` or `%+` — current job  
- `%-` — previous job  

---

## Backgrounding Processes

<div align="center">
<img width="809" height="717" alt="Backgrounding processes" src="https://github.com/user-attachments/assets/c020b852-9667-47f9-a47a-96a7f342128e" />
</div>

---

## Foregrounding Processes

<div align="center">
<img width="1080" height="610" alt="Foregrounding processes" src="https://github.com/user-attachments/assets/0eb9ce9c-7a53-4047-9023-b9c30fe32f28" />
</div>

**Note:** Suspend with Ctrl-Z, background with `bg`, then bring it to the foreground with `fg`.  

---

## Starting Background Processes

<div align="center">
<img width="1300" height="352" alt="Starting background processes" src="https://github.com/user-attachments/assets/5d3a0c2c-f368-4be8-9af4-a9ca85a53a06" />
</div>

---

## Process Exit Codes

<div align="center">
<img width="1062" height="245" alt="Process exit codes" src="https://github.com/user-attachments/assets/68e09005-abd6-40ba-82c0-50d5488da337" />
</div>
