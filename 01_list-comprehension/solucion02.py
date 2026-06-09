## List comprehension

numeros = list(range(100000))

resultado = [num ** 2 for num in numeros if num % 2 == 0]

print(resultado[:10])
