# vypocet limit

from sympy import symbols, sin, limit, oo # vypocet limity
import numpy as num #numerika
import matplotlib.pyplot as plt # pro kresleni grafu

# definujeme promennou
x = symbols('x')
y = sin(x)/x # funkce

# vypocet levostrane limity pro x-> 0-

limita_leva = limit(y, x, 0, dir='-')
print ('limita zleva je', limita_leva)

# vypocet pravostrane limity pro x-> 0+
limita_prava = limit(y, x, 0, dir='+')
print ('limita zprava je', limita_prava)

# limita obecne
limita = limit(y, x, 0) #x - promenna, 0 k cemu jde
print ('limita je', limita)

# limita pro x -> + nekonecno
limita_nekon = limit(y, x, oo) #x - promenna, oo (2 malá o značí nekonečno)
print ('limita v nekonečnu je', limita_nekon)

## vypocty pro kresleni
# definice hodnot (kde se budeme divat)
x = num.linspace(-1, 1, 1000)
x = x[x !=0] # 0 je bod nespojitosti samotne funkce (limita to tam dodefinuje)

#vypocet funkcinich hodnot
y = num.sin(x)/x

# vykresleni grafu pro x->0
plt.figure(figsize=(10, 6)) # velikost
plt.plot(x, y, label=r'$\frac{\sin(x)}{x}$', color="blue") #graf funkce
plt.axhline(1, color='red', linestyle='--', label='Limita pro $x \\to 0$ (y = 1)') #carkovana limita
plt.axvline(0, color='grey', linestyle=':', linewidth=0.8) #seda teckovana carka, osa y
plt.title(r'Graf funkce $\frac{\sin(x)}{x}$ a její limita pro $x \to 0$')
plt.xlabel('x')
plt.ylabel(r'$\frac{\sin(x)}{x}$')
plt.ylim(0.9, 1.1)  #rozsah na ose y
plt.legend()
plt.grid(True)
plt.show()