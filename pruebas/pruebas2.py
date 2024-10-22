# Usamos map para llamar input varias veces
# respuestas = list(
#     map(lambda x: int(input(f"Introduce valor para {x + 1}: ")), range(3))
# )
# print(respuestas)

# lista: int = []
# for i in range(10):
#     numeros = int(input(f"Introduce un número {i+1}: "))
#     lista.append(numeros)
# print(lista)


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# i = 0
# while i < len(matriz):
#     print(matriz[i])
#     i += 1

# for i in range(len(matriz)):
#     print(matriz[i])


for filas in matriz:
    print(filas)
