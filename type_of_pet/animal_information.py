from type_of_pet import Pet

class AnimalInformation:
    def __init__(self):
        self.pet_info = Pet()

    def collect_pet_data(self):
        print("----- Input Pet Details -----")
        name = input("Enter pet name: ")
        animal_type = input("Enter animal type (ex., Dog, Cat, Bird): ")

        while True:
            try:
                age = int(input("Enter pet age: "))
                if age < 0:
                    print(f"Age cannot be negative.")
                    continue
                break
            except ValueError:
                print(f"Please enter a valid whole number for age.")

        self.pet_info.set_name(name)
        self.pet_info.set_animal_type(animal_type)
        self.pet_info.set_age(age)

    def display_pet_data(self):
        print("\n--- Displaying Pet Details ---")
        print(f"Name:        {self.pet_info.get_name()}")
        print(f"Animal Type: {self.pet_info.get_animal_type()}")
        print(f"Age:         {self.pet_info.get_age()} years old")

    def run(self):
        self.collect_pet_data()
        self.display_pet_data()

if __name__ == "__main__":
    program = AnimalInformation()
    program.run()