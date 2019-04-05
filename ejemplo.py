# -*- coding: utf-8 -*-
"""
Respuesta: A primera vista parece trivial determinar la frecuencia segun su representacion,
pero debido a que es una senal sampleada, podria tratarse de una frecuencia alias. Para
poder determinar certeramente la frecuencia, habria que garantizar que el seampleo se realizo
luego de filtrar la senial con un filtro antialias.

Respuesta: No, idem al punto a.1
¿A qué se debe?

Respuesta: Como se explico en el punto a.1 hay infinitas senales que podrian representarse con
estas figuras. En caso de que se garantizara que la senal fue sampleada luego de un filtro antialias
ideal si seria perfectamente deducible. Por ej. en el caso de fo = fs/2, y todos los valores
sampleados son cero (cercanos a cero en la grafica por la imprecision de PI) o bien es una senoidal
de fo que justo se semplea rigorosamente en cero cada 1/fs, o es una continua en cero. En el
caso de a.3 como los valores son simetricos y en -1 y 1, la senial es una senoidas, de amplitud 1
y fo=fs/2. SI los valores no fueses simetricos, la amplitud tambien se podria calcular pero utilizando
la ecuacion del seno en cada punto.

Es posible diferenciar a.1 de a.4 a partir de las gráficas?

Respuesta: Como se puede ver en la grafica superpuesta de a.1 y a.4 las 2 senales son indistinguibles.
Una vez mas esto se debe a que fs no esta compliendo con Nyquist (fs/2>f0) y por lo tanto 1010 es un
alias de 10hz.
¿En caso que no, qué solución podría implementar para evitar dicha ambigüedad?

Respuesta: para resolver la ambiguedad, solo basta con aumentar fs tal que como minimo fs/2>f0, en este
caso 2020hz seria la frecuencia minima de sampleo


"""

import numpy as np                                                                             
                                                                                               
class signal_generator_class:                                                                  
    def __init__(self):                                                                        
        pass                                                                                   
                                                                                               
    # funcion que recibe: fs frecuencia de sampleo, fo es la frec que quiero                   
    # para la senusoide A es la amplitud N el numero de muestras as tomar sim,                 
    # punto de simetria (conde esta el vertice                                                 
    def signal_triangular(self, fs, fo, A, N , sim):                                           
        #inicializo para todos los samples que voy a tener                                     
        tt =   [n/fs  for n in range(N)]                                                       
        ans=[0 for i in range(N)]                                                              
        for i in range(N):                                                                     
            #calculo el porcentaje actual en funcion de i, y usando modulo para                
            #ir repitiendo cuando llego a la fo                                                
            percent=(tt[i]%(1/fo))/(1/fo) * 100                                                
            #si me paso de lo pedido...                                                        
            if percent < sim:                                                                  
                ans[i]=A/sim * percent                                                         
            else:                                                                              
                ans[i]=A-(A/(100-sim) * (percent-sim))                                         
        return ans, tt                                                                         
                                                                                               
                                                                                               
    # funcion que recibe: fs frecuencia de sampleo, fo es la frec que quiero                   
    # para la senusoide A es la amplitud N el numero de muestras as tomar                      
    # cilco,  PWM en porcentaje                                                                
    def signal_quad(self, fs, fo, A, N , ciclo):                                               
        #vector de N elementos, y aprovecho a cargarle la Amplitud negativa                    
        tt = [n/fs  for n in range(N)]                                                         
        ans=[-A for i in range(N)]                                                             
        for i in range(N):                                                                     
        #    #calculo para cada muestra en que parte del PWM estoy                             
            percent=(tt[i]%(1/fo))/(1/fo) * 100                                                
            #si me paso de lo pedido...pongo el valor positivo.                                
            if percent < ciclo:                                                                
                ans[i]=A                                                                       
        return ans, tt                                                                         
                                                                                               
    # funcion que recibe: fs frecuencia de sampleo, fo es la frec que quiero                   
    # para la senusoide A es la amplitud N el numero de muestras as tomar fase,                
    # la fase en radianes                                                                      
    def signal_sin(self, fs, fo, A, N , rad):                                                  
        #con esta magia greo un vector con N valores del seno de fo capturados                 
        #una distancia de 1/fs cada uno. Aplico %1 para que no arrastre error de pi a medida  
        #que el factor multiplicativo se hace mas grande.. como es periodica en 2*pi aprovecho eso
        tt =   [n/fs  for n in range(N)]                                                       
        ans =  [A * np.sin( 2 * np.pi * fo * (tt[n]%1) + rad) for n in range(N)]                   
        return ans, tt                                                                         
                                                                                               
    def signal_noise(self, fs, mean, deviation, N):                                            
        tt =   [n/fs  for n in range(N)]                                                       
        ans = np.random.normal(mean, deviation, N )                                            
        return ans, tt                                                                         
            
        
import matplotlib.pyplot as plt                                                                
                                                                                               
