## filter() + lambda

numeros = list(range(100000))

pares = filter(lambda n:n % 2 == 0, numeros)

resultado = [n ** 2 for n in pares]

print(resultado[:10])
