 CrackMe Writeup - Basic Reverse Engineering

**Author:** idanhajbeko
**Platform:** Unix/Linux
**Architecture:** x86-64
**Difficulty:** 1.2
**Language:** C/C++
**Uploaded:** 04:04 PM 04/26/2025
**Quality:** 3.2



##  Analysis

The decompiled code for the `main` function is as follows:

```c
undefined8 main(void)
{
  int iVar1;
  char *__format;
  char local_3f8 [1008];

  while( true ) {
    puts("Enter the password: ");
    __isoc99_scanf("%999s", local_3f8);
    iVar1 = strcmp(local_3f8, "!_-P@$$w0rD-_!");
    if (iVar1 == 0) break;
    printf("The password ");
    putchar(0x69);  // 'i'
    putchar(0x73);  // 's'
    putchar(0x20);  // ' '
    puts("\x1b[0;31mincorrect\x1b[0m");
  }

  printf("\x1b[0;32m");
  __format = (char *)getFlag();
  printf(__format);
  printf("\x1b[0m");
  return 0;
}
```

---

## Reverse Engineering

Looking at the logic:

* The program prompts the user to enter a password.
* It compares the user input against the hardcoded string `"!_-P@$$w0rD-_!"` using `strcmp`.
* If the password matches, it breaks out of the loop and prints the flag using `getFlag()`.
* Otherwise, it displays an error message saying the password is incorrect.

---

##  Solution

The hardcoded password is:

```
!_-P@$$w0rD-_!
```

Entering this when prompted will cause the program to print the flag.

---

