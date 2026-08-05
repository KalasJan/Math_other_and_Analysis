# Aplikace urciteho integralu
# funkce a meze je vygenerovana AI, aby vsechny 4 priklady vychazely "krasne"

from scipy.integrate import quad
import numpy as np
import sympy as sm
import matplotlib.pyplot as plt

x = sm.Symbol("x") # kvuli SymPy vypoctum

# definice funkce a mezi
a = 0
b = 1

f_sympy = x**2

dx = sm.diff(f_sympy, x) # derivace

f = sm.lambdify(x, f_sympy, 'numpy') # prevod nepolynomickych na NumPy
# ==========================================================
# 1) obsah plochy
area, _ = quad (f, a, b) # _ tam je kvuli odchylce

print(f" Obsah plochy {f_sympy} v mezích [{a}, {b}] je {area:.2f}.")
print(f" Pokud se bod pohybuje rychlostí {f_sympy} v intervalu [{a}, {b}], dráha je {area:.2f}")
print(f" Pokud se bod posouvá silou {f_sympy} v intervalu [{a}, {b}], vykonaná práce je {area:.2f}\n")

# ============================================================
# 2) objem rotacniho telesa
def objem(x):
    return f(x) ** 2

vol_int, _ = quad(objem, a, b)
volume = np.pi * vol_int

print("=========================================================================")
print(f" Objem tělesa rotujícího kolem osy x v mezích [{a}, {b}] je {volume:.2f}.\n")

# ===========================================================   
# 3) delka krivky sqrt(1+(f')^2)
delka = sm.sqrt(1+dx**2)

f_long = sm.lambdify(x, delka, 'numpy') # prevod na NumPy
long, _ = quad(f_long, a, b)

print("=========================================================================")
print(f" Délka křivky {f_sympy} v mezích [{a}, {b}] je {long:.2f}.\n")

# ============================================================
# 4) objem plaste
# podle x: 2 * pi * f(x) * sqrt(1 + (f')^2)
plast_x = 2 * sm.pi * f_sympy * sm.sqrt(1 + dx**2)

f_plast_x = sm.lambdify(x, plast_x, 'numpy') # prevod na NumPy
surface_x, _ = quad(f_plast_x, a, b) # samotny vypocet

# podle y: 2 * pi * x * sqrt(1 + (f')^2)
plast_y = 2 * sm.pi * x * sm.sqrt(1 + dx**2)

f_plast_y = sm.lambdify(x, plast_y, 'numpy')
surface_y, _ = quad(f_plast_y, a, b)

print("=========================================================================")
print(f" Obsah pláště při rotaci kolem osy x v mezích [{a}, {b}] je {surface_x:.2f}")
print(f" Obsah pláště při rotaci kolem osy y v mezích [{a}, {b}] je {surface_y:.2f}")

# ==========================================================
# 5) graf f(x)

x_graph = np.linspace(a-1, b+1, 1000)
y_graph = f(x_graph)

plt.figure(figsize=(12, 7), layout='constrained')

# a) kresleni krivky a legendy
plt.plot(x_graph, y_graph, color='black', linewidth=2.5)

plt.plot([], [], ' ', label=f"Obsah plochy: $S$ = {area:.2f}")
plt.plot([], [], ' ', label=f"Objem telesa: $V$ = {volume:.2f}")
plt.plot([], [], ' ', label=f"Delka krivky: $l$ = {long:.2f}")
plt.plot([], [], ' ', label=f"Obsah plaste podle $x$: $P_x$ = {surface_x:.2f}")
plt.plot([], [], ' ', label=f"Obsah plaste kolem $y$: $P_y$ = {surface_y:.2f}")

# b) vykreleni plochy pod krivkou
shadow = np.linspace(a, b, 500)
plt.fill_between(shadow, f(shadow), color='orange', alpha=0.2, hatch='//', label='Integrovaná plocha')

# c) zvyrazneni mezi x = a, x = b
plt.axvline(a, color='crimson', linewidth=1.5, linestyle='--', alpha=0.7, label=f'Mez a = {a}')
plt.axvline(b, color='crimson', linewidth=1.5, linestyle='--', alpha=0.7, label=f'Mez b = {b}')
plt.axhline(0, color='gray', linewidth=1.5, linestyle='--', alpha=0.4)

# d) zacisteni
plt.xlim(a - 0.5, b + 1.5)
plt.ylim(np.min(y_graph) - 1, np.max(y_graph) + 1)

# e) popisy
math_linear = sm.nsimplify(f_sympy)
math_prof = sm.latex(math_linear)

plt.xlabel('Osa X', fontsize=11)
plt.ylabel('Osa Y', fontsize=11)
plt.title(fr'Integrální aplikace pro křivku $y = {math_prof}$ v mezích $[{a}, {b}]$', fontsize=13, weight='bold', pad=15)

# f) legenda a samotne vykresleni
plt.legend(fontsize=11, framealpha=0.9)
plt.grid(True, linestyle=':', alpha=0.4)

plt.show()