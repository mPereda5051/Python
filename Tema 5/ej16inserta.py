#crea un programa que lea por teclado una cadena y un caracter
#e inserte el caracter entre cada letra de cadena
cad = input("escribe algo: ")
#simbolo = input("escribe un simbolo: ")
#cadLenght = len(cad)
#resultado = simbolo.join(cad)
#rint(resultado)

#reemplazar todos los caracteres de la cadena
#buscar= cad
#resultado= cad.replace(buscar, simbolo * cadLenght)

#print(resultado)

#3 lee dos cadenas e indica la seguna cadena es subcadena de la 1
#ademas muestra la primera en orden alfabetico
cad1 = input("Escribe algo")
cad2 = input("Escribe otra cosa")
if cad1.find(cad2):
    print("Es subcadena")
else:
    print("No es subcadena")

#4 dada una palabra indica si es palindromo
verify = cad[::-1]
if cad == verify:
    print("Es palindromo")
else:
    print("No es palindromo")