class plotter_class:                                                                           
                                                                                        
    def __init__(self,row,col):                                                                
        self.row=row                                                                           
        self.col=col                                                                           
        self.fig=plt.figure(figsize=( 10, 7))                                                  
        self.ax1=self.fig.add_subplot(row,col,1)                                               
        plt.tight_layout(pad=4, w_pad=5, h_pad=6)                                              
        plt.draw()                                                                             
                                                                                               
    def plot_signal(self, pos, x, y, title, xLabel, yLabel, about):                            
        ax=self.fig.add_subplot(self.row,self.col,pos)                                         
        line, =ax.plot(x,y,'.', label=about)                                                 
        ax.set_title(title)                                                                    
        ax.set_xlabel(xLabel)                                                                  
        ax.set_ylabel(yLabel)                                                                  
        ax.grid(which='both', axis='both')                                                     
        #ax.legend(loc='best')                                                                  
        plt.draw()                                                                             
                                                                                               
    def plot_show(self):                                                                       
        plt.show()                                                                             
                                                                                               
    def plot_draw(self,pause):                                                                 
        plt.draw()                                                                             
        plt.pause(pause)                                                                       
                                                                                               
    def plot_close(self):                                                                      
        plt.close()    
        
#signal_quad(self, fs, fo, A, N , ciclo): 
print("hola")
#signal_generator_class.signal_quad(self, 1000, 50, 1000, 1000, 1000)
# NO modifiques este bloque,
############################
N  = 1000 # muestras
fs = 1000 # Hz
sg= signal_generator_class()

# Insertar aquí el código para inicializar tu notebook
########################################################
a0 = 1       # Volts                                                                           
p0 = np.pi/2 # radianes                                                                        
f0 = fs/2    # Hz 

plg1= plotter_class(2,2)                                                                        
for f0 in range(5,21,5):                                                                       
    ans,tt=sg.signal_sin(fs ,f0 ,a0 ,N ,0 )                                                    
    plg1.plot_signal (f0/5,tt,ans,'senoidal f0=%fhz' %f0 ,'tiempo' ,'a0' ,'senoidal')           
                                                                                               
plg2= plotter_class(2,2)                                                                        
for M in range(1,5,1):                                                                         
    ans,tt=sg.signal_noise(fs, M ,2 ,N)                                                        
    plg2.plot_signal (M,tt,ans,'noise mean=%f0' %M ,'tiempo' ,'a0' ,'noise')                    
                                                                                               
plg3= plotter_class(2,2)                                                                        
for f0 in range(5,21,5):                                                                       
    ans,tt=sg.signal_triangular(fs, f0, a0, N, 75)                                             
    plg3.plot_signal (f0/5,tt,ans,'triangular f0=%fhz' %f0 ,'tiempo' ,'a0' ,'triangular')       
                                                                                               
plg4= plotter_class(2,2)                                                                        
for F in range(5,21,5):                                                                        
    ans,tt=sg.signal_quad(fs, F, a0, N, 25)                                                    
    plg4.plot_signal (F/5,tt,ans,'cuadrada F=%fhz' %F ,'tiempo' ,'a0' ,'cuadrada')



##################                                                                         
# a.1) Senoidal #                                                                          
#################                                                                          
a0 = 1 # Volts                                                                             
p0 = 0 # radianes                                                                          
f0 = 10   # Hz                                                                             
                                                                                               
# Insertar aquí el código para generar y visualizar la señal                               
##############################################################        
                                                                                               
pl1= plotter_class(1,1)                                                                        
ans,tt=sg.signal_sin(fs ,f0 ,a0 ,N , p0 )                                                 
pl1.plot_signal (1,tt,ans,'senoidal f0=%fhz' %f0 ,'tiempo' ,'a0' ,'senoidal')



##################
# a.2) Senoidal #
#################
a0 = 1 # Volts
p0 = 0 # radianes
f0 = fs/2   # Hz

# Insertar aquí el código para generar y visualizar la señal
##############################################################

pl2= plotter_class(1,1)                                                                        
ans,tt=sg.signal_sin(fs ,f0 ,a0 ,N , p0 )                                                 
pl2.plot_signal (1,tt,ans,'senoidal f0=%fhz' %f0 ,'tiempo' ,'a0' ,'senoidal')


##################
# a.3) Senoidal #
#################

a0 = 1       # Volts
p0 = np.pi/2 # radianes
f0 = fs/2    # Hz

# Insertar aquí el código para generar y visualizar la señal
##############################################################

pl3= plotter_class(1,1)                                                                        
ans,tt=sg.signal_sin(fs ,f0 ,a0 ,N , p0 )                                                 
pl3.plot_signal (1,tt,ans,'senoidal f0=%fhz' %f0 ,'tiempo' ,'a0' ,'senoidal')



##################
# a.4) Senoidal #
#################

a0 = 1     # Volts
p0 = 0     # radianes
f0 = fs+10 # Hz

a1 = 1 # Volts                                                                             
p1 = 0 # radianes                                                                          
f1 = 10   # Hz                                                                             

# Insertar aquí el código para generar y visualizar la señal
##############################################################
pl4a= plotter_class(2,2)  

ans0,tt0=sg.signal_sin(fs ,f0 ,a0 ,N , p0 )                                                 
pl4a.plot_signal (1,tt0,ans0,'senoidal f0=%fhz' %f0 ,'tiempo' ,'a0' ,'senoidal')

ans1,tt1=sg.signal_sin(fs ,f1 ,a1 ,N , p1 )
pl4a.plot_signal (2,tt1,ans1,'senoidal f1=%fhz' %f1 ,'tiempo' ,'a1' ,'senoidal')

pl4a.plot_signal (3,tt0,ans0,'','tiempo' ,'a0' ,'senoidal')
pl4a.plot_signal (3,tt1,ans1,'senoidal f1 vs f0' ,'tiempo' ,'a1' ,'senoidal')