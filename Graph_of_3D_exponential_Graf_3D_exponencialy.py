# plot crazy functions
# f(x,y) = x**x + y**y and x**y + y**x

import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

x, y = sm.symbols('x y', real = True, positive = True) # x, y > 0

# interval
bet = 0.01
to = 1

# 1) definition of functions
f1 = x**x  + y**y
der1x = sm.diff(f1, x) # derivative
der1y = sm.diff(f1, y)

f2 = x**y + y**x
der2x = sm.diff(f2, x) # derivative
der2y = sm.diff(f2, y)

# Switch to numpy
f1_num = sm.lambdify((x,y), f1, 'numpy')
der1x_num = sm.lambdify((x,y), der1x, 'numpy')
der1y_num = sm.lambdify((x,y), der1y, 'numpy')

f2_num = sm.lambdify((x,y), f2, 'numpy')
der2x_num = sm.lambdify((x,y), der2x, 'numpy')
der2y_num = sm.lambdify((x,y), der2y, 'numpy')

# plot the 2 lines, 3 columns graphs
fig = plt.figure(figsize=(14, 12))

x3 = np.linspace(bet, to, 100)
y3 = np.linspace(bet, to, 100)
X3, Y3 = np.meshgrid(x3, y3) # 3D graphs

ax1 = fig.add_subplot(231, projection='3d')
ax2 = fig.add_subplot(232, projection='3d')
ax3 = fig.add_subplot(233, projection='3d') 

ax4 = fig.add_subplot(234, projection='3d') 
ax5 = fig.add_subplot(235, projection='3d') 
ax6 = fig.add_subplot(236, projection='3d')

# titles
f1_latex = sm.latex(f1)
der1x_latex = sm.latex(der1x)
der1y_latex = sm.latex(der1y)

f2_latex = sm.latex(f2)
der2x_latex = sm.latex(der2x)
der2y_latex = sm.latex(der2y)

# f1 = x**x + y**y
Z1 = f1_num(X3, Y3)
ax1.plot_surface(X3, Y3, Z1, cmap='cividis', edgecolor='none', alpha=0.8)
ax1.set_title(rf'$f_1(x,y) = {f1_latex}$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x,y)')

#  der f1 / dx
D1x = der1x_num(X3, Y3)
ax2.plot_surface(X3, Y3, D1x, cmap='cividis', edgecolor='none', alpha=0.8)
ax2.set_title(rf'$\frac{{\partial f_1}}{{\partial x}} = {sm.latex(der1x)}$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('f(x,y)')

# der f1 / dy
D1y = der1y_num(X3, Y3)
ax3.plot_surface(X3, Y3, D1y, cmap='cividis', edgecolor='none', alpha=0.8)
ax3.set_title(rf'$\frac{{\partial f_1}}{{\partial y}} = {sm.latex(der1y)}$')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('f(x,y)')

# f2 = x**y + y**x
Z2 = f2_num(X3, Y3)
ax4.plot_surface(X3, Y3, Z2, cmap='rainbow', edgecolor='none', alpha=0.8)
ax4.set_title(rf'$f_2(x,y) = {f2_latex}$')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('f(x,y)')

#  der f2 / dx
D2x = der2x_num(X3, Y3)
ax5.plot_surface(X3, Y3, D2x, cmap='rainbow', edgecolor='none', alpha=0.8)
ax5.set_title(rf'$\frac{{\partial f_2}}{{\partial x}} = {sm.latex(der2x)}$')
ax5.set_xlabel('x')
ax5.set_ylabel('y')
ax5.set_zlabel('f(x,y)')

# der f2 / dy
D2y = der2y_num(X3, Y3)
ax6.plot_surface(X3, Y3, D2y, cmap='rainbow', edgecolor='none', alpha=0.8)
ax6.set_title(rf'$\frac{{\partial f_2}}{{\partial y}} = {sm.latex(der2y)}$')
ax6.set_xlabel('x')
ax6.set_ylabel('y')
ax6.set_zlabel('f(x,y)')

plt.suptitle(rf'Special graph funciton on $[x,y]^2 \in [{bet},{to}]^2$', fontsize=14)
plt.tight_layout()
plt.show()

