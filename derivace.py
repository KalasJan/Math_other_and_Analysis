# vypocitejte derivace funkce 7x^3 a 7x^3*y^2

# 1) vyresime derivaci 1 promenne

import sympy as sm

x = sm.Symbol("x")

print (sm.diff(7*x**3))

x,y = sm.symbols("x y")

print (sm.diff(7*x**3*y**2, y)) # za carkou je podle ktere se derivuje