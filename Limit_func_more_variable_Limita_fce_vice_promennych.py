# je dana funkce f(x,y)
# reste lim (x,y) -> (a,b) a fci (s timto bodem) nakreslete

import sympy as sm
import matplotlib.pyplot as plt
import numpy as np

# definice promennych
x, y = sm.symbols ('x y', real=True)
r, phi = sm.symbols ('r phi', real=True, positive = True)

# lim (x,y) -> (a,b)
a = 2
b = 3

# definice funkce
f = (x * y) / (x**2 + y**2)

# polarizace
# x = r * cos(phi) +a , y = r * sin(phi) + b
f_polar = f.subs({x: r * sm.cos(phi) + a, y: r * sm.sin(phi) + b})

# lim r -> 0
limita = sm.limit(f_polar, r, 0, dir = '+')

if limita.has(phi):
    lim_val = "NEEXISTUJE"
else:
    lim_val = str(limita)
    
# Spočítáme si hodnotu limity jako float pro pozdější vykreslení
z0_num = float(sm.N(limita)) if lim_val != "NEEXISTUJE" else 0.0

print(f"Limita pro {f} v bodě ({a}, {b}) je: {lim_val}")

# vykresleni grafu i s bodem

# prevod na numpy, 1e-15 je "technicka nula", pocitani se zlomkem
citatel, jmenovatel = sm.fraction(f)
f_safe = citatel / (jmenovatel + 1e-15)
f_num = sm.lambdify((x, y), f_safe, 'numpy')

x_vals = np.linspace(a - 2, a + 2, 200)
y_vals = np.linspace(b - 2, b + 2, 200)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f_num(X, Y)

# samotny graf
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

#povrch
povrch = ax.plot_surface(X, Y, Z, cmap='magma_r', edgecolor='none', alpha=0.9)

# existence limity
if lim_val != "NEEXISTUJE":
    ax.scatter([a], [b], [z0_num], color='crimson', s=100, zorder=10, 
               label=rf'Dodefinovaný bod limity $({a},{b}, {z0_num:.0f})$')

f_mat = sm.latex(f) # matemticky zapis v nadpise
    
ax.set_title(rf'Povrch funkce $f(x,y) = {f_mat}$ s lim (x,y) -> ({a}, {b}): ', fontsize=13, pad=15)
ax.set_xlabel('Osa x')
ax.set_ylabel('Osa y')
ax.set_zlabel('Osa z')

ax.view_init(elev=30, azim=-60)

plt.legend()
plt.show()
