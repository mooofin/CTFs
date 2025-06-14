This reverse engineering task involved a *Virtual-Machine-0.dae* file—a 3D COLLADA model of a gear system. The goal was to derive a flag by analyzing gear rotations: the red axle (40 spikes) drove a grey gear (8 spikes), requiring 5 full turns of the red gear to rotate the blue axle once.

The solution felt more like a math puzzle than a typical RE challenge:

Multiply the input.txt value (2525411025) by 5 (gear ratio).

Convert the result to hex, then ASCII, yielding the flag:
picoCTF{g34r5_0f_m0r3_05e5104d}

Why I disliked it:

Misleading category: More mechanical math than reverse engineering.

Over-reliance on guessing: Without hints, the gear ratio logic wasn’t intuitive.


