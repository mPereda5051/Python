def sumar(n1,n2):
    return n1 + n2

sumar(5,7)

#sumar(4)

def operar(n1,n2,operador='+',respuesta='El resultado es '):
    if operador == "+":
        return respuesta+str(n1+n2)
    elif operador == "-":
     return respuesta+str(n1-n2)
    else:
        return "Error"

print(operar(5,7))
print(operar(5,7,"-"))
print(operar(5,7,"-", "La resta es "))

###parametro *

def sumar2(n1,n2,*,op="+"):
    if op == "+":
        return n1 + n2
    elif op=="-":
        return n1 - n2
    else:
        return "error"

sumar2(3,2)
#con * para multiples argumentos
def suma_total(*numeros):
    return sum(numeros)
print(suma_total(1,2,3,4,5,6))
#ejemplo 3 mezclando argumentos normales y *
def describir_persona(nombre,*caracteristicas):
    print(f"Nombre: {nombre}")
    print("Caracateristicas: ")
    for n in caracteristicas:
        print(f"-{n}")

describir_persona("pepe","Espabilado", "feliz")

#-----------
def multiplicar(*valores):
    total = 1
    for n in valores:
        total*= n
        return total



valores= [2,3,4]
print(multiplicar(*valores))

def max(*numeros):
    resultado = 0
    resultado = numeros[0]
    for numero in numeros:
        if numero > resultado:
            resultado = numero
        
    return resultado

print(max(4, 6, 90))