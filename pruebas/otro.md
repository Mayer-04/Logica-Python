# Platzi

## ¿Qué es la abstracción en programación orientada a objetos?

La abstracción te permite definir estructuras básicas sin entrar en detalles específicos. En el código, hemos creado instancias de diferentes vehículos, como un auto, una bicicleta y un camión, asignándoles atributos como marca, modelo y precio. Este enfoque nos permite trabajar con conceptos generales antes de precisar características específicas.

## ¿Cómo se aplica el encapsulamiento?

El encapsulamiento se refiere a mantener los datos privados dentro de una clase y acceder a ellos solo mediante métodos públicos. En nuestro ejemplo, las variables de instancia de los vehículos son privadas. Solo podemos acceder a ellas a través de métodos específicos, como GetPrice o verificarDisponibilidad, asegurando así que los datos se manejen de manera controlada y segura.

## ¿Qué rol juega la herencia?

La herencia permite que una clase hija adopte atributos y métodos de una clase padre. Aquí, la clase auto hereda de la clase vehículo, lo que significa que todas las características y comportamientos definidos en vehículo están disponibles en auto sin necesidad de duplicar el código. Este principio facilita la reutilización y extensión del código.

## ¿Qué es el polimorfismo y cómo se usa?

El polimorfismo permite que diferentes clases respondan a los mismos métodos de maneras distintas. En nuestro caso, tanto el auto como la bicicleta heredan métodos de vehículo, pero cada uno los implementa de forma diferente. Por ejemplo, el método para indicar que el auto está en marcha difiere del método de la bicicleta, que no usa motor. Este comportamiento flexible es clave para escribir código más dinámico y reutilizable.

## PLatzi 2 ------------------------------------------

Trabajar con iteradores y generadores en Python permite manejar grandes cantidades de datos de manera eficiente, sin necesidad de cargar todo en memoria.

¿Qué es un iterador y cómo se usa?
Un iterador en Python es un objeto que permite recorrer todos los elementos de una colección, uno a la vez, sin necesidad de usar índices. Para crear un iterador, se utiliza la función iter() y para obtener el siguiente elemento, se usa la función next(). Veamos un ejemplo:

# Crear una lista

lista = [1, 2, 3, 4]

# Obtener el iterador de la lista

iterador = iter(lista)

# Usar el iterador para obtener elementos

print(next(iterador)) # Imprime: 1
print(next(iterador)) # Imprime: 2
print(next(iterador)) # Imprime: 3
print(next(iterador)) # Imprime: 4

# Intentar obtener otro elemento después de finalizar la iteración

print(next(iterador)) # Esto generará una excepción StopIteration
Los iteradores también pueden recorrer cadenas de texto:

# Crear una cadena

texto = "hola mundo"

# Obtener el iterador de la cadena

iterador_texto = iter(texto)

# Iterar a través de la cadena

for caracter in iterador_texto:
print(caracter)
¿Cómo crear un iterador con range para números impares?
La función range se puede usar para crear un iterador que recorra números impares:

# Crear un iterador para números impares hasta 10

limite = 10
iterador_impares = iter(range(1, limite + 1, 2))

# Iterar a través de los números impares

for numero in iterador_impares:
print(numero)
Para cambiar a números pares, solo se debe modificar el inicio del rango:

# Crear un iterador para números pares hasta 10

iterador_pares = iter(range(0, limite + 1, 2))

# Iterar a través de los números pares

for numero in iterador_pares:
print(numero)
¿Qué es un generador y cómo se utiliza?
Un generador es una función que produce una secuencia de valores sobre los cuales se puede iterar, usando la palabra clave yield en lugar de return. Aquí hay un ejemplo básico:

def mi_generador():
yield 1
yield 2
yield 3

# Usar el generador

for valor in mi_generador():
print(valor)
¿Cómo crear un generador para la serie de Fibonacci?
La serie de Fibonacci es una secuencia donde cada número es la suma de los dos anteriores. Podemos crear un generador para producir esta serie:

def fibonacci(limite):
a, b = 0, 1
while a < limite:
yield a
a, b = b, a + b

# Usar el generador para la serie de Fibonacci hasta 10

for numero in fibonacci(10):
print(numero)

## cadenas ---------------------------------------------------------------------------------------

¿Cómo se indexan las cadenas en Python?
Las cadenas son colecciones ordenadas y accesibles por índices. Puedes acceder a un carácter específico utilizando corchetes:

name = 'Carly'
print(name[0]) # Imprime 'C'
print(name[-1]) # Imprime 'y'
¿Qué pasa si intentas acceder a un índice que no existe en Python?
Si intentas acceder a un índice fuera del rango de la cadena, Python arrojará un IndexError:

print(name[20]) # Genera IndexError

## Input ------------------------------------------------------------------------------------------

En Python, cuando trabajamos con proyectos que requieren interacción del usuario, es común solicitar datos como correo o contraseña para ejecutar acciones específicas. Este mismo enfoque es útil para entender la función input.

¿Cómo se recibe información del usuario en Python?
Para recibir información del usuario desde la consola, creamos una variable y asignamos el resultado de la función input. Por ejemplo, para pedir el nombre del usuario:

nombre = input("Ingrese su nombre: ")
print(nombre)
Al ejecutar este código, se habilita una sección para introducir información. Ingresamos un nombre, presionamos Enter y se imprime el valor guardado en la variable nombre.

¿Qué ocurre si eliminamos la función print?
Si eliminamos print y ejecutamos el código, el nombre ingresado no se mostrará en la consola:

nombre = input("Ingrese su nombre: ")
Para ver el resultado, es imprescindible usar print.

Podemos solicitar la edad del usuario creando una variable edad y utilizando input, luego imprimimos ambos valores:

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print(nombre)
print(edad)
Al ejecutar, ingresamos el nombre y la edad, y ambos valores se muestran en pantalla.

¿Cuál es el tipo de dato devuelto por input?
El resultado de input es siempre un string, incluso si ingresamos un número. Podemos verificar el tipo de dato usando type:

name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
print(type(name))
print(type(age))
Al ejecutar, se mostrará que ambos valores son de tipo str.

¿Cómo se convierte el tipo de dato (casting)?
Si queremos que la edad sea un número entero en lugar de un string, usamos el casting:

age = int(input("Ingrese su edad: "))
Ejecutamos y verificamos que age ahora es un entero. También podemos convertir a otros tipos de datos, como flotantes:

age = float(input("Ingrese su edad: "))
¿Qué sucede si ingresamos un dato inesperado?
Si el código espera un entero, pero ingresamos un string, se produce un ValueError. Es importante manejar el tipo de datos correctamente para evitar errores:
