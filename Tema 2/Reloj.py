#si el reloj marca las 3:15 serian las 8:45

#pedir hora y minutos al usuario

hora = int(input("Introduce la hora (1-12)"))
minutos = int(input("Introduce los minutos (0-59)"))

horaReal = 11- hora
minutosR = 60 - minutos

if hora >=1 and hora <=12:
    if minutos >=0 and hora <=59:
        print("Son las "+ horaReal+ " y " +minutosR)