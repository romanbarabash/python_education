'''
Relations with Other Patterns

Facade defines a new interface for existing objects, whereas Adapter tries to make the existing interface usable.
Adapter usually wraps just one object, while Facade works with an entire subsystem of objects.

Abstract Factory can serve as an alternative to Facade
when you only want to hide the way the subsystem objects are created from the client code.

Flyweight shows how to make lots of little objects,
whereas Facade shows how to make a single object that represents an entire subsystem.

Facade and Mediator have similar jobs: they try to organize collaboration between lots of tightly coupled classes.

A Facade class can often be transformed into a Singleton since a single facade object is sufficient in most cases.

Facade is similar to Proxy in that both buffer a complex entity and initialize it on its own.
Unlike Facade, Proxy has the same interface as its service object, which makes them interchangeable.

'''


class _IgnitionSystem:

    @staticmethod
    def produce_spark():
        return True


class _Engine:

    def __init__(self):
        self.revs_per_minute = 0

    def turn_on(self):
        self.revs_per_minute = 2000

    def turn_off(self):
        self.revs_per_minute = 0


class _FuelTank:

    def __init__(self, level=30):
        self._level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level


class _DashBoardLight:

    def __init__(self, is_on=False):
        self._is_on = is_on

    def __str__(self):
        return self.__class__.__name__

    @property
    def is_on(self):
        return self._is_on

    @is_on.setter
    def is_on(self, status):
        self._is_on = status

    def status_check(self):
        if self._is_on:
            print("{}: ON".format(str(self)))
        else:
            print("{}: OFF".format(str(self)))


class _HandBrakeLight(_DashBoardLight):
    pass


class _FogLampLight(_DashBoardLight):
    pass


class _Dashboard:

    def __init__(self):
        self.lights = {"handbreak": _HandBrakeLight(),
                       "fog": _FogLampLight()}

    def show(self):
        for light in self.lights.values():
            light.status_check()


# Facade
class Car:

    def __init__(self):
        self.ignition_system = _IgnitionSystem()
        self.engine = _Engine()
        self.fuel_tank = _FuelTank()
        self.dashboard = _Dashboard()

    @property
    def km_per_litre(self):
        return 14.0

    def consume_fuel(self, km):
        litres = min(self.fuel_tank.level, km / self.km_per_litre)
        self.fuel_tank.level -= litres

    def start(self):
        print("\nStarting...")
        self.dashboard.show()
        if self.ignition_system.produce_spark():
            self.engine.turn_on()
        else:
            print("Can't start. Faulty ignition system")

    def has_enough_fuel(self, km, km_per_litre):
        litres_needed = km / km_per_litre
        if self.fuel_tank.level > litres_needed:
            return True
        else:
            return False

    def drive(self, km=100):
        print("\n")
        if self.engine.revs_per_minute > 0:
            while self.has_enough_fuel(km, self.km_per_litre):
                self.consume_fuel(km)
                print("Drove {}km".format(km))
                print("{:.2f}l of fuel still left".format(self.fuel_tank.level))
        else:
            print("Can't drive. The Engine is turned off!")

    def park(self):
        print("\nParking...")
        self.dashboard.lights["handbreak"].is_on = True
        self.dashboard.show()
        self.engine.turn_off()

    def switch_fog_lights(self, status):
        print("\nSwitching {} fog lights...".format(status))
        boolean = True if status == "ON" else False
        self.dashboard.lights["fog"].is_on = boolean
        self.dashboard.show()

    def fill_up_tank(self):
        print("\nFuel tank filled up!")
        self.fuel_tank.level = 60


# App
car = Car()
car.start()
car.drive()
car.switch_fog_lights("ON")
car.switch_fog_lights("OFF")
car.park()
car.fill_up_tank()
car.drive()
car.start()
car.drive()

# Create parts of functionality -> Cover logic and functionalities behaviour at Facade class -> Use facade framework in the app
