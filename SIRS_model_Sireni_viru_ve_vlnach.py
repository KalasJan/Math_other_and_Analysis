# Matematická simulace epidemie pomocí nelineárního dynamického systému SIR
# S = zdravi, kteri se mohou nakazit
# I = v moment nakazeni
# R = uzdraveni (maji imunitu) nebo zemreli
# Vše v jednom grafu pro přímé srovnání časového posunu a výšky vln

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Definice soustavy diferenciálních rovnic SIR
def sir_model(t, state, gamma, N):
    S, I, R = state
    
    if t < 50:
        beta = 0.35   # Vlna 1 - šíření
    elif t < 100:
        beta = 0.08   # Lockdown 1
    elif t < 140:
        beta = 0.28   # Rozvolnění, vlna 2
    elif t < 200:
        beta = 0.10   # Lockdown 2
    elif t < 220:
        beta = 0.40   # rozjezd vlny 3 
    else:
        beta = 0.05   # mutace viru, vlna 3
    
    # presun z R do S
    # ztrata imunity po 180 dnech, o 2 %
    om = 0.02 if t >= 180 else 0 
    
    dS_dt = -beta * S * I / N + om * R # pocet zdravych muze jen klesat (podle setkavani s nakazenymi)
    dI_dt = beta * S * I / N - gamma * I # + rust nakazenych, - uzdraveni nebo zemreli
    dR_dt = gamma * I - om * R # rust uzdraenych
    return [dS_dt, dI_dt, dR_dt]

# 2. Počáteční podmínky
N = 10**6    # Celková populace
I0 = 1          # 1 nakažený pacient na začátku
R0 = 0          # Nikdo nemá imunitu
S0 = N - I0 - R0 # pocet zdravych

pocatecni_stav = [S0, I0, R0]
den0 = 0
den_last = 300
casovy_rozsah = (den0, den_last) # Sledujeme vývoj po dobu den_last dnů
t_eval = np.linspace(den0, den_last, 1000)

# 3. Parametry viru (nemoc trvá průměrně 7 dní)
gamma = 1.0 / 10.0 

# faze
reseni = solve_ivp(sir_model, casovy_rozsah, pocatecni_stav, 
                         args=(gamma, N), t_eval=t_eval)


# Vytáhnutí pouze křivek NEMOCNÝCH (index 1 v poli y)
I_volny = reseni.y[1]
max_I_volny = np.max(I_volny)
den_max_volny = reseni.t[np.argmax(I_volny)] # globalni maximum

# ====================================================================
# 4. Graf

plt.figure(figsize=(12, 7))

# Vykreslení obou vln podle tvého zadání barev (volný = zeleně, zploštělá = červeně)
plt.plot(reseni.t, I_volny, color='navy', linewidth=2.5, 
         label=rf'Vývoj epidemie ve vlnách [Globální Max: {den_max_volny:.0f}. den]')

# globální maximum
plt.scatter([den_max_volny], [max_I_volny], color='black', s=80, zorder=5)
plt.axvline(den_max_volny, color='red', linestyle=':', alpha=0.6)

# změny parametrů beta
plt.axvline(50, color='red', linestyle='--', alpha=0.5)
plt.axvline(100, color='green', linestyle='--', alpha=0.5)
plt.axvline(140, color='red', linestyle='--', alpha=0.5)
plt.axvline(200, color='green', linestyle='--', alpha=0.5)
plt.axvline(220, color='red', linestyle='--', alpha=0.5)

# vizualizace
plt.title('Model šíření viru se změnami opatření a mutacemi (SIRS model)', fontsize=14, pad=15, weight='bold')
plt.xlabel('Čas od začátku epidemie (Dny)', fontsize=11)
plt.ylabel('Aktuálně nemocní lidé [v tisících]', fontsize=11)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{int(x/1000)}"))

plt.xlim(den0, den_last)
plt.ylim(0, max_I_volny * 1.1)
plt.grid(True, linestyle=':', alpha=0.6)

# Přehledná legenda
plt.legend(fontsize=11, frameon=True, shadow=True)
plt.show()