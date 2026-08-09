# VYkreslete graf fce y = e^x (i s log měřítkem) 
# najdete tecnu v x = 8

import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

x = sm.symbols('x', real=True)
x0  = 8 # ve kterem bode chceme tecnu

f = sm.exp(x) #  funkce

der_f = sm.diff(f, x) # derivace
y0 = float(f.subs(x,x0))
k = float(der_f.subs(x, x0))

# numerika
f_num = sm.lambdify(x, f, 'numpy')
tecna = k * (x-x0) + y0
tecna_num = sm.lambdify(x, tecna, 'numpy')

# data na osy
x_val = np.linspace(0, 10, 500)
y_val = f_num(x_val)
y_tecna = tecna_num(x_val)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# 1) klasicke meritko (vlevo)
ax1.plot(x_val, y_val, color='blue', linewidth=2.5, label=f'Funkce ${sm.latex(f)}$')
ax1.plot(x_val, y_tecna, color='crimson', linestyle='--', linewidth=1.8, label=f'Tečna v bodě x={x0}')
ax1.scatter([x0], [y0], color='black', s=80, zorder=5, label=f'Bod dotyku [{x0}, {y0:.1f}]')

ax1.set_title('Klasické lineární měřítko', fontsize=12)
ax1.set_xlabel('Osa x')
ax1.set_ylabel('Osa y')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left')

# 2) logaritmicke meritko (vpravo)
ax2.plot(x_val, y_val, color='blue', linewidth=2.5, label=f'Funkce ${sm.latex(f)}$')
ax2.plot(x_val, y_tecna, color='crimson', linestyle='--', linewidth=1.8, label=f'Tečna v bodě x={x0}')
ax2.scatter([x0], [y0], color='black', s=80, zorder=5, label=f'Bod dotyku [{x0}, {y0:.1f}]')

# logaritmizace meritka
ax2.set_yscale('log')

ax2.set_title('Logaritmické měřítko osy Y', fontsize=12)
ax2.set_xlabel('Osa x')
ax2.set_ylabel('Osa y (Log)')
ax2.grid(True, which="both", linestyle=':', alpha=0.6) # which="both" vykreslí i pomocné logaritmické linky
ax2.legend(loc='upper left')

f_latex = sm.latex(f)
plt.suptitle(rf'Srovnání měřítek pro exponenciální funkci $f(x) = {f_latex}$', fontsize=14, weight='bold')
plt.tight_layout()
plt.show()