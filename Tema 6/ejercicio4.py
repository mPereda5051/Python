
with open("files/temperaturas.txt", "r") as f, open("files/TemperaturasAltas.txt", "w", encoding="utf-8") as a:
    lineas = f.readlines()
    for linea in lineas:
        if int(linea) > 20:
            a.write(linea)
    a.close()