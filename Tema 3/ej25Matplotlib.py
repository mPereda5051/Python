import matplotlib.pyplot as plt
import numpy as np
#plors sencillos: eje x de 1-4 y eje y de 1 a 1-16
#plt.plot([1,2,3,4], [1,4,9,16])
#plt.show()

#2 lineas
#plt.plot([1,2,3,4], [1,4,9,16])
#plt.plot([1,2,3,4], [5,1,2,17])
#plt.show()
# puntos individuales
#plt.scatter([1,2,3,4], [1,4,9,16])
#plt.show()

#mezclamos numpy con matplotib
t = np.arange(0.,5.,0.2)
print(t)
plt.plot(t, t, 'r--', t, t**2,'bs', t, t**3, 'g^')
plt.show()

