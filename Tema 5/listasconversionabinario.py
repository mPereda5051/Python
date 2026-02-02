numeros = [3, 5, 10, 15]

binarios = [bin(n)[2:] for n in numeros]

print(binarios)

numeros2 = [3, 5, 10, 15]
binarios2 = []

for n in numeros:
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2
    binarios.append(binario)

print(binarios)
