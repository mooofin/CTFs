### Main Function (FUN_00100b6a)

The entry point 

<img width="1912" height="809" alt="image" src="https://github.com/user-attachments/assets/b0904b9f-94e2-4fc6-acab-a392734eb688" />


```c
1. Initialize hardcoded string: "GpLaMjEWpVOjnnmkRGiledp6Mvcezxls" (32 bytes)
2. Initialize permutation array: [8, 2, 7, 1]
3. Read 16-byte password from user
4. Interleave password with hardcoded string
5. Hash the interleaved data using MD5
6. Apply permutation to extract 16 bytes
7. Execute the resulting bytes as shellcode
```

### Data Structures i found 

```c
char local_c8[47];      // Hardcoded secret string
int local_e8[4];        // Permutation indices: {8, 2, 7, 1}
char acStack_99[65];    // User input buffer
char local_58[72];      // Interleaved data buffer
```




### Algorithm

The interleaving process alternates between user input and the secret string:

```c
for (i = 0; i < 4; i++) {
    strncat(result, password + (i * 4), 4);    // 4 bytes from password
    strncat(result, secret + (i * 8), 8);      // 8 bytes from secret
}
```

### then it does 

```
Input:  [P0 P1 P2 P3][P4 P5 P6 P7][P8 P9 PA PB][PC PD PE PF]  (16 bytes)
Secret: [S0..S7][S8..SF][S10..S17][S18..S1F]                  (32 bytes)

Output: [P0 P1 P2 P3][S0..S7][P4 P5 P6 P7][S8..SF]...         (48 bytes)
```

This creates a 48-byte buffer where every 12-byte segment contains 4 bytes of user input followed by 8 bytes of hardcoded data



## Stage 2: MD5 Hashing (FUN_00100e3e)

### This righ here 

```c
void FUN_00100e3e(long output_buffer, void *input_data, int length)
{
    int num_chunks = (length % 12 == 0) ? (length / 12) : (length / 12 + 1);
    
    for (int i = 0; i < num_chunks; i++) {
        int chunk_size = (i == num_chunks - 1 && length % 12 != 0) 
                         ? (length % 12) 
                         : 12;
        
        MD5_Init(&ctx);
        MD5_Update(&ctx, input_ptr, chunk_size);
        MD5_Final(hash, &ctx);
        
        // Store 16-byte hash in circular buffer
        for (int j = 0; j < 16; j++) {
            output_buffer[(i * 16 + j) % 64] = hash[j];
        }
        
        input_ptr += chunk_size;
    }
}
```

### in short this does ? 

1. Split 48 bytes into 4 chunks of 12 bytes each
2. Compute MD5 hash of each chunk (16 bytes output per chunk)
3. Store hashes sequentially in 64-byte buffer
4. Result: 4 x 16 = 64 bytes of hashed data



### Algo

The permutation applies a two-dimensional extraction pattern:

```c
int permutation[4] = {8, 2, 7, 1};

for (col = 0; col < 4; col++) {
    for (row = 0; row < 4; row++) {
        source_index = permutation[row] + (row * 16) + col;
        dest_index = (row * 4) + col;
        output[dest_index] = hashed_data[source_index];
    }
}
```

### we can see this as a matrix 

Viewing the 64-byte buffer as a 4x16 matrix:

```
Row 0: [00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F]
Row 1: [10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F]
Row 2: [20 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F]
Row 3: [30 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E 3F]
```

The permutation selects specific columns from each row based on the indices [8, 2, 7, 1]:

```
Output bytes extracted:
- From row 0, offset 8: 0x08
- From row 1, offset 2: 0x12
- From row 2, offset 7: 0x27
- From row 3, offset 1: 0x31
(Repeated for all 4 columns)
```

This produces 16 bytes arranged as: [08 12 27 31][09 13 28 32][0A 14 29 33][0B 15 2A 34]


## then x2

### Memory Mapping

```c
code *shellcode = mmap(NULL, 16, PROT_READ|PROT_WRITE|PROT_EXEC, 
                       MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
memcpy(shellcode, permuted_bytes, 16);
shellcode(FUN_0010102b);
```

The program:
1. Allocates 16 bytes of executable memory
2. Copies the permuted bytes into this region
3. Executes it as a function, passing `FUN_0010102b` as the first argument



## how 2 pwm 

### Target Function

```c
void FUN_0010102b(long param_1)
{
    if (param_1 == 0x7b3dc26f1) {
        FILE *fp = fopen("flag", "r");
        char buffer[136];
        fgets(buffer, 128, fp);
        puts(buffer);
    }
    else {
        puts("Hmmmmmm... not quite");
    }
}
```

### in short 

The shellcode must:
1. Set RDI register to `0x7b3dc26f1`
2. Call the function pointer that was passed as the first argument




## pwning 



Given the hint that the password starts with "D1v1" and the reference to a paper on "Divide and Conquer" techniques, the password is:

```
D1v1d3AndC0nqu3r
```

This is leetspeak for "Divide and Conquer". 



The password produces the following 16-byte shellcode:

```
48 89 fe                    mov    rsi, rdi
48 bf f1 26 dc b3 07 00 00 00   movabs rdi, 0x7b3dc26f1
ff d6                       call   rsi
c3                          ret
```

<img width="773" height="48" alt="image" src="https://github.com/user-attachments/assets/dccbe562-2ef3-478c-b9bd-0901092eec95" />


1. `mov rsi, rdi`: Preserve the function pointer (originally in RDI) to RSI
2. `movabs rdi, 0x7b3dc26f1`: Load the magic constant into RDI (first argument register)
3. `call rsi`: Invoke the preserved function pointer
4. `ret`: Return to caller

This satisfies the requirement of calling `FUN_0010102b(0x7b3dc26f1)`.


<img width="600" height="80" alt="image" src="https://github.com/user-attachments/assets/933cc886-f9bd-4118-af91-102445f25ae6" />


Notes- very guessy , 1/10 , the paper was nice 
[Anti-disassembly using Cryptographic Hash Functions](https://link.springer.com/article/10.1007/s11416-006-0011-3)

