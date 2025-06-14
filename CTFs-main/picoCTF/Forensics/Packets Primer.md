
# Lookey here – picoCTF Writeup

**Author:** LT 'syreal' Jones / Mubarak Mikail  
**Category:** Forensics  
**Tags:** pcap, wireshark, network forensics

---

## Description

> Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.  
> Download the packet capture file and use packet analysis software to find the flag.

---

## Provided File

- `network-dump.flag.pcap`

---

## Tools Used

- Wireshark

---

## Approach

1. **Open the `.pcap` file** in Wireshark.
2. **Inspect the TCP stream** by looking at the packet data that could contain embedded messages or payloads.
3. Navigate to a **TCP packet with data**, particularly one with a `[PSH, ACK]` flag (usually where payloads are delivered).
4. In **Frame 4**, a segment of ASCII content was visible in the packet's payload pane.
5. The ASCII dump revealed:

```
picoCTF{p4ck37_5h4rk_cecca7f}
```

6. We verified the formatting to ensure no additional whitespace or corrupted characters.

---

## Flag

```
picoCTF{p4ck37_5h4rk_cecca7f}
```

---

## Conclusion

This challenge involved analyzing raw network traffic in a `.pcap` file using Wireshark. By focusing on TCP payloads and decoding ASCII contents, we successfully retrieved the hidden flag. This is a common technique in real-world network forensics and incident response.
