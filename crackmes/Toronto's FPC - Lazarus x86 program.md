



"project1.1000072F0" shows the message "Input your passwd":

0000000100001493 | 48:89D9                  | mov rcx,rbx                             |
0000000100001496 | E8 555E0000              | call project1.1000072F0                 |



"project1.1000078A0" is used to read user input and store it at the buffer pointed by 0x10000F000.

00000001000014B4 | 48:8D15 45DB0000         | lea rdx,qword ptr ds:[10000F000]        | rdx:&"\t0\t5\t0\t@\t:", 000000010000F000:&"22222"
00000001000014BB | 48:89D9                  | mov rcx,rbx                             |
00000001000014BE | 41:B8 00000000           | mov r8d,0                               |
00000001000014C4 | E8 D7630000              | call project1.1000078A0                 |



"project1.100007640" reads the input password and returns it into "rax"

00000001000014CE | 48:89D9                  | mov rcx,rbx                             |
00000001000014D1 | E8 6A610000              | call project1.100007640                 |




At 00000001000014DB, the program loads into "rdx" the value "11111". Then it loads into "rcx" the provided password.
Then it compares the two strings in 00000001000014EE. The following result is returned in "rax":
- if the two strings have different length, it returns len(password) - len("11111")
- if the strings have same length, but password > 11111, then it returns 1
- if the strings have same length, but password < 11111, then it returns -1
- if they are equals, it returns 0

00000001000014DB | 48:8D15 4EBB0000         | lea rdx,qword ptr ds:[10000D030]        | rdx:"1111", 000000010000D030:"11111"
00000001000014E2 | 48:8B0D 17DB0000         | mov rcx,qword ptr ds:[10000F000]        | 000000010000F000:&"22222"
00000001000014E9 | E8 B2140000              | call project1.1000029A0                 |



If "rax" is zero, the jump is not taken, and the function "project1.1000072F0" shows a congrats message on the console.
Otherwise, the execution is redirected to "project1.100001523", where a message shows that the password typed is not correct.


00000001000014EE | 48:85C0                  | test rax,rax                            |
00000001000014F1 | 75 30                    | jne project1.100001523                  |
00000001000014F3 | E8 985C0000              | call project1.100007190                 |
00000001000014F8 | 48:89C3                  | mov rbx,rax                             |
00000001000014FB | 4C:8D05 36BB0000         | lea r8,qword ptr ds:[10000D038]         |
0000000100001502 | 48:89DA                  | mov rdx,rbx                             | rdx:"1111"
0000000100001505 | B9 00000000              | mov ecx,0                               |
000000010000150A | E8 A15E0000              | call project1.1000073B0                 |
000000010000150F | E8 BC240000              | call project1.1000039D0                 |
0000000100001514 | 48:89D9                  | mov rcx,rbx                             |
0000000100001517 | E8 D45D0000              | call project1.1000072F0                 |
000000010000151C | E8 AF240000              | call project1.1000039D0                 |
0000000100001521 | EB 2E                    | jmp project1.100001551                  |
0000000100001523 | E8 685C0000              | call project1.100007190                 |
0000000100001528 | 48:89C3                  | mov rbx,rax                             |
000000010000152B | 4C:8D05 1EBB0000         | lea r8,qword ptr ds:[10000D050]         | 000000010000D050:"\f = Not  ;-( "
0000000100001532 | 48:89DA                  | mov rdx,rbx                             | rdx:"1111"
0000000100001535 | B9 00000000              | mov ecx,0                               |
000000010000153A | E8 715E0000              | call project1.1000073B0                 |
'''

print("[+] PASSWD: 11111")
When executed, the binary prompts the user to input a password. By reverse engineering the binary using tools like IDA, Ghidra, or x64dbg, we identify that user input is read into memory at address 0x10000F000, and then compared to a hardcoded string located at 0x10000D030. The comparison function at 0x1000029A0 performs a length check and lexicographical string comparison: if the input has a different length than the target (11111), it returns the length difference; if the same length, it returns 1, -1, or 0 depending on whether the input is greater than, less than, or equal to 11111. If the comparison returns 0, the program proceeds to print a success message; otherwise, it jumps to a failure message (= Not ;-(). By tracing the static data and function logic, we determine that the correct password is simply "11111". Entering this input into the program successfully triggers the congratulatory output, confirming a correct reverse engineering process and completion of the challenge.
