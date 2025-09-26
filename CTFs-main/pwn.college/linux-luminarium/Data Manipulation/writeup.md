# DATA MANIPULATION 


## Translating characters 



<img width="1204" height="193" alt="screenshot-1758821724" src="https://github.com/user-attachments/assets/959d4116-f30b-4c71-8688-2cd372776f55" />


Note - The man page for tr 

<img width="898" height="487" alt="screenshot-1758821875" src="https://github.com/user-attachments/assets/9f4b1bbd-05d1-4998-9a69-43fc3eebde8f" />


## Deleating characters 

<img width="1300" height="272" alt="screenshot-1758821961" src="https://github.com/user-attachments/assets/d79834a7-e4cb-4459-b7be-7d587393c4d7" />

Note - tr -d is basically like a filter that cleans unwanted characters from text streams


## Deleting new lines 

<img width="1301" height="339" alt="screenshot-1758872813" src="https://github.com/user-attachments/assets/fc324469-06f3-424b-9365-43f6b84f1b73" />

Note - Use `tr -d "\n"` to remove all newline characters and print the flag as one continuous line.

 ## Extracting the first lines with head 

<img width="1101" height="343" alt="screenshot-1758872898" src="https://github.com/user-attachments/assets/6c4f2e9e-edbe-4a5b-97ea-240a27c60417" />

Note - keeps only its first 7 lines with head -n 7, and passes those lines to /challenge/college 

## Extract specific part of text 

<img width="1090" height="325" alt="screenshot-1758873092" src="https://github.com/user-attachments/assets/968523f9-d946-40c6-bb1c-71a7b85e936f" />

Note - The -d argument specifies the column delimiter (how columns are separated). In this case, it's a space character , The -f argument specifies the field number (which column to extract)
 
## Sorting data 

<img width="1077" height="260" alt="screenshot-1758873299" src="https://github.com/user-attachments/assets/9ed14187-f21a-42ee-8642-fc6928c9bd54" />

Note - By default, sort orders lines alphabetically. Arguments can change this:

    -r: reverse order (Z to A)
    -n: numeric sort (for numbers)
    -u: unique lines only (remove duplicates)
    -R: random order!



