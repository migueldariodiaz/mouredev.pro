# Variables

my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

# Funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea (No abusar de esta sintaxis)
name, surname, alias, age = "Miguel", "Diaz", 'MikeDiazSnow', 34
print("Me llamo:", name, surname, "mi alias es:", alias, "y tengo:", age, "años de edad.")

# Inputs
name = input("¿Cual es tu primer nombre? ")
age = input("¿Cuantos años tienes? ")

print(name)
print(age)

# Cambiamos el tipo de las variables
name = 35
age = "Miguel"
print(name)
print(age)

