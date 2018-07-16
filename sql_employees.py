import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS nums(number INT)")

    for i in range(100):
        c.execute("INSERT INTO nums(number) VALUES(?)", (random.randint(0,100),))
    
