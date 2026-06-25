import random
import string

# Generar datos
datos_numericos = [random.randint(1, 100000) for _ in range(7500)]

datos_texto = [
    ''.join(random.choices(string.ascii_letters, k=6))
    for _ in range(7500)
]

# Combinar
datos = datos_numericos + datos_texto

# Menú de opciones
print("1. Orden ascendente")
print("2. Orden descendente")
print("3. Aleatorio")
print("4. Pares primero")
print("5. Impares primero")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    resultado = sorted(datos, key=str)

elif opcion == "2":
    resultado = sorted(datos, key=str, reverse=True)

elif opcion == "3":
    resultado = datos[:]
    random.shuffle(resultado)

elif opcion == "4":
    numeros = [x for x in datos if isinstance(x, int)]
    textos = [x for x in datos if isinstance(x, str)]

    pares = sorted([x for x in numeros if x % 2 == 0])
    impares = sorted([x for x in numeros if x % 2 != 0])

    resultado = pares + impares + textos

elif opcion == "5":
    numeros = [x for x in datos if isinstance(x, int)]
    textos = [x for x in datos if isinstance(x, str)]

    impares = sorted([x for x in numeros if x % 2 != 0])
    pares = sorted([x for x in numeros if x % 2 == 0])

    resultado = impares + pares + textos

print(resultado[:50])  # Mostrar solo una parte