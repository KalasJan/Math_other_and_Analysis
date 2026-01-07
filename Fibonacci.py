# Vypocitejte, kolik je napr. 50. clen Fibonacciho posloupnosti
# Fib. posloupn.: 1, 1, 2, 3, 5, 
# tj. F(1) = 1, F(2) = 1, F(n) = F(n-1) + F(n-2)

# Fib. posloupnost je dana rekurzivne

n = int(input('Zadej hodnotu n='))

#definujeme samotnou posloupnost
def Fib(n):
    if n<0:
        print ("Nelze")
    elif n == 1 or n == 2:
        return 1
    else:
        return (Fib(n-1) + Fib(n-2))
print (f'{n}-ty clen Fibonacciho posloupnosti je {Fib(n)}.')

# vypis radu az do n-teho clenu
def vypis_rady(n):
   rada = []
   for k in range(1, n+1):
       rada.append(Fib(k))
   return(rada)
print(f'Fibonacciho posoupnost o {n} clenech je {vypis_rady(n)}')

# součet n clenu Fibonacciho posloupnosti
# napr. soucet prvnich 5 clenu je 1+1+2+3+5 = 12
def soucet_Fib(n):
    return sum(vypis_rady(n))

# formatovani vysledku souctu
posloupnost = vypis_rady(n) #zjednoduseni promenne

soucet = '+'.join(map(str,posloupnost)) #chceme 1+1+...
print(f'Soucet prvni {n} clenu posloupnosti je {soucet} = {soucet_Fib(n)}')