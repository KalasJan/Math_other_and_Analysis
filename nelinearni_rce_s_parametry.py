# res rovnici x+sin(x+A)+B = 0, kde A,B jsou ruzna cisla

print('Zadej hodnoty parametrů A, B:')
A = float(input('A=', ))
B = float(input('B=', ))

from scipy.optimize import fsolve #pro reseni
from numpy import sin, linspace #funkce v rovnici
import matplotlib.pyplot as plt #pro vykresleni grafu

#rovnici prevedeme na funkci
def f(x):
    return x+sin(x+A)+B

# Hledání kořenů
odhady = [1]  # různé počáteční odhady, kde bychom mohli najít kořeny, 
              # navic pocet hodnot v zavorce = pocet vsech vypsanych reseni
solutions = [fsolve(f, x0)[0] for x0 in odhady]

# Výpis řešení
for sol in solutions:
    print("Řešení rovnice BEZ zaokrouhleni je přibližně x =", sol) #bez zaokrouhleni
    print("Zaokrouhlene na 2 desetinna mista je řešení rovnice přibližně x =", f"{sol:.2f}")
        #zaokrouhleni na 2 desetinna mista

# graf
# rozsah hodnot
osa_x = linspace(-10, 10, 500) #rozsah od, do, pocet bodu
osa_y = f(osa_x)

#samotny graf
plt.figure(figsize=(10, 6)) #rozmry v pixelech
plt.plot(osa_x, osa_y, label=f'f(x) = x + sin(x + {A}) + {B}') #co ma vykreslit
plt.axhline(0, color='gray', linestyle='--')  # osa x
plt.axvline(0, color='gray', linestyle='--')  # osa y
plt.xlabel('x') #popis osy x
plt.ylabel('f(x)') #popis osy y
plt.title('Graf funkce f(x) = x + sin(x + A) + B') #jmeno
plt.legend()
plt.grid(True)
plt.show()