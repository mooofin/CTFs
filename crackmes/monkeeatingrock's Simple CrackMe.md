![image](https://github.com/user-attachments/assets/5cae222c-30fc-4c00-a8c4-5b05b639ae67)
A simple CrackMe binary that asks for a password and checks it against a hardcoded value.

Initial Analysis
First Attempt (Ghidra Static Analysis)

Loaded the binary into Ghidra.

Initially, no obvious strings or logic were found.

Suspected anti-decompilation tricks or debug checks.

Dynamic Analysis with GDB

Ran the binary in GDB (gdb ./crackme).

Used info functions and strings to locate interesting data.

Found the welcome message in memory:

"Welcome to your first Crack Me program!"
Traced cross-references to find the main validation logic.
![image](https://github.com/user-attachments/assets/1759ef26-13f7-490d-99a5-843150550df0)


Back to Ghidra (Targeted Analysis)

Located the memory address of the string.

Found the main function referencing it.

Discovered the hardcoded password check.

void FUN_140018060(void)

{
  char cVar1;
  basic_ostream<> *pbVar2;
  undefined8 uVar3;
  longlong lVar4;
  undefined4 *puVar5;
  undefined1 local_198 [32];
  undefined4 local_178 [2];
  longlong local_170 [8];
  longlong local_130 [31];
  undefined4 local_34;
  ulonglong local_20;
  
  puVar5 = local_178;
  for (lVar4 = 0x2a; lVar4 != 0; lVar4 = lVar4 + -1) {
    *puVar5 = 0xcccccccc;
    puVar5 = puVar5 + 1;
  }
  local_20 = DAT_140027040 ^ (ulonglong)local_178;
  __CheckForDebuggerJustMyCode(&DAT_14002d066);
  thunk_FUN_1400152c0(local_170,"QuiteEasyRight");
  thunk_FUN_140015360(local_130);
  pbVar2 = (basic_ostream<> *)
           thunk_FUN_1400138e0((basic_ostream<> *)cout_exref,
                               "Welcome to your first Crack Me program!");
  std::basic_ostream<>::operator<<
            (pbVar2,(_func_basic_ostream<>_ptr_basic_ostream<>_ptr *)&LAB_140011050);
  pbVar2 = (basic_ostream<> *)thunk_FUN_1400138e0((basic_ostream<> *)cout_exref," ");
  std::basic_ostream<>::operator<<
            (pbVar2,(_func_basic_ostream<>_ptr_basic_ostream<>_ptr *)&LAB_140011050);
  thunk_FUN_1400138e0((basic_ostream<> *)cout_exref,"What is the password?: ");
  thunk_FUN_1400134a0((longlong *)cin_exref,local_130);
  pbVar2 = (basic_ostream<> *)thunk_FUN_1400138e0((basic_ostream<> *)cout_exref," ");
  std::basic_ostream<>::operator<<
            (pbVar2,(_func_basic_ostream<>_ptr_basic_ostream<>_ptr *)&LAB_140011050);
  cVar1 = thunk_FUN_140013d80((longlong)local_130,(longlong)local_170);
  if (cVar1 == '\0') {
    pbVar2 = (basic_ostream<> *)
             thunk_FUN_1400138e0((basic_ostream<> *)cout_exref,"Authentication Failed.");
    std::basic_ostream<>::operator<<
              (pbVar2,(_func_basic_ostream<>_ptr_basic_ostream<>_ptr *)&LAB_140011050);
  }
  else {
    pbVar2 = (basic_ostream<> *)
             thunk_FUN_1400138e0((basic_ostream<> *)cout_exref,"Authentication Successful.");
    std::basic_ostream<>::operator<<
              (pbVar2,(_func_basic_ostream<>_ptr_basic_ostream<>_ptr *)&LAB_140011050);
  }
  pbVar2 = (basic_ostream<> *)thunk_FUN_1400138e0((basic_ostream<> *)cout_exref," ");
  std::basic_ostream<>::operator<<
            (pbVar2,(_func_basic_ostream<>_ptr_basic_ostream<>_ptr *)&LAB_140011050);
  thunk_FUN_1400138e0((basic_ostream<> *)cout_exref,"Press ENTER to exit!");
  uVar3 = thunk_FUN_140017ae0();
  std::basic_istream<>::ignore((basic_istream<> *)cin_exref,1,(int)uVar3);
  std::basic_istream<>::get((basic_istream<> *)cin_exref);
  local_34 = 0;
  thunk_FUN_140015d80(local_130);
  thunk_FUN_140015d80(local_170);
  _RTC_CheckStackVars((longlong)local_198,(int *)&DAT_140023080);
  thunk_FUN_140018ce0(local_20 ^ (ulonglong)local_178);
  return;
}
Password Check Logic
The program compares user input against a hardcoded string:

c
thunk_FUN_1400152c0(local_170, "QuiteEasyRight"); // Hardcoded password
cVar1 = thunk_FUN_140013d80(user_input, local_170); // Comparison
if (cVar1 == '\0') {
    // Failure
} else {
    // Success
}
Conclusion
Static + Dynamic Analysis Combo:

Ghidra alone didn’t reveal the password immediately.

GDB helped locate the string, leading back to Ghidra for full decompilation.

Password: "QuiteEasyRight" (simple hardcoded check).



