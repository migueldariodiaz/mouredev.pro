# 1. Crea una lista con los nÃºmeros del 1 al 5 e imprÃ­mela.
my_list = [1, 2, 3, 4, 5]
print(my_list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
my_list = [10, 20, 30, 40, 50]
third_element = my_list[2]
print(third_element)

# 3. Agrega el nÃºmero 6 al final de la lista [1, 2, 3, 4, 5] e imprÃ­mela.
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

# 4. Inserta el nÃºmero 15 en la posiciÃ³n 2 de la lista [10, 20, 30, 40, 50].
my_list = [10, 20, 30, 40, 50]
my_list.insert(2, 15)
print(my_list)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
my_list = [10, 20, 30, 30, 40, 50]
my_list.remove(30)
print(my_list)

# 6. Usa la funciÃ³n pop() para eliminar el Ãºltimo elemento de la lista [1, 2, 3, 4, 5] y almacÃ©nalo en una variable. Imprime la variable y la lista.
my_list = [1, 2, 3, 4, 5]
pop_value = my_list.pop()
print(pop_value)
print(my_list)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprÃ­mela.
my_list = [100, 200, 300, 400, 500]
reversed_list = my_list[::-1]
print(reversed_list)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprÃ­mela.
my_list = [3, 1 ,4, 2, 5]
my_list.sort()
print(my_list)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_concatenated_string = my_first_list + my_second_list
print(my_concatenated_string)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posiciÃ³n 1 hasta la 3 (sin incluir la posiciÃ³n 3).
my_list = [10, 20, 30, 40, 50]
my_sub_list = my_list[0:2]
print(my_sub_list)