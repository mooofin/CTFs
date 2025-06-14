![image](https://github.com/user-attachments/assets/9332678c-e786-4332-866b-05f6e7ff8fbd)







### **Writeup: Recovering Forgotten Secrets with Git Log**  

**Challenge Description:**  
*"What was I last working on? I remember writing a note to help me remember..."*  

The challenge provides a ZIP file (`challenge.zip`) containing a Git repository. Based on the hint, the solution involves checking prior commits to find a forgotten message—likely the flag.  

---

### **Step-by-Step Solution:**  

1. **Download & Extract the Repository**  
   - Downloaded the challenge files:  
     ```sh
     wget https://artifacts.picoctf.net/c_titan/68/challenge.zip
     ```
   - Extracted the ZIP and navigated into the repository:  
     ```sh
     unzip challenge.zip && cd drop-in
     ```

2. **Inspect Git History**  
   - Ran `git log` to view commit history:  
     ```sh
     git log
     ```
   - If `less` is missing (common on minimal Arch Linux setups), installed it first:  
     ```sh
     sudo pacman -S less  # Or use `git --no-pager log`
     ```

3. **Discovered the Flag**  
   - The output revealed a commit with the flag in its message:  
     ```plaintext
     commit 712314f105348e295f8cadd7d7dc4e9fa871e9a2 (HEAD -> master)
     Author: picoCTF <ops@picoctf.com>
     Date:   Tue Mar 12 00:07:26 2024 +0000

         picoCTF{t1m3m@ch1n3_e8c98b3a}
     ```
   - No further digging was needed—the flag was plainly visible in the commit log.

---

