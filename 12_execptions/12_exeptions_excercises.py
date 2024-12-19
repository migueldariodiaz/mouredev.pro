# 1. Crea una funciÃ³n que intente dividir dos nÃºmeros proporcionados por el usuario. Usa try-except para capturar cualquier error de divisiÃ³n (por ejemplo, divisiÃ³n por cero).
def division_number():
    try:
        a = 1 #int(input("inserte el dividendo: "))
        b = 0 #int(input("inserte el divisor: "))
        c = a / b
        print(c)
    except ZeroDivisionError:
        print("No se puede dividir un numero entre 0")
    
division_number()
# 2. Crea una funciÃ³n que tome una cadena e intente convertirla en un nÃºmero entero. Usa try-except para capturar cualquier error en la conversiÃ³n.
def conversion_string_int(string_value):
    try:
        int_value = int(string_value)
        print(int_value)
    except ValueError:
        print("No se puede hacer una conversion de una cadena de texto a entero")

conversion_string_int("a")

# 3. Crea una funciÃ³n que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.
def open_file(name_file):
    try:
        open(name_file, mode = 'r')
    except FileNotFoundError:
        print("El archivo no se ha encontrado")

open_file("tmp.txt")

# 4. Crea una funciÃ³n que realice mÃºltiples operaciones (suma, resta, divisiÃ³n, multiplicaciÃ³n) con dos nÃºmeros. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.
def operations(a, b):
    try:
        add_operation = a + b
        print(f"La operacion suma da el siguiente resultado: {add_operation}")
        sustraction_operation = a - b
        print(f"La operacion resta da el siguiente resultado: {sustraction_operation}")
        multiply_operation = a * b
        print(f"La operacion multiplicacion da el siguiente resultado: {multiply_operation}")
        division_operation = a / b
        print(f"La operacion division da el siguiente resultado: {division_operation}")
    except TypeError:
        print("No se puede hacer una operacion matematica de una cadena de texto con entero")
    except ZeroDivisionError:
        print("No se puede dividir un numero entre 0")
    else:
        print("No se ha producido un error")
    finally:
        print("Se termino de ejecutar el programa")

operations(1, "0")
    
# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError si la entrada no es un nÃºmero entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.
def personal_data():
    try:
        age = 18 #int(input("Diganos cual es su edad: "))
        if age <= 0:
            raise ValueError("La edad debe ser un valor entero positivo")
        else:
            print(f"La edad del usuario es: {age}")
    except ValueError as error:
        print(f"Error: {error}")
    
personal_data()

# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista por Ã­ndice. Usa try-except para manejar el caso donde el Ã­ndice estÃ© fuera de rango.
def index_list(my_list, index):
    try:
        element = my_list[index]
        return element
    except IndexError:
        print(f"El indice {index} esta fuera del rango de la lista")

my_list = [1, 2, 3, "Miguel"]
element = index_list(my_list, 3)
print(element)

# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples excepciones: ZeroDivisionError, ValueError y TypeError.
def operations(a, b, operation = ""):
    try:
        if operation == "1":
            add_operation = a + b
            print(f"La operacion suma da el siguiente resultado: {add_operation}")
        elif operation == "2":
            sustraction_operation = a - b
            print(f"La operacion resta da el siguiente resultado: {sustraction_operation}")
        elif operation == "3":
            multiply_operation = a * b
            print(f"La operacion multiplicacion da el siguiente resultado: {multiply_operation}")
        elif operation == "4": 
            division_operation = a / b
            print(f"La operacion division da el siguiente resultado: {division_operation}")
        else:
            raise ValueError
    except ValueError:
        print("No se puede hacer la conversion de una cadena de texto a entero")
    except TypeError:
        print("No se puede hacer una operacion matematica de una cadena de texto con entero")
    except ZeroDivisionError:
        print("No se puede dividir un numero entre 0")

operations(1, 20, 1)

# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una excepciÃ³n personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.
def transaction(withdraw, balance):
    try:
        if balance < withdraw:
            raise Exception
        else:
            print(f"Monto retirado: {withdraw} \nSaldo: {balance - withdraw}")
    except Exception:
        print("InsufficientFundsError")

transaction(200, 500)
# 9. Crea una funciÃ³n que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.
def conversion_list_int(my_list):
    index_list = 0
    try:
        for index in my_list:
            my_list[index_list] = int(index)
            index_list += 1
        return my_list
    except ValueError:
        print("No se ha podido connvertir la cadena de texto en string")

my_list = ["2", "3", "5"]
print(my_list)
my_list = conversion_list_int(my_list)
print(my_list)

# 10. Crea una funciÃ³n que calcule la raÃ­z cuadrada de un nÃºmero. Lanza un ValueError si el nÃºmero es negativo.
def square_root(number):
    try:
        if number < 0:
            raise ValueError
        else:
            return number**0.5
    except ValueError:
        print("Ingrese un valor positivo")

result = square_root(-25)
print(result)