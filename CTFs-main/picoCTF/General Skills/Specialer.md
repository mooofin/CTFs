```bash
Specialer$

\! complete export logout then
./ compopt false mapfile time
: continue fc popd times
[ coproc fg printf trap
[[ declare fi pushd true
]] dirs for pwd type
... (list of available commands)

Specialer$ for folder in abra ala sim

> do
> cd "$folder"
> for file in \*
> do
> if [ -d "$file" ]; then
> echo "$file: directory."
> elif [ -f "$file" ]; then
> echo "$folder/$file:"
> \<input redirection; alternative to 'cat'
> printf "\\n\\n"
> fi
> done
> cd ..
> done

abra/cadabra.txt:
Nothing up my sleeve\!

abra/cadaniel.txt:
Yes, I did it\! I really did it\! I'm a true wizard\!

ala/kazam.txt:
return 0 picoCTF{y0u\_d0n7\_4ppr3c1473\_wh47\_w3r3\_d01ng\_h3r3\_d5ef8b71}

ala/mode.txt:
Yummy\! Ice cream\!

sim/city.txt:
05ed181c-4aa0-4d4a-8505-2fe6ca9097d3

sim/salabim.txt:
\#He was so kind, such a gentleman tied to the oceanside\#

Specialer$
Specialer$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
```

### Solving "Specialer"

My initial exploration of the challenge instance was frustrating. Common commands like `ls` and `cat` were completely missing, which immediately told me I'd have to find an alternative. I noticed that some basic shell built-ins were still working, and a quick press of the **\<Tab\>** key for autocompletion confirmed my suspicion. The shell was missing a lot of standard binaries, but it had a powerful set of scripting tools like `for`, `if`, `do`, `echo`, and `printf`. This was the key to moving forward.

My first task was to replicate the functionality of `ls`. I wrote a simple `for` loop that would iterate through all items in the current directory (`for file in *`). Inside the loop, I used an `if` statement to check if each item was a **file (`-f`)** or a **directory (`-d`)**. The script worked perfectly, revealing three subdirectories: `abra`, `ala`, and `sim`.

My next step was to find the flag, which I assumed would be in a file within one of these directories. I needed to modify my script to not only find the files but also to read their contents. Since `cat` was unavailable, I had to be creative. I decided to use **input redirection** with `printf`.

I wrote a new script with a nested loop. The outer loop would iterate through the three directories (`for folder in abra ala sim`), and the inner loop would handle the files within each directory. For each file, the script would use `printf "%s " $(<$file)` to print its contents. The `$(<$file)` syntax redirects the file's content as a string, and `printf` then prints that string.

I ran the script, and the output was a collection of text snippets from various files. I quickly scanned the output for a `picoCTF` flag format. I found it in the file `ala/kazam.txt`:

```
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_d5ef8b71}
```


