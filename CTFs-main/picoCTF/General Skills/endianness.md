![image](https://github.com/user-attachments/assets/346e7be7-fbed-4c88-8ec9-66b7fcfb010b)



Numbers are always written with the most significant digit on the left and the units on the right but it doesn't follow that the bit numbers are the same between machines. Some machines number the m.s. (left) digit bit zero and others number the l.s. (right) bit zero.

In the early days of computing (not that early, say up to the 1990's), it was common to number the m.s. digit bit 0 because mainframes dealt in floating point values and having it this way round meant that the units would be at the top and highest bit number represented the precision. If we were using decimal digits for example, 0.314 would be a 3 digit FP number, digit 0 would be the 3 and digit 2 would be the 4. Increase the precision and 0.314159, digit 0 is still the 3 and digit 5 is the 9. This scheme was used in binary and BCD in mainframes.

For integers, it makes more sense to number the l.s. digit bit 0 and have the size of the register/variable/bus be represented by the m.s. digit. These days we have completely standardised on this system. So, while it may not be true to say ALL values are numbered this way, it is almost universally true.

BYTE ordering:

Unfortunately byte numbering isn't so clear. This problem is called endian-ness. Big-endian systems put the m.s. byte first in memory e.g. 0x1234 would put 0x12 in the first address then 0x34 in the next address up i.e. addr+1 whereas a little-endian system would do the opposite. If you store 0x12345678 and read the memory in increasing address order, a little endian system would be 0x78 0x56 0x34 0x12 whereas a big-endian system would be 0x12 0x34 0x56 0x78.

It follows that, if you want to send data across a link, you need to know what order the bytes are in and furthermore, if you send it big-endian and try to read it little-endian, then you're in trouble. Code which is immune to endian-ness is called endian-neutral. Libraries and other widely used code is endian-neutral.

All Intel CPUs are little-endian. Some older CPUs from Motorola which were widely used in early networks are big-endian so internet packets are in big-endian order. This makes them easier to read in a memory dump but the reason why they chose big-endian is unlikely to be this reason. It also slows down processing with a little-endian CPU.
