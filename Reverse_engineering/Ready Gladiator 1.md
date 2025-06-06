

I was working on a Core War challenge from picoCTF, where I had to make my Redcode warrior defeat the opponent at least once in 100 rounds. My first attempt was a simple **imp** program:

```
mov 0, 1
```

It just copies itself forward, which didn’t kill the opponent — it only tied.

I needed to build a better warrior that could actually kill. So I made a new warrior called **Imp Ex**:

```redcode
;redcode
;name Imp Ex
;assert 1
ADD.AB #4, 3
MOV.I 2, @2
JMP -2
DAT #0, #0
end
```

I’ll explain what this does in my own words.

The first line, `ADD.AB #4, 3`, adds 4 to the B-field of the instruction 3 steps ahead. This gradually expands how far the warrior attacks in memory. Then, `MOV.I 2, @2` copies instructions from 2 ahead to wherever the instruction 2 ahead points to, creating a bombing effect that overwrites enemy code. The `JMP -2` just loops it back to do it all over again. Finally, `DAT #0, #0` is a deadly bomb — if the opponent runs into this, it’s instant death.

When I saved this code into `imp.red` and sent it to the server with:

```
nc saturn.picoctf.net 61202 < imp.red
```


#### References

* **[Core War Guide](https://vyznev.net/corewar/guide.html#introduction)** – This was super helpful to understand the basics of Core War 

---
![image](https://github.com/user-attachments/assets/b4cc1d7f-511e-47e0-9431-ce0187a618f9)


