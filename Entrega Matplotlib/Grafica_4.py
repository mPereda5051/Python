import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos
data = np.genfromtxt("Centros.csv", delimiter=';', dtype=str,encoding='latin1', skip_header=1, invalid_raise=False)

# Seleccionar la columna de distrito.
distritos = data[:, 22]

# Quitar espacios y comillas
distritos = np.char.strip(distritos)
distritos = np.char.replace(distritos, '"', '')

# Contar cuántas veces aparece cada distrito
unicos, conteos = np.unique(distritos, return_counts=True)

# Convertir distritos a numeros y guardarlos en el array
x = []
y = []

#bucle que junta los dos arrays creados a partir del conteo posicion por posicion.
for c_distritos, cantidad in zip(unicos, conteos):
    if c_distritos.isdigit():     # comprobacion para que se guarde la informacion solo si
                                  #  el valor de codigo de distrito es un numero
        x.append(int(c_distritos))
        y.append(cantidad)

# Hacer el gráfico
plt.scatter(x, y, color='blue', alpha=0.6)
plt.title("Numero de centros en distrito", fontsize=10)
plt.xlabel("Código de distrito", fontsize=8)
plt.ylabel("Cantidad de centros", fontsize=8)
plt.grid(True)
plt.show()
