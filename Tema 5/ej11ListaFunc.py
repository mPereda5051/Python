#para transformar elementos se usa la estructura
#[expresion for elementos en iterable]
#list comprehension- mas legibles y mas directos
#crea una lista

numeros = [1,2,3,4]
cuadrados = [x*x for x in numeros]
print(cuadrados)
#otro ejemplo obtener pares usando list comprehension

pares = [x for x in numeros if x%2==0]
print(pares)

#usando comprehension eleva al cuadrado los numeros pares
numeroos = [1,2,3,4,5,6]
paresCuadrado = [x**2 for x in numeroos if  x%2==0]
print(paresCuadrado)
