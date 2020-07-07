#Nombre: Javier Saca. 
#Carnet: B66418. 
#Tarea 4 
#Importamos las librerias necesarias
import numpy as np
from scipy import stats
from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt
#Importamos a los pandas 
import pandas as pd
#Leemos el archivo bits10k.csv
bits2 = pd.read_csv('bits10k.csv', header=None)
bits = np.array(bits2)


# Definimos el número de  de bits
#utilizar
N = 10000 

## Punto 1: Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

# Definimos la frecuencia de operación en Hertz:
f = 5000

#  Período de cada símbolo (onda) de 0.2 ms
T = 1/f 

#Cantidad de puntos de muestreo por el periodo
pto = 50 

#Puntos de muestreo por cada uno de los periodos

Npto = np.linspace(0, T, pto)

#Creamos la onda portadora
port = np.sin(2*np.pi * f * Npto)

#Hacemos el ploteo respectivo de la onda portadora
plt.figure(0)
plt.plot(Npto, port)
plt.xlabel('Tiempo / segundos')
plt.savefig('portadora')

#Determinando la frecuencia de muestreo 
fm = pto/T

#Linea temporal para Tx 
time = np.linspace(0, N*T, N*pto)

#Luego inicializamos el vector de la onda modulada (Tx)
signale = np.zeros(time.shape)

#Hacemos la respectiva creación del esquema de modulación tipo BPSK cpn un ciclo (for)
for s, m in enumerate(bits):
    if m == 1:
        signale[s*pto:(s+1)*pto] = port
    else: 
        signale[s*pto:(s+1)*pto] = -port

#Vemos ya los bits que ya estan modulados
mb1 = 0
mb2 = 10
plt.figure(1)
#Hacemos el ploteo de la señal modulada
plt.plot(signale[mb1*pto:mb2*pto])
plt.xlabel('Tiempo / segundos')
plt.savefig('modulada')

## Punto 2: Calcular la potencia promedio de la señal modulada generada.

#Definimos la potencia instantanea de nuestra señal respectiva:
potinst = signale**2

#Calculamos la potencia promedio a partir de la instantanea que ya la calculamos anteriormente
pprom = integrate.trapz(potinst, time) / (N * T)

#Imprimimos la potencia promedio: 
print('   Potencia promedio calculada  es: ', pprom, 'Watts. \n')

## Punto 3: Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.

#Definimos los valores del SNR, sabiendo que se tiene la señal de ruido 
# Relación señal-a-ruido deseada
SNR = -3
for SNR in range(-2, 4):
  print (SNR)
  # Potencia del ruido para SNR y potencia de la señal dadas
  pruido = pprom / (10**(SNR / 10))
  
  # Desviación estándar del ruido
  
  desvest = np.sqrt(pruido)
  
  # Creando  ruido (Pn = sigma^2)
  
  ruido = np.random.normal(0, desvest, signale.shape)
  
  # Simular "el canal": señal recibida
  if SNR == -2:
    Rx1 = signale + ruido
    #print (Rx1)
  if SNR == -1:
    Rx2 = signale + ruido
    #print (Rx2)
  if SNR == 0:
    Rx3 = signale + ruido
    #print (Rx3)
  if SNR == 1:
    Rx4 = signale + ruido
    #print (Rx4)
  if SNR == 2:
    Rx5 = signale + ruido
    #print (Rx5)
  if SNR == 3:
    Rx6 = signale + ruido
    #print (Rx6)
  
  SNR +=1

##Punto 4: Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.

#Antes del canal ruidoso: 
fw, PSD = signal.welch(signale, fm, nperseg=1024)
plt.figure(3)
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hertz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('densidad espectral') 

#Despues de canal ruidoso:
#Para RX1
fw, PSD = signal.welch(Rx1, fm, nperseg=1024)
plt.figure(4)
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hertz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('Densidad con ruido asociado con SNR de -2 dB ')
#Para RX2
fw, PSD = signal.welch(Rx2, fm, nperseg=1024)
plt.figure(5)
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hertz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('Densidad con ruido asociado con SNR de -1 dB ')
#Para RX3
fw, PSD = signal.welch(Rx3, fm, nperseg=1024)
plt.figure(6)
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hertz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('Densidad con ruido asociado con SNR de 0 dB ')
#Para RX4
fw, PSD = signal.welch(Rx4, fm, nperseg=1024)
plt.figure(7)
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hertz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('Densidad con ruido asociado con SNR de 1 dB ')
#Para RX5
fw, PSD = signal.welch(Rx5, fm, nperseg=1024)
plt.figure(8)
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hertz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('Densidad con ruido asociado con SNR de 2 dB ')
#Para RX6
fw, PSD = signal.welch(Rx6, fm, nperseg=1024)
plt.figure(9)
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hertz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('Densidad con ruido asociado con SNR de 3 dB ')

