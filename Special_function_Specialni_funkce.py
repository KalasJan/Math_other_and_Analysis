import numpy as np
import matplotlib.pyplot as plt
import sympy as sm

# definujeme funkce
x = sm.symbols('x')

f1 = sm.Abs(x)
f2 = sm.ceiling(x) # horni cast
f3 = sm.floor(x) # dolni cast
f4 = sm.floor(x + 0.5) # zaokrouhleni

# vykresleni
numerika = sm.lambdify(x, [f1, f2, f3, f4], 'numpy')

od = -5
do = 5
osa_x = np.linspace(od, do, 1000)
(y1, _, _, _) = numerika(osa_x) # pouze pro abs(x)

# schodovite funkce
x_stair = []
x_round_stair = []
y2_stair = [] # horni, ceiling
y3_stair = [] # dolni, floor
y4_stair = [] # zaokrouhleni, round


for i in range(od, do):
    usek_x_floor = np.linspace(i, i + 1, 50, endpoint=False)
    _, _, y3_u, _ = numerika(usek_x_floor)
    
    usek_x_ceil = np.linspace(i + 1e-9, i + 1, 50, endpoint=True)
    _, y2_u, _, _ = numerika(usek_x_ceil)
    
    usek_x_round = np.linspace(i - 0.5 + 1e-9, i + 0.5, 50, endpoint=False)
    _, _, _, y4_u = numerika(usek_x_round)
    

# vlozeni schodu do grafu
    x_stair.extend(usek_x_floor)
    x_round_stair.extend(usek_x_round)
    
    y2_stair.extend(y2_u)
    y3_stair.extend(y3_u)
    y4_stair.extend(y4_u)

# nespojeni
    x_stair.append(np.nan)
    x_round_stair.append(np.nan)
    
    y2_stair.append(np.nan)
    y3_stair.append(np.nan) 
    y4_stair.append(np.nan)
    
# vykreslenni
plt.figure(figsize=(11, 11))

plt.plot(osa_x, y1, label=r"$f(x) = |x|$ (absolutní hodnota)", color="green", lw=2)
plt.plot(x_stair, y2_stair, label=r"$f(x) = \lceil x \rceil$ (horní část)", color="royalblue", lw=2, linestyle="--")
plt.plot(x_stair, y3_stair,label=r"$f(x) = \lfloor x \rfloor$ (dolní část)",color="darkorange",lw=3.5, linestyle="-.")
plt.plot(x_round_stair, y4_stair, label=r"$f(x) = \mathrm{{round}}(x)$ (zaokrouhleno na celá čísla)", color="crimson", lw=5,linestyle=":")

plt.axhline(0, color="gray", linewidth=1, alpha=0.5)
plt.axvline(0, color="gray", linewidth=1, alpha=0.5)

kroky_os = np.arange(-6, 7 + 1, 1) # na osach dana jednotka (0, 1, 2, ..)
plt.xticks(kroky_os)
plt.yticks(kroky_os)

plt.xlim(od-1, do+1)
plt.ylim(od-1, do+1)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Porovnání speciálních funkcí")
plt.legend(loc = "lower right")
plt.grid(True, linestyle=":", alpha=0.6)
plt.axis('scaled')
plt.show()
