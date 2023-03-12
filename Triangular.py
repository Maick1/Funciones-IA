import matplotlib.pyplot as plt 
import numpy as np

# Función trimf(x, param): función de pertenencia triangular. # Argumentos: 
# x: int, float, numpy.ndarray # Contiene los valores de x en el universo de discurso 
# para los cuales se evalúa su valor de pertenencia. # param = [a, b, c]: list, numpy.ndarray 
# contiene los parámetros de la función de pertenencia # debe cumplirse a <= b <= c # Retorna: 
# valor de pertencia de x según función de membresía triangular. 
# trimf(x, param): float, si x es int, float. # trimf(x, param): numpy.ndarray: si x es numpy.ndarray 
# -1 si no es posible calcular el valor
def trimf(x, param):
    # param = [a, b, c] 
    # # a <= b <= c
    a = float(param[0]) 
    b = float(param[1]) 
    c = float(param[2])
    if (a <= b) and (b <= c): 
        if (type(x) is int) or (type(x) is float) or (type(x) is np.float64):
            if x <= a: 
                m = 0.0
                if x <= a: 
                    m = 0.0 
                elif (a <= x) and (x <= b): 
                    m = (x - a)/(b - a) 
                elif (b <= x) and (x <= c): 
                    m = (c - x)/(c - b)
                else: 
                    m = 0.0
                return m
        else:
            m = np.zeros(x.size)
            for i in range(x.size):
                if x[i] <= a:
                    m[i] = 0.0
                elif (a <= x[i]) and (x[i] <= b):
                    m[i] = (x[i] - a)/(b - a)
                elif (b <= x[i]) and (x[i] <= c):
                    m[i] = (c - x[i])/(c - b)
                else:
                    m[i] = 0.0
        return m 
        
    else: 
        return -1

x = np.linspace(-10,10,1001)
a, b, c = -5, -2, 7
xtest = 2
m = trimf(x,[a, b, c])
plt.plot(x,m,'r')
plt.title("Funcion Triangular") 
plt.show()




