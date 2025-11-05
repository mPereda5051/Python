"""En lugar de return usamos yield (lo que convierte a la función en un generador).
Esto permite devolver los valores uno a uno, sin almacenar la lista en memoria
yield es más eficiente en memoria que return con listas grandes."""
def par(inicio, fin):
    for i in range(inicio, fin):
        if i % 2 == 0:
            yield i

# ----------------- Uso y resultados paso a paso -----------------

datos = par(inicio=1, fin=5)

# La primera llamada a next() ejecuta el código hasta el primer 'yield'
print(next(datos))

# La segunda llamada a next() retoma la ejecución justo después del 'yield' anterior
print(next(datos))

# Si llamas de nuevo, buscaría el siguiente par (que sería 4 en este caso)
# print(next(datos))