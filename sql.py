import sqlite3
import csv

# connect to database
db = sqlite3.connect('test.db')

# create cursor
cur = db.cursor()

# create tables
cur.execute("Create table if not exists tax (company text, tax_paid text)")


# insert data
# cur.execute("insert into users values ('Artem', 'artem@daniliants.com')")
# cur.execute("insert into links values ('https://www.daniliants.com', 'artem@daniliants.com')")

with open('data.csv', 'r', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    line = 0
    for row in reader:
        if line != 0:
            print('Inserting line {}'.format(line))
            cur.execute("insert into tax values (?, ?)", (row[2], row[5]))
        line += 1


# for row in cur.execute('select * from users'):
#     print(row[0])
#     for link in cur.execute('select url from links where email=?', (row[1],)):
#         print(link[0])


# insert data
db.commit()

# close connection
db.close()