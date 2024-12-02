### Strings ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es String\ncon salto de pagina"
print(my_new_line_string)

my_tab_string = "\tEste es String con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es String \\n escapado"
print(my_scape_string)

# Formateo de strings

name, surname, age = "Miguel", "Diaz", 34
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " " + "y mi edad es" + " " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempacado de variables
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# Division
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)


# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Metodos o funciones del sistema para strings
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("956".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))
print(language.startswith("Py"))
print(language.startswith("PY"))