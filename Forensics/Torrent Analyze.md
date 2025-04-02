**Analyzing BitTorrent Traffic Using Wireshark**

### Introduction
In this analysis, we explore network traffic associated with the BitTorrent protocol, focusing on how peers communicate, exchange metadata, and join a torrent swarm. The objective is to understand the structure of BitTorrent packets, identify key components such as `info_hash`, and infer the host's activity based on the captured packets.

### Observing DNS Queries
We begin by examining DNS queries made to domain names such as `ipv6.torrent.ubuntu.com` and `torrent.ubuntu.com`. These queries are essential for resolving the IP addresses of BitTorrent trackers or peers in a Distributed Hash Table (DHT). By filtering for the host IP address (`192.168.73.132` in this case), we can isolate these DNS requests and responses, identifying the peers the host is communicating with.

### Enabling BitTorrent Protocols in Wireshark
Since BitTorrent operates using specialized P2P protocols, it is necessary to enable the relevant protocol analyzers in Wireshark. This can be done via:
- **Analyze > Enabled Protocols**
- Enable `bittorrent_dht_udp` and `bt_utp_udp`

This step ensures that all BitTorrent-related traffic is correctly parsed and displayed in Wireshark.

### Understanding BitTorrent Swarm Communication
BitTorrent uses a decentralized approach where each participant (peer) both downloads and uploads data. A user initially joins a **torrent swarm**—a network of peers sharing the same file. The roles in a swarm include:
- **Seeders:** Peers that have the complete file and are only uploading.
- **Leechers:** Peers that are still downloading and sharing pieces simultaneously.

### Analyzing BitTorrent DHT Traffic
Sorting the packet capture by protocol, we focus on **BT-DHT** (BitTorrent Distributed Hash Table) packets. These packets are **bencoded** (binary encoded) and contain essential metadata about peers, nodes, and the file being shared.

Observations include:
- Outgoing packets from `192.168.73.132` list multiple peer nodes, indicating that the host is sharing peer information.
- Incoming packets contain request types such as:
  - `find_node`
  - `get_peers`
  - `announce_peer`
  - `ping`

These actions are defined in the **DHT protocol specification** and help manage peer discovery.

### Extracting Torrent Metadata
Although the actual file download is not present unless the capture includes the full session, we can still extract metadata, particularly the `info_hash`. This is a **20-byte SHA-1 hash** that uniquely identifies a torrent file.

Using `tshark`, we extract `info_hash` values:
```bash
frame contains info_hash
```
This filter isolates packets that contain `info_hash` values and queries for `get_peers` or `announce_peer`, which provide information about the torrent's state.

### Identifying Downloaded Torrents
After extracting `info_hash` values, we can match them against public torrent databases such as `torrentdb`. Searching for these hashes online can reveal the file associated with each torrent.

For example:
- `announce_peer` packets indicate that the host **successfully joined the swarm**.
- `get_peers` packets suggest that the torrent client was still searching for peers.
- If only `get_peers` packets exist, it is possible that the torrent was **added but not downloaded**.

### Legal and Ethical Considerations
Torrenting itself is not illegal; it is a P2P file-sharing system. However, downloading or distributing copyrighted content without authorization can result in legal action, depending on jurisdiction. Some countries have strict laws against piracy, and ISPs or law enforcement agencies may monitor BitTorrent traffic for potential violations.

### Conclusion
Through packet analysis, we can infer the activity of a BitTorrent client, from peer discovery to joining a swarm. The ability to extract `info_hash` and match it against databases allows us to determine the content being shared. While this analysis highlights forensic methods for network monitoring, it also underscores the importance of ethical use of P2P networks.

---

### References
1. **BitTorrent Protocol Specification:** [Official Documentation](https://www.bittorrent.org/protocol.html)
2. **Understanding DHT in BitTorrent:** [DHT Documentation](https://www.bittorrent.org/beps/bep_0005.html)
3. **Torrent Metadata Analysis Tools:** [Project Nayuki](https://www.nayuki.io/page/bittorrent-file-parser-in-java)

