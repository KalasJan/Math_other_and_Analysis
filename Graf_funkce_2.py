#vysetrete prubeh funkce y = 2sin(2x)

from numpy import sin, linspace, pi
import matplotlib.pyplot as mal 

# defunujeme funkci
def f(x):
    return 2*sin(2*x)

# od do
od = 0
do = 2*pi

# rozsah hodnot (od, do, kolik bodu)
x = linspace(od,do,1000)

# samotne vykresleni grafu
mal.plot(x, f(x), label="f(x)", color="blue") #co to má vykreslit a barva
# mal.xlabel("x") # osa x
# mal.ylabel("f(x)") # osa y
# mal.title("Graf funkce f(x)") # jmeno grafu
mal.xlim(od, do)  #rozsah na ose x
mal.ylim(min(f(x)-1/2), max(f(x)+1/2))  #rozsah na ose y, max(f) - maximum funkce f na danem useku
# mal.legend()
mal.grid(True) #mrizka
mal.show()
