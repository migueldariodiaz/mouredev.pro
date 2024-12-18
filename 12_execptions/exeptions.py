### Exeptions Handling ###

'''
Diagram:

try:
    # Run this code
except:
    # Excecute this code when there is an exception
else:
    # No exceptions? Run this code.
finally:
    # Always run this code


'''
# Try-Except

number_one, number_two = 5, 1
print(number_one + number_two)
number_two = "1"

try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")


# Try-Except-Else

number_one, number_two = 5, 1
print(number_one + number_two)
number_two = 1 #"1"

try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")


# Try-Except-Else-Finally

number_one, number_two = 5, 1
print(number_one + number_two)
number_two = "1"

try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecucion continua")

# Captura de excepciones por tipo de error

number_one, number_two = 5, 1
print(number_one + number_two)
number_two = "1"

try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except ValueError:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")
except TypeError:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")


# Captura de de la informacion del tipo de error

number_one, number_two = 5, 1
print(number_one + number_two)
number_two = "1"

try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except TypeError as error:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")
    print(error)


# Captura de la informacion del tipo de error y ademas capotura de errores genericos (Si no se sabe que error es)

number_one, number_two = 5, 1
print(number_one + number_two)
number_two = "1"

try:
    print(number_one + number_two)
    print("No se ha producido ningun error")
except ValueError as error:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")
    print(error)
except Exception as my_random_error_name:
    print("Se ha producido un error my_random_error_name")
    print(my_random_error_name)