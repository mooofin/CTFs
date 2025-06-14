# WebNet Series Writeup

## Challenge 1: WebNet0

**Description:**  
This challenge provided two files:
- A `.pcap` file (packet capture)
- A key file that appeared to be a private key

### Step-by-Step Solution

1. **Initial Analysis**  
   Upon opening the `.pcap` file in **Wireshark**, the traffic appeared to be routine at first glance—mostly unimportant headers and noise.

2. **Discovering Encrypted Traffic**  
   Further inspection revealed several packets containing the keyword **"Encrypted"**.  
   Checking **Statistics > Protocol Hierarchy**, I noticed a significant amount of traffic under **TLS** (Transport Layer Security), which is used for secure communications over TCP.

3. **Using the Provided Key**  
   The key file’s header indicated it was an **RSA private key**. With this knowledge, I proceeded to decrypt the TLS traffic:
   - In Wireshark, go to **Edit > Preferences > Protocols > TLS**.
   - Under **RSA Keys List**, I added an entry:
    
   - Click **OK** and refresh the packet view.

4. **Reading Decrypted Data**  
   The previously encrypted TLS traffic was now displayed as readable **HTTP traffic**.  
   To locate the flag quickly, I used the display filter:

![image](https://github.com/user-attachments/assets/d88bc1ff-9fb0-4bb3-a079-5196b6153257)
