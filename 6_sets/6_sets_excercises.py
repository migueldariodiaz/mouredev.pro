# 1. Crea un set con los nÃºmeros del 1 al 5 e imprÃ­melo.
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. AÃ±ade el nÃºmero 6 al set {1, 2, 3, 4, 5} e imprÃ­melo.
my_set.add(6)
print(my_set)

# 3. Intenta aÃ±adir el nÃºmero 5 al set {1, 2, 3, 4, 5} nuevamente. Â¿QuÃ© sucede?
my_set.add(5)
print(my_set) # No pasa nada porque los set no admiten valores repetidos, como ya el 5 existe en el set, entonces no lo agrega.

# 4. Verifica si el nÃºmero 3 estÃ¡ en el set {1, 2, 3, 4, 5} e imprime el resultado.
element = 3 in my_set
print(element)

# 5. Elimina el nÃºmero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
my_set.remove(4)
print(my_set)

# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.
my_set.clear()
print(len(my_set))

# 7. Convierte el set {"manzana", "naranja", "plÃ¡tano"} en una lista e imprime el primer elemento de la lista.
my_set = {"manzana", "naranja", "platano"}
my_list = list(my_set)
print(my_list[0])

# 8. Realiza la uniÃ³n de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
set_a = {1, 2, 3}
set_b = {4, 5, 6}
union_set = set_a.union(set_b)
print(union_set)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
difference_set = set_a.difference(set_b)
print(difference_set)

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
my_set = {"Miguel", "Diaz", 34}
del my_set
#print(my_set) NameError: name 'my_set' is not defined
