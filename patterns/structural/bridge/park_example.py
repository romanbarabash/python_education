import random


class Creature:
    def goto_clinic(self, qty):
        pass

    def goto_salon(self, qty):
        pass


class Animals(Creature):
    animals_list = ['rabbits', 'foxes', 'badgers', 'raccoons', 'cats']

    def goto_clinic(self, animals):
        print(f'{animals} {random.choice(self.animals_list)} went to clinic')

    def goto_salon(self, animals):
        print(f'{animals} {random.choice(self.animals_list)} went to beauty salon')


class Humans(Creature):
    def goto_clinic(self, people):
        print(f'{people} people went to clinic')

    def goto_salon(self, people):
        print(f'{people} people went to beauty salon')


class Facility:
    def __init__(self, Creature, visitors):
        # Bridge between Facility and Creature, Facility has Creature
        self.creature = Creature
        self.items = visitors

    def show_attendance(self):
        pass

    def add_visitor(self, visitors):
        pass


class MedicalCenter(Facility):
    def __init__(self, Creature, visitors):
        super().__init__(Creature, visitors)
        self.visitors = visitors

    def show_attendance(self):
        self.creature.goto_clinic(self.items)

    def add_visitor(self, visitors):
        self.visitors += visitors


class BeautySalon(Facility):
    def __init__(self, Creature, visitors):
        super().__init__(Creature, visitors)
        self.visitors = visitors

    def show_attendance(self):
        self.creature.goto_salon(self.items)

    def add_visitor(self, visitors):
        self.visitors += visitors


# app
animals = Animals()
humans = Humans()

med_center_1 = MedicalCenter(animals, 5)
beauty_salon_1 = BeautySalon(animals, 1)

med_center_2 = MedicalCenter(humans, 3)
beauty_salon_2 = BeautySalon(humans, 2)

med_center_1.add_visitor(1)
med_center_1.show_attendance()

med_center_2.add_visitor(1)
med_center_2.show_attendance()

beauty_salon_1.add_visitor(2)
beauty_salon_1.show_attendance()

beauty_salon_2.add_visitor(2)
beauty_salon_2.show_attendance()

# Facility and subclases -> Creature and subclases -> Facility has Creature by composition as a bridge between them
