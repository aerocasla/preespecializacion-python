import numpy as np

# Creamos una lista tradicional con los montos de compras de 3 clientes
lista_compras = [100, 50, 200]

#Convertimos esa lista en un array de numpy utilizando la función np.array()
array_compras = np.array(lista_compras)

# Imprimir el resultado y su tipo para verificar la transformación
print("Contenido del array: ", array_compras)
print("Tipo de estructura:", type(array_compras))
