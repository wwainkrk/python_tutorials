import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 11, 1)

a = 1
b = -3
c = 1

y = [a*(x**2) + b*x + c for x in x]

plt.plot(x, y, 'go--')
plt.title(f'Function graph f(x): {a}$x^{2}$ + {b}x + {c}')
plt.legend(["f(x)"])
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
