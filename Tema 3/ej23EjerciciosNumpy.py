import numpy as np

print("Versión de NumPy:", np.__version__)

#np.reshape() cambia la forma del array(numero de filas, columnas) sin cambiar sus datos
# a) 
A = np.array([[1, 1, 1], [1, 1, 1]])
B = np.array([[1, 2, 3], [4, 5, 6]])
print("a)\n", A + B)

# b) 
columna = np.array([1, 3, 5]).reshape(3, 1)
linea = np.array([2, 4, 6]).reshape(1, 3)
print("b)\n", columna @ linea) #@ para hacer la multiplicacion matricial

# c) 
#np.arange crea un array con valores espaciados uniformewmente dentro de un intervalo, similar a range()

C = np.arange(1, 17).reshape(4, 4)
#mascara booleana selecciona todos los elementos donde mask es True.
C[C % 2 == 0] = -1
print("c)\n", C)

# d) 
# dtype = complax combierte el array para que todos sean numeros complejos.
D = np.array([[2, 3, 4], [5, 6, 7]], dtype=complex)
print("d) \n", D)