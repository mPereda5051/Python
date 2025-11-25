#Encapsulacion, convertir metodos en atributos, decoradores
class Circulo():
    def __init__(self,radio):
        self.radio = radio #esto seria como un setter

    #Vamos a usar un decorador llamado @property para convertir un metodo en atributo
    #asi podremos acceder a los metodos directamente
    @property
    def radio(self):
        print("Estoy dando el radio en un metodo con decorador")
        return self._radio

    #es necesario definir un setter
    @radio.setter
    def radio(self,radio):
        if radio >= 0:
            self._radio = radio
        else:
            raise ValueError("Radio debe ser positivo")
            self._radio=0

    @radio.deleter
    def radio(self):
        del self._radio


circulo1= Circulo(5)
print(circulo1.radio )#Al estar tratando al metodo como un atributo no hay que poner ()
circulo1.radio = 8
print(circulo1.radio)
#borramos el atributo
del circulo1.radio
print(circulo1.radio)
