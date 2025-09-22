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



