![image](https://github.com/user-attachments/assets/e63fc3f5-a7c9-4e88-a1a2-45a1c757494d)



sub RSP, 28h at the top. For this function that's the entire prologue. It's setting up the function by moving the stack pointer and creating a new stack frame area


![image](https://github.com/user-attachments/assets/1fbd14ec-1f2a-483c-84fb-e5ca5876a00a)



Inlining
One compiler/linker optimization that makes noticeable changes to the code is inlining. When a function gets inlined it's essentially pasted where the call would be instead of making a call. See the following example.

Without Function Inlining:
```c

int Add(int x, int y){
    return x+y;
}
int main(){
    int x = RandInt();
    int res = Add(x, 5)
}

```

With Function Inlining:
```c

int main(){
    int x = RandInt();
    int res = x + 5;
}

```
