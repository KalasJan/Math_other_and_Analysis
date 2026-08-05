# Vykreslete Dirichletovu funkci

# f(x) = 1 pro racionalni, f(x) = 0 pro iracionalni

import numpy as np
import matplotlib.pyplot as plt

# bude to huste zobrazni
x_dirichlet = np.linspace(0, 4, 2000)

# skakani mezi 0 a 1
y_dirichlet = np.random.choice([0, 1], size=len(x_dirichlet))

# graf
plt.figure(figsize=(10, 6))

# graf jsou pouze "izolovane" body
plt.scatter(x_dirichlet, y_dirichlet, color='crimson', s=1, alpha=0.8)

plt.xlim(-0.2, 4.2)
plt.ylim(-0.2, 1.2)
plt.grid(True, linestyle=':', alpha=0.4)

plt.title('Dirichletova funkce $\\mathcal{D}(x)$ (všude nespojitá)', fontsize=13, pad=15)
plt.xlabel('x')
plt.ylabel('y (pouze hodnoty 0 (iracionální x) a 1 (racionální x))')

plt.show()