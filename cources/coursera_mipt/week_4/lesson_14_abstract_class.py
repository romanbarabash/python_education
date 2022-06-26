from abc import ABCMeta, abstractmethod


class Sender(metaclass=ABCMeta):
    """
    Abstract class with 1 method
    """

    @abstractmethod
    def send(self):
        raise NotImplementedError


class Child(Sender):
    """
    Child should implement abstract method, another way err will be raised:
    TypeError: Can't instantiate abstract class Child with abstract methods send
    """

    def send(self):
        print('Sending')


c = Child()
c.send()
