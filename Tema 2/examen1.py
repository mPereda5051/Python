# Ejercicio vuelta ciclista - 10 octubre

total_km = 0  # Total de kilómetros recorridos
dia = 1       # Contador de días

try:
    while True:
        km = int(input("Introduce km recorridos (0 para terminar): "))

        if km == 0:
            break  # Termina cuando se introduce 0

        # Control de errores: no se puede pasar de 30 km
        if km > 30:
            print("Error: no puedes recorrer más de 30 km en un día.")
            continue

        # Cada día se hace ida y vuelta, por eso se multiplica por 2
        total_km += km * 2
        dia += 1

    print(f"Distancia total (ida y vuelta): {total_km} km")

except ValueError:
    print("VALOR NO VÁLIDO")
