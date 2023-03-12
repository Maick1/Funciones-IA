import numpy as np 
import matplotlib.pyplot as plt

def trapmf(x, param): 
    a = float(param[0]) 
    b = float(param[1]) 
    c = float(param[2]) 
    d = float(param[3]) 
    if (a <= b) and (b <= c) and (c <= d): 
        if (type(x) is int) or (type(x) is float) or (type(x) is np.float64):
            if x < a:
                m = 0.0
            elif (a <= x) and (x < b): 
                m = (x - a)/(b - a) 
            elif (b <= x) and (x <= c): 
                m = 1.0 
            elif (c < x) and (x <= d): 
                m = (d - x)/(d - c)
            else: 
                m = 0.0 
            return m
        else:
            m = np.zeros(x.size)
            for i in range(x.size):
                if x[i] < a: 
                    m[i] = 0.0
                elif (a <= x[i]) and (x[i] < b): 
                    m[i] = (x[i] - a)/(b - a) 
                elif (b <= x[i]) and (x[i] <= c): 
                    m[i] = 1.0 
                elif (c < x[i]) and (x[i] <= d): 
                    m[i] = (d - x[i])/(d - c) 
                else: m[i] = 0.0 
            return m
    else:
        return -1
x = np.linspace(0, 10, 1001, endpoint=True) 
a, b, c, d = 1, 4, 6, 7 
m = trapmf(x, [a, b, c, d]) 
xtest = 7.5 
plt.plot(x,m,'y') 
plt.title("Funcion Trapezoidal") 
plt.show()       