from type_of_car import Car

class CarSimulator:
    def __init__(self, year_model, make):
        self.my_car = Car(year_model, make)

    def test_run(self):
        print(f" Starting test run for {self.my_car.get_year_model()} {self.my_car.get_make()}")
        print(f"\nAccelerating....")
        for stomp in range(1, 6):
            self.my_car.accelerate()
            print(f"  Stomp {stomp}: Speed is now {self.my_car.get_speed()} km/h")

        print(f"\nApplying Brakes...")
        for step in range(1, 6):
            self.my_car.brake()
            print(f"  Step {step}: Speed is now {self.my_car.get_speed()} km/h")

        print(f"\nTest run complete....")

def simulation():
    simulation = CarSimulator("2024", "Toyota")
    simulation.test_run()

if __name__ == "__main__":
    simulation()