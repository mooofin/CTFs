Sleuth Kit is a suite of command line forensic tools for examining disk images and filesystems without mounting them. It provides utilities to inspect partition tables, list directory entries, extract file contents by inode, recover deleted files, and perform many common forensic tasks. The tools operate on raw images or device files and interpret filesystem structures like superblocks, inodes, and directory entries so you can examine evidence without altering it.

mmls is the Sleuth Kit tool that reads and prints the partition table inside a disk image. It shows each partition entry with start and end sectors and a type code. The main reason to run mmls is to learn the sector offset where a filesystem begins. That offset is needed by other Sleuth Kit tools so they read the correct bytes inside the image. mmls output uses 512-byte sectors by default, so to get the byte offset you multiply the start sector by 512. For example, if mmls shows a partition starting at sector 2048, the filesystem byte offset is 2048 × 512 = 1,048,576.

fls lists files and directories inside a filesystem contained in an image. You give it the partition offset (option -o) and it prints the directory tree with inode numbers and type tags. Typical tags are d/d for a directory entry, r/r for a regular file, and V/V $OrphanFiles for orphaned or deleted files. fls is how you find filenames and their corresponding inode numbers without mounting the filesystem. You can also pass a specific inode to fls to list the contents of that directory inode, which is useful for drilling down into a particular folder like /root.

icat is the companion tool you will often use after fls. icat extracts the raw bytes of a single inode and prints them to stdout or a file. You must specify the input type and filesystem type (for example -i raw -f ext4) and the same offset used with fls. Because icat reads the inode directly, it returns the exact file contents as stored on disk, including deleted but unallocated data blocks in some cases



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








