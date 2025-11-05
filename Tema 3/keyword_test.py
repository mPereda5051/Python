def saludar(nombre="pepe",**kwargs):
    cadena=nombre
    for valor in kwargs.values():
        cadena=cadena+" "+valor
    return "Hola "+cadena

print(saludar())
print(saludar("juan"))
print(saludar("juan", nombre2="pepe", nombre3 ="maria"))
# def f()
#def f(a,b=1)
#def f(a,*args,b=1)
#def f(*args,b=1)
#def f(*args,b=1,*kwargs)
#def f(*args,*kwargs)
#def f(*args)
#def f(*kwargs)
