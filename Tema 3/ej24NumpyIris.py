import numpy as np
#Leemos el archivo iris.csv, lo cargamos en una matriz
#y descartamos primera fila y decimos que el separador es la coma
iris = np.loadtxt("./iris.csv", skiprows=1, delimiter=",",)
print("Matriz a partir de archivo de datos. \n", iris.shape)

#: indica los elementos en el eje, si se pone al principio sin nada delante significa que empieza desde el inicio y viceversa. 
# si lo pones como a:z empiza desde a y termina en z-1
#mean() para sacar la media 
# axis = 0 opera a lo largo de las filas y axis= 1 opera a lo largo de las columnas
#1-selecciona 5 filas y calcula la media
media = np.mean(iris[:5, :])
print("Media de las 5 primeras filas:", media)

#2-usando axis de mean calcula la media de las columnas
medias_col = np.mean(iris, axis=0)
print("Media de cada columna:", medias_col)

#3-encuentra el valor mínimo de cada característica np.min
min_col = np.min(iris, axis=0)
print("Mínimo de cada columna:", min_col)

#4-devuelve todas las filas con largo de pétalo (col2) mayor que 5
largo_petalo = iris[iris[:,2] >5]
print("Filas con largo de pétalo en la columna 2 mayores que 5: \n", largo_petalo)

#5-filas de 50 a 99 pero solo las columnas largo y ancho del pétalo (col 2 y 3)
matriz = iris[50:100, 2:4]
print("Filas 50-99, columnas 2 y 3: \n", matriz)
#6-normalizar para que los valores estén en el rango 0-1

#7-guarda las 4 primeras columnas en una variable llamda x
x = iris[:, 0:4]
print(x)

#8-guarda la última columna en una variable y
y = iris[:, 4]
print(y)