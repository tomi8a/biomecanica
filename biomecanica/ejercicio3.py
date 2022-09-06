import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt 


df = pd.read_csv("Santiago_Diaz_Pabon_Plot_and_Store_Rep_4.5.csv")
triceps = df ["R TRICEPS BRACHII: EMG 6"]
biceps = df['R BICEPS BRACHII: EMG 5']
fs = 2000
plt.subplot(2,1,1)
plt.plot(triceps)
plt.title('triceps ej 3')
plt.subplot(2,1,2)
plt.plot(biceps)
plt.title('biceps ej 3')
plt.show()
#rectificado
rectificatri = np.abs(triceps)
rectificabi = np.abs(biceps)
#normalizado
normal_array = rectificatri - np.min(rectificatri) / np.max(rectificatri)-np.min(rectificatri)
normal_array1 = rectificabi - np.min(rectificabi) / np.max(rectificabi)-np.min(rectificabi)
 
plt.plot(normal_array,'r')
plt.plot(normal_array1,'m')
plt.title('tricep(rojo) y bicep(magenta) en el tercer  ejercicio')
plt.show()
#rms del tricep
wn = 3/(fs/2)
b,a = signal.butter(5, wn, btype='lowpass')
sig = signal.filtfilt(b,a,normal_array)
# rms del bicep
wn = 3/(fs/2)
b,a = signal.butter(5, wn, btype='lowpass')
sig1 = signal.filtfilt(b,a,normal_array1)
plt.plot(sig,'r')
plt.plot(sig1,'m')
plt.title('rms de los musculos en el ejercicio 3')
plt.show()