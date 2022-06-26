class A:
    print("class A")

    'hello'.replace('l', '?')
    x = str.replace('hello', 'l', '?')  # self, arg1, arg2

    print(x, end="\n\n")


class B:
    print("class B")

    a = {'x': 1}

    z = a.get('f', 999)  # arg1, arg2
    y = dict.get(a, 'f', 999)  # self, arg1, arg2

    print(z)
    print(y, end="\n\n")


class Z:
    print("class Z")

    name = 'default'

    def say_name(obj):
        print(obj.name)


# created object
say = Z()
# get name property
print(say.name)
print(Z.name)

# changed property
say.name = 'UuUuUuUu'

# Z is class, we call say_name class method and specify to what already created object
Z.say_name(say)

# say is object of class Z and we apply say_name class method to this object, say is also 1st argument
say.say_name()

# created object
tell = Z()
# print default name, name not changed for another object
tell.say_name()

# changed property name of the class Z
Z.name = 'hi'
greeting = Z()
# different name
greeting.say_name()

invitation = Z()
greeting.say_name()

"""
Notes:
Метод будет вызываться с объкетом в первом аргументе.
Все методы работают относительно объекта жертвы
Если смотреть на вызов методов, сам объект выполняет эти действия.
Первый аргумент любого метода, это не просто объект соответствующего класса, это сам объект который выполняет действия.
Если хотим узнать name объекта, то мы хотим узнать собственное свойство этого объекта. #34
Если захотим изменить имя объекта, то меняем имя конкретного объекта #38
Если захотим изменить имя свойства, изменяем имя свойство ссылающегося на класс. #52
"""


class Operations:
    print("class Operations")
    name = 'Dale Cooper'

    def say(self):
        print(self.name)

    def set(self, new_name):
        self.name = new_name

    def get(self):
        return self.name

    def reset(self):
        self.name = 'Dale Cooper'


dale = Operations()

dale.say()

name = dale.get()
print(name)

dale.set("Bob")
name = dale.get()
print(name)

dale.reset()
name = dale.get()
print(name)
