from os import write

with open("files/logs.dat", "r") as f:
    a = open("files/info.txt", "w", encoding="utf-8")
    b= open("files/error.txt", "w", encoding="utf-8")
    c= open("files/warning.txt", "w", encoding="utf-8")

    lineas = f.readlines()

    for linea in lineas:
        if "[INFO]" in linea:
            a.write(linea)
        elif "[WARNING]" in linea:
            c.write(linea)
        elif "[ERROR]" in linea:
            b.write(linea)
        else:
            print("error")

    a.close()
    b.close()
    c.close()