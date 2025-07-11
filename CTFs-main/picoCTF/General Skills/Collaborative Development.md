

After extracting the contents of the challenge archive, the following files are present:

```bash
$ ls
flag.py  message.py  message.txt
```

The file `flag.py` contains only a single line:

```python
print("Printing the flag...")
```

There is no visible flag in the current state. However, the presence of a Git repository (either from context or by checking for a `.git` directory) suggests that useful information might exist in the commit history or other branches.

---

### Inspecting Git History

Attempting to view a branch named `feature/part2` results in an error:

```bash
$ git log feature/part2
fatal: ambiguous argument 'feature/part2': unknown revision or path not in the working tree.
```

After trying a corrected branch name using hyphens, `feature/part-2`, the log is successfully retrieved:

```bash
$ git log feature/part-2
commit e1629c7...
Author: picoCTF
Date:   Mar 12 2024

    add part 2
```

This confirms that branches are named in the format `feature/part-1`, `feature/part-2`, and so on.

---

### Extracting Flag Segments from Git Diffs

The command `git diff <commit>` is used to view the changes introduced in each part branch. These diffs reveal fragments of the flag that were removed or altered.

#### Part 1

```bash
$ git diff b2e05429742e8784eee7dc83b6a9d1fb904988c0
```

Relevant output:

```diff
-print("picoCTF{t3@mw0rk_", end='')
```

This provides the beginning of the flag:

```
picoCTF{t3@mw0rk_
```

#### Part 2

```bash
$ git diff e1629c73b55d8831cfa3cda13a74c3e8f7c9e2f1
```

Relevant output:

```diff
-print("m@k3s_th3_dr3@m_", end='')
```

This adds the next segment:

```
m@k3s_th3_dr3@m_
```

#### Part 3

```bash
$ git diff 8fccfcdaeeb259a51b642ba76ec2e5feb086c057
```

Relevant output:

```diff
-print("w0rk_7ae8dd33}")
```

This completes the flag:

```
w0rk_7ae8dd33}
```

---

### Final Flag



```
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_7ae8dd33}
```



