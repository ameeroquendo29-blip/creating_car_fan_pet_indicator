from type_of_pet import Pet

class AnimalInformation:
    def __init__(self):
        self.pet_info = Pet()

    def collect_pet_data(self):
        print("----- Input Pet Details -----")
        name = input("Enter pet name: ")
        animal_type = input("Enter animal type (ex., Dog, Cat, Bird): ")

        