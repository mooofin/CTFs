# DATA MANIPULATION

---
<div align="center" style="border:1px solid #ccc; padding:10px; width:400px; border-radius:8px; background-color:#f9f9f9;">
<b>Command Summary:</b><br>
<code>tr [SET1] [SET2]</code> → replace characters from SET1 with SET2<br>
<code>tr -d [CHAR]</code> → delete specified characters<br>
<code>tr -d "\n"</code> → remove all newlines<br>
<code>head -n [N]</code> → get first N lines of input<br>
<code>cut -d "[DELIM]" -f [FIELD]</code> → extract a column based on delimiter<br>
<code>sort [OPTIONS] [FILE]</code> → sort lines alphabetically or numerically
</div>

## Translating characters

<div align="center">

<img src="https://github.com/user-attachments/assets/959d4116-f30b-4c71-8688-2cd372776f55" width="900" />

**Note:** See the `tr` man page for details.

<img src="https://github.com/user-attachments/assets/9f4b1bbd-05d1-4998-9a69-43fc3eebde8f" width="700" />

</div>

---

## Deleting characters

<div align="center">

<img src="https://github.com/user-attachments/assets/d79834a7-e4cb-4459-b7be-7d587393c4d7" width="900" />

**Note:** `tr -d` acts like a filter that removes unwanted characters from text streams.

</div>

---

## Deleting newlines

<div align="center">

<img src="https://github.com/user-attachments/assets/fc324469-06f3-424b-9365-43f6b84f1b73" width="900" />

**Note:** Use `tr -d "\n"` to remove all newline characters and print text as one continuous line.

</div>

---

## Extracting the first lines with `head`

<div align="center">

<img src="https://github.com/user-attachments/assets/6c4f2e9e-edbe-4a5b-97ea-240a27c60417" width="900" />

**Note:** `head -n 7` keeps only the first 7 lines and passes them onward to `/challenge/college`.

</div>

---

## Extract specific part of text

<div align="center">

<img src="https://github.com/user-attachments/assets/968523f9-d946-40c6-bb1c-71a7b85e936f" width="900" />

**Note:**  
- `-d` specifies the column delimiter (here, a space `" "`).  
- `-f` specifies the field number (which column to extract).

</div>

---

## Sorting data

<div align="center">

<img src="https://github.com/user-attachments/assets/9ed14187-f21a-42ee-8642-fc6928c9bd54" width="900" />

**Note:**  
By default, `sort` orders lines alphabetically. Options include:  
- `-r`: reverse order (Z → A)  
- `-n`: numeric sort  
- `-u`: unique lines only  
- `-R`: random order  

</div>
