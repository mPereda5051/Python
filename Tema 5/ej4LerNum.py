#leer un numero por pantalla
num = int(input("Numero: "))
lista=[]
while num >= 0:
    lista.append(num)
    num = int(input("NUmero: "))

print("Y el mayor de la lista es: %d", max(lista))

for n in lista:
    if n % 2 == 0:
        print(n, end=" ")