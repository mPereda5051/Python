#variables enteras
x=3
print(x,"El tipo es:", type(x))
print(x+1);print(x-1);print(x*2);print(x **2)#potencia de...
#Mas ejemplos
x+=1
print(x)
x*=2
print(x)
print("XXXXXXXXXXXXXFloatXXXXXXXXXXXXXXX")
y = 2.5
print(y, "El tipo es: ", type(y))
print("XXXXXXXXXXXXXBooleanXXXXXXXXXXXXXXX")
t,f=True, False
print(t,f); print(type(t), type(f))
print(t and f)
print(t or f)
print(not t)
print(t != f)
print("XXXXXXXXXXXXXCadenasXXXXXXXXXXXXXXX")
hello = "hello"
world = "world"
print(hello, world, len(hello))
#cocatenacion
hw= hello + " " + world
print(hw)
#funciones sobre cadenas
s = "hello"
print (s.upper())
print(s.rjust(7))#justifica a la derecha con 7 espacios
print(s.replace("l", "ell"))#reemplaza una parte de la cadena por una nueva