This challenge focuses on Linux file permissions and exploiting `sudo` access. We're trying to read a file in the `/root` directory, which is normally restricted.

Running `ls /root` results in a “Permission denied” error, confirming we can't access it directly. To see if we have any `sudo` privileges, we run `sudo -l`. The output shows that the user `picoplayer` is allowed to run `/usr/bin/vi` as root.

Since we can run `vi` with `sudo`, we use it to open the `/root` directory:

```
$ sudo vi /root
```

This launches `vi`'s directory browser (netrw), which shows the contents of `/root`. Among the files listed is `.flag.txt`.

To read it, we navigate to `.flag.txt` in `vi` and press `Enter` to open it. The flag will be displayed in the file contents.
