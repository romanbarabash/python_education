import csv
import os
import statistics

from apps.real_estate_app.data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file_csv(filename)
    query_data(data)


def print_header():
    print('-------------------------------')
    print('  REAL ESTATE DATA MINING APP  ')
    print('-------------------------------')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'utils', 'SacramentoRealEstateTransactions2008.csv')


def load_file_csv(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []

        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)
#
#         print(lines[:5])

def query_data(data):
    # if data was sorted by price:
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchase = data[-1]
    print("The most expensive house is ${:,}".format(high_purchase.price))

    # least expensive house?
    low_purchase = data[0]
    print("The least expensive house is ${:,}".format(low_purchase.price))

    # average price house?
    prices = (
        p.price  # projection or items
        for p in data
    )

    ave_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(ave_price)))

    # average price of 2 bedrooms houses
    two_bed_homes = (
        p  # projection or items
        for p in data  # the set to process
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_price = statistics.mean((announce(p.price, 'price') for p in homes))
    ave_baths = statistics.mean((p.baths for p in homes))
    ave_sqrt = statistics.mean((p.sq__ft for p in homes))
    print("The average price of a 2-bedroom home is ${:,}, baths={}, sq ft={:,}"
          .format(int(ave_price), round(ave_baths, 1), round(ave_sqrt, 1)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()
