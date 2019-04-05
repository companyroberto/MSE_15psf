# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:56:20 2019

@author: Roberto

sino poner esto en cada script, pero también desde herramientas->consola que los graficos afuera
%matplotlib qt5
%matplotlib inline

https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.square.html

"""

#libreria numerica
import numpy as np

#libreria de impresión
import matplotlib.pyplot as plt

#
import scipy.fftpack as sc
import scipy.signal as sg

#Para usar en las muestras, utilizar multiplos de 2 (al ser iguales la resolución es 1)
N    = 1024   #muestras
Fs   = 1024   #herz   Como N no lo puede tocar, puedo bajar Fs y aumentar la resolución a 0.5Hz por ejemplo 512
Ts   = 1/Fs   #por definición
#Resolución espectra, ojo con relación de compromiso...
fsig = 10     #sigue estando en 50Hz, pero hay un desparramo... en .5 se llama desintonia
#fsig en la frecuencia de la señal

plt.close('all')

# Si tenemos espacios lineales, conviene linspace para generar el vector de tiempo.
# Esto va a definir el muestro temporal
t = np.linspace(0.0,(N-1)/Fs,N)          # al no poner el N-1, hubiera terminado con 1025 muestras

s = np.sin(2*np.pi*fsig*t)
#s = sg.square(2*np.pi, duty=0.5)
#https://hangouts.google.com/hangouts/_/ytl/5O0qZULBSltcNvJSz37yiwPyZ0VRrpQFoqL_W7NMzmk=?hl=en_US

spectrum = (2/N)*np.abs(sc.fft(s))       # entender que es la DFT tranf discreta de furier. Como tiene fase y ..., hacemos el abs para quedarnos con el modulo. (2/N) es para que el num. sea secuencial...

half = spectrum[:N//2]                   # la doble // es que el resultado de la división sea entera

frec = np.linspace(0.0,Fs/2,N/2)         # Para que no se repita es solo Fs/2 y se pone N/2 porque...

#resolución espectral (relación de compromiso)
#plt.stem(frec,half)

#resolución temporal (relación de compromiso)
plt.plot(t,s)   # muestra la señal en el tiempo y se ve destruida, solo en la frecuencia es bonita 

plt.show()
