#Programa que pide un nombre de usuario y una contraseña
#si se introduce pepe y pepepws muestra "Has entrado al sistema"
#Si no "Usuario incorrecto"
#Hay que usar and

usuario= input("Usuario: ")
contraseña= input("Contraseña: ")

if usuario == "pepe" and contraseña == "pepepwd":
    print("Has entrado al sistema")
else:
    print("Usuario incorrecto")
