I wrote a tiny pwntools exploit that launches the challenge binary, waits for the prompt `:)\n###\n` using `sendafter`, sends the bypass string `pokemon` (with a newline if the program expects a line), then reads and prints the flag with `recvline`; `sendafter` avoids race conditions by only sending once the prompt appears, and the newline/no-newline choice depends on how the binary reads input.


<img width="1290" height="290" alt="screenshot-1759498213" src="https://github.com/user-attachments/assets/2591f77d-b88e-48ac-b62d-3a6c68b39cd3" />


<img width="1781" height="1003" alt="screenshot-1759498447" src="https://github.com/user-attachments/assets/06c91489-2338-4f97-8375-9cca031047fe" />
