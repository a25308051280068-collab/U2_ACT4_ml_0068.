# importar librerias
print("Christian Garcia jimenez Nc = 0068")
import pandas as pd
import numpy as np

# variables
n_filas = 5
n_columnas = 5
tag_columnas = tuple("ABCDE") # etiquetas para las columnas
print(tag_columnas)

# definir
# Nota: Si deseas que los números aleatorios lleguen hasta 10, puedes cambiar 6 por 11 en randint(1, 11)
matriz = np.random.randint(1, 6, size=(n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre  1 y 10")
print(matriz)
# la variable df es dataframe 

# Se cambió 'columna=' por 'columns='
df = pd.DataFrame(matriz, columns=tag_columnas)
print(" ------ la tabla o dataframe ---- nc = 0068  ")
print(df)
print(" ------ Christian Gaeracia Jimenez  ")