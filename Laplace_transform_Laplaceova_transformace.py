# Analyticke reseni Volterrovy rovnice (prevzata z DP)

# f(x) = f0*e^(-cx) + lam * int_{0}^{x} e^(-c*(x-y)) * f(y) dy
# kde c > 0, lam > 0

import sympy as sm

# definice vsech symbolu
# real, positive -> realna cisla
f0, c, lam, x, y = sm.symbols('f0 c \lambda x y', real = True, positive = True)
s = sm.symbols('s', real = True, positive = True)

# Jadro integralni rovnice
# L{e^(-cx)} = 1/(s+c)
L_kernel = 1/(s+c)

# rovnice po transormaci
F = sm.symbols('F')
rovnice = sm.Eq(F, f0 * L_kernel + lam * L_kernel * F)

print ("Řešení Volterrovy integralni rovnice")
print (f"Transformovaná rovnice v tzv. s-doméně je:\n {rovnice}")

# vyjadreni F(s)
F_vysledek = sm.solve(rovnice, F)[0]
F_prehledneji = sm.simplify(F_vysledek)

# navrat k feseni f(x) - zpetna Laplaceova transformace
f_reseni = sm.inverse_laplace_transform(F_prehledneji, s, x)

print (f"Řešení této rovnice je f(x) = {sm.simplify(f_reseni)}")