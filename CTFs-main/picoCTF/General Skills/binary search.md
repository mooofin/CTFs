# **Binary Search Challenge Writeup**

## **Challenge Overview**
The challenge presents a simple yet effective demonstration of the binary search algorithm. The goal is to guess a randomly selected number between 1 and 1000 within 10 attempts. The challenge mimics real-world scenarios where efficient searching through large datasets (such as logs, vulnerability reports, or forensic data) is crucial.

### **Challenge Details**
- **Connection Command:**  
  ```bash
  ssh -p 52808 ctf-player@atlas.picoctf.net
  ```
- **Password:** Provided when launching the instance.
- **Game Mechanics:**  
  - The system selects a random number between **1 and 1000**.
  - You have **10 guesses** to find the correct number.
  - After each guess, the system responds with:
    - **"Higher!"** if the target number is greater than your guess.
    - **"Lower!"** if the target number is less than your guess.
    - **"Congratulations!"** if you guess correctly, along with the flag.

---

## **Solution Approach**
The optimal way to solve this challenge is by implementing a **binary search algorithm**, which efficiently narrows down the possible range of the target number.

### **Binary Search Steps:**
1. **Initialize Bounds:**  
   - **Low (`L`):** 1  
   - **High (`H`):** 1000  

2. **Iterative Guessing:**  
   - **Guess the midpoint:** `mid = (L + H) // 2`  
   - If the response is **"Higher!"**, set `L = mid + 1`.  
   - If the response is **"Lower!"**, set `H = mid - 1`.  
   - Repeat until the correct number is found.

3. **Termination:**  
   - The loop ends when the correct number is guessed (within 10 attempts).

### **Example Execution**
```
Enter your guess: 500  
Higher! Try again.  
Enter your guess: 750  
Higher! Try again.  
Enter your guess: 900  
Higher! Try again.  
Enter your guess: 950  
Lower! Try again.  
Enter your guess: 925  
Lower! Try again.  
Enter your guess: 914  
Lower! Try again.  
Enter your guess: 907  
Higher! Try again.  
Enter your guess: 911  
Congratulations! You guessed the correct number: 911  
Here's your flag: picoCTF{g00d_gu355_6dcfb67c}
```

---


---

## **Flag**
The flag obtained after successfully guessing the number is:  
**`picoCTF{g00d_gu355_6dcfb67c}`**

---

