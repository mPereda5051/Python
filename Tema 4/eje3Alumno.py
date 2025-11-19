class Alumno():
    contador=0
    nombre = "Los mariachis"
    def __init__(self, nombre=""):
        self.nombre = nombre
        Alumno.contador+=1



alum1=Alumno("Pepe")
alum2=Alumno("Luis")
alum3=Alumno("Jaime")
print("¿Cuantos alumnos hay? ", Alumno.contador)
print("¿Como se llama?", alum1.nombre)
print("Nombre clase", Alumno.nombre)