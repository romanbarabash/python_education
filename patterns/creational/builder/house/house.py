class House():
    "The Product"

    def __init__(self, building_type="Apartment", doors=0,
                 windows=0, wall_material="Brick"):
        self.wall_material = wall_material
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def construction(self):
        "Returns a string describing the construction"
        return f"This is a {self.wall_material} " \
               f"{self.building_type} with {self.doors} " \
               f"door(s) and {self.windows} window(s)."
