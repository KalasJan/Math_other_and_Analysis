# je dana Fourierova rada:
# f(N, t) = 4/pi * sum (k= 0 to N-1) 1/(2k+1)*sin((2k+1)t)
# ilustracne N = [1, 3, 11, 50]

import numpy as np
import matplotlib.pyplot as plt

# 1) Definicni obor
t = np.linspace(-2 * np.pi, 2 * np.pi, 5000)

plt. figure (figsize = (16, 8))

# 2) idealni obdelnik 
ideal = np.sign(np.sin(t))
plt.plot(t, ideal, label='Ideální obdélník', color='black', linewidth=1.5, linestyle='--')

# 3) vybrane N
hodnoty_N = [1, 3, 11, 50]
colors = ['orange', 'green', 'magenta', 'blue']

#  4) vykresleni N
for N, colours in zip (hodnoty_N, colors):
    f_fourier = np.zeros_like(t) # zacatek jsou prazdne hodnoty
    
    for k in range (0, N):
        f_fourier += 1 / (2 * k + 1) * np.sin((2 * k + 1) * t)
        
    f_fourier = (4/np.pi) * f_fourier
    
    plt.plot(t, f_fourier, label=rf'Fourierova řada ($N = {N}$)', color=colours, linewidth=2)

# 5) samotny graf
plt.axhline(0, color='black', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='black', linewidth=0.8, alpha=0.5)
plt.xlim(- 2* np.pi, 2 * np.pi)
plt.ylim(-1.5, 1.5)

plt.title(rf'Aproximace obdélníkového signálu Fourierovou řadou $f_N(t) = \frac{{4}}{{\pi}} \cdot \sum_{{k = 0}}^{{N-1}} \frac{{1}}{{2k+1}} \cdot \sin((2k+1)t)$'
          , fontsize=14)
plt.xlabel('Čas (t)', fontsize=12)
plt.ylabel('f(t)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=10)

plt.show()