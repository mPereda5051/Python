#Lectura dse ficheros
#opcion 1
f = open("files/temps.dat")
#read carga todo el archivo en memoria RAM a la vez
contenido = f.read()
print(contenido)
f.close() #imprescindible cerrarlo despues de open
#opcion 2
print("\n**Opcion 2 con lista")
f = open("files/temps.dat")
#leemos todas lass lineas y las guardamos en una lista
lineas = f.readlines()
#mostramos recoriendo la lista
for linea in lineas:
    print(linea.strip())
f.close()

#opcion 3
print("\n**Opcion 3 linea a linea")
f = open("files/temps.dat")

for line in f:
    print(line.strip())
f.close()