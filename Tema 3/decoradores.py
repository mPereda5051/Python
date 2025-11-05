"""tablas es un decorador: una función que recibe otra función (funcion)
y devuelve una nueva función (envoltura)."""
def tablas(funcion):
    """envoltura imprime una cabecera, ejecuta la función decorada 11 veces (de 0 a 10),
    y luego imprime una línea de cierre."""
    def envoltura(tabla=1):
        print(f'Tabla del %i:' %tabla)
        print('-' * 15)
        for numero in range(0, 11):
            funcion(numero, tabla)
        print('-' * 15)
    return envoltura

#Decoradores (@)
@tablas
def suma(numero, tabla=1):
    print(f'%2i + %2i = %3i' %(tabla, numero, tabla+numero))

@tablas
def multiplicar(numero, tabla=1):
    print(f'%2i X %2i = %3i' %(tabla, numero, tabla*numero))