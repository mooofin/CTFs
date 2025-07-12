In this challenge, I was given SSH credentials to access a remote Linux machine. I connected using:

```bash
ssh picoplayer@saturn.picoctf.net -p 53154
```

and used the provided password: `H9RmN0m18U`.

After logging in as the `picoplayer` user, I navigated around the system to look for readable files. Attempts to access sensitive directories like `/challenge` were met with `Permission denied`, confirming limited user privileges. However, I still had read access to other system-level files.

Keeping the hint in mind — about automating tasks — I checked the **crontab** system, which manages scheduled tasks on Linux. The system-wide crontab file is located at `/etc/crontab`, and I viewed it with:

```bash
cat /etc/crontab
```

This immediately revealed the flag as a comment inside the file:

```
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_d83baed1}
```

The `crontab` (short for **cron table**) is a configuration file used by the `cron` daemon in Unix-like systems to schedule and automate repetitive tasks at specific intervals—ranging from every minute to monthly or in custom time patterns. These tasks, known as **cron jobs**, can include running scripts, backups, system maintenance, and more.


<img width="919" height="321" alt="screenshot-1752317162" src="https://github.com/user-attachments/assets/d534e9a7-a1ef-4e13-a475-2f82d2a303e8" />



