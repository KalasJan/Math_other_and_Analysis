# napis horni, dolni a celou cast cisla n

# libovolne desetinne cislo (klidne i jako zlomek)

from numpy import sin, cos, pi
from math import ceil, floor

def sqrt(x):
    return x**(1/2)

def tan(x):
    return sin(x)/cos(x)

def cotan(x):
    return 1/tan(x)

n = 2*sin(3*pi+sqrt(pi/3))

# dolni cast
dolni = floor(float(n))

# horni cast
horni = ceil(float(n))

# cela cast
cela = int(n)

# zaokrouhleni (bez desetin)
zaokrouhleni = round(n)


# vysledek
print (f'Cislo n = {n}, dale:')
print (f'Dolní část je {dolni}.')
print (f'Horní část je {horni}')
print (f'Cela cast je {cela}.' )
print (f'Zaokrouhlene je {zaokrouhleni}')
