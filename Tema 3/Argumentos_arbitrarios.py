def sumar(n, *args):
    resultado = n
    for i in args:
        resultado += i
        return resultado


print(sumar(2))
print(sumar(2, 3, 4))
