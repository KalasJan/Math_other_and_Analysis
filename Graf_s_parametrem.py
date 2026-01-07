# vykresli y=x^(2/3)*0.9sin(kx)*sqrt(3-x^2)
# k in <0,100>
# (x,y) in <-2;2>^2

from numpy import sin, sqrt, errstate, linspace, power, isnan
import matplotlib.pyplot as mal

# Zadej hodnotu k
print('Zadej hodnoty parametru v rozmezí (0, 100): ')
try:
    k = float(input('k = '))
    if not (0 < k <= 100):
        raise ValueError("Hodnota k musí být v rozmezí (0, 100)!")
except ValueError as p:
    print(p)
    exit()

# Definice funkce
def f(x):
    with errstate(invalid='ignore'):  # Skryje warningy pro neplatné výpočty
        result = power(abs(x), 2/3) + 0.9 * sin(k * x) * sqrt(3 - x**2)
        # abs (x^2/3), 
        result[isnan(result)] = 0  # Nastaví NaN hodnoty na 0
    return result

# Rozsah osy x
ox = linspace(-1, 1, 500)  # Rozsah dle zadání
oy = f(ox)

# Samotný graf
mal.figure(figsize=(6, 6))
mal.plot(ox, oy, label=f'Graf funkce f(x) pro hodnotu k = {k}')
mal.axhline(0, color='gray', linestyle='--')  # osa x
mal.axvline(0, color='gray', linestyle='--')  # osa y
mal.xlabel('x')  # Popis osy x
mal.ylabel('f(x)')  # Popis osy y
mal.xlim(-5, 5)  #rozsah na ose x
mal.ylim(-1.5, 3)
mal.title(r'Graf funkce $f(x) = x^{2/3} + 0.9 \sin({k}x) \sqrt{3 - x^2}$')  # Jméno grafu
mal.legend()
mal.grid(True)
mal.show()
