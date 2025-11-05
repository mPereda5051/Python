# Entrada de datos
distancia = float(input("Distancia entre los dos aparatos en metros: "))
velocidad_maxima = float(input("Velocidad máxima permitida en km/h: "))
segundos = float(input("Tiempo en segundos: "))

# Cálculo de la velocidad del vehículo en m/s y luego convertir a km/h
velocidad_m_s = distancia / segundos
velocidad_km_h = velocidad_m_s * 3.6

# Verificación de la velocidad y condición para multas
if velocidad_km_h <= velocidad_maxima:
    print("ok")
elif velocidad_maxima < velocidad_km_h <= velocidad_maxima * 1.2:
    print("multa")
else:
    print("puntos")
