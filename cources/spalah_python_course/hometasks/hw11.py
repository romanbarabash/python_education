from datetime import datetime


class File:
    file = None

    def open(self, file_name):
        self.file = open(file_name, 'w')

    def line(self, text):
        self.file.write(text + '\n')

    def save(self, file_name):
        self.file = open(file_name, 'r')
        self.file.read()
        self.file.close()


f = File()
f.open('xxx.txt')
f.line('hello')
f.line('world')
f.save('xxx.txt')
f.open('xxx.txt')
f.line('bye')
f.line('world')


class Translator:
    def translate(self, number):
        pass


obj = Translator()
print(obj.translate(1))


class Date:
    def parse(self, date):
        datetime_object = datetime.strptime(date, '%d/%m/%Y').strftime('%d %B %Y year')
        print(datetime_object)


obj = Date()
obj.parse('21/03/1991')
