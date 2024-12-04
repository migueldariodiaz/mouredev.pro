### Sets ###

my_set = set()
my_other_set = {} # Con esta estructura podemos definir tanto el diccionario como el set

print(type(my_set))
print(type(my_other_set)) # Inicialmente nos dice que es un diccionario

my_other_set = {"Miguel", "Diaz", 35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Miguel Diaz")
print(my_other_set) # Un set no es una estructura ordenada, por ende, no se puede acceder a ningun elemento porque en teoria no estan ordenados los mismos

my_other_set.add("Miguel Diaz")
print(my_other_set) # Un set no admite valores repetidos.

print("Diaz" in my_other_set)
print("Diaz " in my_other_set)

my_other_set.remove("Diaz")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(len(my_other_set)) NameError: name 'my_other_set' is not defined

my_set = {"Miguel", "Diaz", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kortlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Javascript", "C#"}))

print(my_new_set.difference(my_set))