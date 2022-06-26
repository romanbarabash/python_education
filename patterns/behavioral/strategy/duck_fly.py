from abc import ABC, abstractmethod


class Fly(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithRocket(Fly):
    def fly(self):
        print('FLying with rocket') # custom realisation


class FlyWithWings(Fly):
    def fly(self):
        print('FLying with wings')  # custom realisation


class CantFly(Fly):
    def fly(self):
        print('i can\'t fly')  # custom realisation


class SuperDuck:
    def __init__(self, fly: Fly):
        self._fly = fly

    def perform_fly(self):
        self._fly.fly()


# app
duck = SuperDuck(FlyWithRocket())
duck.perform_fly()

another_duck = SuperDuck(CantFly())
another_duck.perform_fly()
