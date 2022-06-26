# Напишите код, который позволит отсортировать предоставленный массив в порядке убывания длины вложенных элементов.

sortList = [
    'hello',
    [1, 2, 4, 5],
    ['world'],
    'world!',
    [],
    [50, 1],
    [7, 3, 'hoho']
]


def sortByLength(inputStr):
    return len(inputStr)


sortList.sort(key=sortByLength)
print(sortList)

sortList.sort(key=sortByLength, reverse=True)
print(sortList)
