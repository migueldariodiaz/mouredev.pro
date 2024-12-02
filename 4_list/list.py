### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Miguel", "Diaz"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
#print(my_other_list[-5]) Index Error
#print(my_other_list[4]) Index Error
print(my_list.count(30))

age, height, name, surname = my_other_list
print(f"Mi nombre es {name} {surname}, tengo {age} y mido {height}")

name, height, agee, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(f"Mi nombre es {name} {surname}, tengo {age} y mido {height}")

print(my_list + my_other_list)

# Metodos o funciones para listas
my_other_list.append("DeepControl")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_other_list.remove("Rojo")
print(my_other_list)


print(my_list)
my_list.remove(30)
print(my_list)

my_list.pop()
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_list = "Hola python"
print(my_list)

my_list = list("Hola python")
print(my_list)

