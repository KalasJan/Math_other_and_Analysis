# we have a function f(x,y) = (x*y*e^(-x-y))/(e^(-2))

import numpy as np #maths
import matplotlib.pyplot as plt #create a graph
from scipy.integrate import nquad #integral

# create data
x = np.linspace(0, np.pi, 50)
y = np.linspace(0, np.pi, 50)
X, Y = np.meshgrid(x, y) #free variable
Z = (X * Y * np.exp(-X - Y)) / (np.exp(-2))

# Create graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create surface
ax.plot_surface(X, Y, Z, cmap='ocean')

# View
ax.view_init(elev=30, azim=-60)

# axes, title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("3D graf fce f(x,y)")

plt.show()

# integral Z for x in [0, pi], y in [1, 2]

# again definition of function
def f(y,x):
    return (x * y * np.exp(-x - y)) / (np.exp(-2))

# intervals, x in [0, pi], y in [1, 2]
intervals = [[1, 2], [0, np.pi]] # interval y, then x

i, err = nquad (f, intervals)
print ('Integrál f(x) je', i)
print ('Chyba je', err)