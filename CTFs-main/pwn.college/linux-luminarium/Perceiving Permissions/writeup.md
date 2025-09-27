# Perceiving Permissions 

## CHEAT SHEET 


| **Item**                                               |                                **Meaning / Use** |  **Symbolic example**  | **Octal example** | **What it does**                        |
| ------------------------------------------------------ | -----------------------------------------------: | :--------------------: | :---------------: | :-------------------------------------- |
| Who — user (owner)                                     |                                   The file owner |           `u`          |         —         | Refers to the owning **user**           |
| Who — group                                            |                        Users in the owning group |           `g`          |         —         | Refers to the file’s **group**          |
| Who — others                                           |                                    Everyone else |           `o`          |         —         | Refers to **other** users               |
| Who — all                                              |                           user, group and others |  `a` (same as `ug o`)  |         —         | Applies to **all** categories           |
| Read                                                   |               Permission to read file / list dir |           `r`          |         4         | Read bit (4)                            |
| Write                                                  | Permission to modify file / create/delete in dir |           `w`          |         2         | Write bit (2)                           |
| Execute                                                |                Run file / enter directory (`cd`) |           `x`          |         1         | Execute bit (1)                         |
| Add permission                                         |                        Add bits to existing mode |           `+`          |         —         | e.g. `g+w` gives group write            |
| Remove permission                                      |                   Remove bits from existing mode |           `-`          |         —         | e.g. `o-r` strips others’ read          |
| Set exactly                                            |            Replace permissions for WHO with WHAT |           `=`          |         —         | e.g. `u=rw` makes owner read+write only |
| Read for owner only (make file readable only by owner) |                                                — | `u+r,g-r,o-r` or `u=r` |       `400`       | Owner read, nobody else                 |
| Make readable by group                                 |                                                — |          `g+r`         |         —         | Group gains read                        |
| Make readable by others                                |                                                — |          `o+r`         |         —         | Everyone can read                       |
| Common full read-only for all                          |                                                — |          `a=r`         |       `444`       | Read by everyone, no write/exec         |
| Common rwx for owner, rx for group/others              |                                                — |    `u=rwx,g=rx,o=rx`   |       `755`       | Typical executable dir/program          |
| Common rw for owner, r for group, others none          |                                                — |      `u=rw,g=r,o=`     |       `640`       | Owner read/write, group read            |
| Shortcut: remove all group/other perms                 |                                                — |        `go-rwx`        |         —         | Tighten access to owner only            |
| Verify permissions                                     |                   See current mode and ownership |      `ls -l /path`     |         —         | Shows e.g. `-rw-r--r--`                 |

### How to read `-rwxr-xr--`

Break into three groups after the first character:

* `rwx` → owner (user) = read, write, execute
* `r-x` → group = read, execute
* `r--` → others = read only

### Quick examples

* `chmod g+w /flag` → give the group write on `/flag`
* `chmod o+r /flag` → make `/flag` readable by everyone
* `chmod u+x script.sh` → make `script.sh` executable by its owner
* `chmod 644 file` → equivalent to `u=rw,g=r,o=r`
* `chmod 700 dir` → owner full access, nobody else (good for private dirs)

---




## Changing file ownership 


<img width="1196" height="235" alt="screenshot-1758980134" src="https://github.com/user-attachments/assets/e32f3721-f0ed-4105-962e-3cc58b275186" />

## Groups and files 

<img width="1081" height="293" alt="screenshot-1758980887" src="https://github.com/user-attachments/assets/efd1a7d5-5ecd-4c72-acda-cbdd01d6ef59" />

Note - The chgrp command in Linux is used to change the group ownership of a file or directory. Every file has both an owner (a user) and a group, and permissions can be set separately for each


## Fun with group names 

<img width="1091" height="325" alt="screenshot-1758981071" src="https://github.com/user-attachments/assets/a8c5c4bb-0002-4277-addf-3e0869db9165" />

Note  - I see I’m in group grp9600 (from id). I'll change the flag’s group and read it : ) 

## Changing permissions


<img width="1312" height="256" alt="screenshot-1758982279" src="https://github.com/user-attachments/assets/484e14a9-c7fe-4076-9276-e615142e994a" />

Note - Giving others read (o+r) is the smallest change needed alsoess  you can use chmod 444 /flag to make it read-only for everyone mhmmm

## Executable Files

<img width="1306" height="231" alt="screenshot-1758983240" src="https://github.com/user-attachments/assets/1b782cb4-e1af-4d2c-91ee-1aecaf725efb" />

## Permission tweaking practises 


<img width="876" height="76" alt="screenshot-1758984242" src="https://github.com/user-attachments/assets/5840bafb-002f-4307-9e6c-a59e3135262a" />


Note - this was a very long game , went wrong multiple times skill isuue xd 

WHO — u (owner), g (group), o (others), a (all)

WHAT — r (read), w (write), x (execute)

ACTION — + (add), - (remove), = (set exactly)


## Permission setting practise 

<img width="1081" height="368" alt="screenshot-1758986872" src="https://github.com/user-attachments/assets/1618ff69-a03a-4c6d-9f0b-bce75a09c1e9" />

In `chmod`, **`a`** is a shorthand for `u,g,o` combined, meaning it applies to the owner, the group, and others simultaneously. For example, `chmod a=rx file` sets the permissions for all three categories owner, group, and others to read and execute (`r-x`) at once. This is equivalent to writing `chmod u=rx,g=rx,o=rx file`, which explicitly sets the same permissions separately for the user, group, and others.



