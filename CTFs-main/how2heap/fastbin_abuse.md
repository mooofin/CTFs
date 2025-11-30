<img width="933" height="731" alt="image" src="https://github.com/user-attachments/assets/cbe98232-be80-4d1f-858b-0b8debb554a6" />


Internally, the heap manager needs to keep track of freed chunks so that malloc can reuse them during allocation requests. In a naive implementation, the heap manager could do this by simply storing all freed chunks together on some enormous linked list. This would work, but it would make malloc slow. Since malloc is a high-utilization component of most programs, this slowness would have a huge impact on the overall performance of programs running on the system.

To improve performance, the heap manager instead maintains a series of lists called “bins”, which are designed to maximize speed of allocations and frees.



<img width="1832" height="837" alt="image" src="https://github.com/user-attachments/assets/f497fa74-1fa2-476a-98de-8adc25ab5024" />

mall freed chunks go into fastbins as a singly linked list. Normally a double free crashes because glibc detects when the freed chunk is already at the head of the list, but you can bypass this by inserting another chunk between two frees. The classic pattern is free(A), free(B), then free(A) again. Since A is no longer the head when you free it the second time, glibc accepts it, and the fastbin list becomes [A, B, A]. Now when you call malloc three times, glibc pops from the fastbin in order and returns A, then B, and then A again, giving you two separate pointers that alias the same memor


Tcache  malloc implementation keeps a smallish pool of preallocated blocks of various sizes for each thread. That way many calls can be satisfied without lock.
```c
This file demonstrates a simple double-free attack with fastbins.
Fill up tcache first.
Allocating 3 buffers.
1st calloc(1, 8): 0x9133a0
2nd calloc(1, 8): 0x9133c0
3rd calloc(1, 8): 0x9133e0
Freeing the first one...
If we free 0x9133a0 again, things will crash because 0x9133a0 is at t
he top of the free list.
So, instead, we'll free 0x9133c0.
Now, we can free 0x9133a0 again, since it's not the head of the free 
list.
Now the free list has [ 0x9133a0, 0x9133c0, 0x9133a0 ]. If we malloc 3 
times, we'll get 0x9133a0 twice!
1st calloc(1, 8): 0x9133a0
2nd calloc(1, 8): 0x9133c0
3rd calloc(1, 8): 0x9133a0
```
