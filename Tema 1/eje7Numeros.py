"""
Python trabaja con 3 tipos de datos numericos:

*Enteros(int) : positivos, negativos y 0 sin partedecimal ni limitacion
*Reales (float): numeros reales con parte decimal.
*complejos (complex): numeros complejos con parte real y parte imaginaria.

"""

entero = 7
print(entero, type(entero))
real = 7.2
print(real, type(real))
complejo = 1+2j
print(complejo, type(complejo))


"""
*Operadores aritmeticos:
+ - * / (devuelve un float // (division entera) % (modulo) ** (potencia))

*Funciones predefinidas que trabajan con numeros

abs, divmod, hex, oct, pow, round
"""
print(abs(-7)) #valor absoluto
print(divmod(7,2)) #devuelve la 
print(hex(255))#hexadecimal
print(oct(255))#Octal
print(bin(255))#Binario
print(pow(2,3))#Potencia
print(round(7.567,1))#Redondeo

#test
a=int(7.2);print(a)
a= int("345");print(a)
print(type(a))

b=float(1); print(b)
b=float("1.234");print(b)