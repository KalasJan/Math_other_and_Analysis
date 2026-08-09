# Gradient
# Je dána funkce f(x,y) = x*sin(y) + y*sin(x). Bod P (pi, pi/2)
# 1) nakresli tento graf
# 2) vypočítej gradient a gradient v tomto bode
# 3) vypočítej smerovou derivaci ve směru (-1, 2)
# 4) zjisti směr kterým je v P nejvetsi sklon a jaky je
# 5) vykresli tyto smery

import numpy as np
import matplotlib.pyplot as plt
import sympy as sm

# definice funkce
def function(x,y):
    f = x * np.sin(y) + y * np.sin(x)
    return f

# def bod (Px,Py):
Px = np.pi
Py = np.pi/2


# 1) vykresleni puvodniho grafu
x = np.linspace(Px - 1, Px+1, 100)
y = np.linspace(Py-1, Py+1, 100)
X, Y = np.meshgrid(x, y) #volne promenne
Z = X * np.sin(Y) + Y * np.sin(X)

# Vytvoření grafu
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vykreslení povrchu
ax.plot_surface(X, Y, Z, cmap='ocean')

ax.view_init(elev=30, azim=30)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("3D graf fce $f(x,y) = x \cdot \sin(y) + y \cdot \sin(x)$")

# -----------------------------------------------------

# 2) vypocet gradientu
x_sm, y_sm = sm.symbols('x y') # definice promennych
f_sm = x_sm * sm.sin(y_sm) + y_sm * sm.sin(x_sm) # definice funkce

x_grad = sm.diff(f_sm, x_sm)
y_grad = sm.diff(f_sm, y_sm) # vypocet gradientu

print (rf'Gradient funkce f(x,y) je (df/dx, df/dy) = ({x_grad}, {y_grad})')

# 2, B) gradient v bode P = (pi, pi/2)
x_grad_point = float(x_grad.subs({x_sm: Px, y_sm: Py}).evalf())
y_grad_point = float(y_grad.subs({x_sm: Px, y_sm: Py}).evalf())

gradient_v_bode = np.array([x_grad_point, y_grad_point])

print (f'Gradient funkce f(x,y) v bodě P = (df/dx (P), df/dy (P)) = ({x_grad_point:.4f}, {y_grad_point:.4f})')

# ------------------------------------------------------------------------

# 3) Vypocet smerove derivace ve smeru (-1, 2)

u = np.array([-1, 2]) # smerovy vektor
size_u = np.linalg.norm(u) # delka vektoru
u_normovany = u / size_u #normovany (jednotkovy) vektor u

# skalarni soucin (grad * u_norm)
smerova_der = np.dot(gradient_v_bode, u_normovany)

# vysledek
print(f"Délka vektoru u = {size_u:.2f}")
print(f"Normovaný / Jednotkový vektor směru = ({u_normovany[0]:.2f}, {u_normovany[1]:.2f})")
print(f"Směrová derivace v bodě P ve směru u: {smerova_der:.2f}\n")

# -----------------------------------------------------------------------------

# 4) Zjisti, kterym smerem je nejvetsi sklon a jaka je jeho hodnota (tj. smerova derivace)

smer = gradient_v_bode # smer stoupani je smer gradientu
delka_smer = np.linalg.norm(smer) # velikost (norma) sklonu/gradientu

# vysledek
print(f"Směr největšího stoupání (Gradient) je s = ({smer[0]:.2f}, {smer[1]:.2f}) a jeho velikost je {delka_smer:.4f}, tedy {delka_smer * 100:.2f} %")

# ------------------------------------------------------------------------------------

# 5) Graf funkce s vrstevnicemi, 

plt.figure(figsize=(10,10)) # rozmery

# a) vrstevnice - cary se stejnou hodnotou (z))
vrstevnice = plt.contour(X, Y, Z, levels=20, cmap='Greens', alpha=0.6)
plt.clabel(vrstevnice, inline=True, fontsize=8) # Popisky výšek u vrstevnic

# b) zvyrazneny bod
plt.scatter(Px, Py, color='Green', s=150, zorder=5, label=r'Bod P ($\pi$, $\pi/2$)')
# c) zadany vektor
plt.quiver(Px, Py, u_normovany[0], u_normovany[1], 
           color='orange', scale=5, zorder=4, label='Zadaný směr $u$')

# d) nejvetsi gradient
grad_unit = gradient_v_bode / delka_smer

plt.quiver(Px, Py, grad_unit[0], grad_unit[1], 
           color='red', scale=5, zorder=4, label='Směr největšího stoupání (Gradient)')

# e) osy 
plt.axhline(Py, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)
plt.axvline(Px, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)

plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.grid(True, linestyle=':', alpha=0.4)
plt.title(r'Analýza gradientu a směrové derivace v bodě $P$', fontsize=12, pad=15)
plt.legend(loc='upper right')

# ---------------------------------------------------------

# 6) 3D graf
fig_3d = plt.figure(figsize=(12, 9))
ax_3d = fig_3d.add_subplot(111, projection='3d')

# povrch
povrch = ax_3d.plot_surface(X, Y, Z, cmap='ocean', edgecolor='none', alpha=0.7, zorder=1)

# vyska
Pz = function(Px, Py)

# a) zobrazeni bodu
ax_3d.scatter([Px], [Py], [Pz], color='Green', s=150, zorder=10, label='Bod P na povrchu')

dist = 0.5

# b) zadany smer
dx_u = u_normovany[0] * dist
dy_u = u_normovany[1] * dist
dz_u = smerova_der * dist

ax_3d.quiver(Px, Py, Pz, dx_u, dy_u, dz_u, 
             color='orange', linewidth=3, arrow_length_ratio=0.3, zorder=5, label='Zadaný směr $u$')

# Souranice bodu D - ve smeru
Dx, Dy, Dz = Px + dx_u, Py + dy_u, Pz + dz_u

ax_3d.scatter([Dx], [Dy], [Dz], color='orange', s=100, zorder=10, 
             label=f'Cílový bod D ve směru u [{Dx:.2f}, {Dy:.2f}, {Dz:.2f}]')

# c) Nejvetsi stoupani / nejvetsi snizovani, podle jeho vlastni delky
dx_g = grad_unit[0] * dist
dy_g = grad_unit[1] * dist
dz_g = delka_smer * dist

ax_3d.quiver(Px, Py, Pz, dx_g, dy_g, dz_g, 
             color='red', linewidth=3, arrow_length_ratio=0.3, zorder=5, label='Směr největšího stoupání')

# bod M - maximalni
Mx, My, Mz = Px + dx_g, Py + dy_g, Pz + dz_g

ax_3d.scatter([Mx], [My], [Mz], color='red', s=100, zorder=10, 
             label=f'Bod M - max. stoupání [{Mx:.2f}, {My:.2f}, {Mz:.2f}]')


# vizualizace
ax_3d.set_title('Prostorový 3D pohled na gradient a sklony v bodě $P$', fontsize=13, pad=15)
ax_3d.set_xlabel('Osa X')
ax_3d.set_ylabel('Osa Y')
ax_3d.set_zlabel('Osa Z (Výška)')

ax_3d.grid(True, linestyle=':', alpha=0.4)
ax_3d.legend()

plt.show()
