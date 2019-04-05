# -*- coding: utf-8 -*-
"""
TP1

https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.square.html

"""

#libreria numerica
import numpy as np

#libreria de impresión
import matplotlib.pyplot as plt

#
import scipy.fftpack as sc
import scipy.signal as sg

def generador_senoidal (fs, f0, N, a0=1, p0=0):
    """
    brief:  Generador de señales senoidal, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    f0:     frecuencia de la senoidal [Hz]
    a0:     amplitud pico de la señal [V]
    p0:     fase de la señal sinusoidal [rad]
    
    como resultado la señal devuelve:
    
    signal: senoidal evaluada en cada instante 
    tt:     base de tiempo de la señal
    """

    #Para usar en las muestras, utilizar multiplos de 2 (al ser iguales la resolución es 1)
    #N    = 1024   #muestras
    #fs   = 1024   #herz   Como N no lo puede tocar, puedo bajar Fs y aumentar la resolución a 0.5Hz por ejemplo 512
    #ts   = 1/fs   #por definición
    
    #Resolución espectra, ojo con relación de compromiso...
    #f0 = 10     #sigue estando en 50Hz, pero hay un desparramo... en .5 se llama desintonia
    #f0 en la frecuencia de la señal


    # comienzo de la función

    # Si tenemos espacios lineales, conviene linspace para generar el vector de tiempo.
    # Esto va a definir el muestro temporal
    tt = np.linspace(0.0, (N-1)/fs, N).flatten()   # al no poner el N-1, hubiera terminado con 1025 muestras

    #Genero la senoidal con los parametros de entrada.
    signal = a0 * np.sin(2 * np.pi * f0 * tt + p0);


    #spectrum = (2/N) * np.abs (sc.fft(signal) )   # entender que es la DFT tranf discreta de furier. Como tiene fase y ..., hacemos el abs para quedarnos con el modulo. (2/N) es para que el num. sea secuencial...
    #half = spectrum[:N//2]                        # la doble // es que el resultado de la división sea entera    
    #frec = np.linspace(0.0, fs/2, N/2)            # Para que no se repita es solo Fs/2 y se pone N/2 porque...

    #resolución espectral (relación de compromiso)
    #plt.stem(frec,half)
    
    #resolución temporal (relación de compromiso)
    #plt.plot(tt,signal)                           # muestra la señal en el tiempo y se ve destruida, solo en la frecuencia es bonita 
    
    #plt.show()

    # fin de la función
    
    return tt, signal


N  = 1000   # muestras
fs = 1000   # Hz

a0 = 1      # Volts
p0 = 0      # radianes
f0 = fs+10  # Hz


[tt,signal] = generador_senoidal(fs,f0,N,a0,p0)

plt.close( 'all' )
plt.plot( tt,signal )
plt.figure( 1, (10,5) )
plt.title( 'Señal: Senoidal')
plt.xlabel('tiempo [segundos]')
plt.ylabel('Amplitud [V]')
plt.show()
