import matplotlib.pyplot as plt
import numpy as np

#Función gaussmf(x, param): función de pertenencia gaussiana. 
#Argumentos: 
# x: int, float, numpy.ndarray # Contiene los valores de x en el universo de discurso 
# para los cuales se evalúa su valor de pertenencia. 
# param = [sig, x0]: list, numpy.ndarray # contiene los parámetros de la función de pertenencia # debe cumplirse sig > 0 
# Retorna: # valor de pertencia de x según función de membresía triangular. 
# gaussmf(x, param): float, si x es int, float. 
#gaussmf(x, param): numpy.ndarray: si x es numpy.ndarray 
#-1 si no es posible calcular el valor 

def gaussmf(x, param): 
    #param = [sig, x0] 
    # sig > 0 
    sig = param[0] 
    x0 = param[1] 
    if (sig > 0): 
        if (type(x) is int) or (type(x) is float) or (type(x) is np.float64):
            m = np.exp(-0.5*((x - x0)/sig)**2)
        else: 
            m = np.zeros(x.size)
            for i in range(x.size):
                m[i] = np.exp(-0.5*((x[i] - x0)/sig)**2)
            return m
    else:
        return -1
x = np.linspace(0, 10, 1001, endpoint=True)
sig, x0 = 1, 8
m = gaussmf(x, [sig, x0])
xtest=6
plt.plot(x,m,'g') 
plt.title("Funcion Gaussiana") 
plt.show()