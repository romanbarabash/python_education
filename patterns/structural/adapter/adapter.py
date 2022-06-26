'''
Relations with Other Patterns

Adapter is commonly used with an existing app to make some otherwise-incompatible classes work together nicely.

Adapter changes the interface of an existing object, while Decorator enhances an object without changing its interface.
In addition, Decorator supports recursive composition, which isn’t possible when you use Adapter.

Adapter provides a different interface to the wrapped object,
Proxy provides it with the same interface,
and Decorator provides it with an enhanced interface.

Facade defines a new interface for existing objects, whereas Adapter tries to make the existing interface usable.
Adapter usually wraps just one object, while Facade works with an entire subsystem of objects.

Bridge, State, Strategy (and to some degree Adapter) have very similar structures.
Indeed, all of these patterns are based on composition, which is delegating work to other objects.
However, they all solve different problems. A pattern isn’t just a recipe for structuring your code in a specific way.
It can also communicate to other developers the problem the pattern solves.

'''


# Target interface
class EuropeanSocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

    def earth(self): pass


# Target interface
class USASocketInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass


# Adaptee
class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# The Adapter
class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


# Client
class ElectricKettle:
    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle on fire!")
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print("Coffee time!")
            else:
                print("No power.")


def main():
    # Plug in
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    # Make coffee
    kettle.boil()


if __name__ == "__main__":
    main()
