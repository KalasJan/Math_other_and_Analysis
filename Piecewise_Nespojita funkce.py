# Vykreslete Nespojitou funkci (Piecewise)

# f(x) = x**2 (x<2) and sin(x) (x=>2)

import numpy as np
import matplotlib.pyplot as plt

# bod "zlomeni" je x = 2
bod_zlomu = 2
x1 = np.linspace(-3, 1.99, 300)
x2 = np.linspace(2, 20, 300)

# definice funkce
f1 = lambda x: x ** 2
f2 = lambda x: np.sin(x)

y1 = f1(x1)
y2 = f2(x2)


plt.figure(figsize=(10, 6))

#vykresleni obou vetvi
plt.plot(x1, y1, color='blue', linewidth=2.5, label=rf'Větev $x^2$ ($x < {bod_zlomu}$)')
plt.plot(x2, y2, color='green', linewidth=2.5, label=rf'Větev $\sin(x)$ ($x \geq {bod_zlomu}$)')

# zvyrazneni nespojitosti
plt.scatter([bod_zlomu], [f1(bod_zlomu)], facecolors='none', edgecolors='blue', s=80, zorder=5, label='Limita zleva (neobsahuje bod)')
plt.scatter([bod_zlomu], [f2(bod_zlomu)], color='green', s=80, zorder=5, label=r'Hodnota v bodě (obsahuje bod)')

# vizual
plt.axvline(bod_zlomu, color='black', linewidth=0.8, alpha=0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.title('Standardní nespojitá dělená funkce', fontsize=13, pad=15)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()