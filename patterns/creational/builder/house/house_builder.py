from patterns.creational.builder.house.house import House
from patterns.creational.builder.house.interface_house_builder import IHouseBuilder


class HouseBuilder(IHouseBuilder):
    "The House Builder."

    def __init__(self):
        self.house = House()

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self

    def set_wall_material(self, wall_material):
        self.house.wall_material = wall_material
        return self

    def set_number_doors(self, number):
        self.house.doors = number
        return self

    def set_number_windows(self, number):
        self.house.windows = number
        return self

    def get_result(self):
        return self.house