- **Challenge Description:**
  We are given a file named **encrypted.txt**, which contains a string of seemingly random characters. The challenge title suggests that the encryption method involves some kind of **rotation**.

## What is a ROT Cipher?
A **ROT cipher (Rotation cipher)** is a type of **Caesar cipher** where each letter in the plaintext is shifted by a fixed number of places in the alphabet. The most common variant is **ROT13**, which shifts letters by **13 positions**. Since the English alphabet has **26 letters**, applying ROT13 twice results in the original text.

For example:
```
Plaintext:  HELLO
ROT13:      URYYB
```
Applying ROT13 again:
```
URYYB → HELLO
```
Since ROT13 is a special case where **encryption and decryption are the same operation**, it's commonly used in CTFs for simple obfuscation.

## Decryption Process
We suspect that the text is encrypted using a **ROT cipher** with an unknown shift amount. To solve this, we attempt a **ROT brute-force attack**, checking each possible shift from **1 to 25**.

### Using CyberChef:
1. Open **CyberChef** (https://gchq.github.io/CyberChef/).
2. Use the **ROT13 Brute Force** operation, which applies ROT shifts from **1 to 25** and shows all possible outputs.
3. Look through the results to find the flag.

### Using Python (Alternative method):
If CyberChef is unavailable, we can use Python to brute-force the rotation shifts:
```python
import string

def rot_cipher(text, shift):
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet + alphabet.upper(), shifted + shifted.upper())
    return text.translate(table)

encrypted_text = "yrlxLCO{a0cjc1xw_m3lahyc3m_j4k7m759}"
for shift in range(1, 26):
    print(f"ROT{shift}: {rot_cipher(encrypted_text, shift)}")
 or from cyber chef after applying rot13 brute force 
 Amount =  1: yrlxLCO{a0cjc1xw_m3lahyc3m_j4k7m759}
Amount =  2: zsmyMDP{b0dkd1yx_n3mbizd3n_k4l7n759}
Amount =  3: atnzNEQ{c0ele1zy_o3ncjae3o_l4m7o759}
Amount =  4: buoaOFR{d0fmf1az_p3odkbf3p_m4n7p759}
Amount =  5: cvpbPGS{e0gng1ba_q3pelcg3q_n4o7q759}
Amount =  6: dwqcQHT{f0hoh1cb_r3qfmdh3r_o4p7r759}
Amount =  7: exrdRIU{g0ipi1dc_s3rgnei3s_p4q7s759}
Amount =  8: fyseSJV{h0jqj1ed_t3shofj3t_q4r7t759}
Amount =  9: gztfTKW{i0krk1fe_u3tipgk3u_r4s7u759}
Amount = 10: haugULX{j0lsl1gf_v3ujqhl3v_s4t7v759}
Amount = 11: ibvhVMY{k0mtm1hg_w3vkrim3w_t4u7w759}
Amount = 12: jcwiWNZ{l0nun1ih_x3wlsjn3x_u4v7x759}
Amount = 13: kdxjXOA{m0ovo1ji_y3xmtko3y_v4w7y759}
Amount = 14: leykYPB{n0pwp1kj_z3ynulp3z_w4x7z759}
Amount = 15: mfzlZQC{o0qxq1lk_a3zovmq3a_x4y7a759}
Amount = 16: ngamARD{p0ryr1ml_b3apwnr3b_y4z7b759}
Amount = 17: ohbnBSE{q0szs1nm_c3bqxos3c_z4a7c759}
Amount = 18: picoCTF{r0tat1on_d3crypt3d_a4b7d759}
Amount = 19: qjdpDUG{s0ubu1po_e3dszqu3e_b4c7e759}
Amount = 20: rkeqEVH{t0vcv1qp_f3etarv3f_c4d7f759}
Amount = 21: slfrFWI{u0wdw1rq_g3fubsw3g_d4e7g759}
Amount = 22: tmgsGXJ{v0xex1sr_h3gvctx3h_e4f7h759}
Amount = 23: unhtHYK{w0yfy1ts_i3hwduy3i_f4g7i759}
Amount = 24: voiuIZL{x0zgz1ut_j3ixevz3j_g4h7j759}
Amount = 25: wpjvJAM{y0aha1vu_k3jyfwa3k_h4i7k759}
```

## Extracting the Flag
After applying ROT **13**, we successfully decrypt the text to:
```
picoCTF{r0tat1on_d3crypt3d_a4b7d759}
```
This confirms that the flag is:
```
picoCTF{r0tat1on_d3crypt3d_a4b7d759}
