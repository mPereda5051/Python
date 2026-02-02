#el map transforma
#el filter selecciona
#reduce se aplica a todos los elementos de una lista

from functools import reduce

#1- la funcion
def sumar(x,y):
    return x+y
#2- iterable
numeros = [1,2,3,4,5]
#3- aplicar reduce
resultado_reduce = reduce(sumar,numeros)

print(resultado_reduce)

# 1- la funcion
def unir_cadenas(x, y):
    return x + " " + y

# 2- iterable (lista de cadenas)
palabras = ["Python", "es", "muy", "genial"]

# 3- aplicar reduce
resultado_reduce = reduce(unir_cadenas, palabras)

# 4- imprimir
print(resultado_reduce)