# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
my_variable = -1

if my_variable > 0:
    print("El numero es positivo")
elif my_variable < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
age = int(input("¿Que edad tienes? Vamos a evaluar si eres mayor de edad. "))

if age >= 18:
    print("Eres mayor de edad :( ¿Como va la vida de adulto?")
else:
    print("Eres menor de edad :) ¡Disfruta!")

# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.
my_string = ""

if not my_string:
    print("La cadena de texto esta vacia")
else:
    print("La cadena de texto no esta vacia")

# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
number_a = int(input("Ingrese el primer numero a evaluar: "))
number_b = int(input("Ingrese el segundo numero a evaluar: "))

if number_a < number_b:
    print(f"El numero {number_a} es menor al numero {number_b}")
elif number_a > number_b:
    print(f"El numero {number_a} es mayor al numero {number_b}")
else:
    print("Los numeros introducidos son iguales")

# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.
my_number = 30

if (my_number % 3 == 0) and (my_number % 5 == 0):
    print(f"El numero {my_number} es divisible entre 3 y entre 5")
elif (my_number % 3 == 0) and (my_number % 5 != 0):
    print(f"El numero {my_number} es divisible entre 3 pero no es divisible entre 5")
elif (my_number % 3 != 0) and (my_number % 5 == 0):
    print(f"El numero {my_number} no es divisible entre 3 pero es divisible entre 5")
else:
    print(f"El numero {my_number} no es divisible entre 3 y tampoco es divisible entre 5")

# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.
my_number = int(input("Ingrese un numero a evaluar si es par o impar: "))

if (my_number % 2 == 0):
    print(f"El numero {my_number} es par")
else:
    print(f"El numero {my_number} es impar")

# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.
age = int(input("¿Que edad tienes? Vamos a evaluar si puedes votar. "))

if age >= 16:
    if age < 18:
        print("Puedes votar pero con permiso especial")
    else:
        print("Puedes votar normalmente")
else:
    print("Aun no puedes votar")

# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide, muestra un mensaje de error.
default_password = "hola_123"
password = input("Ingrese la contraseña: ")

if password == default_password:
    print("La contraseña introducida es correcta")
else:
    print("La contraseña introducida es incorrecta")

# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).
my_number = 12

if my_number >= 10 and my_number <= 20:
    print("El numero esta entre 10 y 20 (ambos incluidos)")
else:
    print("El numero NO esta entre 10 y 20 (ambos incluidos)")
# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
color = input("Inserte el color del semaforo. (rojo, amarillo, verde): ")

if color.lower() == "verde":
    print("Avanza")
elif color.lower() == "amarillo":
    print("Alerta")
elif color.lower() == "rojo":
    print("Detengase")
else:
    print("Por favor inserte un valor correspondiente entre los colores del semaforo (rojo, amarillo, verde)")