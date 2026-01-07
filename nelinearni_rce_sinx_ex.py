# reseni nelinearnich rovnic

# reste rovnici e^x = sin (x)

from scipy.optimize import fsolve #pro reseni
from numpy import sin, exp, linspace #funkce v rovnici

# Rovnici prevedeme na funkci
def f(x):
    return sin(x) - exp(x)

# Hledání kořenů
odhady = [-10, 0, 1]  # různé počáteční odhady, kde bychom mohli najít kořeny
solutions = [fsolve(f, x0)[0] for x0 in odhady]

# Výpis řešení
for sol in solutions:
    print("Řešení rovnice je přibližně x =", sol)
    
# graficke reseni
import matplotlib.pyplot as plt

# Definice hodnot x a odpovídajících funkcí
x = linspace(-10, 1, 100) # interval eseni
y1 = sin(x)
y2 = exp(x)

# Vykreslení grafů
plt.plot(x, y1, label='sin(x)') # graf 1
plt.plot(x, y2, label='exp(x)') # graf 2
plt.xlabel("x") # osa x
plt.ylabel("y") # osa y
plt.title("Průsečíky funkcí sin(x) a exp(x)")
plt.legend()
plt.grid()
plt.show()