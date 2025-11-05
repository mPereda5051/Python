def sumar(n,*args):
    resultado=n
    for i in args:
        resultado+=i
    return resultado

lista = [1,2,3,4,5]
print(sumar(*lista))
print(sumar(2,*lista))
print(sumar(2,3,*lista))
