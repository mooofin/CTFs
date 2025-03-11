# KeygenMe Challenge Write-Up

## Challenge Description
We are given a Java program that checks for a specific key. The key must be 34 characters long, and each character is validated in reverse order. Our task is to analyze the conditions and reconstruct the correct key.

## Code Analysis
The program reads user input and performs several checks:
1. Ensures the key is **34 characters long**.
2. Validates individual characters using `charAt()` conditions in reverse order.

### Extracting the Key
By analyzing the `charAt()` conditions, we reconstruct the key:

```
33: }
32: 9
31: 8
30: c
29: a
28: c
27: 8
26: 3
25: 7
24: _
23: d
22: 3
21: r
20: 1
19: u
18: q
17: 3
16: r
15: _
14: g
13: n
12: 1
11: l
10: 0
9: 0
8: 7
7: {
6: F
5: T
4: C
3: o
2: c
1: i
0: p
```

Since most CTF keys follow the `picoCTF{...}` format, we assume the first part is:

```
picoCTF{gn1l007_r3qu1r3d_738ca98}
```

## Flag
```
picoCTF{gn1l007_r3qu1r3d_738ca98}
```

## Challenge Code
Here is the Java program used in the challenge:

```java
import java.util.Scanner;

public class KeygenMe {
  public static void main(String[] paramArrayOfString) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter key:");
    String str = scanner.nextLine();
    if (str.length() != 34) {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(33) != '}') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(32) != '9') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(31) != '8') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(30) != 'c') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(29) != 'a') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(28) != 'c') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(27) != '8') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(26) != '3') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(25) != '7') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(24) != '_') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(23) != 'd') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(22) != '3') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(21) != 'r') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(20) != '1') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(19) != 'u') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(18) != 'q') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(17) != '3') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(16) != 'r') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(15) != '_') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(14) != 'g') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(13) != 'n') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(12) != '1') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(11) != 'l') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(10) != '0') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(9) != '0') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(8) != '7') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(7) != '{') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(6) != 'F') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(5) != 'T') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(4) != 'C') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(3) != 'o') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(2) != 'c') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(1) != 'i') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(0) != 'p') {
      System.out.println("Invalid key");
      return;
    } 
    System.out.println("Valid key");
  }
}
```



