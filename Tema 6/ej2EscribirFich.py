#opcion 1
f = open("files/nuevo_archivo.txt", "w", encoding="utf-8")
#escribir un cadena simple
f.write("Hola, esta es la primera linea\n")
f.write("Y esta la segunda\n")
f.close()
print("Fichero generado correctamente")
f = open("files/nuevo_archivo.txt", "a", encoding="utf-8")
texto_añadido = "Texto añadido con append"
f.write(texto_añadido +"\n")
f.close()
print("Texto añadido correctamente")