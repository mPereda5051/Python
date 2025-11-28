from ej9Punto import Punto,Punto3d
p1=Punto(3,4)
print("Coordenadas del punto 1: ",p1)
print("¿Que tiene la clase punto: ", dir(p1))

miPunto3D = Punto3d(3,4,5)
print("¿Que tiene la clase punto3d?: ". dir(miPunto3D) )

otroPunto3d = Punto3d(6,7,8)
print("Distancia entre dos puntos en 3D: ", miPunto3D.distancia(otroPunto3d))
