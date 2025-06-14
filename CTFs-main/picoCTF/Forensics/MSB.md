

## Objective
Extract a `picoCTF` flag from a file using command-line tools and save it into a file named with a `.png` extension.

---

## Step-by-Step

### 1. Create a Dummy File
First, I created a sample `outputSB.txt` file with some fake flag content:

```bash
echo "some junk text picoCTF{this_is_a_fake_flag_12345} more junk" > outputSB.txt
echo "nothing here" >> outputSB.txt
echo "another one: picoCTF{another_fake_flag_67890} wow" >> outputSB.txt
```

---

### 2. Extract the Flag Using `grep`

Then, I used `grep` with a regular expression to search for any line containing `picoCTF` followed by up to 50 characters:

```bash
grep -o -E "picoCTF.{0,50}" outputSB.txt > "Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png"
```

#### Explanation:
- `grep`: searches through the text.
- `-o`: outputs only the matching parts.
- `-E`: enables extended regular expressions (needed for `{0,50}`).
- `"picoCTF.{0,50}"`: matches `picoCTF` followed by up to 50 characters.
- `> "Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png"`: saves the result in a file with a `.png` extension.

---

### 3. View the Output
To confirm the result:

```bash
cat "Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png"
```

Output:
```
picoCTF{this_is_a_fake_flag_12345}
picoCTF{another_fake_flag_67890}
```

---

## Takeaway

Even if the file does not actually contain an image, naming it with a `.png` extension can help conceal the flag or bypass basic file inspection techniques. The `grep` command with regular expressions is highly effective in CTFs for extracting flags from noisy or unstructured output.

---

