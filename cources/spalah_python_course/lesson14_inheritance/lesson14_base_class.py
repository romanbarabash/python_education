class Runner:
    def run(self):
        return 'run'


class FastRunner(Runner):
    def run(self):
        original = super().run()  # super() is used here to get method from Parent class, is substitute to self, but
        # for parent class
        return original + ' faster'


a = Runner()
print(a.run())

b = FastRunner()
print(b.run())
