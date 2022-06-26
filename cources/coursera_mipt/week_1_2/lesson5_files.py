text = "The world is changed.\nI taste it in the water.\n"

# # opened file for writing, then close
# f = open("/Users/roman.barabash/Documents/PycharmProjects/python_edu/coursera_mipt/files/sample", "w")
# f.write(text)
# f.close()

# # open file for (r+) reading/writing mode
# f = open("files/sample", "r+")
# print(f.read())
#
# # check cursor position (32)
# print(f.tell())
#
# # cursor is under position 32 here, we cannot read file once again
# print(f.read())
#
# # put cursor on position 0
# f.seek(0)
# print(f.tell())
#
# # now we can read file once again (note that cursor position will be 32, after reading)
# print(f.read())
# f.close()
#
# # read file by each line and the close
# f = open("files/sample", "r+")
# f.readlines()
# f.close()
#
# # we cannot read closed file
# # f.read()

# we can also use context manager to write file and not care about closing files
with open("/Users/roman.barabash/Documents/PycharmProjects/python_edu/coursera_mipt/files/sample", "w") as f:
    print(f.write(text))

# we can also use context manager to read file and not care about closing files
with open("/Users/roman.barabash/Documents/PycharmProjects/python_edu/coursera_mipt/files/sample") as f:
    print(f.read())
