**Challenge Overview**

- **Points:** 50
- **Category:** Reverse Engineering
- **Description:**
  - We need to investigate a service running at `nc mercury.picoctf.net 28067` to determine what it is.
- **Hint:**
  - What language does a CNC machine use?

---

**Solution Approach**

1. **Understanding the Challenge:**
   - The hint suggests that we are dealing with a CNC (Computer Numerical Control) machine.
   - CNC machines use **G-code**, a programming language that controls automated tools like mills, lathes, and 3D printers.

2. **Extracting the Data:**
   - We can use Netcat (`nc`) to connect to the given service and capture its output.
   - Run the following command to save the output into a file:
     ```sh
     nc mercury.picoctf.net 28067 > cnc.txt
     ```

3. **Analyzing the Extracted File:**
   - The output file `cnc.txt` contains **G-code commands**.
   - G-code consists of lines starting with `G` or `M`, controlling tool movement and operations.

4. **Interpreting the G-code:**
   - The best way to interpret G-code is to use an online G-code simulator.
   - One such tool is [ncviewer.com](https://ncviewer.com/), which provides a visualization of tool paths.
   - Copy and paste the content of `cnc.txt` into the viewer.
   - The simulation reveals the flag!

---

**Extracted Flag:**
```
picoCTF{num3r1cal_c0ntr0l_84d2d117}
```

---

**G-code **

```gcode
G17 G21 G40 G90 G64 P0.003 F50
G0Z0.1
G0Z0.1
G0X0.8276Y3.8621
G1Z0.1
G1X0.8276Y-1.9310
G0Z0.1
G0X1.1034Y3.8621
G1Z0.1
G1X1.1034Y-1.9310
G0Z0.1
G0X1.1034Y3.0345
G1Z0.1
G1X1.6552Y3.5862
G1X2.2069Y3.8621
G1X2.7586Y3.8621
G1X3.5862Y3.5862
G1X4.1379Y3.0345
G1X4.4138Y2.2069
G1X4.4138Y1.6552
G1X4.1379Y0.8276
G1X3.5862Y0.2759
G1X2.7586Y0.0000
G1X2.2069Y0.0000
G1X1.6552Y0.2759
G1X1.1034Y0.8276
G0Z0.1
G0X2.7586Y3.8621
G1Z0.1
G1X3.3103Y3.5862
G1X3.8621Y3.0345
G1X4.1379Y2.2069
G1X4.1379Y1.6552
G1X3.8621Y0.8276
G1X3.3103Y0.2759
G1X2.7586Y0.0000
G0Z0.1
G0X0.0000Y3.8621
G1Z0.1
G1X1.1034Y3.8621
G0Z0.1
G0X0.0000Y-1.9310
G1Z0.1
G1X1.9310Y-1.9310
G0Z0.1
G0X7.2414Y5.7931
G1Z0.1
G1X6.9655Y5.5172
G1X7.2414Y5.2414
G1X7.5172Y5.5172
G1X7.2414Y5.7931
G0Z0.1
G0X7.2414Y3.8621
G1Z0.1
G1X7.2414Y0.0000
G0Z0.1
G0X7.5172Y3.8621
G1Z0.1
G1X7.5172Y0.0000
G0Z0.1
G0X6.4138Y3.8621
G1Z0.1
G1X7.5172Y3.8621
G0Z0.1
G0X6.4138Y0.0000
G1Z0.1
G1X8.3448Y0.0000
G0Z0.1
G0X13.6552Y3.0345
G1Z0.1
G1X13.3793Y2.7586
G1X13.6552Y2.4828
G1X13.9310Y2.7586
G1X13.9310Y3.0345
G1X13.3793Y3.5862
G1X12.8276Y3.8621
G1X12.0000Y3.8621
G1X11.1724Y3.5862
G1X10.6207Y3.0345
G1X10.3448Y2.2069
G1X10.3448Y1.6552
G1X10.6207Y0.8276
G1X11.1724Y0.2759
G1X12.0000Y0.0000
G1X12.5517Y0.0000
G1X13.3793Y0.2759
G1X13.9310Y0.8276
G0Z0.1
G0X12.0000Y3.8621
G1Z0.1
G1X11.4483Y3.5862
G1X10.8966Y3.0345
G1X10.6207Y2.2069
G1X10.6207Y1.6552
G1X10.8966Y0.8276
G1X11.4483Y0.2759
G1X12.0000Y0.0000
G0Z0.1

```
This snippet demonstrates basic G-code movements, similar to what was received in the challenge.

---

**Key Takeaways:**
- Recognizing CNC machines use G-code helped identify the format of the output.
- Using `nc` to capture the data allowed us to analyze it effectively.
- Online G-code viewers were essential in visualizing the tool path to extract the flag.
- The challenge was an exercise in recognizing and decoding machine control language.

This method can be useful in CTFs involving industrial systems, embedded devices, or automated machinery!

