 There was no source and no symbols to help, so the only option was to read the program and see what it does.

Inside the binary  the program uses a set of small helper routines to manipulate an internal block of memory and a few registers. In plain terms, the binary builds a little internal state, asks the user for four bytes of input, and then compares those bytes to a secret it had written into its own memory earlier. If the bytes match, it opens the flag file and prints it. If any byte is wrong, it prints INCORRECT and exits.

 Those bytes end up at addresses 0x5c through 0x5f and are, in order: 0x4c, 0xde, 0xa6, 0x12. After that the program reads four bytes from standard input into a buffer and compares each input byte with the corresponding secret byte. All four comparisons must succeed for the program to proceed to the flag-reading steps.

 the binary expects exactly those four raw bytes on stdin. The input must be the literal bytes, not their text representations. Sending the sequence 4c de a6 12 prints /flag.



```bash
python -c "import sys; sys.stdout.buffer.write(b'\x4c\xde\xa6\x12')"  
```


<img width="1921" height="1081" alt="screenshot-1760278204" src="https://github.com/user-attachments/assets/d53aed21-0da8-4aca-bbdd-b566f15de1a0" />


