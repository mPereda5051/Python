# -------------------------------
# Clase DNIMiguel
# -------------------------------
class DNIMiguel:
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    def __init__(self, numero):
        self.numero = numero  # cadena de 8 dígitos
        self.letra = self.calcular_letra()

    def calcular_letra(self):
        return DNIMiguel.letras[int(self.numero) % 23]

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        if len(numero) != 8 or not numero.isdigit():
            raise ValueError("El número debe tener 8 dígitos.")
        self._numero = numero
        self._letra = self.calcular_letra()

    @property
    def letra(self):
        return self._letra

    def __str__(self):
        return f"{self.numero}{self.letra}"


# -------------------------------
# Clase PersonaMiguel
# -------------------------------
class PersonaMiguel:
    def __init__(self, numero_dni, nombre, edad):
        self.dni = DNIMiguel(numero_dni)
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, {self.edad} años, DNI: {self.dni}"


# -------------------------------
# Clase NotasMiguel (SIN diccionarios)
# -------------------------------
class NotasMiguel:
    def __init__(self):
        self.asignaturas = []  # lista de asignaturas
        self.notas = []        # lista de notas paralela

    def addnotas(self, asignatura, nota):
        self.asignaturas.append(asignatura)
        self.notas.append(nota)

    def modnotas(self, asignatura, nueva_nota):
        if asignatura in self.asignaturas:
            idx = self.asignaturas.index(asignatura)
            self.notas[idx] = nueva_nota
        else:
            print("La asignatura no existe.")

    def delnotas(self, asignatura):
        if asignatura in self.asignaturas:
            idx = self.asignaturas.index(asignatura)
            self.asignaturas.pop(idx)
            self.notas.pop(idx)
        else:
            print("No se puede borrar, la asignatura no existe.")

    def media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        texto = ""
        for asign, nota in zip(self.asignaturas, self.notas):
            texto += f"{asign}: {nota}\n"
        return texto.strip()


# -------------------------------
# Clase AlumnoMiguel
# -------------------------------
class AlumnoMiguel(PersonaMiguel, NotasMiguel):
    def __init__(self, numero_dni, nombre, edad):
        PersonaMiguel.__init__(self, numero_dni, nombre, edad)
        NotasMiguel.__init__(self)

    def __str__(self):
        return (
            f"Alumno: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}\n"
            f"Notas:\n{NotasMiguel.__str__(self)}"
        )
