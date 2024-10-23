"""
* Diferentes maneras de recorrer matrices en Python
"""

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1
i = 0
while i < len(matriz):
    print(matriz[i])
    i += 1

# 2
for i in range(len(matriz)):
    print(matriz[i])

# 3
for filas in matriz:
    print(filas)

numero = -17 * -1

# if numero < 0:
#     numero = numero * -1

print(numero)  # Imprime: 17
