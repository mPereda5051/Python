def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numeros = (2, 5, 8, 11, 14, 17, 20, 23)

primos = tuple(n for n in numeros if es_primo(n))

print(primos)
