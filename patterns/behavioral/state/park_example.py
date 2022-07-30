'''
Bridge, State, Strategy (and to some degree Adapter) have very similar structures.
Indeed, all of these patterns are based on composition, which is delegating work to other objects.
However, they all solve different problems.
A pattern isn’t just a recipe for structuring your code in a specific way.
It can also communicate to other developers the problem the pattern solves.

State can be considered as an extension of Strategy.
Both patterns are based on composition: they change the behavior of the context by delegating some work to helper objects.
Strategy makes these objects completely independent and unaware of each other.
However, State doesn’t restrict dependencies between concrete states, letting them alter the state of the context at will.

'''
from enum import Enum


class RiskZone(Enum):
    SAFE = 'safe'
    ATTENTION = 'attention'
    RISK = 'risk'


class State:
    distance = {'safe': 200, 'attention': 100, 'risk': 50}
    tundra_zone_animals = {'safe': 'penguins', 'attention': 'sea elephants', 'risk': 'polar bears'}
    moderate_zone_animals = {'safe': 'rabbits', 'attention': 'mooses', 'risk': 'bears'}

    def observe(self, distance):
        animals_dict = self._get_animals_dict()
        animals = []

        if distance <= self.distance[RiskZone.RISK.value]:
            print(f"Distance is: {distance}, you not allowed to observe animals less than {self.distance[RiskZone.RISK.value]}m distance")
        if distance > self.distance[RiskZone.RISK.value]:
            animals.append(animals_dict[RiskZone.SAFE.value])
            if distance > self.distance[RiskZone.ATTENTION.value]:
                animals.append(animals_dict[RiskZone.ATTENTION.value])
                if distance > self.distance[RiskZone.SAFE.value]:
                    animals.append(animals_dict[RiskZone.RISK.value])

            print(f'Distance is: {distance}, you allowed to observe: ' + ', '.join(animals))

    def _get_animals_dict(self):
        if isinstance(self, TundraClimaticZone):
            return self.tundra_zone_animals
        else:
            return self.moderate_zone_animals


class TundraClimaticZone(State):

    def __init__(self, climatic_zone):
        self.climatic_zone = climatic_zone

    def change_climatic_zone(self):
        print("Changing climatic zone to Moderate")
        self.climatic_zone.zone = self.climatic_zone.climatic_zone_moderate

    def show_climatic_zone(self):
        print(f"Current climatic zone is Tundra Climatic Zone")


class ModerateClimaticZone(State):

    def __init__(self, climatic_zone):
        self.climatic_zone = climatic_zone

    def change_climatic_zone(self):
        print("Changing climatic zone to Tundra")
        self.climatic_zone.zone = self.climatic_zone.climatic_zone_tundra

    def show_climatic_zone(self):
        print(f"Current climatic zone is 'Moderate Climatic Zone")


class Park:

    def __init__(self):
        self.climatic_zone_tundra = TundraClimaticZone(self)
        self.climatic_zone_moderate = ModerateClimaticZone(self)
        self.zone = self.climatic_zone_tundra

    def change_climatic_area(self):
        self.zone.change_climatic_zone()

    def show_climatic_area(self):
        self.zone.show_climatic_zone()

    def observe_distance(self, distance):
        self.zone.observe(distance)


# app
park = Park()

park.show_climatic_area()
park.observe_distance(30)
park.observe_distance(60)
park.observe_distance(110)
park.observe_distance(310)

park.change_climatic_area()
park.observe_distance(100)
park.observe_distance(250)

park.change_climatic_area()
park.observe_distance(10)
park.observe_distance(250)
