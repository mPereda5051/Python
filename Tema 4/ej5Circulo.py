class Circulo():
    def __init__(self,radio):
        self.set_radio(radio)

    def set_radio(self,radio):
        #indicamos el atributo _radio con _ por convencion para indicar que es privado
        if radio>=0:
            self._radio = radio
        else:
            self._radio = 0
            raise ValueError("El radio debe ser positivo")

    def get_radio(self):
        print("Estoy devolviendo el radio")
        return self._radio

circulo1 = Circulo(10)
print(circulo1.get_radio())

circulo2 = Circulo(-245)
print(circulo2.get_radio())