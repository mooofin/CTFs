```c
int __cdecl main(int _Argc,char **_Argv,char **_Env)

{
  uint uVar1;
  undefined8 uVar2;
  size_t sVar3;
  FILE *_File;
  char *pcVar4;
  int iVar5;
  char local_138 [48];
  char local_108 [65];
  char local_c7 [15];
  undefined8 local_b8;
  undefined8 local_b0;
  char local_a4 [44];
  char local_78 [28];
  int local_5c;
  char local_58 [16];
  undefined1 local_48 [32];
  char local_28 [28];
  int local_c;
  
  __main();
  uVar2 = is_debugger_present();
  if ((int)uVar2 != 0) {
    builtin_strncpy(local_138,"\n(5=(;7z.?(734;.?>z>/?z.5z>?8/==?(z>?.?9.354",0x2d);
    sVar3 = strlen(local_138);
    deobfuscate_string((longlong)local_108,(longlong)local_138,sVar3);
    puts(local_108);
                    /* WARNING: Subroutine does not return */
    ExitProcess(0x29a);
  }
  builtin_strncpy(local_28,"\x1f4.?(z*;))-5(>`z",0x11);
  sVar3 = strlen(local_28);
  deobfuscate_string((longlong)local_48,(longlong)local_28,sVar3);
  __mingw_printf("%s",local_48);
  _File = (*__imp___acrt_iob_func)(0);
  pcVar4 = fgets(local_58,0x10,(FILE *)_File);
  if (pcVar4 == (char *)0x0) {
    builtin_strncpy(local_a4,"\x134*/.z?((5(",0xc);
    sVar3 = strlen(local_a4);
    deobfuscate_string((longlong)local_108,(longlong)local_a4,sVar3);
                    /* WARNING: Subroutine does not return */
    ExitProcess(1);
  }
  sVar3 = strcspn(local_58,"\n");
  local_58[sVar3] = '\0';
  local_5c = 0;
  for (local_c = 0; local_c < 1000; local_c = local_c + 1) {
    uVar1 = rand();
    if ((uVar1 & 1) == 0) {
      iVar5 = -1;
    }
    else {
      iVar5 = 1;
    }
    local_5c = local_5c + iVar5;
  }
  uVar2 = check_password(local_58);
  if ((int)uVar2 != 0) {
    local_b8 = 0x3d7a29293f39391b;
    local_b0 = 0x7b3e3f2e343b28;
    sVar3 = strlen((char *)&local_b8);
    deobfuscate_string((longlong)local_108,(longlong)&local_b8,sVar3);
    puts(local_108);
    builtin_strncpy(local_78,"\n(?))z\x1f4.?(z.5z?\"3.ttt",0x17);
    sVar3 = strlen(local_78);
    deobfuscate_string((longlong)(local_a4 + 0xc),(longlong)local_78,sVar3);
    puts(local_a4 + 0xc);
    getchar();
    return 0;
  }
  builtin_strncpy(local_c7,"\x1b99?))z>?43?>{",0xf);
  sVar3 = strlen(local_c7);
  deobfuscate_string((longlong)local_108,(longlong)local_c7,sVar3);
  puts(local_108);
                    /* WARNING: Subroutine does not return */
  ExitProcess(0xd);
}
```
```c

undefined8 check_password(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  
  sVar1 = strlen(param_1);
  if (sVar1 == 7) {
    if (*param_1 == 'M') {
      if (param_1[1] == '1') {
        if (param_1[2] == 'd') {
          if (param_1[3] == '3') {
            if (param_1[4] == 's') {
              if (param_1[5] == '1') {
                if (param_1[6] == '9') {
                  uVar2 = 1;
                }
                else {
                  uVar2 = 0;
                }
              }
              else {
                uVar2 = 0;
              }
            }
            else {
              uVar2 = 0;
            }
          }
          else {
            uVar2 = 0;
          }
        }
        else {
          uVar2 = 0;
        }
      }
      else {
        uVar2 = 0;
      }
    }
    else {
      uVar2 = 0;
    }
  }
  else {
    uVar2 = 0;
  }
  return uVar2;
}

```
The correct password is M1d3s19
