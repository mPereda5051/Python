class Gato():
    def hablar(self):
        print("MIAU")

class  Perro():
    def hablar(self):
        print("Guau")


def escucharMascota(animal):
    animal.hablar()

miGato = Gato()
miPerro = Perro()
escucharMascota(miGato)
escucharMascota(miPerro)
