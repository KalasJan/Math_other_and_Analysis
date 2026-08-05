# Najdi extremy funkce f(x,y) = x**3 - 3*x + y**3 -3*y
# obecne
# na vazebni podmince g(x,y) = x**2 + y**2 - 4

import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

# 1) primo na 2 promenne

# definice promennych
x_ex, y_ex, lam = sm.symbols('x y lambda')

# definice funkce
f_xy = x_ex**3 - 3*x_ex + y_ex**3 -3*y_ex

# parcialni derivace
dx = sm.diff(f_xy, x_ex)
dy = sm.diff(f_xy, y_ex)

# kriticke body (dx = 0, dy = 0)
potencial = sm.solve([dx, dy], (x_ex, y_ex), dict=True)

# mame body podezrele, chceme druhe derivace
print("--- 1) RUČNÍ ANALÝZA (PRO 2 PROMĚNNÉ) ---")
for body in potencial:
    bx = float(body[x_ex])
    by = float(body[y_ex])
    
    # druhe derivace
    d_xx = sm.diff(dx, x_ex).subs({x_ex: bx, y_ex: by})
    d_yy = sm.diff(dy, y_ex).subs({x_ex: bx, y_ex: by})
    d_xy = sm.diff(dx, y_ex).subs({x_ex: bx, y_ex: by}) 
    d_yx = sm.diff(dy, x_ex).subs({x_ex: bx, y_ex: by})
    
    # determinant Hessovy matice (pro 2 promenne)
    DH = float(d_xx * d_yy - d_xy * d_yx)
    
    # rozhodnuti
    if DH > 0 and d_xx > 0:
        typ = "Lokální minimum"
    elif DH > 0 and d_xx < 0:
        typ = "Lokální maximum"
    elif DH < 0:
        typ = "Sedlový bod"
    else:
        typ = "Nerozhodnutelný bod"
        
    print(f"Bod P({bx:.1f}, {by:.1f}) -> Hessian: {DH:.1f} -> Typ: {typ}")
    
# =========================================================================

# 2) obecne pres hessian (i vice promennych)

# definice promennych (x_ex, y_ex)
# funkce (f_xy)
# parcialni derivace (dx, dy) 

hessian = sm.hessian(f_xy, (x_ex, y_ex)) # Hessova matice

# body podezrele z extremu mame (potencial)
print("\n--- 2) MATICOVÁ ANALÝZA (I PRO VÍCE PROMĚNNÝCH) ---")
for bod in potencial:
    bod_x = float(bod[x_ex])
    bod_y = float(bod[y_ex])
    
    hodnota_bodu = hessian.subs({x_ex: bod_x, y_ex: bod_y})
    
    DH2 = float(hodnota_bodu.det()) # Hessian
    d_xx_pot = float(hodnota_bodu[0,0]) # prvni prvek Hessovy matice
    
    # klasifikace
    if DH2 > 0 and d_xx_pot > 0:
        typ2 = "Lokální minimum"
    elif DH2 > 0 and d_xx_pot < 0:
        typ2 = "Lokální maximum"
    elif DH2 < 0:
        typ2 = "Sedlový bod"
    else:
        typ2 = "Nerozhodnutelný bod"
        
    print(f"Bod P({bod_x:.1f}, {bod_y:.1f}) -> Hessián: {DH2:.1f} -> Typ: {typ2}")
    
# ===============================================================================

# 3) Vázané extrémy na funkci g(x,y)

# definice promennych (x_ex, y_ex)
# funkce (f_xy)

g_xy = x_ex**2 + y_ex**2 - 4 # vazebni podminka

L_xy = f_xy + lam * g_xy # Lagrangeova funkce

# parcialni derivace Lagrange
dLx = sm.diff(L_xy, x_ex)
dLy = sm.diff(L_xy, y_ex)
dLlam = sm.diff(L_xy, lam) # vazba g(x,y) = x**2 + y**2 - 4

dgx = sm.diff(g_xy, x_ex)
dgy = sm.diff(g_xy, y_ex)

# soustava rovnic (dL = 0)
vazane = sm.solve([dLx, dLy, dLlam], (x_ex, y_ex, lam), dict=True)

