class Subject:
    """Represents what is being observed"""

    def __init__(self):
        """Create an empty observer list"""
        self._observers = []

    def notify(self):
        """Alert the observers"""
        for observer in self._observers:
            observer.update(self)

    def attach(self, observer):
        """If the observer is not in the list, append it into the list"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Remove the observer from the observer list"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


class Listener(Subject):
    """Monitor the object"""

    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        self.notify()


class HexViewer:
    """Updates the Hex viewer"""

    def update(self, subject):
        print('HexViewer: Subject {} has price 0x{:x}'.format(subject.name, subject.price))


class OctalViewer:
    """Updates the Octal viewer"""

    def update(self, subject):
        print('OctalViewer: Subject ' + str(subject.name) + ' has price ' + str(oct(subject.price)))


class DecimalViewer:
    """updates the Decimal viewer"""

    def update(self, subject):
        print('DecimalViewer: Subject % s has price % d' % (subject.name, subject.price))


if __name__ == "__main__":
    listener_1 = Listener('Processor')
    listener_2 = Listener('Video Card')

    decimal_view = DecimalViewer()
    hex_view = HexViewer()
    octal_view = OctalViewer()

    listener_1.attach(decimal_view)
    listener_1.attach(hex_view)
    listener_1.attach(octal_view)
    listener_2.attach(decimal_view)
    listener_2.attach(hex_view)
    listener_2.attach(octal_view)

    listener_1.price = 10

    listener_1.detach(hex_view)
    listener_2.detach(hex_view)
    listener_1.detach(octal_view)
    listener_2.detach(octal_view)

    listener_1.price = 20
    listener_2.price = 15
    listener_1.price = 100
    listener_2.price = 150

# Listen to some entity. eg 'Video Card' ->
# attach subscribers ->
# update entity value and got notifications (3 subscribers) ->
# detach subscribers ->
# update entity value and got notifications (1 subscribers)
