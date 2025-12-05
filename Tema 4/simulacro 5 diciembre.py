class DNIMiguel:
    def __init__(self,numero,letra):
        self.numero = numero
        self.letra = letra
        
    @property
    def numero(self):
        return._numero
    
    @numero.setter
    def numero(self,numero):
        self.numero = numero
        
    @property
    def letra(self):
        return._letra
    
    @letra.setter
    def letra(self,letra):
        self.letra = letra
    
    def __str__(self):
        return f"DNI de miguel: {self.numero} {self.letra}"
class PersonaMiguel(DNIMiguel):
    def __init__(self,numero,letra,nombre,edad):
        DNIMiguel.__init__(self, numero,letra)
        self.nombre = nombre
        self.edad = edad
    @property
    def nombre(self):
        return._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.nombre = nombre
    @property
    def edad(self):
        return._edad
    
    @edad.setter
    def edad(self,numero):
        self.edad = edad
    
    def __str__(self):
        return f"Persona= {self.nombre} con edad {self.edad} y dni {self.numero}{self.letra}"

class NotasMiguel:
    def __init__(self):
        self.nota = nota
        self.materia = materia
        
    def addnotas(*self):
        asignatura= self.materia
        calificacion= self.nota
    def modnotas(self.materia,self.nota)
        asignatura= self.materia
        calificacion= self.nota
    
    @nota.deleter
    def delnotas(self):
        del self._nota
    def __str__(self):
        return f"{asignatura} = {calificacion}"
    
    
        
    