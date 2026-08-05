# Vykresli Vektorové pole, které je dáno předpisem (x,y) -> (x*sin(y), y*sin(x))

import numpy as np
import matplotlib.pyplot as plt

# predpis samotneho pole
def vect(x,y):
    fx = x*np.sin(y)
    fy = y*np.sin(x)
    return fx, fy
    
# mrizka, nemusi byt tak husta, staci 15x15
x = np.linspace(-2, 2, 15)
y = np.linspace(-2, 2, 15)
X, Y = np.meshgrid(x, y)

fX, fY = vect(X, Y)
size = np.sqrt(fX**2 + fY**2) 

# kresleni
plt.figure(figsize=(8, 8))

# quiver - kresleni sipek
# pivot = middle -> stred sipky na souradnici
plt.quiver(X, Y, fX, fY, size, cmap='coolwarm', pivot='middle')

plt.title(r'Vektorové pole s předpisem $(x,y) \rightarrow (x\cdot \sin(x), y \cdot \sin(y))$')
plt.grid(True, linestyle=':', alpha=0.5)
plt.axis('equal')
plt.show()