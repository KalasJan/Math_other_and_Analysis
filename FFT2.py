# Analyza Rychle Fourierovy transformace (FFT)

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# 1) celkovy signal
Fs = 1500 #vzorek

sec = 1
t = np.linspace(0, sec, int(Fs * sec), endpoint=False) # casova osa (vzdy po sec)

# kombinace signalu (max Fs/2)
f1 = 500
f2 = 30
#cisty = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
cisty = np.where(t < (sec/2), np.sin(2 * np.pi * f2 * t), np.sin(2 * np.pi * f1 * t))

# ruseni
ruch = np.random.normal(0, 1.5, len(t))
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

# ================================================

# 3) Spektrogram (kdy doslo k vychylce)
frekvence_spektr, cas_spektr, Sxx = spectrogram(total_ruseni, fs=Fs, nperseg=128, noverlap=110)
Sxx_dB = 10 * np.log10(Sxx + (1e-10))

vmax_auto = np.max(Sxx_dB)
vmin_auto = np.percentile(Sxx_dB, 30) # Ponoří spodních 30% šumu do černo-fialové tmy

# ===================================================

# 3) vizualizace
fig = plt.figure(figsize=(16, 9))

# vytvorime matici grafu
gs = fig.add_gridspec(4, 4, hspace=0.6, wspace=0.3)

ax_cas = fig.add_subplot(gs[0, 0:3]) # Horní široký (Amplituda na case)
ax_spektr = fig.add_subplot(gs[1:4, 0:3], sharex=ax_cas) # Centrální velký (Spektrogram, frekvence na case)
ax_fft = fig.add_subplot(gs[1:4, 3], sharey=ax_spektr)    # Pravý vysoký (Amplituda na frekvenci)

# Amlituda na case
ax_cas.plot(t, total_ruseni, color='gray', alpha=0.5, label='Celkový ruch')
ax_cas.plot(t, cisty, color='black', linewidth=1.8, label='Čistý trend')
ax_cas.axvline(sec/2, color='crimson', linestyle='--', linewidth=1.5)
ax_cas.axhline(0, color='gray', linewidth=0.8, linestyle='--', alpha=0.4)
ax_cas.set_ylabel('Amplituda', fontsize=10)
ax_cas.set_title('1) Amplituda v čase', fontsize=11, loc='left')
ax_cas.grid(True, linestyle=':', alpha=0.4)
ax_cas.legend(bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=9)

# Spektrogram, frekvence na case
pcm = ax_spektr.pcolormesh(cas_spektr, frekvence_spektr, Sxx_dB,
                           shading='gouraud', cmap='magma',
                           vmin=vmin_auto, vmax=vmax_auto)
ax_spektr.set_ylim(0.5 * min(f1, f2), max(f1, f2)*1.5) # Omezíme pohled na klíčové frekvence (o něco víc než je f_max)
ax_spektr.set_xlabel('Čas (s)', fontsize=11)
ax_spektr.set_ylabel('Frekvence (Hz)', fontsize=11)
ax_spektr.set_title('2) Spektrogram, závislost frekvence na čase', fontsize=11, loc='left')
ax_spektr.grid(True, linestyle=':', alpha=0.3, color='white')

# Amplituda na frekvenci
# otoceno o 90 st (prohozeni x,y)
ax_fft.stem(frekvence_vysledek, amplituda_vysledek, linefmt='crimson', markerfmt='ro', basefmt=' ', orientation='horizontal')
ax_fft.set_xlim(0, np.max(amplituda_vysledek) + 0.2)
ax_fft.set_xlabel('Výkon / Amplituda', fontsize=10)
ax_fft.set_ylabel('Frekvence (Hz)', fontsize=10)

ax_fft.tick_params(labelleft=False) 
ax_fft.set_title('3) Globální FFT', fontsize=11, loc='left')
ax_fft.grid(True, linestyle=':', alpha=0.4)

# zvyrazneni intenzity
cbar = fig.colorbar(pcm, ax=ax_fft, orientation='horizontal', pad=0.15)
cbar.set_label('Energie tónu (dB)', fontsize=9)

# titulek
plt.suptitle('Analýza Fourierovy transformace', fontsize=14, weight='bold', y=0.96)
plt.show()