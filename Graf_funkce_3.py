import numpy as num
import matplotlib.pyplot as mal
from sympy import symbols, sin, cos, lambdify

# defunujeme symboly x,y
x = symbols('x')
y = -3*(cos(x)**2)*sin(x)

# Převod symbolické funkce na číselnou
numerika = lambdify(x, y, 'numpy')

# Numericke vykresleni
osa_x = num.linspace(-num.pi, num.pi, 1500)
osa_y = numerika(osa_x)

# Plotting the function
mal.figure(figsize=(10, 6))
mal.plot(osa_x, osa_y)
mal.xlabel("x")
mal.ylabel("y")
mal.title(f"Graf fce {y}")
# mal.legend() v mal.plot není label
mal.grid(True)
mal.show()
