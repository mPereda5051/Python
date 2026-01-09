lista=["1234","admin","password","segura","admin123", "admin"]
print("Lista de contraseñas actuales:", lista)
password = input("Introduce tu contraseña: ")
if password in lista:
    print("Esa pw ya la has usado muchas veces, total: ", lista.count(password),"veces")
    #Pide una nueva contraseña y cambiala por esta repetida
    lista.remove(password)
    password = input("Introduce una nueva contraseña: ")
    lista.append(password)
    print("lista de contraseñas: ", lista)
    #hacer un bucle para borrar todas las coincidencias     cf

else:
    print("Muy bien, nueva password")