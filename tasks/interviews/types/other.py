# task 1, find words qty in sentence
print("_" * 100)
task_1 = "hi, i am an arm and i sound like uUuUuuUU"


def words_counter(st):
    li = st.split(" ")
    return len(li)


print("task 1:", words_counter(task_1))

# task 2, list objects in the memory
print("_" * 100)
a = [5, 6, 8]
b = a + []
print("task 2:")

print(a == b, a is b)
print(id(a), id(b))  # diff ids

b = a
print(id(a), id(b))  # same ids

b[2] = 10
print(a)
print(b)

# task 3, check if string is palindrome
print("_" * 100)


def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome('madam'))
