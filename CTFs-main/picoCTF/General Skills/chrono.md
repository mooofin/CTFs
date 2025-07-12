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



