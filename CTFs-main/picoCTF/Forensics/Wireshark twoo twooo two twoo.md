
In this challenge, we were given a network capture file named `shark2.pcapng` and asked to locate the flag hidden within it. Upon opening the file in Wireshark, one of the first noticeable patterns was the presence of numerous HTTP requests to a `/flag` endpoint. However, each of these returned a different flag, suggesting they were likely red herrings designed to mislead and distract.

Digging deeper into the capture, I observed a large number of DNS queries for subdomains under the domain `reddshrimpandherring.com`, which stood out as unusual and potentially suspicious. Most of the DNS traffic was directed toward Google's public DNS server at `8.8.8.8`, but a smaller subset of queries were instead sent to the IP address `18.217.1.57`. This deviation from the norm was the key clue.

To isolate these requests, I applied the Wireshark display filter `dns and ip.dst == 18.217.1.57`. This allowed me to focus exclusively on DNS queries directed to that IP address. The subdomains in these requests appeared to be fragments of base64-encoded data. By extracting the queried subdomains in the order they appeared and concatenating them, I obtained the string `cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==`.

Upon decoding this string from base64, it revealed the final flag:

`picoCTF{dns_3xf1l_ftw_deadbeef}`



