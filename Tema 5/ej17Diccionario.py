#dictionario, tipo de datos mutable parecidos a json, son clave-valor

diccionario = dict(one=1, two=2, three=3)
print(diccionario)
diccionario2 = {"one":1, "two":2, "three":3}
print(diccionario2)
dic3 = dict(zip(["one","two","three"],[1,2,3]))
print(dic3)
dic4 = dict([("two",2),("one",1),("three",3)])
print(dic4)
dic5 = {}
dic5["one"] =1
dic5["two"]=2
dic5["three"]=3
print(dic5)

#operaciones basicas
print("len: ", len(dic5))
print("Poisicion:", dic5["one"])
#copia del diccionario
dic6 = dic5.copy()
del(dic5["one"])

print("dict5 tras borrar:", dic5)
print("¿Estas dos?", "two" in dic5)
dic5.clear()
print("dict5 tras borrar:", dic5)
print(dic6)

dic7 = {"four":4,"five":5,}
print("dic7:", dic7)

dic6.update(dic7)
print("Dict6 ahora:", dic6)
print("el cuatro", dic6.get("four"))
#ahora el pop
print("el cuatro con pop", dic6.pop("four"))
print("Dict6 ahora:", dic6)
print("el cuatro con popitem", dic6.popitem())
print("Dict6 ahora:", dic6)
print("Lista de items: ", dic6.items())
print("Lista de claves: ", dic6.keys())

#ver las claves con bucles
for clave in dic6.keys():
    print(clave)
#ver los valores con bucles
for clave in dic6.values():
    print(clave)

#todo junto
for clave,valor in dic6.items():
    print(clave, "Con valor: ", valor)