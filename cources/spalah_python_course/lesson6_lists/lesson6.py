"""List to string, string to list"""

eg_str = "hello"
eg_list = list(eg_str)
print(eg_list)

list_to_str = ['h', 'e', 'l', 'l', 'o']
joined_list = "".join(list_to_str)
print(joined_list)

"""Join 2 lists custom"""

list_to_join = ['h', 'e', 'l', 'l', 'o', 'y', 'o', 'u']
glue = [":", ",", "+"]

b = ''
i = 0

while i < len(list_to_join):
    item = list_to_join[i]
    b += str(item)
    if i < len(list_to_join) - 1:
        gi = i % len(glue)
        b += glue[gi]
    i += 1

print(b)

print("""List methods""")

list_to_join_2 = ['h', 'e', 'l', 'l', 'o', 'y', 'o', 'u']
x = ['&', '%', '*']
list_to_join_2.append("r")  # added el
print(list_to_join_2)

list_to_join_2.extend(x)  # added list
print(list_to_join_2)

list_to_join_2.insert(0, "y")  # insert el to 0
print(list_to_join_2)

list_to_join_2.pop()
print(list_to_join_2)  # del last el

list_to_join_2.pop(1)
print(list_to_join_2)  # del 2 el

x = list_to_join_2.index('u')  # find index of el
print(x)

z = list_to_join_2.copy()  # make a copy of list

z.reverse()  # revers list
print(z)

z.sort()  # sort list
print(z)


