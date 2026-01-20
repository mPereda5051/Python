#El estandar de python es usar with
#su gran ventaja es que no es necesario el close()
with open("files/salida.txd","w",encoding="UTF-8") as f:
    f.write("Linea 1: configuracion inicial \n")
    f.write("Linea 2: proceso finalizado|n \n")

#al llegar aqui el fichero se ha cerrado correctamente
print("Fichero generado correctamente")

#concatenar
with open("files/salida.txd","a",encoding="UTF-8") as f:
    f.write("Linea 3:añadida con append\n")

#varias lineas a la vez
dias = ["Lunes\n","Martes\n", "Miercoles\n"]
with open("files/diasSemana.txt", "w", encoding="utf-8") as f:
    f.writelines(dias)

