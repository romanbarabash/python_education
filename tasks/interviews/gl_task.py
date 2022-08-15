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
