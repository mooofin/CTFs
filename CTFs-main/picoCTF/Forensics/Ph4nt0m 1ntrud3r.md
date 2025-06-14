

## **First Look at the PCAP**
When I opened `myNetworkTraffic.pcap` in Wireshark, I saw a bunch of TCP packets with what looked like encoded data. The packets weren't in order - some that should've come later appeared earlier in the capture.

## **Initial Extraction Attempt**
I tried dumping all TCP data first:
```bash
tshark -r myNetworkTraffic.pcap -Y "tcp" -T fields -e tcp.segment_data | xxd -p -r | base64 -d
```
This gave me a mess of random characters - clearly too much noise.

## **Spotting the Pattern**
Looking closer, I noticed many packets had exactly 12 bytes of TCP payload. When I filtered for these:
```bash
tshark -r myNetworkTraffic.pcap -Y "tcp.len==12" -T fields -e tcp.segment_data | xxd -p -r | base64 -d
```
I got:
```
{1t_w4s318db22_34sy_tpicoCTFbh_4r_fnt_th4t
```
Partial flag! But scrambled and incomplete.

## **Fixing the Order**
The packets were out of sequence. I needed to sort them by capture time:
```bash
tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data | sort -k4 | awk '{print $6}' | xxd -p -r | base64 -d
```
This gave me the complete, properly ordered flag:
```
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_f318db22}
```

## **Why This Worked**
- **12-byte packets**: Contained Base64-encoded flag fragments
- **4-byte packets**: Had the remaining pieces
- **Sorting by time**: Reconstructed the original transmission order
- **Decoding pipeline**: Converted hex → raw → Base64 to reveal the flag

## **Final Answer**
The complete flag is:
```
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_f318db22}
```
