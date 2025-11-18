import numpy as np
import matplotlib.pyplot as plt
#Top 3 tipos de centros mas comunes
# Cargar los datos
data = np.genfromtxt("Centros.csv", delimiter=';', dtype=str, encoding='latin1', skip_header=1, invalid_raise=False)
#recogemos la informacion
centros = np.array(data[:, 4])
# Contar frecuencia de cada tipo
unicos, conteos = np.unique(centros, return_counts=True)

# Ordenar de mayor a menor y seleccionar los 3 más comunes
orden = np.argsort(conteos)[::-1]
nombres = unicos[orden][:3]
conteo= conteos[orden][:3]

# Crear gráfico
plt.figure(figsize=(9, 6))
plt.bar(nombres, conteo, color='blue')
plt.title("Los 3 tipos de centros más comunes")
plt.xlabel("Tipo de centro")
plt.ylabel("Número de centros")
plt.xticks(rotation=10, fontsize=9)
plt.tight_layout()
plt.show()
