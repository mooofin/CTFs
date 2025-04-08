
# Redacted – picoCTF Writeup

**Category:** Forensics  
**Tags:** document analysis, metadata, redacted text

---

## Description

> A redacted document was shared. Can you uncover what’s hidden?

---

## Provided File

- A `.docx` or similar document with redacted content.

---

## Tools Used

- Any modern word processor (MS Word or LibreOffice)
- Terminal (Zsh on Kali Linux)

---

## Approach

The redacted document appeared to have content hidden using visual obfuscation (black bars or similar). This is a common but ineffective method when done using basic drawing tools or highlight colors.

To uncover the hidden content, I simply **selected all text** or **copied and pasted it** into a terminal or text editor.

Here's the terminal interaction:

```bash
┌──(sid㉿kali)-[~/Downloads]
└─$ picoCTF{C4n_Y0u_S33_m3_fully}
```

Despite some initial confusion with terminal commands misinterpreting lines of text (e.g., "Breakdown" or "Credit"), the full flag was revealed in plaintext within the document content.

---

## Flag

```
picoCTF{C4n_Y0u_S33_m3_fully}
```

---

## Conclusion

This challenge demonstrates the importance of proper redaction. Simply "painting over" sensitive text in Word does **not** actually remove the data. Always use tools that **remove** the underlying text, not just hide it visually.

