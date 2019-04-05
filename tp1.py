#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Creado:       15/03/2019
Autor:        Roberto Compañy
Repositorio:  https://github.com/companyroberto
Descripción:  Trabajo Práctico 1 - Muestreo de señales - Fourier

"""


#%%  Import
import pdsmodulos.utiles as utiles



#%%  Funciones propias del TP

def generador_senoidal (fs, f0, N, a0=1, p0=0):
    """ 
    brief:  Generador de señales senoidal, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    f0:     frecuencia de la senoidal [Hz]              como formo las tuplas?
    N:      cantidad de muestras de la señal a generar
    a0:     amplitud pico de la señal [V]               como formo las tuplas?
    p0:     fase de la señal sinusoidal [rad]           como formo las tuplas?
    
    como resultado la señal devuelve:
    
    signal: senoidal evaluada en cada instante 
    tt:     base de tiempo de la señal
    """    

    # comienzo de la función

    sig_props = { 'tipo':       'senoidal', 
#                  'frecuencia': (1, 1001), # Uso de tuplas para las frecuencias 
                  'frecuencia': (1, f0),
                  'amplitud':   (1, a0),
                  'fase':       (0, p0),
                  'fs':         fs,
                  'N':          N
                 } 
    # Como también puedo agregar un campo descripción de manera programática
    # este tipo de sintaxis es *MUY* de Python
    sig_props['descripcion'] = [ str(a_freq) + ' Hz' for a_freq in sig_props['frecuencia'] ]

    
    # Usar CTRL+1 para comentar o descomentar el bloque de abajo.
#    sig_props = { 'tipo': 'ruido', 
#                  'varianza': (1, 1, 1) # Uso de tuplas para las frecuencias 
#                 } 
#    sig_props['descripcion'] = [ '$\sigma^2$ = ' + str(a_var) for a_var in sig_props['varianza'] ]
        
    # Invocamos a nuestro testbench exclusivamente: 
    utiles.generar( sig_props )

    # fin de la función
    #return tt, signal


#%%  Funciones propias del TP

def generador_cuadrada (fs, f0, N, a0=1, p0=0):

    # comienzo de la función
    sig_props = { 'tipo':       'cuadrada', 
#                  'frecuencia': (1, 1001), # Uso de tuplas para las frecuencias 
                  'frecuencia': (1, f0),
                  'amplitud':   (1, a0),
                  'fase':       (0, p0),
                  'fs':         fs,
                  'N':          N
                 } 
    # Como también puedo agregar un campo descripción de manera programática
    # este tipo de sintaxis es *MUY* de Python
    sig_props['descripcion'] = [ str(a_freq) + ' Hz' for a_freq in sig_props['frecuencia'] ]

    
    # Usar CTRL+1 para comentar o descomentar el bloque de abajo.
#    sig_props = { 'tipo': 'ruido', 
#                  'varianza': (1, 1, 1) # Uso de tuplas para las frecuencias 
#                 } 
#    sig_props['descripcion'] = [ '$\sigma^2$ = ' + str(a_var) for a_var in sig_props['varianza'] ]
        
    # Invocamos a nuestro testbench exclusivamente: 
    utiles.generar( sig_props )

#%%  Test del TP

generador_senoidal(1000.0,50,1000)
#generador_cuadrada(1000.0,50,1000)

