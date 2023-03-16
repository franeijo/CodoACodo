import re

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

    def __init__(self, name="Jorge", age=0, dni=0):
        self.name = name
        self.age = age
        self.dni = dni

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        regex = "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$"
        if not re.match(regex, new_name):
            raise ValueError("Its not a valid name.")
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age <= 0:
            raise ValueError("Its not a valid age.")
        self._age = new_age

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, new_dni):
        if new_dni <= 0:
            raise ValueError("Its not a valid DNI.")
        self._dni = new_dni

    def show(self):
        print("Person:", self.name, self.age, self.dni)

    def is_older(self):
        return self.age >= 18


"""
Ejercicio 7
Clase Cuenta
"""


class Account:

    def __init__(self, person, initial_balance=0):
        self.person = person
        self.balance = initial_balance

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, new_person):
        if not isinstance(new_person, Person):
            raise ValueError("Its not a valid Person.")
        self._person = new_person

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 1:
            raise ValueError("Its not a valid balance")
        self._balance = new_balance

    def show(self):
        print("Bank Account: ")
        self.person.show()
        print("Balance: ", self.balance)

    def add_money(self, money):
        if money > 0:
            self._balance += money

    def extract_money(self, money):
        self._balance -= money


class YoungAccount(Account):

    def __init__(self, person, initial_balance=0, discount=0):
        super().__init__(person, initial_balance)
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, new_discount):
        if new_discount < 0:
            raise ValueError("Its not a valid discount.")
        self._discount = new_discount

    def is_valid(self):
        return 17 < self.person.age < 25

    def show(self):
        print("Young Account: ")
        self.person.show()
        print("Balance: ", self.balance)
        print("Discount: ", self.discount)

    def extract_money(self, money):
        if self.is_valid():
            self.balance -= money
        else:
            print("Not valid extract")


"""
Area de Pruebas
"""

print("MCD", mcd(12, 8))
print("MCM", mcm(12, 8))

dictionary_test = string_to_dict("Hello my name name is John John")
print(dictionary_test)
print(dictionary_to_tuple(dictionary_test))

person_one = Person("Martin Gomez", 35, 33222434)
person_two = Person("Martin", 15, 3332232)
person_one.show()


account_one = Account(person_one, 1000)
account_one.show()
account_one.add_money(450)
account_one.show()
account_one.extract_money(100)
account_one.show()

account_two = YoungAccount(person_two, 500, 5)
account_two.show()
account_two.extract_money(35)
account_two.show()
