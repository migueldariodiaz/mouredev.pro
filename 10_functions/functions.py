### Functions ###

def my_function():
    print("Esto es una funcion")

my_function()
my_function()
my_function()

def sum_two_values(first_values, second_values):
    my_sum = first_values + second_values
    print(my_sum)

sum_two_values("Hello ", "World") # El tipado en python no funciona
sum_two_values(5, 7)
sum_two_values(568656, 76468445)
sum_two_values("5", "7") # El tipado en python no funciona
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_values, second_values):
    return (first_values + second_values)

my_result = sum_two_values_with_return(10, 5)
print(my_result)
my_other_result = sum_two_values(1.4, 5.2)
print(my_other_result) # Devuelve NONE porque simplemente la funcion no devuelve nada, o devuelve NONE, como se entienda mejor.

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Miguel", "Diaz")
print_name(surname = "Miguel", name = "Diaz")

def print_name_whit_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_whit_default("Miguel", "Diaz", "migueldarioDev") # Funcion con valores por defecto
print_name_whit_default("Miguel", "Diaz")

def print_texts(*text): # El asterisco nos dice que "De ese tipo de datos, podemos pasar los parametros que queramos" - Numero de parametros dinamicos
    for i in text:
        print(i)

my_texts = print_texts("Hola")
print(my_texts)
print_texts("Miguel", "Diaz", "migueldarioDev")