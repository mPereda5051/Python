#dictionario, tipo de datos mutable parecidos a json, son clave-valor

diccionario = dict(one=1, two=2, three=3)
print(diccionario)
diccionario2 = {"one":1, "two":2, "three":3}
print(diccionario2)
dic3 = dict(zip(["one","two","three"],[1,2,3]))
print(dic3)
dic4 = dict([("two",2),("one",1),("three",3)])
print(dic4)