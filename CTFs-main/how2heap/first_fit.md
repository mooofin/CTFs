When you free a large chunk in glibc, it goes to the unsorted bin. If you later request an allocation that’s smaller than or equal to the freed chunk, glibc uses a first-fit strategy and returns the same chunk again. This means the old pointer you still hold becomes a dangling pointer that now aliases the new allocation


<img width="642" height="667" alt="image" src="https://github.com/user-attachments/assets/489f17cb-d1aa-43e4-a1de-f892b004806b" />




<img width="467" height="99" alt="image" src="https://github.com/user-attachments/assets/c7e928fa-3331-4fc0-91ca-67c3cf5aa0fc" />

