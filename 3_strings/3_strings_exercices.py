# 1. Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: "Hola" y "Python", y muestra el resultado en una sola lÃ­nea.
print("Hola" + " Python")

# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
text = "Esta es una cadena que contiene un\nsalto de linea"
print(text)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name, surname, age = "Miguel", "Diaz", 34
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprÃ­melos uno por uno.
p, y, t, h, o, n = "Python"
print(p)
print(y)
print(t)
print(h)
print(o)
print(n)
print(f"{p}{y}{t}{h}{o}{n}")

# 6. Extrae un "slice" de la palabra "ProgramaciÃ³n" para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.
text = "Programacion"
print(text[2:7])

# 7. Invierte la cadena "Python" usando slicing y muestra el resultado.
text = "Python"
print(text[::-1])

# 8. Convierte la cadena "aprendiendo python" en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.
text = "aprendiendo Python"
print(text.upper())

# 9. Cuenta cuÃ¡ntas veces aparece la letra "n" en la cadena "ProgramaciÃ³n en Python".
text = "Programacion Python"
print(text.count("n"))

# 10. Verifica si la cadena "12345" es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.
numerical_text = "12345"
print(numerical_text.isnumeric())
