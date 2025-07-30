


1
    The first step was to download the provided `flag.png` file from the PicoCTF artifacts server using `wget`.

    ```bash
    [nix-shell:~/sid/CTF/picogym]$ wget https://artifacts.picoctf.net/c/260/flag.png
    --2025-07-31 00:42:46--  https://artifacts.picoctf.net/c/260/flag.png
    Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 2600:9000:2241:9400:16:5ec5:2840:93a1, 2600:9000:2241:6a00:16:5ec5:2840:93a1, 2600:9000:2241:3c00:16:5ec5:2840:93a1, ...
    Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|2600:9000:2241:9400:16:5ec5:2840:93a1|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 43005 (42K) [application/octet-stream]
    Saving to: ‘flag.png’

    flag.png            100%[========>]  42.00K   174KB/s   in 0.2s

    2025-07-31 00:42:47 (174 KB/s) - ‘flag.png’ saved [43005/43005]
    ```

    We used `binwalk` to examine the structure of `flag.png` and identify any embedded files.

    ```bash
    [nix-shell:~/sid/CTF/picogym]$ binwalk flag.png

                    /home/muffin/sid/CTF/picogym/flag.png
    ------------------------------------------------------------------
    DECIMAL            HEXADECIMAL        DESCRIPTION
    ------------------------------------------------------------------
    0                  0x0                PNG image, total size: 39739 bytes
    39739              0x9B3B             ZIP archive, file count: 2, total size: 3266 bytes
    ------------------------------------------------------------------
    Analyzed 1 file for 85 file signatures (187 magic patterns) in 4.0 milliseconds
    ```

    The `binwalk` output clearly indicated that in addition to the PNG image at offset `0x0`, there was a **ZIP archive** embedded within the `flag.png` file, starting at offset `0x9B3B`.


    To retrieve the contents of the embedded ZIP archive, we used `binwalk` with the `-e` (extract) option.

    ```bash
    [nix-shell:~/sid/CTF/picogym]$ binwalk -e flag.png

                    /home/muffin/sid/CTF/picogym/extractions/flag.png
    ------------------------------------------------------------------------------
    DECIMAL            HEXADECIMAL        DESCRIPTION
    ------------------------------------------------------------------------------
    0                  0x0                PNG image, total size: 39739 bytes
    39739              0x9B3B             ZIP archive, file count: 2, total size: 3266 bytes
    ------------------------------------------------------------------------------
    [#] Extraction of png data at offset 0x0 declined
    [+] Extraction of zip data at offset 0x9B3B completed successfully
    ------------------------------------------------------------------------------
    Analyzed 1 file for 85 file signatures (187 magic patterns) in 25.0 milliseconds
    ```

    This command successfully extracted the contents of the ZIP archive into a new directory named `extractions` (the default for `binwalk`).


    After extraction, we navigated into the `extractions` directory and listed its contents.

    ```bash
    [nix-shell:~/sid/CTF/picogym]$ ls
    extractions  heapedit    solve.py        vuln
    flag.png     output.bin  solve.py.save   vuln.c

    [nix-shell:~/sid/CTF/picogym]$ cd extractions

    [nix-shell:~/sid/CTF/picogym/extractions]$ ls
    flag.png  flag.png.extracted
    ```

    Inside the `extractions` directory, we found two files: `flag.png` (likely a copy of the original or the first extracted image) and `flag.png.extracted`. The `flag.png.extracted` file, being the result of the ZIP extraction, was the one to investigate further. It contained the flag directly visible as a string.



The flag found was:
**`picoCTF{Hidding_An_imag3_within_@n_ima9e_ad9f6587}`**
