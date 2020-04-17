"""
Few details before we start write some code:

We will write a program that simulates Brownian motion. 
As you know, these are chaotic movements of the particles that we can visualize in a two-dimensional plane. 
At the beginning we make the following assumptions:

- the particle whose movement we will follow is at the beginning of the coordinate system (0, 0);
- in each movement the molecule moves by a constant vector with a value of 1;
- the direction of movement will be determined by randomizing an angle from the range <0; 2pi>;
- the coordinates of the next position of the molecule will be calculated from the following formulas:

x = x + r * cos(Ф)
y = y + r * sin(Ф)

where:
- r - length of one step,
- Ф - angle indicating the direction of movement in relation to the OX axis.

we calculate the final shift vector using the formula:

|s| = sqrt(x**2 + y**2)
"""

import numpy as np
import random as rnd
import matplotlib.pyplot as plt

n = int(input("How many moves do you want? "))       # we make declaration how many steps we will do
x = y = 0          # initialization of coordinates

# lists for moves
lx = [x]
ly = [y]

# lists for shift vector on graph
lsx = [x]
lsy = [y]

for i in range(0, n):
    rad = float(rnd.randint(0, 360)) * np.pi / 180  # we switched angle to the radians

    # According our rules we take r = 1, so:
    x = x + np.cos(rad)
    y = y + np.sin(rad)
    # print(x, y)
    lx.append(x)
    ly.append(y)

lsx.append(x)
lsy.append(y)
s = np.fabs(np.sqrt(x**2 + y**2))
# print(f"Shift vector: {s.round(2)}")

# print(lx, ly)

plt.plot(lx, ly, 'o--', color='orange', linewidth=2, alpha=0.5)                # graph changing data
plt.plot(lsx, lsy, 'b')                                                        # graph shift vector
plt.legend(["Data: x, y", f"Shift vector = {s.round(3)}"], loc="upper left")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Brown moves")
plt.grid(True)
plt.show()
