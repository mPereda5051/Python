class Astro:
    def __init__(self,nombre,masa,diametro,periodo_rotacion, periodo_traslacion, distancia_media):
        
        self.nombre=nombre
        self.masa = masa
        self.diametro = diametro
        self.periodo_rotacion = periodo_rotacion
        self.periodo_traslacion = periodo_traslacion
        self.distancia_media = distancia_media
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def masa(self):
        return self._masa

    @masa.setter
    def masa(self, masa):
        self._masa = masa
    @property
    def diametro(self):
        return self._diametro

    @diamtro.setter
    def diametro(self, diametro):
        self._diametro = diametro
    @property
    def periodo_rotacion(self):
        return self._periodo_rotacion

    @periodo_rotacion.setter
    def periodo_rotacion(self, periodo_rotacion):
        self._periodo_rotacion = periodo_rotacion
    
    @property
    def periodo_traslacion(self):
        return self._periodo_traslacion

    @periodo_traslacion.setter
    def periodo_traslacion(self, periodo_traslacion):
        self._periodo_traslacion = periodo_traslacion
    
    @property
    def distancia_media(self):
        return self._distancia_media
    @distancia_media.setter
    def distancia_media(self, distancia_media):
        self._distancia_media = distancia_media
        
    def __str__(self):
        return f"{self.nombre} reconocido"

class Satelite(Astro):
    def __init__(self, planeta_orbita, nombre,masa,diametro,periodo_rotacion, periodo_traslacion, distancia_media):
        self.planeta_orbita = planeta_orbita
        Astro.__init__(self, nombre,masa,diametro,periodo_rotacion, periodo_traslacion, distancia_media)
        
    def __str__(self):
        return f"motramos la informacion del satelite: nombre: {self.nombre}, masa: {self.masa}, diametro: {self.diametro}, Periodo de rotacion: {self.periodo_rotacion}, Periodo de traslacion: {self.periodo_traslacion}, distancia media: {self.distancia_media}"
    
class Planeta(Astro):
    def __init__(self, satelites, nombre,masa,diametro,periodo_rotacion, periodo_traslacion, distancia_media):
        self.satelites = []
        Astro.__init__(self, nombre,masa,diametro,periodo_rotacion, periodo_traslacion, distancia_media)
        
    def agregar_satelite(self, satelite):
        self.satelites.append(satelite)
        
    def __str__(self):
        return f"motramos la informacion del planeta: nombre: {self.nombre}, masa: {self.masa}, diametro: {self.diametro}, Periodo de rotacion: {self.periodo_rotacion}, Periodo de traslacion: {self.periodo_traslacion}, distancia media: {self.distancia_media}"
    
   
   
    