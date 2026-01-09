lista1= [1,2,3,4]
lista2 = lista1[:]
lista1.sort()
print(lista2)
print(lista1)
if lista1 == lista2:
    print("lista ordenada")
else:
    print("Lista no ordenada")