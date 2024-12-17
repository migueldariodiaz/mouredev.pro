# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.
'''
class Animal:
    def __init__(self, species = "Dog"):
        self.species = species

    def make_sound(self):
        print("GUAU GUAU")

my_dog = Animal()
my_dog.make_sound()
'''


# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad pÃºblica. AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.
class Animal:
    def __init__(self, species):
        self.species = str(species).lower()

    def make_sound(self):
        if self.species == "perro":
            print("GUAU GUAU")
        elif self.species == "gato":
            print("MIAU")
        elif self.species == "paloma":
            print("GRUUU")
        elif self.species == "serpiente":
            print("SHHHHH")
        elif self.species == "vaca":
            print("MUUUU")
        else:
            print("No existe ese animal en nuestra base de datos")

my_dog = Animal("GATO")
my_dog.make_sound()

# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.
'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0
'''

# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. AÃ±ade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad no sea negativa.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0
        print(f"Has comprado un {self.brand} {self.model}. Te lo mereces")


    def accelerate(self):
        if not self.__speed >= 220:
            self.__speed += 10
            print(self.__speed)
        else:
            print("Alcanzada la velocidad maxima")
            print(self.__speed)


    def brake(self):
        if not self.__speed <= 0:
            self.__speed -= 10
            print(self.__speed)
        else:
            print("El vehiculo se freno")
            print(self.__speed)


# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author
    
    def get_author(self):
        print(f"{self.__author}")
    
    def change_title(self, new_title):
        previous_title = self.title
        self.title = new_title
        print(f"El titulo se ha cambia de \"{previous_title}\" a \"{self.title}\"")

my_book = Book("Por un mejor mañana", "Miguel Diaz H.")
#print(my_book.__author)
my_book.get_author()
my_book.change_title("Porque sera grandioso con mi familia")

# 6. Crea una clase "Students" que tenga como propiedades su name, surname y una lista de grades. AÃ±ade un mÃ©todo para calcular y devolver la grade media del Students.
class Students:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def grade_average(self):
        accumulated = 0
        for grade in self.grades:
            accumulated += grade
        average = accumulated/len(self.grades)
        return (average)

mi_Students = Students("Miguel", "Diaz", [18.6, 19.3, 20])
average_grade = mi_Students.grade_average()
print(f"La nota acumulada promedio del estudiante {mi_Students.name} {mi_Students.surname} es: {average_grade}")

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". AÃ±ade mÃ©todos para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        print(f"Your balance is: {self.balance}")

    def deposit_money(self, amount):
        self.balance += amount
        print(f"You have made a deposit of {amount}. Your new balance is: {self.balance}")
        
    def withdraw_money(self, amount):
        if (self.balance > 0) and (amount <= self.balance):
            self.balance -= amount
            print(f"You have made a withdraw of {amount}. Your new balance is: {self.balance}")
        else:
            print(f"You do not have enough balance. Current balance {self.balance}")

my_bank_account = BankAccount("Miguel Diaz", 200000)
my_bank_account.deposit_money(30000)
my_bank_account.withdraw_money(240000)
my_bank_account.withdraw_money(210000)

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". AÃ±ade un mÃ©todo que calcule la distancia entre dos puntos.
class Point:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def distance_between_two_points(self):
        distance_vector = [self.p2[1] - self.p1[1], self.p2[0] - self.p1[0]]
        distance_module = (distance_vector[0]**2 + distance_vector[1]**2)**0.5
        return distance_module

p1 = [2, 1]
p2 = [-3, 2]
vector = Point(p1, p2)
distance = vector.distance_between_two_points()
print(distance)

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". AÃ±ade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def total_pay(self):
        total_salary = self.hours_worked*self.hourly_wage
        return total_salary
    
employee_salary = Employee("Miguel Diaz", 125, 40)
salary = employee_salary.total_pay()
print(f"El pago por remuneraciones de esta semana para el trabajador {employee_salary.name} es: {salary}$")

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). AÃ±ade un mÃ©todo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
'''
class Store:
    def __init__(self, inventory):
        self.inventory = list(inventory)

    def show_products(self):
        for product in self.inventory:
            print(product)

    def add_product(self, product):
        self.inventory.append(product)

store = Store(["Armario", "Escritorios", "Mesas", "Pizarras"])
store.show_products()
store.add_product("Caja fuerte con mucho dinero")
store.show_products()
'''

class Store:
    def __init__(self):
        self.inventory = list()

    def show_products(self):
        for product in self.inventory:
            print(product)

    def add_product(self, product):
        self.inventory.append(product)

store = Store()
store.add_product("Escritores")
store.show_products()