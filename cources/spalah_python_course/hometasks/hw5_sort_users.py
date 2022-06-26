a = [['Peter', 10, 130, 35], ['Nick', 11, 135, 39], ['Jack', 9, 140, 33], ['Gerrard', 10, 128, 30]]

n = input('Sort by name (1), age (2), height (3), weight (4): ')

if not n.isdigit():
    print("Should be a digit")
    exit()

if int(n) > 4 or int(n) < 1:
    print("Number should be in range of 1-4")
    exit()

n = int(n) - 1


def sorted(i):
    return i[n]


a.sort(key=sorted)

for i in a:
    print("%7s %3d %4d %3d" % (i[0], i[1], i[2], i[3]))



