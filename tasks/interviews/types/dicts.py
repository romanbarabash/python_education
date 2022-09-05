# task, iterate over dict
print("_" * 100)

beatles_map = {
    'Paul': 'Bass',
    'John': 'Guitar',
    'George': 'Guitar',
}

# iterating by keys
print("iterating by keys: ")
for key in beatles_map.keys():
    print(key)

# iterating by keys, values
print("iterating by keys, values: ")
for key, value in beatles_map.items():
    print('{}: {}'.format(key, value))

# iterating by values
print("iterating by values: ")
for value in beatles_map.values():
    print(value)

# task, extract values from dict
print("_" * 100)
payments = ['Cash', 'Credit']
summary_table_data = {'Tax': '$0.00', 'Subtotal': '$7.77', 'Discounts': '$0.00', 'Cash': '$6.77', 'Credit': '$2.00'}


def get_payments_data(payment_types: list, payment_data: dict):
    all_returned_items = {}
    for item, price in payment_data.items():
        if item in payment_types:
            all_returned_items[item] = price
    return all_returned_items


print(f'task 3: {get_payments_data(payments, summary_table_data)}')

# task, traffic calculator
print("_" * 100)
raw = [x.split(" ") for x in open("log.txt")]

traffic_dict = {}
for ip, traffic in raw:
    if ip in traffic_dict:
        traffic_dict[ip] += int(traffic)
    else:
        traffic_dict[ip] = int(traffic)

traffic_list = sorted(traffic_dict.items(), key=lambda x: x[0], reverse=True)
print('task 4: ')
[print(i) for i in traffic_list]

# task, create dict from 2 lists, switch its values
print("_" * 100)
ids = [8, 4, 6, 9]
cities = ['Bristol', 'Toronto', 'Jakarta', 'Sydney']

cities_dict = dict()

for id, city in zip(sorted(ids), cities):
    cities_dict[id] = city

print('task 5: ')
print(cities_dict)


def switch_dict_values(d: dict):
    switched_dict = {}
    for k, v in d.items():
        switched_dict[v] = k
    return switched_dict


print(switch_dict_values(cities_dict))
