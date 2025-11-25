#Ejemplo de clase con metodo estatico
from traceback import print_tb


class Calculadora():
    def __init__(self, nombre):
        self.nombre = nombre

    def modelo(self):
        return self.nombre

    @staticmethod
    def sumar(x,y):
        return x+y

calcu1 = Calculadora("Samuel")
print("Nombre de la calculadora: ", calcu1.modelo())
print("Llamada al metodo sumar: " , Calculadora.sumar(1,2))
print(calcu1.sumar(1,2))#funciona pero no tiene sentido

#uso de funciones
print("Nombre de la calculadora: ", getattr(calcu1, "nombre"))
setattr(calcu1,'nombre',"Jaime")
print("Nombre de la calculadora: ", getattr(calcu1, "nombre"))
#¿existe un atributo?
print("Hay atributo nombre? ", hasattr(calcu1,"nombre"))
#borrar atributo
delattr(calcu1, "nombre")
print("Nombre de la calculadora: ", getattr(calcu1, "nombre"))
