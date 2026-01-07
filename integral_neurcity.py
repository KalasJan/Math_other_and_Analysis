# vypocitejte neurcity integral
# tan(ln(x))/x

from numpy import linspace
import matplotlib.pyplot as mal # vykresleni grafu
from sympy import symbols, integrate, tan, log, lambdify #symbolicke vypocty

# promenne
x = symbols('x')

# funkce, se kterou budeme pracovat
f = tan(log(x))/x

# vypocet integralu
integral = integrate(f, x) # co integrujeme, podle promenne
print (f'Primitivni funkce k funkci {f} je', integral)

# integral je vyraz, udelame z nej funkci
int_fce = lambdify(x, integral, 'numpy')

# interval grafu (od, do, body)
hodnoty_x = linspace(0.1, 10, 400)

# Definujeme různé hodnoty konstanty C
con = [-10, -5, 0, 5, 10]

# Vykreslení grafu pro různé hodnoty konstanty
mal.figure(figsize=(10, 6))
for C in con:
    hodnoty_y = int_fce(hodnoty_x) + C
    mal.plot(hodnoty_x, hodnoty_y, label=f'C = {C}')

mal.xlabel('x')
mal.ylabel('f(x)')
mal.title(f'Funkce {integral} s různými konstantami {C}')
mal.legend()
mal.grid(True)
mal.show()