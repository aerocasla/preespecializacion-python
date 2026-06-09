## map() + filter()

numeros = list(range(100000))

resultado = list(
    map(
        lambda n: n ** 2,
        filter(lambda n: n % 2 == 0, numeros)
    )
)

print(resultado[:10])