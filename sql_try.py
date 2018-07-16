import sqlite3

with sqlite3.connect("new.db") as con:
	c = con.cursor()
	cities = [('Boston', 'MA', 245325), ('Chicago', 'IL', 2234452)]
	c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)
)

