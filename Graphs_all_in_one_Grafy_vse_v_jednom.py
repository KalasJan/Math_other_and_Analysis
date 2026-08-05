# # Je dana funkce f(x)
# nakreslete jeji graf, graf derivace, integral (pro C = random) a derivaci v bode

import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

# definice promenne
x = sm.symbols('x', real = True, positive = True) # positive kvuli logaritmu

# ================================================
# 1) analytika

# definice funkce
f = sm.exp(x) * sm.sin(x**2)

# derivace
der = sm.diff(f, x)

# integral
C = np.random.randint(-5, 5) # integracni konstanta
integral_pure = None
integral = None

try:
    integral_res = sm.integrate(f, x)
    # Kontrola, zda SymPy nevrátil nevyhodnocený integrál (sm.Integral)
    if not isinstance(integral_res, sm.Integral) and "Integral" not in str(type(integral_res)):
        integral_pure = integral_res
        integral = integral_pure + C
except:
    integral_pure = None
    integral = None


# derivace v bode
bod_x = np.random.randint(1, 4)
bod_y = float(f.subs({x: bod_x}).evalf())
der_bod = float(der.subs({x: bod_x}).evalf())

sklon_rad = float(sm.atan(der_bod).evalf())
sklon_deg = np.degrees(sklon_rad)

podil_pi = sm.nsimplify(sm.atan(der_bod) / sm.pi, tolerance=0.01)
if podil_pi == 0:
    pi_text = "0"
elif podil_pi == 1:
    pi_text = "pi"
else:
    pi_text = f"{podil_pi}*pi"

# # specialni limity
# lim_fce = sm.limit (f, x, 0, dir='+')
# print(f" limita x -> 0+ f(x) je {lim_fce}")

# lim_der = sm.limit (der, x, 0, dir='+')
# print(f" limita x -> 0+ f'(x) je {lim_der}")

# lim_der_inf = sm.limit (der, x, sm.oo)
# print(f" limita x -> oo f'(x) je {lim_der_inf}")


# analyticky vystup
print(f" Původní funkce f(x) = {sm.nsimplify(f)}")
print(f" Derivace f'(x) = {sm.nsimplify(der)}")

if integral_pure is not None:
    print(f" Integrál F(x) + C   = {sm.nsimplify(integral_pure)} + ({C})")
else:
    print(" Integrál F(x) + C   = Nelze analyticky vyjádřit!")
    
print(f" Derivace v bodě je f'(x = {bod_x}) = {der_bod:.2f}, sklon (phi) je = {sklon_deg:.1f}° = {sklon_rad:.2f} rad ({pi_text})")

# ===========================================================

# 2) prevod SM do NP
f_num = sm.lambdify(x, f, 'numpy')
der_num = sm.lambdify(x, der, 'numpy')
integral_num = None
if integral is not None:
    integral_num = sm.lambdify(x, integral, 'numpy')

# ====================================================================

# 3 vykresleni

x_graph = np.linspace(0.1, 5, 5000)
plt.figure(figsize = (10, 7))

# pouze krivky
plt.plot(x_graph, f_num(x_graph), 
         label=f'$f(x)$', color='blue', linewidth=2.5)

plt.plot(x_graph, der_num(x_graph), label=f"Derivace $f'(x)$", color='orange', linestyle='--', linewidth=2)

if integral_num is not None:
    c_sgn = f"+ {C}" if C >= 0 else f"- {abs(C)}"
    plt.plot(x_graph, integral_num(x_graph), label=f"Integrál $F(x) {c_sgn}$", color='green', linestyle='-.', linewidth=2)
    
# tecna, y = f'(x0) * (x - x0) + y0
tangent = der_bod * (x_graph - bod_x) + bod_y
plt.plot(x_graph, tangent, 
         label=rf"Tečna v $x={bod_x}$ ($\varphi={sklon_deg:.1f}^\circ$)", 
         color='red', linestyle=':', linewidth=2)

# bod dotyku
plt.scatter([bod_x], [bod_y], color='red', s=50, zorder=5)

# osy a vizual
plt.axhline(0, color='black', linewidth=0.8, alpha=0.7)
plt.axvline(0, color='black', linewidth=0.8, alpha=0.7)
plt.xlim(0, 5)
plt.ylim(-1000, 1000)

plt.title('Funkce, jeji derivace, integral i tečna v bodě', fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=10)

plt.show()
