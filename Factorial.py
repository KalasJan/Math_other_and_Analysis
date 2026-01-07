# Vypocitejte, kolik je 10! (faktorial)

# mame 3 zpusoby

# Zpusob 1 
# faktorial je rekurzivni funkce

#def fac(n):
#    if n == 0:
#        return 1
#    else:
#        return (n * fac(n-1))
#print (fac(3))

# Zpusob 2
# vyuzijeme Python - math

#import math
#print (math.factorial(4))

# Zpusob 3
# zjednoduseni zpusobu 2

from math import factorial
print (factorial(100))


# Dalsi kombinatoricke procesy (Variace, permutace, kombinace) se delaji pres definice jednotlivych procesu
# napr. V(k, n) = fac(n)/fac(n-k)
