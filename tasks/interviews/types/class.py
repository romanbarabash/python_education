class WordCounter:
    words = []

    def add_word(self, word: str):
        self.words.append(word)

    def get_count(self, word: str) -> int:
        count = 0

        for item in self.words:
            if word == item:
                count += 1
        return count


wc = WordCounter()
wc.add_word('apple')
wc.add_word('banana')
wc.add_word('apple')

assert wc.get_count('apple') == 2
assert wc.get_count('banana') == 1
assert wc.get_count('cucumber') == 0
print("_" * 100)


class Animal:
    def sound_now(self):
        pass


class Dog(Animal):

    def __init__(self, name: str):
        self.name = name

    def sound_now(self):
        print(f"I'am a Dog My name is {self.name}. Gav")


class Cat(Animal):
    def __init__(self, name: str):
        self.name = name

    def sound_now(self):
        print(f"I'am a Cat My name is {self.name}. Mew")


if __name__ == "__main__":
    animals = []

    animals.append(Dog("Tuzik"))
    animals.append(Cat("Vasia"))

    for animal in animals:
        animal.sound_now()

''' Expected result
I'am a Dog My name is Tuzik. Gav
I'am a Cat My name is Vasia. Mew
'''
