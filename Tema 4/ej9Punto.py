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
        self._y=y
    #Visualizar los datos
    def __str__(self):
        return "{}:{1}".format(self.x,self.y)
    def distancia(self,otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return (dx*dx + dy+dy)**0.5
    
#Definimos una clase Punto3d que reutiliza la clase punto
#con un atributo mas que es el eje z
class Punto3d(Punto):
    #Constructor
    def __init__(self, x=0, y=0, z= 0):
        super().__init__(x, y)
        self.z =Z

    #getter y setter
    @property
    def z(self):
        return self._z
    @z.setter
    def z(self,nuevoZ):
        self._z=nuevoZ
    
    def __str__(self):
        return super().__str__()+":"+str(self.z)
    
    #distancia en 3D
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        dz = self.z - otro.z
        return (dx *dx + dy *dy+dz*dz)**0.5
    
