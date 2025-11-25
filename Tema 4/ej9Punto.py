#vamos a ver un ejemplo de herencia
class Punto():
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    #Definimos una propiedad para obtener el valor de x
    @property
    def x(self):
        return self._x
    #Actualizar el valor de x(setter)
    @x.setter
    def x(self,x):
        self._x=x
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,y):
    #Visualizar los datos
    def __str__(self):
