#Define una clase telefono con atributo numero
#metodos:
#telefonear, imprime "llamando", clogar imprime "colgando", "str imprime "numero"

#Define una clase Camara con atributo mpx
#metodos:
#fotografiar, imprime "fotografiando", str imprime mpx

#Define una clase Reproductor con atributo capacidad
#metodos:
#reproducir mp3, imprime "reproduciendo mp3", reproducir video imprime "reproduciendo video", str imprime capacidad

#Define una clasew movil que hereda telefono, camara, reproductor.

#clase test miMovil(6666123456,12,2)
#print(dir(miMovil)
class Telefono:
    def __init__(self, numero):
        self.numero = numero

    def telefonear(self):
        print("llamando")

    def colgar(self):
        print("colgando")

    def __str__(self):
        return f"numero: {self.numero}"


class Camara:
    def __init__(self, mpx):
        self.mpx = mpx

    def fotografiar(self):
        print("fotografiando")

    def __str__(self):
        return f"{self.mpx} mpx"


class Reproductor:
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def reproducirmp3(self):
        print("reproduciendo mp3")

    def reproducirVideo(self):
        print("reproduciendo video")

    def __str__(self):
        return f"capacidad: {self.capacidad} GB"


class Movil(Telefono, Camara, Reproductor):
    def __init__(self, numero, mpx, capacidad):
        Telefono.__init__(self, numero)
        Camara.__init__(self, mpx)
        Reproductor.__init__(self, capacidad)

    def __str__(self):
        return f"Numero: {self.numero}, mpx: {self.mpx}, capacidad: {self.capacidad}GB"

miMovil = Movil(666612345, 12, 2)
print(dir(miMovil))
print(miMovil)