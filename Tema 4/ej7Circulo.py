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
    #Podemos reescribir los metodos del sistema
    def __str__(self):
        clase = type(self).__name__
        msg = "{0} en mi mensaje de radio {1}"
        return msg.format(clase,self._radio)
    #otra forma de representar un objeto para desarrollo y depurar
    def __repr__(self):
        clase = type(self).__name__
        msg = "{0}({1})"
    #Puedo reescribir el metodo para comparar objetos
    def __eq__(self, otro):
        return self.radio == otro.radio
    #Puedo determinar como se suman circulos
    def __add__(self, other):
        self.radio += other.radio

circulo1= Circulo(5)
print(circulo1.radio )#Al estar tratando al metodo como un atributo no hay que poner ()
circulo1.radio = 8
print(circulo1.radio)
#borramos el atributo
print(circulo1.radio)
circulo2 = Circulo(7)
print(str(circulo2))

print(circulo1==circulo2)
circulo1 +circulo2
print(circulo1)