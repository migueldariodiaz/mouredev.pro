# 1. Imprime "¡Hola Mundo!" por consola.
print("Hola mundo")

# 2. Escribe un comentario de una sola lÃ­nea explicando quÃ© hace el cÃ³digo del Ejercicio 1.
#El codigo del ejercicio imprime por la consola a traves de la funcion print(), el string que se le coloque entre comillas, en este caso "Hola mundo"

# 3. Imprime tu nombre y edad en la misma lÃ­nea utilizando la funciÃ³n print.
print("Hola, mi nombre es Miguel Diaz Hernandez y tengo 34 años de edad.")

# 4. Usa la funciÃ³n type() para imprimir el tipo de dato de una cadena de texto, un nÃºmero entero y un nÃºmero decimal.
print(type("Una cadena de texto")) # Cadena de texto
print(type(25)) # Numero entero
print(type(3.1416)) # Numero decimal

# 5. Escribe un comentario en varias lÃ­neas explicando quÃ© son los tipos de datos en Python.
"""
Algunos de los tipos de datos en python son:
"Cadenas de texto" --> <str> --> String
1, 2, 3... --> <int> --> Enteros
1.86, 2.82, 3.14, 4.74... --> <float> --> Decimales
True - False --> <bool> --> Booleanos
"""

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
print("Hola " + "Mundo")

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma lÃ­nea.
nombre = "Miguel Diaz Hernandez"
edad = 34
print("Hola, mi nombre es {} y tengo {} años de edad.".format(nombre, edad))

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
nombre = input("¿Cual es tu nombre? ")
print("Hola {}. Bienvenido al curso de Python en Mouredev.PRO".format(nombre))

# 9. Usa print() para mostrar el resultado de la suma de dos nÃºmeros enteros y el tipo de dato resultante.
print("Introduzca dos numeros enteros para que sean sumados: ") # Iniciamos con una bienvenida para indicar que se debe hacer luego
n1 = int(input("Introduzca el primer numero: ")) # Solicitamos el pirmer numero a sumar. Se coloca int() a la funcion input() para convertir el string que recojamos de la terminal.
n2 = int(input("Introduzca el segundo numero: ")) # Solicitamos el segundo numero a sumar. Se coloca int() a la funcion input() para convertir el string que recojamos de la terminal.
print("La suma de los dos numeros introducidos es: {}".format(n1 + n2)) # Imprimimos el resultado de la suma de los dos numeros suministrados.

# 10. Comenta el cÃ³digo del Ejercicio 9, y explica quÃ© hace cada lÃ­nea usando comentarios de una sola lÃ­nea.
