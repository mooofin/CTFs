Easily the worst CTF ive had the pleasure of solving , glad they updated the wayback machine url 

This challenge revolves around the Rockstar programming language, where values are represented by word lengths and keywords mimic poetic lyrics. The file provided contains Rockstar code that, when compiled, prompts for two inputs. The goal is to analyze the logic to determine the correct values.

The first part defines `a guitar` as 136 (from the phrase “a six-string”), and checks if the user input equals that. The second part checks if another input equals `Music`, which is calculated from the phrase “a billboard-burning razzmatazz” as 1970. So the two required inputs are **136** and **1970**.

Entering those values produces a final output string. When converted from ASCII, it spells `BONJOVI`, which gives the flag:
**picoCTF{BONJOVI}**.
