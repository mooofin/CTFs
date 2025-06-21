

The challenge titled **"useless"** from picoCTF involved connecting to a remote machine via SSH using the provided credentials. Upon logging in, we were informed that a script in the user's home directory performed basic mathematical calculations. The script, named `useless`, was a simple Bash script that supported four operations: addition, subtraction, multiplication, and division. If incorrect arguments were passed, it would respond with either “Read the code first” or “Read the manual.” This seemed suspicious and hinted that the real content might be hidden elsewhere.

On inspecting the script, nothing out of the ordinary appeared in its logic—it performed basic arithmetic using command-line arguments. Suspecting that the message "Read the manual" might be a clue, we decided to run the script or command using just `useless` instead of `./useless`. To our surprise, this printed out a manual-style help page describing how to use the script. At the end of this output, nestled between the credits and example usage, we found the flag: `picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_5657}`.

![image](https://github.com/user-attachments/assets/d04fb20e-c0bd-46d1-ba8f-eb7463620160)
