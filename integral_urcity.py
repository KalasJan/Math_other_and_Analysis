from scipy.integrate import quad
from numpy import linspace, sin, pi
import matplotlib.pyplot as plt #pro graf

def f(x):
    return sin(x) #predpis funkce

# meze
a = 0
b = 2*pi

#vypovet urc integralu
i, err = quad (f, a, b)
print (f'Integrál f(x) v mezích {a}, {b} je:', i)
print ('Chyba je', err)
# err - chyba, odchylka

# rozsah hodnot (od, do, kolik bodu)
x = linspace(0,b,254)


# samotne vykresleni grafu
plt.plot(x, f(x), label="f(x)", color="blue") #co to má vykreslit a barva
plt.xlabel("x") # osa x
plt.ylabel("f(x)") # osa y
plt.title("Graf funkce f(x)") # jmeno grafu
plt.xlim(a, b)  #rozsah na ose x
plt.ylim(min(f(x)), max(f(x)))  #rozsah na ose y, max(f) - maximum funkce f na danem useku
plt.legend()
plt.grid(True) #mrizka
plt.show()