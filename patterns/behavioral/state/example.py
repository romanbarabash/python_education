'''
Bridge, State, Strategy (and to some degree Adapter) have very similar structures.
Indeed, all of these patterns are based on composition, which is delegating work to other objects. However, they all solve different problems. A pattern isn’t just a recipe for structuring your code in a specific way. It can also communicate to other developers the problem the pattern solves.

State can be considered as an extension of Strategy.
Both patterns are based on composition: they change the behavior of the context by delegating some work to helper objects.
Strategy makes these objects completely independent and unaware of each other.
However, State doesn’t restrict dependencies between concrete states, letting them alter the state of the context at will.

'''


class State:
    """Base state. This is to share functionality"""

    def scan(self):
        """Scan the dial to the next station"""
        self.position += 1

        """check for the last station"""
        if self.position == len(self.stations):
            self.position = 0
        print("Visiting... Station is {} {}".format(self.stations[self.position], self.name))


class AmState(State):
    """Separate Class for AM state of the radio"""

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.position = 0
        self.name = "AM"

    """method for toggling the state"""

    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    """Constructor for FM state"""

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.position = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate


class Radio:
    """A radio. It has a scan button, and an AM / FM toggle switch."""

    def __init__(self):
        """We have an AM state and an FM state"""
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


# app
radio = Radio()
radio.scan()
radio.scan()
radio.scan()
radio.scan()
radio.toggle_amfm()
radio.scan()
radio.scan()
radio.scan()
radio.scan()
radio.toggle_amfm()
radio.scan()
radio.scan()
radio.scan()
