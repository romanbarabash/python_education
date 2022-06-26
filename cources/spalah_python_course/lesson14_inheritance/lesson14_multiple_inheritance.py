class Fly:
    def fly(self):
        print('flying')


class Walk:
    def walk(self):
        print('walking')


class Move(Walk, Fly):
    def move(self):
        if hasattr(self, 'walk'):
            return self.walk()
        elif hasattr(self, 'fly'):
            return self.fly()
        else:
            return 'undefined'


obj = Move()
obj.move()  # inheritance provide an ability for us to range attribute of our object and input in accordance with it
