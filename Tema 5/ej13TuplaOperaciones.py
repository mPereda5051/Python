#acceder a elementos
datos_persona= ('ana',30,'Madrid')
nombre = datos_persona[0]
print(f"Nombre: {nombre}")
#ultimom elemento
ciudad = datos_persona[-1]
print(f"Ciudad: {ciudad}")
#desempaquetado
tupla1 = 1,2,3
a,b,c = tupla1
print("Valor de a:", a)
nueva_tupla1 = tupla1 + (4,)
print("nueva_tupla:",nueva_tupla1)
tupla2= (1,2,3,4,5,1,5,4,3,4,6)
#contar 1
print("¿Cuantos 1 hay en la tupla?")
print(tupla2.count(1))
print("Posicion del numero 2")
print(tupla2.index(2))
print("Posicion del numero 1")
print(tupla2.index(1))
print("Posicion del otro numero 1")
print(tupla2.index(1,2))

print("Posicion del otro numero 1 entre 2 y 6")
print(tupla2.index(1,2,6)) #pregunta tipo test