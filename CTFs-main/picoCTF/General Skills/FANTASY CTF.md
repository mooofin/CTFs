# picoCTF 2025 - Fantasy CTF Simulation Writeup

## Challenge Name: Fantasy CTF Simulation
## Category: General Skills
## Points: 10

### Description:
The challenge presents an interactive fiction-style game that introduces players to fundamental rules of Capture The Flag (CTF) competitions, specifically for picoCTF 2025. The goal is to navigate the game, follow ethical hacking practices, and ultimately retrieve the correct flag.

---

### Solution Walkthrough:

#### Step 1: Connecting to the Challenge Server
To begin the challenge, I used `netcat` to connect to the provided server:

```bash
nc verbal-sleep.picoctf.net 58889
```

#### Step 2: Navigating the Simulation
Upon connecting, I was introduced to a futuristic setting where the protagonist, Eibhilin, interacts with an AI assistant named Nyx. The game simulates the registration process for picoCTF 2025 and introduces rules about ethical play.

**Key Lessons from the Simulation:**
- Players must register a single, private account.
- Sharing accounts or flags is against the rules and may lead to disqualification.
- The correct approach is to solve challenges honestly rather than searching for others' flags.

#### Step 3: Playing the Sanity Challenge
The AI, Nyx, guided me towards starting with an easy challenge called the "sanity challenge." At this point, the game provided options:

- **(A) Play the game**
- **(B) Search the Ether for the flag** *(Incorrect choice, leading to warnings)*

Choosing option **A (Play the game)** led to successfully completing the challenge and obtaining the flag.

#### Step 4: Retrieving the Flag
Upon completing the game simulation, the flag was displayed:

```
picoCTF{m1113n1um_3d1710n_9a3a7333}
```

This confirmed that I had solved the challenge correctly.

---

### Key Takeaways
- The challenge effectively reinforced fundamental CTF principles.
- Ethical participation is crucial—do not share or steal flags.
- The interactive storytelling approach made the learning experience engaging and fun.

---

### Submission
To complete the challenge, I submitted the retrieved flag:

```bash
picoCTF{m1113n1um_3d1710n_9a3a7333}
```

This successfully awarded me **10 points** in the competition.

---