# Verze Hessovy matice pro Vazane extremy
H_rozsir = sm.Matrix([
    [0, dgx, dgy],
    [dgx, sm.diff(dLx, x_ex), sm.diff(dLx, y_ex)],
    [dgy, sm.diff(dLy, x_ex), sm.diff(dLy, y_ex)]
])


print("\n--- VÁZANÉ EXTRÉMY (NA PODMÍNCE) ---")
for bod in vazane: # budeme brat pouze realna reseni, nikoliv komplexni
    if bod[x_ex].is_real and bod[y_ex].is_real:
        bx = float(bod[x_ex].evalf())
        by = float(bod[y_ex].evalf())
        blam = float(bod[lam].evalf())
        
        # dosazeni bodu do matice a hejo hodnota
        hes_bodu = H_rozsir.subs({x_ex: bx, y_ex: by, lam: blam})
        det_vaz = float(hes_bodu.det())
        
        # Typ extremu
        if det_vaz > 0:
            typ_vaz = "Vázané maximum"
        elif det_vaz < 0:
            typ_vaz = "Vázané minimum"
        else:
            typ_vaz = "Sedlo / Nerozhodnutelné"
            
        print(f"Vázaný bod na podmínce: P({bx:.2f}, {by:.2f}) s lambda = {blam:.2f}-> Typ: {typ_vaz}")
        
# ==========================================================================

# 4) graf se zvyraznenim extemu

# mrizka
osa_x = np.linspace(-3, 3, 500)
osa_y = np.linspace(-3, 3, 500)
X,Y = np.meshgrid(osa_x, osa_y)
Z = X**3 - 3*X + Y**3 - 3*Y

# kruznice (vazebni funkce), parametricky
uhel = np.linspace(0, 2* np.pi, 500)
x_podm = 2 * np.cos(uhel)
y_podm = 2 * np.sin(uhel)
z_podm = x_podm**3 - 3*x_podm + y_podm**3 - 3*y_podm

# promitnuti
fig = plt.figure(figsize=(12, 10))
ax3d = fig.add_subplot(111, projection='3d')

ax3d.view_init(elev=25, azim=135)
               

# vykresleni funkce f(x,y)
ax3d.plot_surface(X, Y, Z, cmap='ocean', alpha=0.5, zorder=1)

# vykresleni vazby
ax3d.plot(x_podm, y_podm, z_podm, color='crimson', linewidth=3.5, 
          label='Vazební podmínka ($x^2+y^2=4$)', zorder=2)

# Volne extremy
legenda_volne = True
for bod in potencial:
    bx = float(bod[x_ex])
    by = float(bod[y_ex])
    bz = float(f_xy.subs({x_ex: bx, y_ex: by}))
    lbl = 'Volné extrémy (bez vazby)' if legenda_volne else ""
    ax3d.scatter(bx, by, bz, color='limegreen', s=150, edgecolors='black', zorder=5, label=lbl)
    legenda_volne = False
    
# vazane extremy
leg_max, leg_min = True, True
for bod in vazane:
    if bod[x_ex].is_real and bod[y_ex].is_real:
        bx = float(bod[x_ex].evalf())
        by = float(bod[y_ex].evalf())
        bz = float(f_xy.subs({x_ex: bx, y_ex: by}))
        blam = float(bod[lam].evalf())
        
        hes_bodu = H_rozsir.subs({x_ex: bx, y_ex: by, lam: blam})
        
        if float(hes_bodu.det()) > 0:
            lbl = 'Vázané maximum' if leg_max else ""
            ax3d.scatter(bx, by, bz, color='red', s=130, marker='^', edgecolors='black', zorder=6, label=lbl)
            leg_max = False
        else:
            lbl = 'Vázané minimum' if leg_min else ""
            ax3d.scatter(bx, by, bz, color='blue', s=130, marker='v', edgecolors='black', zorder=6, label=lbl)
            leg_min = False
            
# zobrazeni
ax3d.set_xlabel('Osa X')
ax3d.set_ylabel('Osa Y')
ax3d.set_zlabel('Osa Z (Výška)')
ax3d.set_title(r"Extrémy funkce $f(x,y) = x^3 - 3x + y^3 - 3y$ obecně nebo na vazbě $x^2+y^2=4$", 
             fontsize=13, pad=15)
ax3d.legend(loc='upper right')

plt.tight_layout()
plt.show()
