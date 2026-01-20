import csv

with open("files/alumnos.csv", "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    for fila in lector:
     #cada fila es una lista
     print(f"Nombre: {fila[0]},Edad: {fila[1]},Ciudad: {fila[2]}")

#Opcion 2 con pandas
import pandas as pd

#panda integraen la misma linea el with y el close
df = pd.read_csv("files/alumnos.csv")
print("Leemos las primeras 5 lineas")
print(df.head())

#calcular la media de la columna edad
print("La media de edad de los alumnos es: ", df["edad"].mean())