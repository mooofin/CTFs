<div align="center">

# Untangling Users

## Becoming root with SU

<figure>
  <img src="https://github.com/user-attachments/assets/e98ac864-7359-4663-99c8-0df354f53876" alt="screenshot-1758910828" style="max-width:900px; width:100%; height:auto;">
</figure>

## Other users with su

<figure>
  <img src="https://github.com/user-attachments/assets/2e2f3299-2407-4bca-8dbd-b5570635ea20" alt="screenshot-1758914550" style="max-width:900px; width:100%; height:auto;">
</figure>

**Note** - almost similar

## Cracking passwords

<figure>
  <img src="https://github.com/user-attachments/assets/cebd6596-9401-415f-aa87-f3da3287ce93" alt="screenshot-1758915013" style="max-width:900px; width:100%; height:auto;">
</figure>

**Note** - When you log in or use `su` to switch users, the system checks your password by hashing it and comparing it to the stored hash. Historically, these hashes were stored in `/etc/passwd`, but since that file must be world readable for system functions, storing password hashes there was insecure.

To fix this, password hashes were moved to `/etc/shadow`, which is only readable by root. However, if `/etc/shadow` ever leaks for example, through a misconfigured backup or accidental disclosure attackers can try to crack the hashes offline.

ALSO  the use of a salt with a hash is important. The salt is a random piece of information that is used to deter the use of rainbow tables (i.e., pre-computed hashes to attack password hashes).

## using sudo

<figure>
  <img src="https://github.com/user-attachments/assets/a1f6d32a-4411-4528-bfaf-2644a01fa5fd" alt="screenshot-1758915472" style="max-width:900px; width:100%; height:auto;">
</figure>

</div>



Rant - 



If you take a look at the executable sudo:
```
$ which sudo
/usr/bin/sudo
$ ls -la /usr/bin/sudo
---s--x--x 2 root root 208808 Jun  3  2011 /usr/bin/sudo
```
You'll notice that it carries the permission bits ---s--x--x. These can be broken down as follows:
```
-|--s|--x|--x
-      - first dash denotes if a directory or a file ("d" = dir, "-" = file)  
--s    - only the setuid bit is enabled for user who owns file
--x    - only the group execute bit is enabled
--x    - only the other execute bit is enabled
```
So when a program has it's setuid bit enabled (also referred to as SUID) it means that when someone runs this program it will run with the credentials of the user that owns the file, aka. root in this case.
Example

If I run the following command as user muffin:
```
$ whoami
muffin

$ sudo su -
[sudo] password for muffin: 

You'll notice that the execution of sudo actually is running as root:

$ ps -eaf|grep sudo
root     20399  2353  0 05:07 pts/13   00:00:00 sudo su -
```
### setuid mechanism

 Here's an excerpt from the man page that explains it better than I could:

  setuid() sets the effective user ID of the calling process. If the effective UID of the caller is root, the real UID and saved set-user-ID are also set. Under Linux, setuid() is implemented like the POSIX version with the _POSIX_SAVED_IDS feature. This allows a set-user-ID (other than root) program to drop all of its user privileges, do some un-privileged work, and then reengage the original effective user ID in a secure manner.

  If the user is root or the program is set-user-ID-root, special care must be taken. The setuid() function checks the effective user ID of the caller and if it is the superuser, all process-related user ID's are set to uid. After this has occurred, it is impossible for the program to regain root privileges.

The key concept here is that programs have a real userid (UID) and an effective one (EUID). Setuid is setting the effective userid (EUID) when this bit is enabled.

So from the kernel's perspective it's known that in our example, saml is still the original owner (UID), but the EUID has been set with whomever is the owner of the executable.
setgid

I should also mention that when we're breaking down the permissions on the sudo command the second group of bits were for group permissions. The group bits also has something similar to setuid called set group id (aka. setgid, SGID). This does the same thing as SUID except it runs the process with the group credentials instead of the owner credentials.
