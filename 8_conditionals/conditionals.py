### Conditionals ###

my_condition = True

if my_condition: # Es lo mismo que: if my_condition == True:
    print("Se ejecuta la condicion del primer if")

my_condition = 5 * 2

if my_condition == 11:
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10:
    print("Es mayor que 10")
else: 
    print("Es menor o igual que 10")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else: 
    print("Es menor o igual que 10 y mayor o igual que 20")

my_condition = 5 ** 0

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition ==1:
    print("Es igual a 1")
else: 
    print("Es menor o igual que 10 y mayor o igual que 20 o distinto de 1")

print("La ejecucion continua")

my_string = ""

if my_string:
    print("Mi cadena de texto no es vacia")

my_string = "Ahora si no esta vacia"

if my_string:
    print("Mi cadena de texto no es vacia")

