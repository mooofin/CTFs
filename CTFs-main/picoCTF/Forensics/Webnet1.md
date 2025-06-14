

Since Wireshark was already configured to use this key from the previous challenge, I didn’t need to reconfigure anything. (The key configuration process is documented in the WebNet0 writeup.)

---

### Step-by-Step Solution

1. **Open the Capture in Wireshark**
   Loaded `capture.pcap` in Wireshark. Given that HTTP was likely involved (as in WebNet0), I applied a filter:

   ```
   http
   ```

2. **Follow the HTTP Stream**

   * Right-clicked on the **first HTTP packet**.
   * Selected **Follow > HTTP Stream**.

3. **Initial Misdirection**
   In the followed stream, I saw a misleading header:

   ```
   Pico-Flag: picoCTF{this.is.not.your.flag.anymore}
   ```

   This was clearly a decoy.

4. **Continue Exploring the Stream**
   Scrolling down further in the same HTTP stream, I found the **real flag** embedded within the payload.

---

### Flag

![image](https://github.com/user-attachments/assets/13560676-c355-4e95-9625-a6f367419b4e)
