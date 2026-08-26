# plot some types of non-convex set

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap # for the color of Moon

t = np.linspace(0, 2 * np.pi, 2000)

# 1) General

rg = 3 + 0.8 * np.cos(t) - 1.2 * np.sin(4*t)

# Cartesian
xg = rg * np.cos(t)
yg = rg * np.sin(t)

# =================================================
# 2) star, flower

rs = 3 + 0.8 * np.sin(5 * t)

# switch to Cartesian
xs = rs * np.cos(t)
ys = rs * np.sin(t)

#==================================================
# 3) Moon

xm = np.linspace(-4,4,2000)
ym = np.linspace(-4,4,2000)
XM, YM = np.meshgrid(xm, ym)

# moon
big = XM**2 + YM**2 <= 2**2
sma = (XM - 0.75)**2 + YM**2 <= 1.75**2
moon = big & (~sma)

# ===================================================
# 4) Limacon curve

a = 2
b1 = 3 # a/b <1
rl1 = a + b1 * np.cos(t)
xl1 = rl1 * np.cos(t)
yl1 = rl1 * np.sin(t)

b2 = 2 # a/b = 1
rl2 = a + b2 * np.cos(t)
xl2 = rl2 * np.cos(t)
yl2 = rl2 * np.sin(t)

b3 = 1.5 # 1< a/b < 2
rl3 = a + b3 * np.cos(t)
xl3 = rl3 * np.cos(t)
yl3 = rl3 * np.sin(t)

b4 = 0.5 # a/b > 2
rl4 = a + b4 * np.cos(t)
xl4 = rl4 * np.cos(t)
yl4 = rl4 * np.sin(t)

# =========================================================
# 5) Graphs
fig = plt.figure(figsize=(12, 9))

# 2 lines, 12 columns
gs = fig.add_gridspec(2, 12, hspace=0.3)

# upper
ax1 = fig.add_subplot(gs[0, 0:4])
ax2 = fig.add_subplot(gs[0, 4:8])
ax3 = fig.add_subplot(gs[0, 8:12])

# down
ax4 = fig.add_subplot(gs[1, 0:3])
ax5 = fig.add_subplot(gs[1, 3:6])
ax6 = fig.add_subplot(gs[1, 6:9])
ax7 = fig.add_subplot(gs[1, 9:12])

# General (1st)
ax1.fill(xg, yg, color='#78d64b', edgecolor='black', linewidth=2)
ax1.set_aspect('equal')
ax1.set_title('General non-convex set')
ax1.axis('off')

# Star/flower (2nd)
ax2.fill(xs, ys, color='crimson', edgecolor='black', linewidth=2)
ax2.set_aspect('equal')
ax2.set_title('Star / Flower')
ax2.axis('off')

# Moon (3rd)
# area of Moon
ax3.imshow(moon, extent=[-4, 4, -4, 4], origin='lower', cmap=ListedColormap(['none', 'orange']))

# border of Moon
ax3.contour(moon, levels=[0.5], extent=[-4, 4, -4, 4], origin='lower', colors='black', linewidths=2)

ax3.set_aspect('equal')
ax3.set_title('Moon')
ax3.axis('off')

# Down graphs

fig.text(0.5, 0.48, 'Limacon curve ($r = a + b \cdot \\cos\\varphi$)', ha='center', fontsize=14, fontweight='bold')


# Limacon (a/b<1) (4th)
ax4.fill(xl1, yl1, color = 'white', edgecolor='navy', linewidth=2)
ax4.set_aspect('equal')
ax4.set_title('$a/b<1$')
ax4.axis('off')

# Limacon (a/b = 1) (5th)
ax5.fill(xl2, yl2, color = 'white', edgecolor='navy', linewidth=2)
ax5.set_aspect('equal')
ax5.set_title('$a/b = 1$')
ax5.axis('off')

# Limacon (1< a/b < 2) (6th)
ax6.fill(xl3, yl3, color = 'white', edgecolor='navy', linewidth=2)
ax6.set_aspect('equal')
ax6.set_title('$1< a/b < 2$')
ax6.axis('off')

# Limacon (a/b > 2) (7th)
ax7.fill(xl4, yl4, color = 'white', edgecolor='navy', linewidth=2)
ax7.set_aspect('equal')
ax7.set_title('$a/b > 2$')
ax7.axis('off')
