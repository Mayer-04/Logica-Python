nombre = "Lucas"
# 10 (no inclusivo - incluido)
print(nombre[2:10])


# def cuadrado(x):
#     return x**2

# Usando map
numeros = [1, 2, 3, 4]
resultado = map(lambda x: x**2, numeros)
print("El resultado es: ", list(resultado))

# Cadena de texto
texto = "hola mundo"

# Usamos map() para convertir cada carácter a mayúsculas
resultados = map(str.upper, texto)

# Convertimos el objeto map a una lista para ver los resultados
lista_resultados = list(resultados)
print(lista_resultados)  # Salida: ['H', 'O', 'L', 'A', ' ', 'M', 'U', 'N', 'D', 'O']

print(texto)

# # Usamos map para llamar input varias veces
# respuestas = list(map(lambda x: input(f"Introduce valor para {x}: "), range(3)))


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