## Punto 5: Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.

#Calculamos la pseudo energia de la onda original
Es = np.sum(port**2)
# Inicialización del vector de bits recibidos para Rx1
bitsRx1 = np.zeros(bits.shape)

# Decodificación de la señal por detección de energía
for s, m in enumerate(bits):
  # Producto interno de dos funciones
  Ep = np.sum(Rx1[s*pto:(s+1)*pto] * port) 
  if Ep > Es/2:
    bitsRx1[s] = 1
  else:
    bitsRx1[s] = 0

err1 = np.sum(np.abs(bits - bitsRx1))
BER1 = err1/N
print('Cuando SNR es -2 dB ',  'el ruido es: ', BER1)

# Inicialización del vector de bits recibidos para Rx2
bitsRx2 = np.zeros(bits.shape)

# Decodificación de la señal por detección de energía
for s, m in enumerate(bits):
  # Producto interno de dos funciones
  Ep = np.sum(Rx2[s*pto:(s+1)*pto] * port) 
  if Ep > Es/2:
    bitsRx2[s] = 1
  else:
    bitsRx2[s] = 0

err2 = np.sum(np.abs(bits - bitsRx2))
BER2 = err2/N
print('Cuando SNR es -1 dB ',  'el ruido es: ', BER2)

# Inicialización del vector de bits recibidos para Rx3
bitsRx3 = np.zeros(bits.shape)

# Decodificación de la señal por detección de energía
for s, m in enumerate(bits):
  # Producto interno de dos funciones
  Ep = np.sum(Rx3[s*pto:(s+1)*pto] * port) 
  if Ep > Es/2:
    bitsRx3[s] = 1
  else:
    bitsRx3[s] = 0

err3 = np.sum(np.abs(bits - bitsRx3))
BER3 = err3/N
print('Cuando SNR es 0 dB ',  'el ruido es: ', BER3)

# Inicialización del vector de bits recibidos para Rx4
bitsRx4 = np.zeros(bits.shape)

# Decodificación de la señal por detección de energía
for s, m in enumerate(bits):
  # Producto interno de dos funciones
  Ep = np.sum(Rx4[s*pto:(s+1)*pto] * port) 
  if Ep > Es/2:
    bitsRx4[s] = 1
  else:
    bitsRx4[s] = 0

err4 = np.sum(np.abs(bits - bitsRx4))
BER4 = err4/N
print('Cuando SNR es 1 dB ',  'el ruido es: ', BER4)

# Inicialización del vector de bits recibidos para Rx5
bitsRx5 = np.zeros(bits.shape)

# Decodificación de la señal por detección de energía
for s, m in enumerate(bits):
  # Producto interno de dos funciones
  Ep = np.sum(Rx5[s*pto:(s+1)*pto] * port) 
  if Ep > Es/2:
    bitsRx5[s] = 1
  else:
    bitsRx5[s] = 0

err5 = np.sum(np.abs(bits - bitsRx5))
BER5 = err5/N
print('Cuando SNR es 2 dB ',  'el ruido es: ', BER5)

# Inicialización del vector de bits recibidos para Rx6
bitsRx6 = np.zeros(bits.shape)

# Decodificación de la señal por detección de energía
for s, m in enumerate(bits):
  # Producto interno de dos funciones
  Ep = np.sum(Rx6[s*pto:(s+1)*pto] * port) 
  if Ep > Es/2:
    bitsRx6[s] = 1
  else:
    bitsRx6[s] = 0

err6 = np.sum(np.abs(bits - bitsRx6))
BER6 = err6/N
print('Cuando SNR es 3 dB ',  'el ruido es: ', BER6)

## Punto 6: Graficar BER versus SNR.
#Definimos primero BER y SNR
BER=[BER1, BER2, BER3, BER4, BER5, BER6]
SNR=[-2, -1, 0, 1, 2, 3]
#Realiazando el respectivo ploteo
plt.figure(10)
plt.plot(SNR,BER,)
plt.xlabel('BER (bit rate error)')
plt.ylabel('SNR / dB') 
plt.savefig('BERvsSNR')