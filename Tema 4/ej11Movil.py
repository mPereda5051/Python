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
class Telefono():
    def __init__(self, numero):
        self.numero = numero

    def telefonear(self):
        print("Llamando a: ", self.numero)
    def colgar(self):
        print("Colgando a: ", self.numero)
    def __str__(self):
        print(self.numero)
class Camara():
    def __init__(self, mpx):
        self.mpx =mpx

    def fotografiar(self):
        print("fotografiando en: " + self.mpx +"mpx")

    def __str__(self):
        print(self.mpx)
class Reproductor():
    def __init__(self, capacidad):
        self.capacidad = capacidad
    def reproducirmp3(self):
        print("Reproduciendo mp3")
    def reproducirVideo(self):
        print("Reproduciendo video")
    def __str__(self):
        print("Capacidad: " + self.capacidad)
class Movil(Telefono,Camara,Reproductor):
    def __init__(self):
        super().__init__(self.numero)
        super().__init__(self.mpx)
        super().__init__(self.capacidad)
    def __str__(self):
        msg = "Numero: {0}, mpx: {1}, capacidad: {2}"
        return msg.format(self.numero,self.mpx,self.capacidad)



miMovil = Movil(6,12,200)
print(dir(miMovil))
print(miMovil)
