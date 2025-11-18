import numpy as np
import matplotlib.pyplot as plt

# Cargar el CSV
data = np.genfromtxt("centros.csv", delimiter=';', dtype=str, encoding='latin1', skip_header=1, invalid_raise=False)

#guardar la informacion de la columna 21 en este caso, barrios
barrios = data[:, 21]

# Quitar espacios
barrios = np.char.strip(barrios)
# Contar cuántas veces aparece cada barrio
unicos, conteos = np.unique(barrios, return_counts=True)

# Ordenar para mostrar los 5 lugares con más centros
orden = np.argsort(conteos)[::-1]
top5 = unicos[orden][:5]
cantidad = conteos[orden][:5]

# Hacer el gráfico
plt.bar(top5, cantidad, color='blue')
plt.title("Los 5 barrios con más centros")
plt.xlabel("Barrio")
plt.ylabel("Número de centros")
plt.xticks(rotation=14, fontsize=6)
plt.show()
