### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Miguel", "Apellido":"Diaz", "Edad":35, 1:"Python"} # Relacion clave-valor. Estructuras para relacionar datos.

my_dict = {
    "Nombre":"Miguel", 
    "Apellido":"Diaz", 
    "Edad":35, 
    "Lenguaje":{"Python", "Swift", "Kortlin"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

my_dict["Calle"] = "Quinta avenida" # Forma en la que podemos agregar elementos a nuestro diccionario.
print(my_dict)

del my_dict["Calle"] # La funcion del nos ayuda a quitar la relacion clave-valor que le pasemos. Antes nos ele¿iminaba la variable entera, en este caso, solo sera el campo clave-valor requerido.
print(my_dict)

print("Pedro" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_other_dict.fromkeys(("Nombre", "Apellido", "Colegio", 1))
print(my_new_dict) # La funcion fromkeys() lo que hace es crear un nuevo diccionario con sus valores vacios (en None) con las claves que se pasan como parametros a la funcion.

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list) # La funcion fromkeys(keys, values) tiene como parametros 2, keys y values. Si no se pasan los values, entonces aparecen en todos los values None como el anterior.
print(my_new_dict) # En este caso solo en los values aparece True, porque ese fue el unico parametro que meti

my_new_dict = dict.fromkeys(my_list, True) # La funcion fromkeys(keys, values) tiene como parametros 2, keys y values. Si no se pasan los values, entonces aparecen en todos los values None como el anterior.
print(my_new_dict)


my_new_dict = dict.fromkeys(("Nombre", "Apellido", "Colegio", 1))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso", 1))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Miguel", "Diaz"))
print(my_new_dict)
