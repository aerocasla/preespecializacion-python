## For + if
numeros = list(range(100000))

resultado = []

for num in numeros:
    if num % 2 == 0:
        resultado.append(num ** 2)

print(resultado[:10])
