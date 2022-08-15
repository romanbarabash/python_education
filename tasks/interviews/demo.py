# task, count qty of similar chars in string
test_string = 'afdfghtttiioooayyyyyyyyyy11111'

def count_chars(obj):
    for item in sorted(set(obj)):
        qty_of_items_in_obj = obj.count(item)
        print(f'qty of {item} in {obj} is {qty_of_items_in_obj}')

count_chars(test_string)