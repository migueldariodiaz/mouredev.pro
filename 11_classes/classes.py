### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:


    def __init__(self, name, surname, alias = "Sin alias"):
        self.name = name
        self.surname = surname
        self.alias = alias


    def walk(self):
        print(f"{self.name} {self.surname} {self.alias} esta caminando")

my_person = Person("Miguel", "Diaz")
print(f"{my_person.name} {my_person.surname}")
my_person.walk()


class MyOtherPerson:


    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"


    def walk(self):
        print(f"{self.full_name} esta caminando")

my_other_person = MyOtherPerson("Miguel Dario", "Diaz Hernandez")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Alonso Diaz Alejandria"
print(my_other_person.full_name)

class PersonPrivate:


    def __init__(self, name, surname, alias = "Sin alias"):
        self.__name = name # Al tener los __ se convierte en una propiedad privada en la que no se puede acceder desde fuera de la clase
        self.__surname = surname # Al tener los __ se convierte en una propiedad privada en la que no se puede acceder desde fuera de la clase
        self.alias = f"({alias})" # Propiedad publica. Se puede acceder desde fuera de la clase


    def get_name(self):
        print(f"{self.__name}")


    def walk(self):
        print(f"{self.__name} {self.__surname} {self.alias} esta caminando")

my_person_private = PersonPrivate("Sybell", "Alejandria", "La campeona")
my_person_private.walk()
my_person_private.get_name()
print(my_person_private.alias)