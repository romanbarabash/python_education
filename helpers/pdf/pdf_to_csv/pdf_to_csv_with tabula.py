import tabula

table = tabula.read_pdf('weather.pdf')[0]
table.to_csv('output.csv')
