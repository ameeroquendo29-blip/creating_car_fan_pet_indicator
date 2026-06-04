class Pet:
    def __init__(self): #constructor
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    #setters
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age