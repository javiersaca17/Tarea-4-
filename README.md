# Tarea-4-
## Javier Elias Saca (SLV), B66418
Asignaciones sobre la Tarea 4 MPSS

## Punto 1: Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

  Para poder crear el esquema de modulación BPSK (Binary Phase Shift keying) hay que leer la lista  de los 10,000 bits que estan en el archivo bits10kcsv,luego de ello se define que la frecuecia de operación en este cason especifico es de 5000 Hz con lo cual el periodo que es el inverso de la frecuencia sera de 0.2 ms. Se definen además 50 puntos de muestreo para cada período, con lo cual al hacer el ploteo respectivo con estas condiciones de operación, que se genera la onda portadora: 
  
 ![enter image description here](/portadora.png)

Con lo cual ya que se tiene la onda portadora tenemos que aplicarle la modulación tipo BPSK, con lo cual para dicho caso creamos en Repl.it (código) la variable "signale" :
        #Hacemos la respectiva creación del esquema de modulación tipo BPSK cpn un ciclo (for):
        
            for s, m in enumerate(bits):
             if m == 1:
             signale[s*pto:(s+1)*pto] = port
            else: 
            signale[s*pto:(s+1)*pto] = -port
            
Donde la variable de "port" es la onda portadora que se asumimos que tiene un comportamiento parecido a una onda sinusoidal, con lo cual obtenemos la gráfica para el caso de los primeros 10 bits de la lista de los 10,000 bits disponibles, con lo cual la gráfica obtenida con la aplicación de la mosulación de tipo BPSK es la siguiente: 

 ![enter image description here](/modulada.png)
 
 Con la gráfica anterior podemos afirmar que la modulación se realizo de manera satisfactoria dado que se nota el cambio en la onda sinusoidal con lo cual implicitamente hay un cambio en los bits.
 
 ## Punto 2: Calcular la potencia promedio de la señal modulada generada.
 
 Para calcular la potencia promedio que se genero de la señal anterior primero se procedio a calcular la potencia instantanea que para ello elevamos la magnitud de la señal al cuadrado, teniendo esto integramos el resultado y se dividio por el periodo (T) multiplicando por los 10,000 bits que componen al arichivo, a nivel de código se muestra asi: 
 
 
             #Calculamos la potencia promedio a partir de la instantanea que ya la calculamos anteriormente
              pprom = integrate.trapz(potinst, time) / (N * T)
              
Como resultado se obtuvo que la potencia promedio generada por la señal modulada es de aproximandamente 0.49 Watts.


 ## Punto 3: Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.
 
 Para hacer la simulación del canal de ruido blanco gaussiano hacemos la lista de los seis valores posibles de la realción de señal a ruido (SNR) que va de entero a entero empezando por los -2 dB hasta los 3dB, pra luego calcular la desviación estandar del ruido a través del siguiente código: 
 
     # Desviación estándar del ruido:
      desvest = np.sqrt(pruido)
  
     # Creando  ruido (Pn = sigma^2):
      ruido = np.random.normal(0, desvest, signale.shape)
 
  Las señales con ruido  para  los seis valores necesarios de SNR se muestra en la siguiente imagen:
  
  ![enter image description here](/ruido.png)
 
 ## Punto 4: Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.
 
 Primero graficamos antes que la señal entre al canal ruidoso, dicha gráfica es la siguiente: 
 
  ![enter image description here](/densidadespectral.png)
 
 Posteriormente usando el método de Welch encontramos la gráficas correspondientes para los diferentes niveldes de SNR establecidos previamente, el correspondiente para un SNR de -2 dB es la siguiente: 
 
   ![enter image description here](/densidad-2dB.png)
 
 
