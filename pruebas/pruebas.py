nombre = "Lucas"
# 10 (no inclusivo - incluido)
print(nombre[2:10])


# def cuadrado(x):
#     return x**2

# Función lambda
cuadrado = lambda x: x**2

# Usando map
numeros = [1, 2, 3, 4]
resultado = map(cuadrado, numeros)
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


# OTRO EJERCICIO --------------------------------------------------------------------------------------------------

animal1 = "cat"
animal2 = "dog"

arreglo = []
for i in animal1:
    arreglo.append(i)

arreglo2 = []
for i in animal2:
    arreglo2.append(i)

# copia = arreglo[:]
# copia = list(arreglo)
# copia = arreglo.copy()
arreglo[0], arreglo2[0] = arreglo2[0], arreglo[0]
print(arreglo)
print(arreglo2)

nueva_cadena = ""
for i in arreglo:
    nueva_cadena += i
print(nueva_cadena)

nueva_cadena2 = ""
for i in arreglo2:
    nueva_cadena2 += i
print(nueva_cadena2)


# Otra manera
def creandoPalabras(a: str, b: str) -> tuple[str, str]:
    a_list = list(a)
    b_list = list(b)

    a_list[0], b_list[0] = b_list[0], a_list[0]

    return "".join(a_list), "".join(b_list)

    # return b[0] + a[1:], a[0] + b[1:]


a, b = creandoPalabras("cat", "dog")
print(a)
print(b)
