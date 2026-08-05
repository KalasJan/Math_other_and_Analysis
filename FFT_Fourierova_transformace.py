# Analyza Rychle Fourierovy transformace (FFT)

import numpy as np
import matplotlib.pyplot as plt

# 1) celkovy signal
Fs = 1000 #vzorek

sec = 1
t = np.linspace(0, sec, int(Fs * sec), endpoint=False) # casova osa (vzdy po sec)

# kombinace signalu
f1 = 120
f2 = 30
cisty = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# ruseni
ruch = np.random.normal(0, 2, len(t))
total_ruseni = cisty + ruch

# ==============================================

# 2) Vypocet FFT
FFT_result = np.fft.fft(total_ruseni)
frekvence = np.fft.fftfreq(len(t), 1/Fs)

# pouze "kladny cas" -> nejdeme do zaporu
amplituda = np.abs(FFT_result) / len(t)
kladne = frekvence >= 0
frekvence_vysledek = frekvence[kladne]
amplituda_vysledek = amplituda[kladne] * 2

# ===================================================

# 3) vizualizace

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), layout='constrained')

# Levo - čas, celkový ruch
ax1.plot(t, total_ruseni, color='gray', alpha=0.6, label='Celkový ruch')
ax1.plot(t, cisty, color='black', linewidth=2, label='Čistý trend')
ax1.set_xlabel('Čas (s)', fontsize=11)
ax1.set_ylabel('Amplituda', fontsize=11)
ax1.set_title('Časová doména: celkový ruch', fontsize=12)
ax1.axhline(0, color='gray', linewidth=1.2, linestyle=':', alpha=0.4)
ax1.grid(True, linestyle=':', alpha=0.4)
ax1.legend(loc='upper right')

# Pravo - frekvence, rozpadnuti na f1 a f2
ax2.stem(frekvence_vysledek, amplituda_vysledek, linefmt='crimson', markerfmt='ro', basefmt=' ')
ax2.set_xlim(0, 200)
ax2.set_xlabel('Frekvence (Hz)', fontsize=11)
ax2.set_ylabel('Výkon, Amplitua, Výchylka', fontsize=11)
ax2.set_title('Frekvenční doména: Výsledek Fourierovy transformace', fontsize=12)
ax2.grid(True, linestyle=':', alpha=0.4)

plt.suptitle('Analýza časových řad: Detekce skrytých period pomocí FFT', fontsize=14, weight='bold')
plt.show()