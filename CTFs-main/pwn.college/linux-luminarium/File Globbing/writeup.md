# FILE GLOBBING 


## Matching with * 


<img width="908" height="378" alt="screenshot-1758631090" src="https://github.com/user-attachments/assets/46f77fee-9206-4714-aca6-ac52f5a39616" />

Note - if there were multiple matches (like /candy and /challenge), /c* would expand to both → cd would error

## Matching with ?

<img width="1459" height="368" alt="screenshot-1758631323" src="https://github.com/user-attachments/assets/7684ed27-00de-4c7c-a4d8-a9da5b32d124" />

I did not understand the question : ( 

Note - ? is a wildcard for exactly one character in a filename or directory name ,It will match any single character, except / . 


## Matching with []



<img width="1443" height="333" alt="screenshot-1758631536" src="https://github.com/user-attachments/assets/992bec52-1cd6-4cfa-9edd-8eaa12c6c476" />

Note - The bracket glob [...] works a lot like the ? wildcard in that it matches exactly one character in a filename. The difference is that instead of matching any character, it lets you be selective about what counts as a match. 

## Matching paths with []


<img width="1449" height="309" alt="screenshot-1758631781" src="https://github.com/user-attachments/assets/08dfe546-a6df-4bb4-a4b1-ac917d3c665b" />

## Multiple globs


<img width="1453" height="322" alt="screenshot-1758631991" src="https://github.com/user-attachments/assets/46ec39cd-bd3d-46e4-8cc9-cb95a231e851" />


## Mixing globs 


<img width="1472" height="459" alt="screenshot-1758633715" src="https://github.com/user-attachments/assets/227ba360-fbb1-4cc2-9359-b4f0244579aa" />

## Exclutionary globbing 


<img width="923" height="406" alt="screenshot-1758633826" src="https://github.com/user-attachments/assets/589523f6-2a1e-4162-8c71-0d44a1ceca31" />


Note - Inside a bracket glob, ! at the first position negates the set 


## Tab completion 

<img width="888" height="378" alt="screenshot-1758634011" src="https://github.com/user-attachments/assets/af5dfa00-5e62-4186-b317-5954cc96f154" />

Note - tab-completion resolves tricky filenames with hidden characters or unusual symbols that you can’t type manually 

## Multiple option for tab completion


<img width="870" height="727" alt="screenshot-1758634296" src="https://github.com/user-attachments/assets/941c3d54-625b-481c-8c24-dcb4c32669be" />

Got some wierd nix error for some time so i had to restart it  
Note - the trick is that  tab-completion resolves filenames you can’t manually type





