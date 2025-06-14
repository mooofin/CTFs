# **Wireshark Challenge Writeup: "doo dooo do doo…"**  

**Challenge Description**:  
The challenge hints at analyzing a packet capture file (`shark1.pcapng`) using Wireshark to find a hidden flag.  

---

## **Step 1: Open the PCAP in Wireshark**  
1. Download `shark1.pcapng` (if provided).  


---

## **Step 2: Follow the TCP Stream**  
1. In Wireshark, go to:  
   - **Analyze** → **Follow** → **TCP Stream**  
2. Look through different streams (Stream 0, 1, 2, etc.) for suspicious data.  
3. **Stream 5** contains an interesting message:  
   ```
   cvpbPGS{c33xno00_1_f33_h_qrnqorrs}
   ```  
   *(This resembles a flag format but appears encoded.)*  

---

## **Step 3: Decode the Flag (ROT13 Cipher)**  
The hint suggests using **ROT13** (a Caesar cipher shifting letters by 13).  

### **Decoding Method**  
1. **Using Linux/macOS Terminal**:  
   ```bash
   echo "cvpbPGS{c33xno00_1_f33_h_qrnqorrs}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
   ```  
   **Output**:  
   ```
   picoCTF{p33kab00_1_s33_u_deadbeef}
   ```  

2. **Using CyberChef (Online Tool)**:  
   - Go to [CyberChef](https://gchq.github.io/CyberChef/)  
   - Input the encoded string and apply **ROT13**.  

---

## **Flag Found!**  
The decoded flag is:  
```
picoCTF{p33kab00_1_s33_u_deadbeef}
```  

---

## **Notes**  
- Following TCP streams in Wireshark is a standard technique for finding hidden data.  

