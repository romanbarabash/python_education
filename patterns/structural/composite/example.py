'''
Relations with Other Patterns

You can use Builder when creating complex Composite trees because you can program its construction steps to work recursively.

Chain of Responsibility is often used in conjunction with Composite.
In this case, when a leaf component gets a request,
it may pass it through the chain of all of the parent components down to the root of the object tree.

You can use Iterators to traverse Composite trees.

You can use Visitor to execute an operation over an entire Composite tree.

You can implement shared leaf nodes of the Composite tree as Flyweights to save some RAM.

Composite and Decorator have similar structure diagrams
since both rely on recursive composition to organize an open-ended number of objects.

A Decorator is like a Composite but only has one child component.
There’s another significant difference: Decorator adds additional responsibilities to the wrapped object,
while Composite just “sums up” its children’s results.

However, the patterns can also cooperate: you can use Decorator to extend the behavior of a specific object in the Composite tree.

Designs that make heavy use of Composite and Decorator can often benefit from using Prototype.
Applying the pattern lets you clone complex structures instead of re-constructing them from scratch.
'''

from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def return_price(self):
        pass


class Box(Item):
    def __init__(self, contents):
        self.contents = contents

    def return_price(self):
        price = 0
        for item in self.contents:
            price = price + item.return_price()
        return price


class Phone(Item):
    def __init__(self, price):
        self.price = price

    def return_price(self):
        return self.price


class Charger(Item):
    def __init__(self, price):
        self.price = price

    def return_price(self):
        return self.price


class Earphones(Item):
    def __init__(self, price):
        self.price = price

    def return_price(self):
        return self.price


phone_case_contents = []
phone_case_contents.append(Phone(200))
phone_case_box = Box(phone_case_contents)

print("Phone case box total price: " + str(phone_case_box.return_price()))

big_box_contents = []
big_box_contents.append(phone_case_box)
big_box_contents.append(Charger(10))
big_box_contents.append(Earphones(10))
big_box = Box(big_box_contents)

print("Big box total price: " + str(big_box.return_price()))

