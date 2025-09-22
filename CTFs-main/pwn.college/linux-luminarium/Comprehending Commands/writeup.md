# Comprehending Commands

## Cat: not the pet but the command

<img width="887" height="125" alt="screenshot-1758449223" src="https://github.com/user-attachments/assets/70309b56-1bd0-46c5-ac86-536bdf3dc43f" />

Running cat flag  gave the flag

Notes - it's for concatenating documents , 

<img width="892" height="364" alt="screenshot-1758449384" src="https://github.com/user-attachments/assets/77c175b9-c7df-46cf-9969-6893484c5048" />

Also One use of cat that I'm fond of is privleged reading of a file. You can scope the superuser read to a single application, rather than the full pipeline.

```sudo cat /var/log/muffin.txt | head -n 100 | sort | uniq ```


## Catting Absolute Paths

<img width="572" height="79" alt="screenshot-1758449735" src="https://github.com/user-attachments/assets/b8ef3e07-f5bf-41fd-ade1-a47ad7d37a16" />

Notes- This reinforces that cat can take absolute paths as arguments, not just files in your current directory

## More Catting Practice


<img width="726" height="155" alt="screenshot-1758449864" src="https://github.com/user-attachments/assets/55a63fae-704d-4874-9071-d7e3788d1d18" />

Note - Ripgrep (rg) is a good replacement for grep. Colored output, faster, shorter to type.

Also a very cool video with kojia level production by laurie wired


[grep isn't what you think it means... - YouTube](https://youtu.be/iQZ81MbjKpU?si=4sK_5cj19zUKs1DP)


## Comparing files 


By running `diff /challenge/decoys_and_real.txt /challenge/decoys_only.txt`, we compared the file containing both decoys and the real flag against the one with only decoys. The output showed one extra line, marked with `<`, which revealed the flag: `pwn.college{I6IaeqAhkPIzYBjCadL0ATT3I6q.QXzAzM4EDL0ATO0czW}`.

<img width="888" height="278" alt="screenshot-1758524858" src="https://github.com/user-attachments/assets/13ede348-16b9-4bb8-8233-683ee1853006" />

## Listing Files


<img width="918" height="239" alt="screenshot-1758549089" src="https://github.com/user-attachments/assets/49a982b3-1f80-4ba0-a40d-c184cfe01e33" />


Running the file as an executable (`/challenge/10062-renamed-run-30646`) produced the hidden message and revealed the flag: `pwn.college{IzQ8c0OGgydpF4q9CDs0zRjLrRG.dhjM4QDL0ATO0czW}`.

notes - ls = "list the content of a DIRECTORY" (not folder)

## Touching files 
<img width="1008" height="287" alt="screenshot-1758549320" src="https://github.com/user-attachments/assets/e6c4cdc1-fc6c-49df-b24c-6c7df26ff727" />



## Removing files 

<img width="985" height="335" alt="screenshot-1758549819" src="https://github.com/user-attachments/assets/a6f37c20-4eb1-48f0-863a-be2bc839ec5c" />

## moving files 

<img width="984" height="264" alt="screenshot-1758549923" src="https://github.com/user-attachments/assets/41599ec7-7b93-4966-9e28-0829dbb92e6a" />


## Hidden files 

<img width="986" height="525" alt="screenshot-1758550104" src="https://github.com/user-attachments/assets/919eab77-cec8-418f-be5b-e2266f5ae379" />

Notes- 

Traditionally, in UNIX and UNIX-like operating systems, the . prefix means a hidden file, similar to the "Hidden" flag in Windows. It works anywhere, but its primary use is to hide configuration files in your home directory (e.g. ~/.cache/ or ~/.plan – they're frequently called "dotfiles").

To force ls to display hidden files, you need the -a option.

Almost all graphical file managers also honor this prefix; CtrlH toggles "hidden" files in GNOME.


## Epic Filesystem Quest




### Chronological commands & key outputs

1. Start: read the initial memo

```bash
cat MEMO
# → points to /usr/share/javascript/.../Size3/Regular and warns the next clue is trapped
```

2. List the target directory and safely read the trapped file (do **not** cd)

```bash
ls -a /usr/share/javascript/mathjax/jax/output/SVG/fonts/TeX/Size3/Regular
# → .  ..  GIST-TRAPPED  Main.js

cat /usr/share/javascript/mathjax/jax/output/SVG/fonts/TeX/Size3/Regular/GIST-TRAPPED
# → "The next clue is in: /usr/local/lib/python3.8/dist-packages/IPython/lib/tests"
```

3. List and read the next clue:

```bash
ls /usr/local/lib/python3.8/dist-packages/IPython/lib/tests
# → shows files including ALERT

cat /usr/local/lib/python3.8/dist-packages/IPython/lib/tests/ALERT
# → "The next clue is in: /opt/linux/linux-5.4/Documentation/devicetree/bindings/phy"
```

4. Inspect the phy directory and read the trapped teaser:

```bash
ls /opt/linux/linux-5.4/Documentation/devicetree/bindings/phy
# → many filenames, including TEASER-TRAPPED

cat /opt/linux/linux-5.4/Documentation/devicetree/bindings/phy/TEASER-TRAPPED
# → "The next clue is in: /opt/linux/linux-5.4/Documentation/devicetree/bindings/iio/dac"
```

5. Reveal hidden entries and read the hidden clue:

```bash
ls -a /opt/linux/linux-5.4/Documentation/devicetree/bindings/iio/dac
# → contains .TRACE

cat /opt/linux/linux-5.4/Documentation/devicetree/bindings/iio/dac/.TRACE
# → "The next clue is in: /usr/local/lib/python3.8/dist-packages/jupyterlab_server/test_data/workspaces"
# The clue indicates the next file is delayed (requires cd).
```

6. Enter the delayed directory to unlock the clue:

```bash
cd /usr/local/lib/python3.8/dist-packages/jupyterlab_server/test_data/workspaces
ls
# → INSIGHT (and workspace files)

cat INSIGHT
# → "The next clue is in: /opt/linux/linux-5.4/arch/x86/platform/olpc"
```

7. `cd` into the OLPC dir (delayed), list and read:

```bash
cd /opt/linux/linux-5.4/arch/x86/platform/olpc
ls
# → NUGGET, Makefile, etc.

cat NUGGET
# → "The next clue is in: /usr/share/racket/pkgs/r6rs-lib/r6rs/compiled"
# NUGGET was delayed, so `cd` was required.
```

8. Enter the Racket directory (delayed) and read DOSSIER:

```bash
cd /usr/share/racket/pkgs/r6rs-lib/r6rs/compiled
ls
# → DOSSIER, info_rkt*.dep/zo

cat DOSSIER
# → "The next clue is in: /usr/local/lib/python3.8/dist-packages/_argon2_cffi_bindings/__pycache__"
# The clue says the next file is hidden (filename starts with '.')
```

9. Show hidden files in the absolute target and read the hidden file:

```bash
ls -a /usr/local/lib/python3.8/dist-packages/_argon2_cffi_bindings/__pycache__
# → .  ..  .TIP  __init__.cpython-38.pyc  _ffi_build.cpython-38.pyc

cat /usr/local/lib/python3.8/dist-packages/_argon2_cffi_bindings/__pycache__/.TIP
# → "CONGRATULATIONS! ... It is: pwn.college{0zt40yEsdJJy929fQLzPQE9qAj0.dljM4QDL0ATO0czW}"
```

---

### Flag

```
pwn.college{0zt40yEsdJJy929fQLzPQE9qAj0.dljM4QDL0ATO0czW}
```

---

