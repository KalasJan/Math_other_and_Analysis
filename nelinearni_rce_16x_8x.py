# reseni nelinearnich rovnic

# reste rovnici e^x = sin (x)

from scipy.optimize import fsolve #pro reseni
from numpy import linspace #funkce v rovnici

# Rovnici prevedeme na funkci
def f(x):
    return 16**x - 8*x

# Hledání kořenů
odhady = [0, 2]  # různé počáteční odhady, kde bychom mohli najít kořeny
solutions = [fsolve(f, x0)[0] for x0 in odhady]

# Výpis řešení
for sol in solutions:
    print("Řešení rovnice je přibližně x =", sol)
    
# graficke reseni
import matplotlib.pyplot as plt

# Definice hodnot x a odpovídajících funkcí
x = linspace(0.23, 0.55, 1000) # interval eseni
y1 = 16**x
y2 = 8*x

# Vykreslení grafů
plt.plot(x, y1, label='16^x') # graf 1
plt.plot(x, y2, label='8*x') # graf 2
plt.xlabel("x") # osa x
plt.ylabel("y") # osa y
plt.title("Průsečíky funkcí 16^x a 8*x")
plt.legend()
plt.grid()
plt.show()