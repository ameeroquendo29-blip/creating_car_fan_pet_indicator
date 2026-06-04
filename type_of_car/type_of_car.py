class Car:
    def __init__(self, year_model, make): #private attributes
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5 #adds 5 speed when called

    def brake(self):
        self.__speed -= 5 #decrease speed when called
        if self.__speed < 0: self.__speed = 0

    def get_speed(self):
        return self.__speed

    
