from the disass , we can see 
```c

undefined8 main(void)

{
  char cVar1;
  size_t sVar2;
  char *pcVar3;
  undefined8 uVar4;
  undefined8 uStack_140;
  char local_138 [268];
  int local_2c;
  char *local_28;
  int local_20;
  int local_1c;
  size_t local_18;
  int local_10;
  int local_c;
  
  local_28 = "0ov13tc{9zxpdr6na13m6a73534th5a}";
  uStack_140 = 0x1011f0;
  sVar2 = strlen("0ov13tc{9zxpdr6na13m6a73534th5a}");
  local_2c = (int)sVar2;
  local_c = 0;
  for (local_10 = 0; local_10 < local_2c; local_10 = local_10 + 1) {
    uStack_140 = 0x10120d;
    cVar1 = is_prime(local_10);
    if (cVar1 != '\0') {
      local_c = local_c + 1;
    }
  }
  uStack_140 = 0x101235;
  printf("Input flag: ");
  uStack_140 = 0x101250;
  pcVar3 = fgets(local_138,0x100,stdin);
  if (pcVar3 == (char *)0x0) {
    uVar4 = 2;
  }
  else {
    uStack_140 = 0x10126e;
    local_18 = strlen(local_138);
    while ((local_18 != 0 &&
           ((local_138[local_18 - 1] == '\n' || (local_138[local_18 - 1] == '\r'))))) {
      local_138[local_18 - 1] = '\0';
      uStack_140 = 0x101293;
      local_18 = strlen(local_138);
    }
    if (local_c == (int)local_18) {
      local_1c = 0;
      for (local_20 = 0; local_20 < local_2c; local_20 = local_20 + 1) {
        uStack_140 = 0x1012ff;
        cVar1 = is_prime(local_20);
        if (cVar1 == '\x01') {
          if (local_138[local_1c] != local_28[local_20]) {
            uStack_140 = 0x101336;
            puts("WRONG FLAG ");
            return 1;
          }
          local_1c = local_1c + 1;
        }
      }
      uStack_140 = 0x10135f;
      puts("FLAG OK QUACK ");
      uVar4 = 0;
    }
    else {
      uStack_140 = 0x1012de;
      puts("WRONG FLAG ");
      uVar4 = 1;
    }
  }
  return uVar4;
}


```

the  flag is encoded by scattering its characters throughout a string, placing each character only at prime-numbered indices 



```python3
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

encoded = "0ov13tc{9zxpdr6na13m6a73534th5a}"
flag = ''.join(encoded[i] for i in range(len(encoded)) if is_prime(i))
print(flag)
```

FLAg - v1t{pr1m35}
