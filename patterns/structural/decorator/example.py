'''
Relations with Other Patterns

Decorator enhances an object without changing its interface. In addition,
Decorator supports recursive composition, which isn’t possible when you use Adapter.

Adapter provides a different interface to the wrapped object,
Proxy provides it with the same interface,
and Decorator provides it with an enhanced interface.

Chain of Responsibility and Decorator have very similar class structures.
Both patterns rely on recursive composition to pass the execution through a series of objects.
However, there are several crucial differences.

The CoR handlers can execute arbitrary operations independently of each other.
They can also stop passing the request further at any point.
On the other hand, various Decorators can extend the object’s behavior while keeping it consistent with the base interface.
In addition, decorators aren’t allowed to break the flow of the request.

Composite and Decorator have similar structure diagrams
since both rely on recursive composition to organize an open-ended number of objects.


Designs that make heavy use of Composite and Decorator can often benefit from using Prototype.
Applying the pattern lets you clone complex structures instead of re-constructing them from scratch.

Decorator lets you change the skin of an object, while Strategy lets you change the guts.

Decorator and Proxy have similar structures, but very different intents.
Both patterns are built on the composition principle, where one object is supposed to delegate some of the work to another.
The difference is that a Proxy usually manages the life cycle of its service object on its own,
whereas the composition of Decorators is always controlled by the client.

'''


def another_function(func):
    def other_func():
        val = "Результат от %s это %s" % (func(),
                                          eval(func()))
        return val

    return other_func


@another_function
def a_function():
    return "1+1"


if __name__ == "__main__":
    value = a_function()
    print(value)
