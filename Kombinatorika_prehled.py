# kombinatorika

# faktorial
c= 9
def f(p):
    if p == 0:
        return 1
    else:
        return (p * f(p-1))
print (f'Faktoriál čísla {c} je {f(c)}')

# procesy
n = 30 #K z kolika vybirame
k = 4 # kolik vybirame

# definujeme variace bez opakovani
def V(k,n):
    return f(n)/f(n-k)
print(f'Variací bez opakování V({k},{n}) je {f(n)}/{f(n-k)} = {V(k, n):.0f}')

# definujeme permutace bez opakovani
def P(n):
    return f(n)
print(f'Permutací bez opakování P({n}) je {P(n):.0f}')

# definujeme kombinacni cislo
def K(k,n):
    return f(n)/((f(n-k)*f(k)))
print(f'Kombinací bez opakování K({k},{n}) je {f(n)}/({f(n-k)}*{f(k)}) = {K(k, n):.0f}')

# definujeme variace s opakovanim
def Vo(k,n):
    return n**k
print(f'Variací s opakováním Vo({k},{n}) je {n}^{k} = {Vo(k, n):.0f}')

# definujeme kombinace s opakovanim:
from math import comb
def Ko(k,n):
    return comb(n+k-1, k)
print(f'Kombinací s opakováním Ko({k},{n}) je {f(n+k-1)}/({f(n-k)}*{f(k)}) = {Ko(k, n):.0f}')