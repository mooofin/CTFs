 Rather than decompiling the assembly, a more direct approach was to simply execute it using an ARM emulator. Starting in WSL, I initially attempted to assemble the file using `aarch64-linux-gnu-as`, which generated an `a.out` file. However, running this directly with `qemu-aarch64` resulted in an "Invalid ELF image" error. This suggested that the file wasn't properly linked into an executable format—likely lacking an entry point like `_start`.

To resolve this, I tried linking it manually with `ld`, but that failed due to the absence of the necessary glibc libraries for `aarch64`. The cleaner solution was to install the full ARM GCC toolchain (`gcc-aarch64-linux-gnu`) and use it to compile the assembly file with the `-static` flag. This ensured that the binary was fully self-contained and didn't attempt to dynamically load any libraries at runtime—something QEMU wouldn't support without a complete ARM userland.

After successfully building the static binary, I ran it under `qemu-aarch64`, and it output a number. Converting this number from decimal to hexadecimal yielded `5ee79c2b`. With this, we can construct the flag: `picoCTF{5ee79c2b}`.


