from type_of_car import Car

class CarSimulator:
    def __init__(self, year_model, make):
        self.my_car = Car(year_model, make)

    def test_run(self):
        print(" Starting test run for {self.my_car.get_year_model()} {self.my_car.get_make()}")
        print("\nAccelerating....")
        for stomp in range(1, 6):
            self.my_car.accelerate()
            print(f"  Stomp {stomp}: Speed is now {self.my_car.get_speed()} km/h")
            
