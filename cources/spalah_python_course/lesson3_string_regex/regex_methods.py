import re

"""
Regex methods

re.match(pattern, string) # метод ищет по заданному шаблону в начале строки.

.start() # узнать начальную позицию найденной строки.

.end() # узнать конечную позицию найденной строки.

re.search(pattern, string): # ищет по всей строке, но возвращает только первое найденное совпадение.

re.findall(pattern, string): # метод возвращает список всех найденных совпадений. 

re.split(pattern, string, [maxsplit=0]): # разделяет строку по заданному шаблону. maxsplit=0 если указать этот аргумент,
то разделение будет произведено не более указанного количества раз.

re.sub(pattern, repl, string): # ищет шаблон в строке и заменяет его на указанную подстроку. Если шаблон не найден, 
строка остается неизменной.

re.compile(pattern, repl, string): # можем собрать регулярное выражение в отдельный объект,
который может быть использован для поиска. Это также избавляет от переписывания одного и того же выражения.

"""

print("re.match()")
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result)  # <_sre.SRE_Match object; span=(0, 2), match='AV'>
print(result.group(0))  # AV
print(result.start())  # 0
print(result.end())  # 2

print("re.search()")
result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print(result.group(0))  # Analytics

print("re.findall()")
result = re.findall(r'AV', 'AV Analytics Vidhya AV av')
print(result)  # ['AV', 'AV']

print("re.split()")
result = re.split(r'i', 'Analytics Vidhya', maxsplit=1)
print(result)  # ['Analyt', 'cs Vidhya']

print("re.sub()")
result = re.sub(r'India', 'the World', 'AV is largest Analytics community of India')
print(result)  # AV is largest Analytics community of the World

print("re.compile()")
pattern = re.compile('AV')
result = pattern.findall('AV Analytics Vidhya AV')
print(result)  # ['AV', 'AV']
result2 = pattern.findall('AV is largest analytics community of India')
print(result2)  # ['AV']
