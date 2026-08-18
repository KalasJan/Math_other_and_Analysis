# Funkce f je dana parametricky. Vykreslete ji a najdete derivaci
# x = e**t, y = e**(-2*t)

import numpy as np
import matplotlib.pyplot as plt
import sympy as sm

t = sm.symbols('t')
x, y = sm.symbols('x y', positive=True)

# Soustava parametrických rovnic
ox = sm.sin(t)
oy = sm.cos(t)

# prevod do explicitního tvaru
t_solve = sm.solve(sm.Eq(ox, x), t)[0] # (ox = x)
explicitni_tvar = sm.simplify(sm.Abs(oy.subs(t, t_solve))) # t se dosadi do oy

print(f"Explicitní tvar funkce je: y = {explicitni_tvar}")

# derivace
dx_dt = sm.diff(ox, t)
dy_dt = sm.diff(oy, t)
derivace_sym = dy_dt / dx_dt

derivace_sym = sm.simplify(derivace_sym)
print(f"Symbolická derivace dy/dx = (dy/dt) / (dx/dt) = {derivace_sym}")

# kresleni
fx = sm.lambdify(t, ox, 'numpy')
fy = sm.lambdify(t, oy, 'numpy')
f_derivace = sm.lambdify(t, derivace_sym, 'numpy')

rozsah = np.linspace(-1, 1, 1000)

osa_x = fx(rozsah)
osa_y = fy(rozsah)
der = f_derivace(rozsah)

if np.isscalar(der) or np.ndim(der) == 0:
    der = np.full_like(osa_x, der)

fig = plt.figure(figsize=(14, 6), layout='constrained')

axp = fig.add_subplot(121) # Graf původní funkce
axd = fig.add_subplot(122) # Graf derivace

axp.plot(osa_x, osa_y, color='midnightblue', linewidth=2.5, label='Původní funkce parametricky')
axp.plot(osa_x, osa_y, color='lime', linestyle = '--', linewidth=2.5, label='Původní funkce explicitně')
axp.set_xlabel("x")
axp.set_ylabel("y")
axp.set_title(rf'Graf funkce $x = {sm.latex(ox)}, y = {sm.latex(oy)}$ => explicitně: $y = {sm.latex(explicitni_tvar)}$', fontsize=11)
axp.grid(True, linestyle=':', alpha=0.6)
axp.legend()

axd.plot(osa_x, der, color='crimson', linewidth=2.5, label='Derivace funkce')
axd.set_xlabel("x")
axd.set_ylabel("dy/dx")
axd.set_title(rf'Graf derivace $\frac{{dy}}{{dx}} = {sm.latex(derivace_sym)}$', fontsize=11)
axd.grid(True, linestyle=':', alpha=0.6)
axd.legend()

plt.suptitle('Parametrická funkce a její první derivace', fontsize=14, weight='bold')
plt.show()
