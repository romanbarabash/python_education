import sqlite3

import pandas

# Establish a connection and create cursor
con = sqlite3.connect('database.db')
cur = con.cursor()

df = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)
df.to_csv('database.csv')
