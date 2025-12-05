class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Propiedad x
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    # Propiedad y
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    # Visualizar los datos
    def __str__(self):
        return "{0}:{1}".format(self.x, self.y)

    # Distancia en 2D
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return (dx*dx + dy*dy) ** 0.5


class Punto3d(Punto):
    # Constructor
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    # Getter/Setter de z
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, nuevoZ):
        self._z = nuevoZ

    # Mostrar datos en 3D
    def __str__(self):
        return super().__str__() + ":" + str(self.z)

    # Distancia en 3D
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        dz = self.z - otro.z
        return (dx*dx + dy*dy + dz*dz) ** 0.5

