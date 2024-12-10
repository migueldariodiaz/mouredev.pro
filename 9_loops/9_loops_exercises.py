# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.
my_condition = 1

while my_condition < 11:
    print(my_condition)
    my_condition += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.
my_list = [10, 20, 30, 40, 50]

for element in my_list:
    print(element)

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.
my_condition = 1
result = 0

while my_condition < 101:
    result = my_condition + result
    my_condition += 1
print(result)

# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".
my_string = "Python"

for string in my_string:
    print(string)

# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.
number = 1

while number < 51:
    if number % 7 == 0:
        break
    number += 1
print(f"El primer numero divisible entre 7 entre los numeros 1-50 es: {number}")

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}

for i in my_dict.keys():
    print(i)

# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.
number = 1

while number < 21:
    if number % 2 == 0:
        print(number)
    number += 1


# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.
for i in range(10, 0, -1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la lista[30, 10, 30, 20, 30, 40].
my_list = [30, 10, 30, 20, 30, 40]
count = 0

for i in my_list:
    if i == 30:
        count += 1
print(f"La cantidad de veces que aparece el numnero 30 en my_list es: {count}")

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
my_list = ["Miguel", "Sybell", "Alonso", "Jagger", "Mick", "Brais", "Diaz", "Hernandez"]

for i in my_list:
    print(i)
    if i == "Brais":
        break
