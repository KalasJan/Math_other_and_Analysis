# reste rovnici x^5-4x^4+5x^3-2x^2-x+1=0

# postup 1 - odhad
#import numpy as np

# koeficienty
#koeficient = [1, -4, 5, -2, -1, 1]

# kořeny, řešení
##koren = np.roots(koeficient)

# výsledek
#print('Řešení rovnice jsou:', koren)



# postup 2- presne

from sympy import symbols, Eq, solve

# neznámá - definice symbolu
x = symbols('x')

# rovnice (polynom = 0)
rovnice = x**2/15-2*x/3+5/3

#reseni
reseni = solve(Eq(rovnice, 0),x)

# 1 radek 1 reseni s ocislovanim radku
for index, sol in enumerate(reseni, start=1):
   print(f"{index}: {sol}")