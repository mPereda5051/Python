import numpy as np
print("Versión ", np.__version__)

#un array es una estructura similar a una lista, pero optimizada para cálculos numéricos
a = np.array([1,2,3])
print("Mi primer array en numpy ",a)

print("\n*Crear arrays*")
print("Array de enteros: ", np.array([10,20,30]))
print("Array de enteros: ", np.zeros(5))
print("Array de unos que tenga 2 filas y 3 columnas")
print(np.ones((2,3)))
print("Array desde 0 hasta 10 contando de 2 en 2")
print(np.arange(0,10,2))
print("Array con valores aleatorios en 3 filas y 3 columnas")
print(np.random.rand(3,2))
#matriz nueva de 2x2
mat1 = np.array([[1,2], [3,4]])
print(mat1)
#matriz de unos de 2x2
mat2 = np.ones((2,2))
print(mat2)
#comprobar la dimensión de la matriz
print("Dimension de matriz 2: ", mat2.shape, "\n")
#sumar matrices
matSuma = mat1 + mat2
print("Suma de matrices: ",matSuma)

#multiplicar por un valor
matMult = mat1 * 2
print("MatMult\n",matMult)

#Multiplicacion de matrices
print("Mult mat opción 1: \n", np.matmul(mat1,mat2))
print("Mult mat opcion 2: \n", mat1 @ mat2, "\n")

#Inverda de la matriz
#La inversa de una matriz, es la matriz que al multplicar por la matriz original da la matriz identidad
#La matriz identidad tiene unos en la diagonal y ceros en el resto
print("Dada la matriz1: \n", mat1)
print("La inversa es: \n", np.linalg.inv(mat1))
matinv = np.linalg.inv(mat1)
matRes = np.matmul(mat1, matinv)
print("Resultado = ", matRes)

#Más ejemplos
#Crear una matriz con valores del 1 al 9 de fotma rápida
mat3 = np.arange(1,10).reshape((3,3))
print("Matriz del 1 al 9: \n", mat3)
print("Matriz del 1 al 9 (traspuesta): \n", mat3.T)

#Seleccionar celdas
print("fila2, columna2: ", mat3[1,1])
print("Toda la fila2: ", mat3[1, :])
print("Columna 3: ", mat3[: , 2])
print("Dimensiones mat3", mat3.shape)

#filtrados
print("De las matrices > 5: ", mat3[mat3>5])
#media
print("Media de la matriz: ", np.mean(mat3))
print("Media de filas: ", np.mean(mat3, axis=1))
print("Media de columnas: ", np.mean(mat3, axis=0))

