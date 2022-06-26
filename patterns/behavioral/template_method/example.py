class MakeMeal:
    def prepare(self):
        pass

    def cook(self):
        pass

    def eat(self):
        pass

    def clear(self):
        pass

    def perform(self):
        self.prepare()
        self.cook()
        self.eat()
        self.clear()


class MakePizza(MakeMeal):
    def prepare(self):
        print("Prepare Pizza")

    def cook(self):
        print("Cook Pizza")

    def eat(self):
        print("Eat Pizza")

    def clear(self):
        print("Clear kitchen after eat pizza")



class MakeTea(MakeMeal):
    def prepare(self):
        print("Prepare Tea")

    def cook(self):
        print("Cook Tea")

    def eat(self):
        print("Drink Tea")

    def clear(self):
        print("Clear teapot")



makePizza = MakePizza()
makePizza.perform()

print(25 * "+")

makeTea = MakeTea()
makeTea.perform()
