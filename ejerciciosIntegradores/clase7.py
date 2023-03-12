
"""
Funcion para calcular el MCD entre dos numeros utilizando el Algoritmo de Euclides
"""
def MCD(a, b):
    if b == 0:
        return a
    else:
        return MCD(b, a % b)

"""
Funcion para calcular el MCM entre dos numeros utilizando el MCD
"""
def MCM(a, b):
    return (a*b / MCD(a,b))

"""
Funcion que recibe un string y devuelve un diccionario con cantidad de operacciones
"""
def diccionario_string(cadena):
    diccionario = {}
    palabras = cadena.split()
    for palabra in palabras:
        diccionario[palabra] = palabras.count(palabra)
    return diccionario

def diccionario_palabras_tupla(diccionario):
    claves = list(diccionario.keys())
    valores = list(diccionario.values())
    clave_maximo = claves[valores.index((max(valores)))]
    valor_maximo = diccionario[clave_maximo]
    return (clave_maximo,valor_maximo)
    

"""
Clase personas con constructor
"""

class Persona:

    def __init__(self, name="", age=0, dni=""):
        self.name = name
        self.age = age
        self.dni = dni

    def set_name(self, name):
        try:
            name = str(name)
            self.name = name
        except:
            print("Invalid")
    
    def get_name(self):
        return(self.name)

    def set_age(self, age):
        try:
            age = int(age)
            self.age = age
        except:
            print("Invalid")
    
    def get_age(self):
        return(self.age)

    def show(self):
        print(self.name, self.age, self.dni)

    def is_older(self):
        return self.age >= 18
            

persona1 = Persona("Jorge",20,"333333") 
persona1.show()
print(persona1.is_older())       








