# soucet aritmeticke posloupnosti

a1 = float(input('a1='))
n = int(input('n='))
d = float(input('d='))

# definujeme n-ty clen posloupnosti
def a(n):
    return a1+(n-1)*d

#definujeme celkovy soucet:
def s(n):
    return n/2*(a1+a(n))

print (f'celkový součet AP "{a1} + ...+ {a(n)}" s diferencí "{d}" je',s(n))


# soucet GP

A1 = float(input('A1=')) # i desetinne cislo
N = int(input('N=')) #cele cislo
q = float(input('q='))

# definujeme n-ty clen posloupnosti
def A(n):
    return A1*(q**(N-1))

#definujeme celkovy soucet:
def S(N):
    if q==1:
        return N*A1
    else:
        return A1*(q**N-1)/(q-1)

print (f'celkový součet GP "{A1} + ...+ {A(N)}" s kvocientem "{q}" je',S(N))


# soucet GP
