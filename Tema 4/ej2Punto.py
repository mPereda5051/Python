"""Representacion de un punto en el plano, atributos x,y
    Los metodos especiales empiezan y terminan con __
    Los atributos de objeto se inicialiaz en el constructor llamado__init__"""
import math


class Punto():
    def __init__(self, x=0,y=0):
        self.x =x
        self.y = y
    def mostrar(self):
        print(self.x," ",self.y)

    def distacia(self,otro):
        diferencia = math.sqrt((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2)
        print("la distancia es: ", diferencia)

punto1=Punto()
punto1.mostrar()
punto2 = Punto(4,5)
punto2.mostrar()
punto1.distacia(punto2)