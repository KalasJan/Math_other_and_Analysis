# reseni kvadraticke rovnice

# kvadraticka rovnice ma tvar ax^2 + bx + c = 0 pro a != 0

# hodnoty koeficientů
a = int(input("Zadejte hodnotu koeficientu a = " ))
b = int(input("Zadejte hodnotu koeficientu b = " ))
c = int(input("Zadejte hodnotu koeficientu c = " ))

# Diskriminant:
D = b**2 - 4 * a * c
print ("D =", D)

# reseni
import math, cmath

if D >= 0:
    x1 = ((-b + math.sqrt(D))/(2*a))
    x2 = ((-b - math.sqrt(D))/(2*a))
    print ("Reseni teto rovnice jsou:", x1, "a", x2) # realna reseni
else: 
    y1 = ((-b + cmath.sqrt(D))/(2*a))
    y2 = ((-b - cmath.sqrt(D))/(2*a))
    print ("Reseni teto rovnice jsou:", y1, "a", y2) # D < 0 - zadne realne reseni, pouze komplexni
    