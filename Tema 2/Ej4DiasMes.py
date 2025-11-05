#programa que pide un numero entero e imprime el numero de dias del mes
#si meto 5 debe decir "31"

numero = int(input("escribe un numero entre 1 y 12"))

if numero >= 1 <=12 :
    if numero == 1 or numero ==3 or numero==5 or numero == 7 or numero == 8 or numero ==10 or numero ==12 :
        print("Este mes tiene 31 dias")
    elif numero == 4 or numero == 6 or numero == 9 or numero == 11:
        print("Este mes tiene 30 dias")
    else:
        print("Este mes tiene 28 o 29 dias")
    
else:
    print("elige un numero valido")