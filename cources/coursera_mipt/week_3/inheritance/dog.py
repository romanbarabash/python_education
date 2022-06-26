import json

from cources.coursera_mipt.week_3.inheritance.lesson10_inheritance import Pet

"""
Here is an example of Inheritance from class Dog.
"""


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)


dog = Dog("Winsent", "Spaniel")
print(dog.name)
print(dog.breed)
print(dog.say())


class ExportJSON:
    def __init__(self):
        self.breed = None
        self.name = None

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })


"""
Here is an example of multiple Inheritance from classes Dog, ExportJSON
"""


class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super().__init__(name, breed)


dog = ExDog("Harold", breed="Pudel")
print(dog.to_json())

"""
__mro__ attribute shows chain of inheritance for child class ExDog
"""

# Method Resolution Order
var = ExDog.__mro__
print(var)

"""
Here is an example of explicit definition of the class, which will be inherited.
       super(Dog, self).__init__(name)
"""


class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super(Dog, self).__init__(name)
        self.breed = "Woolen dog of {0} breed".format(breed)


dog = WoolenDog("Samson", breed="Pincher")
print(dog.breed)
