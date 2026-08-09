# Matematická simulace epidemie pomocí nelineárního dynamického systému SIR
# S = zdravi, kteri se mohou nakazit
# I = v moment nakazeni
# R = uzdraveni (maji imunitu) nebo zemreli
# Vše v jednom grafu pro přímé srovnání časového posunu a výšky vln

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Definice soustavy diferenciálních rovnic SIR
def sir_model(t, state, beta, gamma, N):
    S, I, R = state
    dS_dt = -beta * S * I / N # pocet zdravych muze jen klesat (podle setkavani s nakazenymi)
    dI_dt = beta * S * I / N - gamma * I # + rust nakazenych, - uzdraveni nebo zemreli
    dR_dt = gamma * I # rust uzdraenych
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

# A: Volný průběh (beta = 0.3)
beta_volny = 0.3

R0_volny = beta_volny / gamma # koeficient nakazenosti, 1 clovek nakazi R0 dalsich

reseni_volny = solve_ivp(sir_model, casovy_rozsah, pocatecni_stav, 
                         args=(beta_volny, gamma, N), t_eval=t_eval)

# B: Zploštěná křivka (beta = 0.15)
beta_opatreni = 0.15

R0_opatreni = beta_opatreni / gamma

reseni_opatreni = solve_ivp(sir_model, casovy_rozsah, pocatecni_stav, 
                             args=(beta_opatreni, gamma, N), t_eval=t_eval)

# Vytáhnutí pouze křivek NEMOCNÝCH (index 1 v poli y)
I_volny = reseni_volny.y[1]
max_I_volny = np.max(I_volny)
den_max_volny = reseni_volny.t[np.argmax(I_volny)] # kdy je maximum, ktery den

I_opatreni = reseni_opatreni.y[1]
max_I_opatreni = np.max(I_opatreni)
den_max_opatreni = reseni_opatreni.t[np.argmax(I_opatreni)]

# ====================================================================
# 4. VYKRESLENÍ DO JEDNOHO RÁMEČKU

plt.figure(figsize=(12, 7))

# Vykreslení obou vln podle tvého zadání barev (volný = zeleně, zploštělá = červeně)
plt.plot(reseni_volny.t, I_volny, color='red', linewidth=2.5, 
         label=f'Volný průběh (Červená), $R_0 = {R0_volny:.2f}$ [Max: {den_max_volny:.0f}. den]')
plt.plot(reseni_opatreni.t, I_opatreni, color='green', linewidth=2.5, 
         label=f'Zploštělý průběh s opatřeními (Zelená), $R_0 = {R0_opatreni:.2f}$ [Max: {den_max_opatreni:.0f}. den]')

# DYNAMICKÉ ZVÝRAZNĚNÍ VRCHOLŮ A ODCHYLEK VE DNECH

# Vrchol 1: Volný průběh
max_I_volny = np.max(I_volny)
den_max_volny = reseni_volny.t[np.argmax(I_volny)]
plt.scatter([den_max_volny], [max_I_volny], color='black', s=80, zorder=5)
plt.axvline(den_max_volny, color='red', linestyle=':', alpha=0.6)

# Vrchol 2: Zploštělý průběh (s opatrenim)
max_I_opatreni = np.max(I_opatreni)
den_max_opatreni = reseni_opatreni.t[np.argmax(I_opatreni)]
plt.scatter([den_max_opatreni], [max_I_opatreni], color='black', s=80, zorder=5)
plt.axvline(den_max_opatreni, color='green', linestyle=':', alpha=0.6)

# Vizuální zvýraznění časového posunu (odchylky) mezi vrcholy
plt.annotate('', xy=(den_max_opatreni, max_I_opatreni + 1000), 
             xytext=(den_max_volny, max_I_opatreni + 1000),
             arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5))
odchylka_dni = den_max_opatreni - den_max_volny
plt.text((den_max_volny + den_max_opatreni)/2, max_I_opatreni + 1500, 
         f'Posun vrcholu o {odchylka_dni:.0f} dnů', 
         ha='center', fontsize=10, weight='bold')

# Vizuální nastavení grafu
plt.title('Přímé srovnání epidemiologických vln (Model SIR)', fontsize=14, pad=15, weight='bold')
plt.xlabel('Čas od začátku epidemie (Dny)', fontsize=11)
plt.ylabel('Aktuálně nemocní lidé [v tisících]', fontsize=11)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{int(x/1000)}"))
# 150 000 se prevede na 150

plt.xlim(den0, den_last)
plt.ylim(0, max_I_volny * 1.1)
plt.grid(True, linestyle=':', alpha=0.6)

# Přehledná legenda
plt.legend(loc='upper right', fontsize=11, frameon=True, shadow=True)
plt.show()
