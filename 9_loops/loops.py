### Loops ###

# Bucle While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor o igual a 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es igual a 15")
        print("Se detiene la ejecucion")
        break

    print(my_condition)

# Bucle For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Miguel", "Diaz", "Miguel")

for element in my_tuple:
    print(element)

my_set = {"Kortlin", "Swift", "Python"}

for element in my_set:
    print(element)

my_dict = {
    "Nombre":"Miguel", 
    "Apellido":"Diaz", 
    "Edad":35, 
    "Lenguaje":{"Python", "Swift", "Kortlin"},
    1:1.77
    }

for element in my_dict.values():
    print(element)
    if element == 35:
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionaro ha finalizado")

