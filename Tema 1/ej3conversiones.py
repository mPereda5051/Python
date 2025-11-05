#hay conversiones explicitas e implicitas.
#1-Implicita(automatica)
entero = 5
decimal = 2.5

resultado = entero + decimal #python convierte el entero a decimal
print(resultado)
print(type(resultado))

#2-explicito (forzada por el programador)
numero_str = "42"
numero_int = int(numero_str)
print(numero_int)
print(type(numero_int))
#Convertimos de float a entero (pierdo decimales)

pi= 3.14159

entero_pi = int(pi)
print(entero_pi)
print(type(entero_pi))

#de entero a string

edad= 30
mensaje = " Tienes " + str(edad) + " años."
print(mensaje)
print(type(mensaje))

#boolean a entero
valor = True

resultado = int(valor)
print (resultado)