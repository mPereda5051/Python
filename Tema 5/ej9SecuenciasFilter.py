#la funcion filter construye un iterador con los elementos que cumplen una funicion
#1-la funcion
def es_par(x):
    #la condicion debe devolver true o false
    return x % 2 == 0
#2-El iterable
numero =[1,2,3,4,5,6,7,8,9,10]

#3-aplicar filter
resultado_filter = filter(es_par, numero)
#4-convertir a lista
resultados_pares = list(resultado_filter)
#5-imprimir
print("Lista resultado:  ", resultados_pares)
