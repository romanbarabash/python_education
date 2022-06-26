seasons_dict = {'winter': 'cold', 'summer': 'hot', 'spring': 'moderate', 'autumn': 'rainy'}
nonexist = {'midsummer': 'hell'}

print("# keys will be converted to list")
seasons_list = list(seasons_dict)
print(seasons_list)

"""Dictionary methods"""

print("# make a copy of dict")
c1_seasons_dict = dict(seasons_dict)
c2_seasons_dict = seasons_dict.copy()

print(seasons_dict)
print(c1_seasons_dict)
print(c2_seasons_dict)
print()

print("# clear dict")
c1_seasons_dict.clear()

print(seasons_dict)
print(c1_seasons_dict)
print(c2_seasons_dict)
print()

print("# update dictionary")
seasons_dict.update(nonexist)

print(seasons_dict)
print(c1_seasons_dict)
print(c2_seasons_dict)
print()

print("# get dict key, if no key get 0")
x = seasons_dict.get('winter', 0)
print(x)
print()

print("# if key is not in dict, than add key : value, if key is in dict, then do nothing")
seasons_dict.setdefault('midwinter', 'freezy')
print(seasons_dict)
print()

"""keys, values, items"""

print("# get all keys or all values of the dictionary")
k = seasons_dict.keys()
v = seasons_dict.values()
i = seasons_dict.items()
print(k)
print(v)
print(i)
print()

keys = list(seasons_dict)
print(keys)

print()

seasons_dict['midspring'] = 'perfect'

print("# dict_keys, dict_values, dict_items types track changes into dict after add another key : pair value")
print(k)
print(v)
print(keys)
print(i)
print()

print("# check each value of dict")
values = list(seasons_dict.values())
for val in values:
    print("value: " + val)
print()

print("# del key : value, if key not found None will return. index store deleted key")
index = c2_seasons_dict.pop("winter", None)
print(index)
print(c2_seasons_dict)
print()
