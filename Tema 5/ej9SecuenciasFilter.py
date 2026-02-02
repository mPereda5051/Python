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

# la funcion filter construye un iterador con los elementos que cumplen una funcion

# 1- la funcion
def empieza_con_vocal(cadena):
    # devuelve True o False
    return cadena[0].lower() in "aeiou"

# 2- el iterable (lista de cadenas)
palabras = ["auto", "casa", "elefante", "perro", "iglesia", "sol", "uva"]

# 3- aplicar filter
resultado_filter = filter(empieza_con_vocal, palabras)

# 4- convertir a lista
palabras_con_vocal = list(resultado_filter)

# 5- imprimir
print("Lista resultado:", palabras_con_vocal)
