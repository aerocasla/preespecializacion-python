import numpy as np

# Creamos una matriz de 2 filas y 3 columnas (matriz 2D)
inventario = np.array([
    [15, 22, 40], # Tienda A: [Prod1, Prod2, Prod3]
    [8, 31, 12]   # Tienda B: [Prod1, Prod2, Prod3]
])

print("--- Auditoría de la Estructura de Datos ---")
print("Número de dimensiones (ndim):", inventario.ndim)
print("Forma/Estructura (shape):", inventario.shape)
print("Total de elementos (size):", inventario.size)
