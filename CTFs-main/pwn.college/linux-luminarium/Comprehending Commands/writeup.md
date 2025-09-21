# Comprehending Commands

## Cat: not the pet but the command

<img width="887" height="125" alt="screenshot-1758449223" src="https://github.com/user-attachments/assets/70309b56-1bd0-46c5-ac86-536bdf3dc43f" />

Running cat flag  gave the flag

Notes - it's for concatenating documents , 

<img width="892" height="364" alt="screenshot-1758449384" src="https://github.com/user-attachments/assets/77c175b9-c7df-46cf-9969-6893484c5048" />

Also One use of cat that I'm fond of is privleged reading of a file. You can scope the superuser read to a single application, rather than the full pipeline.

```sudo cat /var/log/muffin.txt | head -n 100 | sort | uniq ```
