from patterns.creational.builder.house.castle_director import CastleDirector
from patterns.creational.builder.house.houseboat_director import HouseBoatDirector
from patterns.creational.builder.house.icehouse_director import IceHouseDirector

ICEHOUSE = IceHouseDirector.construct()
CASTLE = CastleDirector.construct()
HOUSEBOAT = HouseBoatDirector.construct()

print(ICEHOUSE.construction())
print(CASTLE.construction())
print(HOUSEBOAT.construction())
