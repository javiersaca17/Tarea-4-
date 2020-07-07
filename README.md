# Tarea-4-
## Javier Elias Saca, B66418
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
