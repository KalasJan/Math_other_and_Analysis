#vysetrete prubeh funkce y = sin(ln(sqrt(pi*x)))

import numpy as num
import matplotlib.pyplot as mal
from sympy import symbols, sin, sqrt, pi

# defunujeme symboly x,y
x = symbols('x')
y = 2*sin(3*x+sqrt(pi/3))


# Numericke vykresleni
osa_x = num.linspace(0, 0.5, 500)  # x > 0 to satisfy the domain requirement
osa_y = num.sin(num.log(num.sqrt(num.pi * osa_x)))

# Plotting the function
mal.figure(figsize=(10, 6))
mal.plot(osa_x, osa_y, label=r"$y = \sin(\ln(\sqrt{\pi x}))$")
mal.xlabel("x")
mal.ylabel("y")
mal.title("Graf fce y = sin(ln(sqrt(pi*x)))")
mal.legend()
mal.grid(True)
mal.show()
