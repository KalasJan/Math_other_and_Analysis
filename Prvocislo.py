# je mnou zadane cislo prvocislem?
# pokud ne, vypis vsechny delitele a prvociselny rozklad
# rozklad: 8 = 2*2*2
# delitele: 8 = 1, 2, 4, 8
# do cisla 8 jsou 4 prvocisla, a to 2, 3, 5, 7
# 854842841543 pro zjisteni?

n = int(input('Sem zadej prirozene cislo: '))

# urceni, zda je prvocislem
def n_je_prvocislo(n):
    if n <=1:
        return False 
    for k in range(2, int(n**0.5) + 1): # optimalizace urceni, zda je/neni prvocislem
        # test hrubou silou, deleni do cisla sqrt(n)
            if n % k == 0: # ma delitele
                return False 
    return True # nema delitele

# rozklad
def rozklad(n):
    vycet = [] # bude seznam vsech cisel
    delitel = 2 # nejmensi mozny  delitel
    while n > 1: # dokud se nevypisou vsechna prvocisla
        while n % delitel == 0: #n delitelne bez zbytku
            vycet.append(delitel) #pridani dalsiho
            n //= delitel # n se deli dalsim delitelem
        delitel += 1
    return vycet #vypis vsech prvocisel

# vypis vsech delitelu
def delitele(n):
    seznam = [] # seznam vsech delitelu, na zacatku je prazdny
    for p in range (1, n+1): #diva se na cisla 1, 2, ... , n
        if n % p == 0: # deleni n/p ma zbytek 0
            seznam.append(p) #pridani cisla do seznamu
    return seznam

# vysledky
if n_je_prvocislo(n):
    print (f'Cislo {n} je prvocislo.')
else:
    print (f'Cislo {n} neni prvocislo.')
    print (f'Delitele cisla {n} jsou: {delitele(n)}.')
    print (f'Číslo {n} má {len(delitele(n))} delitelu.')
    # print (f'Rozklad cisla {n} je: {rozklad(n)}.') # vysledek je [2,2,3] pro n = 12
    print (f'Rozklad čísla {n} je: {" * ".join(map(str, rozklad(n)))}') # 12 = 2*2*3
    
# pocet vsech prvocisel do cisla n
def pocet(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
print(f'Pocet prvocisel do cisla {n} je {pocet(n)}.')

# vycet vsech prvocisel do cisla n
prvocisla = [u for u in range(2, n+1) if n_je_prvocislo(u)]
print(f'Vsechna prvocisla do cisla {n} jsou: {prvocisla}.')