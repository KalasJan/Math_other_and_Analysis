# 50 lidi psalo test, mohlo ziska 1-10 bodu
# bodove zisky jsou uvede v hodnoty
hodnoty = [10,5,8,8,9,9,10,1,8,10,
           7,7,2,8,6,1,9,4,7,3,
           6,1,3,3,6,3,4,6,10,7,
           1,4,4,10,5,3,9,6,9,5,
           8,5,1,3,1,7,8,9,8,3]

from scipy.stats import skew, kurtosis
from numpy import mean, std, unique

# aritmeticky prumer
AP = mean(hodnoty)
print (f'Aritmetický průměr souboru je {AP:.2f}.') #2f - zaokrouhleni 2 desetiny

# smerodatna odchylka
So = std(hodnoty)
print(f'Směrodatná odchylka je {So:.2f}.')

# sikmost rozdeleni
sik = skew(hodnoty)
print(f'Koeficient sikmosti je {sik:.2f}.')

# spicatost rozdeleni
spi = kurtosis(hodnoty)
print(f'Koeficient spicatosti je {spi:.2f}.')

import matplotlib.pyplot as mapl # vykresleni grafu

# histogram
mapl.figure(figsize=(12, 4))

mapl.subplot(1, 2, 1)
mapl.hist(hodnoty, bins=10, color='skyblue', edgecolor='black', alpha=1)
mapl.title('Histogram')
mapl.xlabel('Hodnoty')
mapl.ylabel('Frekvence')

# sloupcovy graf
zisky, pocty = unique(hodnoty, return_counts=True)

mapl.subplot(1, 2, 2)
mapl.bar(zisky, pocty, color='lightgreen', edgecolor='black')
mapl.title('Sloupcový graf')
mapl.xlabel('Hodnoty')
mapl.ylabel('Frekvence')
mapl.tight_layout() #optimalizace rozvrzeni

# kolacovy graf
#○pocty = pocty[::-1] #rotace po smeru hodin
#zisky = zisky[::-1] #rotace po smeru hodin

mapl.figure(figsize=(8, 8))  # Nastavení velikosti grafu
mapl.subplot(1, 1, 1)
mapl.pie(pocty, labels=zisky, autopct='%01.2f%%', startangle=-90)
mapl.title('Koláčový graf')
mapl.axis('equal') # aby to byl kruh
mapl.show()

# seskupeni hodnot - vysledek je 
import pandas as pan
# cetnosti uz mame -> zisky, pocty = unique...
#radkovite
prehled = pan.DataFrame([zisky, pocty], index = ['Hodnoty', 'Četnosti'])
print(prehled)

#sloupcovite
prehled2 = pan.DataFrame({'Hodnoty': zisky, 'Četnost': pocty})
print(prehled2)