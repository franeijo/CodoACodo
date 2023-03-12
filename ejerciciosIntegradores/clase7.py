
"""
Ejercicio1
Función para calcular el MCD entre dos números utilizando el Algoritmo de Euclides
"""


def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


"""
Ejercicio 2
Función para calcular el MCM entre dos números utilizando el MCD
"""


def mcm(a, b):
    return a*b / mcd(a, b)


"""
Ejercicio 3 y 4
Función que recibe un string y devuelve un diccionario con cantidad de operaciones
"""


def string_to_dict(input_string):
    dictionary = {}
    words = input_string.split()
    for word in words:
        dictionary[word] = words.count(word)
    return dictionary


def dictionary_to_tuple(input_dictionary):
    keys = list(input_dictionary.keys())
    values = list(input_dictionary.values())
    max_key = keys[values.index((max(values)))]
    max_value = input_dictionary[max_key]
    return max_key, max_value


"""
Ejercicio 5
Utilizando Value Error
"""


def get_int():
    try:
        int_number = int(input("Ingrese un entero: "))
        print(int_number)
        get_int()
    except ValueError as e:
        print(e)


"""
Ejercicio 6
Clase persona con constructor
"""


class Person:

    def __init__(self, name="", age=0, dni=""):
        try:
            self.name = str(name)
            self.age = int(age)
            self.dni = str(dni)
        except ValueError as e:
            print(e)

    def show(self):
        return self.name, self.age, self.dni

    def set_name(self, name):
        try:
            name = str(name)
            self.name = name
        except ValueError as e:
            print(e)

    def get_name(self):
        return self.name

    def set_age(self, age):
        try:
            age = int(age)
            self.age = age
        except ValueError as e:
            print(e)

    def get_age(self):
        return self.age

    def dni(self, dni):
        try:
            dni = str(dni)
            self.dni = dni
        except ValueError as e:
            print(e)

    def get_dni(self):
        return self.dni

    def is_older(self):
        return self.age >= 18


"""
Ejercicio 7
Clase Cuenta
"""


class Account:

    person = Person()

    def __init__(self, person, initial_balance=0):
        try:
            self.person = person
            self.balance = float(initial_balance)
        except ValueError as e:
            print(e)

    def show(self):
        return self.person.show(), self.balance

    def get_person(self):
        return self.person.show()

    def get_balance(self):
        return self.balance

    def add_money(self, money):
        if money > 0:
            self.balance += money

    def extract_money(self, money):
        self.balance -= money


class YoungAccount(Account):

    def __init__(self, person, initial_balance=0, discount=0):
        super().__init__(person, initial_balance)
        try:
            self.discount = float(discount)
        except ValueError as e:
            print(e)

    def is_valid(self):
        return self.person.get_age() > 17 & self.person.get_age() < 25

    def get_discount(self):
        return self.discount

    def show(self):
        return "Cuenta Joven", self.person.show(), self.get_balance(), self.get_discount()

    def extract_money(self, money):
        if self.is_valid():
            self.balance -= money
        else:
            print("No puede retirar dinero una cuenta no valida.")


"""
Area de Pruebas
"""

print("MCD", mcd(12, 8))
print("MCM", mcm(12, 8))

dictionary_test = string_to_dict("Hello my name name is John John")
print(dictionary_test)
print(dictionary_to_tuple(dictionary_test))

person_one = Person("Jorge", 35, "33222434")
person_two = Person("Martin", 18, "3332232")
print(person_one.show())

account_one = Account(person_one, 1000)
print(account_one.get_balance())
account_one.add_money(450)
print(account_one.get_balance())
print(account_one.show())

account_two = YoungAccount(person_two, 500, 5)
print(account_two.get_balance())
print(account_two.show())
account_two.extract_money(35)
print(account_two.show())
