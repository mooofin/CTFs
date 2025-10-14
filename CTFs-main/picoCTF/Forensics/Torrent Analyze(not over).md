We're given a PCAP file containing network traffic where someone has been using BitTorrent to download files. Our goal is to identify the downloaded file without extracting the actual file contents from the PCAP.



Before diving into the analysis, it's important to understand how BitTorrent works :3 

- **InfoHash**: A torrent is uniquely identified by an infohash, which is a SHA-1 hash (20 bytes) calculated over the contents of the info dictionary in bencode form
- **DHT (Distributed Hash Table)**: BitTorrent uses DHT for peer discovery without requiring a central tracker
- **BT-DHT Protocol**: This is the protocol used for DHT communication in BitTorrent

The infohash is crucial because it uniquely identifies the torrent file being downloaded and can be used to look up the torrent metadata online.


First, let's see what kind of traffic we're dealing with:

```bash
tshark -r torrent.pcap -q -z conv,tcp
```

This shows us TCP conversations. We can see:
- Multiple connections to various IPs on different ports (typical BitTorrent behavior)
- One large connection: `192.168.73.132:59477 <-> 104.173.116.244:62581` with 4.6MB transferred
- Several smaller connections on port 51413 (common BitTorrent port)



BitTorrent uses bencode encoding for its metadata. When we examine the strings in the PCAP:

```bash
strings torrent.pcap | grep -E "^[0-9]+:" | head -50
```

We see bencode patterns like:
```
1:v4:LT
1:y1:qe
9:info_hash20:
4:name46:Zoo (2017) 720p WEB-DL x264 ESubs - MkvHub.Com
```

The format `9:info_hash20:` means "the string 'info_hash' (9 characters) followed by 20 bytes of data."



Since BitTorrent uses DHT for peer discovery, there will be multiple `get_peers` queries containing infohashes. The most frequently appearing infohash is the file being actively downloaded.

Let's extract all infohashes:

```python
import re
from collections import Counter

with open('torrent.pcap', 'rb') as f:
    data = f.read()
    
# Find all occurrences of info_hash in bencode format
matches = re.finditer(b'info_hash20:', data)
hashes = []

for match in matches:
    start = match.end()
    info_hash = data[start:start+20]  # Extract the next 20 bytes
    hash_hex = info_hash.hex()
    hashes.append(hash_hex)

# Count occurrences to find the most common hash
counter = Counter(hashes)
print("Info hashes found and their frequencies:\n")
for hash_val, count in counter.most_common():
    print(f"{hash_val}: {count} times")

print(f"\nMost common hash: {counter.most_common(1)[0][0]}")
```



Running the script reveals multiple infohashes, with one appearing significantly more frequently than others. The most common infohash is:

```
e2467cbf021192c241367b892230dc1e05c0580e
```

(Note: This is the hash that appeared most frequently in the DHT traffic)



Now we can search this infohash online to identify the torrent:


Searching this infohash reveals that it corresponds to:

**ubuntu-19.10-desktop-amd64.iso**



```
picoCTF{ubuntu-19.10-desktop-amd64.iso}
```

