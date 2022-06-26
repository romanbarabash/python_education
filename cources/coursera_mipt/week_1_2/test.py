payments = ['Cash', 'Credit']

summary_table_data = {'Tax': '$0.00', 'Subtotal': '$7.77', 'Discounts': '$0.00', 'Cash': '$6.77', 'Credit': '$2.00'}


def get_payments_data(items):
    all_returned_items = {}
    for key, value in summary_table_data.items():
        for item in items:
            if key is item:
                all_returned_items[key] = value
    return all_returned_items


print(get_payments_data(payments))






