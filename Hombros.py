import numpy as np
import matplotlib.pyplot as plt

xmin=0
xmax=10
res=0.5

b = centro = 6
a = inicio = 2

# Generemos la lista de las posibles x
xrange = np.arange(xmin, xmax, res)

perten_hombro_dcho = []   # Lista para guardar los valores de una función
perten_hombro_izdo = []   # y otra lista para los valores de la otra función

# Recorriendo la lista de las posibles x, calculamos cada valor y lo
# guardamos en la lista de la función correspondiente
for x in xrange:
    if x<a:
        perten_hombro_dcho.append(0)  # .append añade el dato a la lista
        perten_hombro_izdo.append(1)
    elif x>=a and x<b:
        perten_hombro_dcho.append((x-a)/(b-a))
        perten_hombro_izdo.append(1-(x-a)/(b-a))
    elif x>=b:
        perten_hombro_dcho.append(1)
        perten_hombro_izdo.append(0)

# Pintamos ambas funciones. Para ambas la lista de x es la misma
# pero cambiamos la lista de los valores y
# Pintamos cada una de un color diferente y le damos una etiqueta diferente
plt.plot(xrange, perten_hombro_dcho,'y--', label="Hombro derecho")
plt.plot(xrange, perten_hombro_izdo,'b--', label="Hombro izquierdo")

# Etiquetamos los ejes y la gráfica
plt.title("Funciones de pertenencia a los hombros")
plt.xlabel("Distancia al origen")
plt.ylabel("Grado de pertenencia")

# Mostramos la leyenda que relaciona colores con funciones
plt.legend()
plt.show()