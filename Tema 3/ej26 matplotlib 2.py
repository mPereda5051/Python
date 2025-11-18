import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0,2.0,0.01)
s= 1 +np.sin(2+np.pi*t)
plt.plot(t,s)
#completar la garfica
#etiquera en el eje Y
plt.ylabel('voltaje (mv)')
#etiqueta en el eje X
plt.xlabel('tiempo(s)')
#titulo
plt.title("Grafico simple de DAW")
#grid rejilla
plt.grid(True)
plt.savefig('eje26Imagen.png')
plt.show()