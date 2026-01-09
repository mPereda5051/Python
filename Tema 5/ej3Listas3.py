#metodos de insercion en listas
lista =[1,2,3]
lista.append(4)
print("lista= ", lista)
lista2=[5,6]
lista.extend(lista2)
print("lista= ",lista)
lista.insert(1,100)
print("lista= ", lista)
print("lista.pop()= ", lista.pop())
print("lista.pop()= ", lista.pop(1))
lista.remove(3)
print("lista.remove(3)= ", lista)
#ordenar la lista
lista.reverse()
print("lista= ", lista)
lista.sort()
print("Lista.sort()= ", lista)
lista.sort(reverse=True)
print("Lista= ", lista)
lista=["hola", "que", "tal", "Hola","Que","Tal" ]
lista.sort()
print("lista =", lista)
lista =[1,2,3,4,5]
print("Cuantos 5 hay?", lista.count(5))
print("En que posicion esta el 5", lista.index(5))
print("que numero sale", lista.index(5,1,4))
#sale -1 y error
