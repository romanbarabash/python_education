mstr = "Moonfish, steelhead, lamprey southern flounder tadpole fish sculpin bigeye, blue-redstripe danio collared dogfish. 6 Smalleye squaretail goldfish arowana butterflyfish pipefish wolf-herring jewel tetra, shiner; gibberfish red velvetfish. Thornyhead yellowfin pike threadsail ayu cutlassfish."

# replace a to b, b to a in python
a = 10
b = 20

a, b = b, a
print(a, b)

# repeat string several times
repeat = "hi" * 10
print(repeat)

"""String methods"""

# len
len_my_str = len(mstr)
print(len_my_str)

# verify if is digit
print(mstr.isdigit())

# is alpha - letters only
print(mstr.isalpha())

# remove all spaces
spaced = " Moonfish, steelhea "
print(spaced.lstrip())

# aссess string by index
char = mstr[1]
print(char)

# find string under string, first appirence. Also .index .
str_find = mstr.find("fish")
print(str_find)

# replace string to string
repleased_string = mstr.replace("fish", "mouse")
print(repleased_string)

# verify if string consist alpha, num or alpha-num
print(mstr.isdigit())
print(mstr.isalpha())
print(mstr.isalnum())

# split into the list
mlist = mstr.split(" ")
print(mlist)

# join string by char
joined = "-".join(mlist)
print(joined)
