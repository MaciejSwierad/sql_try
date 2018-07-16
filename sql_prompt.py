import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    a = input("avg, min, max, sum")
    c.execute("SELECT {}(number) FROM nums".format(a))
    get = c.fetchone()

    print(get[0])
    #b = c.execute('SELECT {}(number) FROM nums'.format(a))
    #print(b)
