import numpy as np #matematika
import matplotlib.pyplot as plt #kresleni grafu
# from mpl_toolkits.mplot3d import Axes3D

# Vytvoření dat
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y) #volne promenne
Z = np.sin(np.sqrt(X**2 + Y**2))

# Vytvoření grafu
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vykreslení povrchu
ax.plot_surface(X, Y, Z, cmap='viridis')

# Popisky
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("3D graf fce f(x,y)")

plt.show()
