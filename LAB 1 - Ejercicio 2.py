
'''
Exercici 2

Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que has creat (x_recuperat, fm = sf.read(‘nom_fitxer.wav’)

- Representa 5 períodes del senyal i la seva transformada. 

- Explica el resultat.

'''
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

from numpy.fft import fft 

x_recuperat, fm = sf.read('so_exemple2.wav')

T= 2.5 
N = 5000  
fx = 440 # Utilizada la de la introduccion
L = int(fm * T)
Tm = 1 / fm
t = Tm * np.arange(L)

Tx = 1 / fx
Ls = int(fm*5*Tx)
plt.figure(0)
plt.plot(t[0:Ls], x_recuperat[0:Ls])
plt.xlabel("t en segons")
plt.title("5 períodes de la sinusoide")
plt.show()

X = fft(x_recuperat[0:Ls],N)

k=np.arange(N)
plt.figure(1)
plt.subplot(211)
plt.plot(k,abs(X))
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')
plt.ylabel('|X[k]|')
plt.subplot(212)
plt.plot(k,np.unwrap(np.angle(X)))
plt.xlabel('Index k')
plt.ylabel('$\phi_x[k]$')
plt.show() 
