# Vypocitej variace, permutace a kombinace bez opakovani, variace a kombinace s opakovanim na zaklade vytvorenych cisel hodnot

n = int(input('n = '))
k = int(input('k = '))

def f(x): #definujeme faktorial
    if x < 0:
        return 'nelze'
    elif x == 0:
        return 1
    else:
        return x * f(x-1)

# definujeme variace bez opakovani
def V(k,n):
    return f(n)/f(n-k)

# definujeme permutace bez opakovani
def P(n):
    return f(n)

# definujeme kombinacni cislo
def K(k,n):
    return f(n)/((f(n-k)*f(k)))

# definujeme variace s opakovanim
def Vo(k,n):
    return n**k

# definujeme kombinace s opakovanim:
from math import comb
def Ko(k,n):
    return comb(n+k-1, k)

# samotne vypocty
if n > k:
    print(f'Variace bez opakování V({k},{n}) je {V(k, n)}.')
    print(f'Kombinací bez opakování K({k},{n}) je {K(k, n)}.')
elif n == k:
    print(f'Permutací bez opakování P({n}) je {P(n)}.')
else:
    print(f'Variací s opakováním Vo({k},{n}) je {Vo(k, n)}.')
    print(f'Kombinací s opakováním Ko({k},{n}) je {Ko(k, n)}.')