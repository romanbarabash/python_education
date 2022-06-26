'''
Relations with Other Patterns

Bridge is usually designed up-front, letting you develop parts of an application independently of each other.
On the other hand, Adapter is commonly used with an existing app to make some otherwise-incompatible classes work together nicely.

Bridge, State, Strategy (and to some degree Adapter) have very similar structures.
Indeed, all of these patterns are based on composition, which is delegating work to other objects.
However, they all solve different problems. A pattern isn’t just a recipe for structuring your code in a specific way.
It can also communicate to other developers the problem the pattern solves.

You can use Abstract Factory along with Bridge.
This pairing is useful when some abstractions defined by Bridge can only work with specific implementations.
In this case, Abstract Factory can encapsulate these relations and hide the complexity from the client code.

You can combine Builder with Bridge: the director class plays the role of the abstraction,
while different builders act as implementations.

'''


# Passenger & Cargo Carriers

class Carrier:
    def carry_military(self, items):
        pass

    def carry_commercial(self, items):
        pass


class Cargo(Carrier):
    def carry_military(self, items):
        print("The plane carries", items, "military cargo goods")

    def carry_commercial(self, items):
        print("The plane carries", items, "commercial cargo goods")


class Passenger(Carrier):
    def carry_military(self, passengers):
        print("The plane carries", passengers, "military passengers")

    def carry_commercial(self, passengers):
        print("The plane carries", passengers, "commercial passengers")


# Military & Commercial Planes
class Plane:
    def __init__(self, Carrier):
        self.carrier = Carrier

    def display_description(self):
        pass

    def add_items(self):
        pass


class Commercial(Plane):
    def __init__(self, Carrier, items):
        super().__init__(Carrier)
        self.items = items

    def display_description(self):
        self.carrier.carry_commercial(self.items)

    def add_items(self, new_items):
        self.items += new_items


class Military(Plane):
    def __init__(self, Carrier, items):
        super().__init__(Carrier)
        self.items = items

    def display_description(self):
        self.carrier.carry_military(self.items)

    def add_items(self, new_items):
        self.items += new_items


cargo = Cargo()
passenger = Passenger()

# Bridging Military and Cargo classes
military1 = Military(cargo, 100)
military1.display_description()
military1.add_items(25)
military1.display_description()

# Bridging Military and Passenger classes
military2 = Military(passenger, 250)
military2.display_description()
military2.add_items(10)
military2.display_description()

# Bridging Commercial and Passenger
commercial1 = Commercial(passenger, 400)
commercial1.display_description()
commercial1.add_items(50)
commercial1.display_description()

# Bridging Commercial and Cargo
commercial2 = Commercial(cargo, 150)
commercial2.display_description()
commercial2.add_items(15)
commercial2.display_description()
