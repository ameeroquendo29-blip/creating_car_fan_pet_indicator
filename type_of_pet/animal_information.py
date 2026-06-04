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
                    print("Age cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid whole number for age.")

        self.pet_info.set_name(name)
        self.pet_info.set_animal_type(animal_type)
        self.pet_info.set_age(age)