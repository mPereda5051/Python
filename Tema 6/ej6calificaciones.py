with open("files/notas.txt", "r", encoding="utf-8") as f:
    r = open("files/resultados.txt", "w",encoding="utf-8")
    lineas = f.readlines()
    for linea in lineas:
        f.