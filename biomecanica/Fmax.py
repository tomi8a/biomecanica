import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt 


df = pd.read_csv("Santiago_Diaz_Pabon_MVC_(EMG_RMS)_(1)_Rep_1.1.csv")
triceps = df ["R TRICEPS BRACHII: EMG 6"]
timepo = df['X[s]']
fs = 2000

df1 = pd.read_csv("Santiago_Diaz_Pabon_MVC_(EMG_RMS)_Rep_1.0.csv")
biceps = df1 ["R BICEPS BRACHII: EMG 5"]
timepo1 = df1['X[s]']
#rectificado
rectificatri = np.abs(triceps)
rectificabi = np.abs(biceps)
#normalizado
# norm = np.linalg.norm(rectificatri)
# normal_array = rectificatri/norm
# norm1 = np.linalg.norm(rectificabi)
# normal_array1 = rectificabi/norm1
normal_array = rectificatri - np.mean(rectificatri) 
normal_array1 = rectificabi - np.mean(rectificabi)
 
# plt.subplot(2,1,1) #fila. columna, posicion
# # fuerza maxima del tricep 
# plt.plot(timepo,normal_array)
# plt.title("fuerza maxima del tricep respecto al tiempo normalizada")
# plt.tight_layout()

# plt.subplot(2,1,2)
# # fuerza maxima del bicep
# plt.plot(timepo1,normal_array1)
# plt.title("fuerza maxima del bicep respecto al tiempo normalizada")
# plt.tight_layout()
# plt.show()
#rms del tricep
wn = 3/(fs/2)
b,a = signal.butter(5, wn, btype='lowpass')
sig = signal.filtfilt(b,a,normal_array)
plt.subplot(2,1,1)
plt.plot(normal_array)
plt.title('fuerza maxima del tricep normalizado')
plt.subplot(2,1,2)
plt.plot(sig)
plt.title('rms de lafuerza maxima del tricep normalizado')
plt.show()

#rms del bicep
wn = 3/(fs/2)
b,a = signal.butter(5, wn, btype='lowpass')
sig1 = signal.filtfilt(b,a,normal_array1)
plt.subplot(2,1,1)
plt.plot(normal_array1)
plt.title('fuerza maxima del bicep normalizado')
plt.subplot(2,1,2)
plt.plot(sig1)
plt.title('rms de fuerza maxima del bicep normalizado')
plt.show()


