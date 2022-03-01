from my_library.human import Human


class HumanWithPet:

    def __init__(self, human_being):
        self.human_being = human_being
        self.list_of_pets = list()

    def __str__(self):
        if len(self.list_of_pets) == 1:
            return f"{self.human_being.get_full_name()}, age {self.human_being.get_age()} with a pet: {self.list_of_pets[0]}"
        else:
            pets_str = str()
            for pet in self.list_of_pets:
                if not pets_str:
                    pets_str = pets_str + str(pet)
                else:
                    pets_str = pets_str + ", " + str(pet)
            return f"{self.human_being.get_full_name()}, age {self.human_being.get_age()} with {len(self.list_of_pets)} pets: {pets_str}"

    def adopt_new_pet(self, pet):
        self.list_of_pets.append(pet)

    def give_away_pet(self, pet):
        self.list_of_pets.remove(pet)

    def get_list_of_pets(self):
        return self.list_of_pets
