def factorial(n):
    if n<0:
        raise ValueError("El factorial no esta definido para numeros negativos")
    if n == 0 or n ==1:
        return 1
    return n *factorial(n-1)

print(factorial(5))