#perimetro de un poligono = dada una base b y una altura h
base = float(input("dime la base:"))
altura = float(input("Dime la altura:"))
perimetro = base*2+altura*2
area = base * altura
print("Resultado: area = ", area, "Perimetro= ", perimetro)
print("Resultado: Area=%d Perimetro=%d" %(area,perimetro))
print("Resultado: Area=%f Perimetro=%f" %(area,perimetro))

#f-strings
print(f"Resultado: Area= {area:.2f} Perimetro={perimetro:.2f}   ")
