#escribe una funcion llamada cuadrado que dado un numero
#lo devuelva al cuadrado

def cuadrado(x):
    return x*x

#lista de numeros
numero = [1,2,3,4,5]
#la funcion map aplica una funcion a todos los elementos de una lista y devuelve un map
resultado_map=map(cuadrado,numero)
#convertir el map a lista
resultado_lista =list(resultado_map)
print(resultado_lista)