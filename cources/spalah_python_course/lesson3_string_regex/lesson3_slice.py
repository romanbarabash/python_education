"""item[START:STOP:STEP] """

sstr = "Hello, I am string"

print("##########srt###########")

# reverse string
print(sstr[::-1])

# slice of step 2
print(sstr[::2])

# slice from to end
print(sstr[7:])

# slice from begin to
print(sstr[:5])

print("##########list##########")

llist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']

# reverse list
print(llist[::-1])

# slice from 3 to the end
print(llist[3:])

# slice from start to 5
print(llist[:5])

# slice of step 2
print(llist[::2])

# slice from end (-1) to of reverse step -2
print(llist[-1:4:-2])

# add elements to position 3
llist[3:3] = ['x', 'y', 'z']
print(llist)

# remove elements from 4 to 7
del llist[4:7]
print(llist)
