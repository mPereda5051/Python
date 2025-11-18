import numpy as np
import matplotlib.pyplot as plt

#Porcentaje de centros en cada distrito

# Cargar los datos
data = np.genfromtxt("Centros.csv", delimiter=';', dtype=str, encoding='latin1', skip_header=1, invalid_raise=False)

#guardar la informacion de la columna de distritos
distritos = data[:, 23]

# Contar cuántas veces aparece cada distrito
unicos, conteos = np.unique(distritos, return_counts=True)

plt.pie(conteos, labels=unicos, autopct="%1.1f%%", startangle=90)
plt.title("Porcentajes de centro por distrito")
plt.show()