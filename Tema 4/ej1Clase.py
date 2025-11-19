#Primera clase (Se nombran en mayusculas)
class Clase():
    #atributo de clase, le damos valor 1
    at_clase = 1
    #Metodo que referencia al objeto que utiliza este metodo
    def metodoInventoParaInicializar(self):
        #atributo del metodo y por tanto del objeto (no de la clase)
        self.at_objeto=1

#Crear un objeto de la clase
objeto = Clase()
print(type(objeto))

#Vamos a ver el valor del atributo de la clase
print(Clase.at_clase)
#para ver el valor del atributo del objeto, tengo que llamar al metodo que crea el atributo
objeto.metodoInventoParaInicializar()
#una vez inicializado el valor del atributo del objeto, pùedo mostrarlo
print(objeto.at_objeto)
