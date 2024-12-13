# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(name = "desconocido"):
    print(f"Hola {name}")

personalized_greeting("Miguel")
personalized_greeting()

# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos y retorne el resultado de multiplicarlos.
def multiply(number_1, number_2):
    return number_1 * number_2

result = multiply(3, 8)
print(result)

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento y retorne True si es par y False si es impar.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

is_a_even_number = is_even(6)
print(is_a_even_number)

# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayÃºsculas.
def convert_to_uppercase(*texts):
    text_result = ""
    for text in texts:
        text_result += text + " "
    return text_result.upper()

text_result = convert_to_uppercase("Miguel", "Diaz", "Alonso", "Diaz", "Sybell", "Alejandria")
print(text_result)

# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario de nÃºmeros como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*numbers):
    sum_result = 0
    for number in numbers:
        sum_result += number
    return sum_result

sum_result = arbitrary_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sum_result)

# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(name, surname):
    print(f"Hola, {name} {surname}")

generate_full_greeting(surname = "Diaz Alejandria", name = "Alonso")


# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base, exponent):
    return base ** exponent

result_power = power(2, 3)
print(result_power)

# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros y retorne su promedio.
def calculate_average(number_1, number_2, number_3):
    return (number_1 + number_2 + number_3)/3

average = calculate_average(16, 16, 16)
print(average)

# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto y retorne el nÃºmero de caracteres que contiene.
def count_characters(text = ""):
    characters = len(text)
    return characters

text_count = count_characters("Hola, mi nombre es Miguel Diaz Hernandez")
print(text_count)


# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero indefinido de cadenas y las imprima en mayÃºsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*texts):
    for text in texts:
        print(str(text).upper())

display_messages("Miguel", "Diaz", "Alonso", "Diaz", "Sybell", "Alejandria", "Mick", "Jagger")