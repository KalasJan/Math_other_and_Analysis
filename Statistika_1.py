# Jsou dány výšky členů týmu (v cm): 178, 185, 189, 194, 194, 199, 203, 207, 212, 213
# vypocitej modus, median, AP, GP, HP, rozpeti (max-min), rozptyl a odchylku
# nakreslete graf normalniho rozdeleni 

import numpy as np
import matplotlib.pyplot as plt #pro grafy
import scipy.stats as stats


# Zadané hodnoty výšek
vysky = np.array([178, 185, 189, 194, 194, 199, 203, 207, 212, 213])

# Výpočet průměru a směrodatné odchylky
prumer = np.mean(vysky)
smerodatna_odchylka = np.std(vysky, ddof=1)  # ddof=1 pro výběrovou směrodatnou odchylku

# Generování hodnot pro osu X
x = np.linspace(prumer - 4 * smerodatna_odchylka, prumer + 4 * smerodatna_odchylka, 100)

# Výpočet normálního rozdělení na základě průměru a směrodatné odchylky
y = stats.norm.pdf(x, prumer, smerodatna_odchylka)

# Vykreslení grafu (pro vykresleni )
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Normální rozdělení', color='blue')
plt.xlabel('Výška')
plt.ylabel('Hustota pravděpodobnosti')
plt.title('Normální rozdělení výšek členů skupiny')
plt.legend()
plt.grid()
plt.show()

# vypocitej modus, median, AP, GP, HP, rozpeti (max-min), rozptyl a odchylku
modus = stats.mode(vysky)
median = np.median(vysky)
AP = np.mean(vysky)
GP = stats.gmean(vysky)
HP = stats.hmean(vysky)
rozptyl = np.var(vysky, ddof=1)
odchylka = np.std(vysky, ddof=1)

print ('Modus je', modus)
print ('Medián je', median)
print ('Aritmetiký průměr je', AP)
print ('Geometrický průměr je', GP)
print ('Harmonický průměr je', HP)
print ('Rozptyl je', rozptyl)
print ('Směrodatná odchylka je', odchylka)
