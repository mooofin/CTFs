

The goal of this analysis was to examine a compressed disk image and extract any hidden or relevant files that might contain a flag. The image, `dds2-alpine.flag.img.gz`, appeared to be a forensic challenge image that required exploration using **The Sleuth Kit (TSK)** tools.





I began by setting up a NixOS environment with the necessary utilities. On NixOS, packages can be loaded temporarily using `nix-shell`. I entered a shell containing both `gzip` and `sleuthkit`:

```bash
nix-shell -p gzip sleuthkit
```

This provided all the tools needed to decompress and analyze the image.





The given file was in gzip format, so I decompressed it with:

```bash
gunzip dds2-alpine.flag.img.gz
```

After decompression, the resulting file `dds2-alpine.flag.img` was ready for analysis.




To understand the structure of the image, I used **mmls**, a Sleuth Kit utility that lists partition tables:

```bash
mmls dds2-alpine.flag.img
```

The output showed that the disk used a DOS partition table. There was one active Linux partition starting at sector `2048` and ending at `262143`. This indicated that any filesystem data would be offset by 2048 sectors, each 512 bytes in size.

DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
```

This confirmed the filesystem offset for all subsequent Sleuth Kit commands.

---



Next, I listed the directory structure of the Linux partition using `fls` with the offset option:

```bash
fls -o 2048 dds2-alpine.flag.img
```

The output revealed the typical Linux root directory layout, including `/home`, `/etc`, `/bin`, and notably, a `/root` directory:

```
d/d 18290:	root
```

This suggested the possible presence of the flag in the root user’s directory.





To look inside `/root`, I ran:

```bash
fls -o 2048 dds2-alpine.flag.img 18290
```

This listed a single file:

```
r/r 18291:	down-at-the-bottom.txt
```

The name hinted at it being the target file for the flag.





Finally, I used `icat`, a Sleuth Kit tool that extracts file contents directly from an image, specifying the partition offset and inode number:

```bash
icat -i raw -f ext4 -o 2048 dds2-alpine.flag.img 18291
```

The output revealed the flag, presented as ASCII art text:

```
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( 3 ) ( _ ) ( f ) ( f ) ( 2 ) ( 7 ) ( f ) ( 1 ) ( 3 ) ( 9 ) ( } )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
```








