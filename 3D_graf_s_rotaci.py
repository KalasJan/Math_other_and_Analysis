import numpy as np #matematika
import matplotlib.pyplot as plt #kresleni grafu
# from mpl_toolkits.mplot3d import Axes3D

# Vytvoření dat
x = np.linspace(-1, 1, 5)
y = np.linspace(-1, 1, 5)
X, Y = np.meshgrid(x, y) #volne promenne
Z = X*Y-9

# Vytvoření grafu
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vykreslení povrchu
ax.plot_surface(X, Y, Z, cmap='ocean')

# pohled
ax.view_init(elev=30, azim=-60)
# elev - osa x, azim = osa y
# puvodni = elev=30, azim =-60

# Popisky
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("3D graf fce f(x,y)")

plt.show()
