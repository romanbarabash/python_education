import random
from abc import ABC, abstractmethod


class Birds(ABC):

    @abstractmethod
    def produce_egs(self):
        pass


class Mammals(ABC):

    @abstractmethod
    def produce_hugs(self):
        pass


class PolarBirds(Birds):
    polar_birds = ['albatross', 'pinguin', 'goose']

    def produce_egs(self):
        print(f'One of the polar birds: {random.choice(self.polar_birds)} produced {random.choice(range(0, 5))} egs')


class PolarMammals(Mammals):
    polar_animals = ['bear', 'fox', 'whale']

    def produce_hugs(self):
        print(f'One of the polar animals: {random.choice(self.polar_animals)} hugs you')

    def heating(self):
        print(f'One of the polar animals: {random.choice(self.polar_animals)} heat you')


class AustralianBirds(Birds):
    australian_birds = ['parrot', 'kolibri', 'kiwi']

    def produce_egs(self):
        print(f'One of the australian birds: {random.choice(self.australian_birds)} produced {random.choice(range(0, 5))} egs')


class AustralianMammals(Mammals):
    australian_animals = ['koala', 'kangoo', 'platipus']

    def produce_hugs(self):
        print(f'One of the australian animals: {random.choice(self.australian_animals)} hugs you')

    def make_laugh(self):
        print(f'One of the australian animals: {random.choice(self.australian_animals)} make you laugh')


class ParkFactory(ABC):

    @abstractmethod
    def create_birds_area(self):
        pass

    @abstractmethod
    def create_mammals_area(self):
        pass


class PolarAnimalsFactory(ParkFactory):

    def create_birds_area(self):
        return PolarBirds()

    def create_mammals_area(self):
        return PolarMammals()


class AustralianAnimalsFactory(ParkFactory):

    def create_birds_area(self):
        return AustralianBirds()

    def create_mammals_area(self):
        return AustralianMammals()


# app
for factory in (PolarAnimalsFactory(), AustralianAnimalsFactory()):
    birds_area = factory.create_birds_area()
    mammals_area = factory.create_mammals_area()

    birds_area.produce_egs()
    mammals_area.produce_hugs()

    if isinstance(factory, PolarAnimalsFactory):
        mammals_area.heating()

    if isinstance(factory, AustralianAnimalsFactory):
        mammals_area.make_laugh()

    print()

# abstract factory and abstract product ->
# create concrete products ->
# create concrete factory ->
# let concrete factory operates your concrete products at the app
