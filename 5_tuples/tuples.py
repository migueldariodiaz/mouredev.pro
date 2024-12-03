### Tuplas ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Miguel", "Diaz", "Miguel")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Miguel"))
print(my_tuple.index("Diaz"))
print(my_tuple.index("Miguel"))

#my_tuple[1] = 1.80 # Tuple object does not support item assigment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MercadoLibre"
my_tuple.insert(1, "Azul")
print(tuple(my_tuple))


