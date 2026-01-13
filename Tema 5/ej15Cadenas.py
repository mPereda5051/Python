#las cadenas son secuencias de caracteres. Inmutable
from numpy.testing.print_coercion_tables import print_new_cast_table

cad ="Hola"
cad2 ="Que tal?"
cad3= '''Hola,
            que tal'''

print(cad,cad2,cad3)
#tambien se pueden crear cadenas con str a partir de
cad4 = str(1)
cad5 = str(2.45)
cad6 =str([1,2,3])
print(cad4,cad5,cad6)
print("a">"A")
cad7 = "hola, como estas"
print(cad7.capitalize())#la primera en mayuscula

cad8="Hola Mundo"
print(cad8.lower())
print(cad8.swapcase().title())
cad9 = "Hola esto es una frase larga"
print(cad9.title())
print(cad9.center(50))
print(cad9.ljust(50,"="))
print(cad9.rjust(50,"="))

#busqueda
cad10 = "bienvenido a mi aplicacion web"
print(cad10, cad10.count('a'))
print(cad10, cad10.count('a', 16))
print("posicion de mi", cad10.find("mi"))
print("cad10.startswith('b'))", cad10.startswith('b'))
print("cad10.endswith('b'))", cad10.endswith('b'))

#sustitucion
cad11 = "Estimado señor nombre apellido:"
buscar = "nombre apellido"
cambiar_por= "Juan Perez"
print(cad11.replace(buscar,cambiar_por))

cad11Aux =cad11[5:9]
print("cad11Aux:",cad11Aux)
cad11Aux2 =cad11[5:]
print("cad11Aux:",cad11Aux2)
cad11Aux3 =cad11[::-1]
print("cad11Aux:",cad11Aux3)

risas= "ja"*3
print(risas)

cad12 = "000000123000000"
print(cad12.strip("0"))

cad13 ="Hola"
print(type(cad13))
print(id(cad13))
cad13 = cad13 + " que tal"
print(cad13)
print(id(cad13))

lista1 =[1,2,3,4]
print(type(lista1))
print(lista1)
print(id(lista1))
lista1.append(5)
print(lista1)
print(id(lista1))