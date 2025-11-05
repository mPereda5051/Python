cuadrado = lambda x:x**2
print(cuadrado(2))

lambda x: x**2

print((lambda x: x**2)(3))


pares =[(1,'uno'),(2,'dos'),(3,'tres'),(4,'cuatro'),]

pares.sort(key=lambda pair: pair[1])
print(pares)