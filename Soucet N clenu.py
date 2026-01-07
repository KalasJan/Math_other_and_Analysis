# Kalkulacka, ktere dame cislo N a ona secte cisla 1+2+3+...+N

N = int(input("Sem zadej, kolik cisel chces secist: "))

soucet = int(N*(N+1)/2) # viz vrotec z analyzy pro soucet clenu 1 + 2 + ... + N

print ("Celkovy soucet cisel od 1 do", N, "je", soucet)