import csv
import json


class CSVExample:
    data = [
        ['title', 'date', 'price'],
        ['pica', '1975', '0'],
        ['flex', '1976', '-1']
    ]

    with open('data.csv', 'w') as f:
        w = csv.writer(f)
    for line in data:
        w.writerow(line)
    print('I am done')

    with open('data.csv', 'r') as f:
        r = csv.reader(f)
    result = list(r)
    print(result)


class JSONExample:
    abc = [
        123, None, True, [
            {'x': 1, 'y': 2}, 133, 'hello'
        ]
    ]

    s = json.dumps(abc)
    print(s)

    data = json.loads(s)
    print(data)
