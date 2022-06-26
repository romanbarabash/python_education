'''
A Facade class can often be transformed into a Singleton since a single facade object is sufficient in most cases.

Flyweight would resemble Singleton if you somehow managed to reduce all shared states of the objects to just one proxy object.
But there are two fundamental differences between these patterns:

There should be only one Singleton instance, whereas a Flyweight class can have multiple instances with different intrinsic states.
The Singleton object can be mutable. Flyweight objects are immutable.
Abstract Factories, Builders and Prototypes can all be implemented as Singletons.
'''


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print("Object created", s)
s1 = Singleton()
print("Object created", s1)
