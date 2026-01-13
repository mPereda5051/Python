#Range: tipo de secuencia que perimte crear secuiencias/rangos de numeros
#inmutable, se suele utilizar para bucles
rango = range(0,10,2)#del 0 al 10 de dos en dos
print(type(rango))
print(rango)
print(list(rango))

#Propiedades de rango
print("Inicio:", rango.start)
print("Fin: ",rango.stop)
print("Intervalo: ", rango.step)
print("rango de 0 a 9", list(range(10)))
print("rango de 1 a 11", list(range(1,11)))
print("rango de multiplos de 5 hasta 30", list(range(0,30,5)))
print("rango de multiplos de 3 hasta 11", list(range(0,10,3)))
print("rango de 0 a -10", list(range(0,-11,-1)))


#recorrer un rango
for i in range(11):
    print(i,end=" ")
