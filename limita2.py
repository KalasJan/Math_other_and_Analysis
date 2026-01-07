# vypocet limit

from sympy import symbols, limit # vypocet limity
import numpy as num #numerika
import matplotlib.pyplot as mal # pro kresleni grafu

# definujeme promennou
x = symbols('x')
f = (x**2-16)/(x**2+x-20) # funkce



limita = limit(f, x, 4) #x - promenna, 0 k cemu jde
print ('limita je', limita)

## vypocty pro kresleni
# definice hodnot (kde se budeme divat)
xh = num.linspace(1, 10, 10000) # i pro vykresleni grafu funkce f
xh = xh[xh != 4] # 4 je bod nespojitosti samotne funkce (limita to tam dodefinuje)

#vypocet funkcinich hodnot
yh = (xh**2-16)/(xh**2+xh-20)

# vykresleni grafu pro x->0
mal.figure(figsize=(10, 6)) # velikost
mal.plot(xh, yh, label=r'$f(x) = \frac{x^2 - 16}{x^2 + x - 20}$', color="blue") #graf funkce
mal.axhline(limita, color='red', linestyle='--', label='Limita pro $x \\to 4$') #carkovana limita
mal.axvline(0, color='grey', linestyle=':', linewidth=0.8) #seda teckovana carka, osa y
mal.title(r'Graf funkce $\frac{x^2 - 16}{x^2 + x - 20}$ a její limita pro $x \to 4$')
mal.xlabel('x')
mal.ylabel(r'$f(x)$')
mal.xlim(3.975, 4.025)  #rozsah na ose x
mal.ylim(0.8875,0.89) # rozsah na ose y
mal.legend()
mal.grid(True)
mal.show()