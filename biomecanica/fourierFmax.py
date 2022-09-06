import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import math 
df = pd.read_csv("Santiago_Diaz_Pabon_MVC_(EMG_RMS)_(1)_Rep_1.1.csv")
triceps = df ["R TRICEPS BRACHII: EMG 6"]
t = df['X[s]']
fs = 2000
N = len(triceps)

df1 = pd.read_csv("Santiago_Diaz_Pabon_MVC_(EMG_RMS)_Rep_1.0.csv")
biceps = df1 ["R BICEPS BRACHII: EMG 5"]
timepo1 = df1['X[s]']                 
f = 2000    
N1 = len(biceps)

#FFT
X = np.fft.fft(triceps)
X1 = np.fft.fft(biceps)
# Frequency vector (half!) 
N2 = np.round(N/2)
f2 = (f/2)*(np.arange(1,N2+1)/N2)
X2 = X[0:int(N2)]
plt.subplot(2,1,1)
plt.plot(f2,X2)
plt.title('analsis espectral fuerza maxima triceps')


N3 = np.round(N1/2)
f3 = (f/2)*(np.arange(1,N3+1)/N3)
X3 = X1[0:int(N3)]
plt.subplot(2,1,2)
plt.plot(f3,X3)
plt.title('analsis espectral fuerza maxima biceps')
plt.show()