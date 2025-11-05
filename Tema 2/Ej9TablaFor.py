numero = int(input("Introduce un numero: "))

print(f"\nTabla de multiplicar del {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")