import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import math 
df = pd.read_csv("Santiago_Diaz_Pabon_Plot_and_Store_Rep_2.3.csv")
triceps = df ["R TRICEPS BRACHII: EMG 6"]
t = df['X[s]']
f = 2000
N = len(triceps)
biceps = df['R BICEPS BRACHII: EMG 5']
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
plt.title('analisis espectral de triceps ejercicio 2')


N3 = np.round(N1/2)
f3 = (f/2)*(np.arange(1,N3+1)/N3)
X3 = X1[0:int(N3)]
plt.subplot(2,1,2)
plt.plot(f3,X3)
plt.title('analisis espectral de biceps ejercicio 2')
plt.show()