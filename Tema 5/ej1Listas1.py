lista = [1,2,3,4,5,6]
print("Recorriendo la lista")
for num in lista:
    print(num, end=" ")

#Pertenencia
print("Esta el 2 en la lista?", 2 in lista)
print("El 8 no esta en la lista?", 8 not in lista)
#concatenar
lista = lista +[7,8,9]
print("nueva lista", lista)
#Repeticion
print("lista*2", lista*2)
#acceder
print("Elemento en posicion 3: ", lista[3])
#Slice (rebanada)
print("Subsecuencia de lista: ", lista[2:4])
#otro slice
print("Subsecuencia de lista: ", lista[1:4:2])
#num elementos
print("Longitud: ", len(lista))
#Maximo y minimo
print("Maximo: ", max(lista))
print("Minimo: ", min(lista))
#como es mutable, puedocmabiar un elemento
lista[2]=99
print("lista cambiada: ", lista)
lista[2:4] = [8,9,10]
print("lista cambiada: ", lista)
#borrado
del lista[5:]
print("Lista cambiada: ", lista)
lista*=2
print(lista)