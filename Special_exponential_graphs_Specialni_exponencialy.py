# plot crazy functions
# f(x) = x**x and derivative
# f(x,y) = x**x + y**y and x**y + y**x

import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

x, y = sm.symbols('x y', real = True, positive = True) # x, y > 0
# 1) definition of functions
f = x**x
der = sm.diff(f, x) # derivative
f_same = x**x + y**y
f_dif = x**y + y**x

# Switch to numpy
f_num = sm.lambdify(x, f, 'numpy')
der_num = sm.lambdify(x, der, 'numpy')
f_same_num = sm.lambdify((x,y), f_same, 'numpy')
f_dif_num = sm.lambdify((x,y), f_dif, 'numpy')

# plot the 2x2 graphs
fig = plt.figure(figsize=(14, 12))

x_val = np.linspace(0.1, 3, 500) # 2D graphs

x3 = np.linspace(0.1, 5, 500)
y3 = np.linspace(0.1, 5, 500)
X3, Y3 = np.meshgrid(x3, y3) # 3D graphs

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223, projection='3d')
ax4 = fig.add_subplot(224, projection='3d')

# titles
f_latex = sm.latex(f)
der_latex = sm.latex(der)
f_same_latex = sm.latex(f_same)
f_dif_latex = sm.latex(f_dif)

# f(x) = x**y
ax1.plot(x_val, f_num(x_val), color='crimson', linewidth=2)
ax1.set_title(rf'$f(x) = {f_latex}$',)
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.grid(True, linestyle=':')

# derivation of x**x
ax2.plot(x_val, der_num(x_val), color='navy', linewidth=2)
ax2.set_title(rf'$\frac{{d}}{{dx}}(x^x) = {der_latex}$')
ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')
ax2.grid(True, linestyle='--')

# f_same = x**x + y**y
Z_same = f_same_num(X3, Y3)
ax3.plot_surface(X3, Y3, Z_same, cmap='spring', edgecolor='none', alpha=0.8)
ax3.set_title(rf'$f(x,y) = {f_same_latex}$')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('f(x,y)')

# f_dif = x**y + y**x
Z_dif = f_dif_num(X3, Y3)
ax4.plot_surface(X3, Y3, Z_dif, cmap='ocean', edgecolor='none', alpha=0.8)
ax4.set_title(rf'$f(x,y) = {f_dif_latex}$')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('f(x,y)')


plt.suptitle('Special functions and their graph', fontsize=14)
plt.tight_layout()
plt.show()

