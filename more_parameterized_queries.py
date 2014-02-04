import sqlite3 as lite
import sys

uId = 4

con = lite.connect('test.db')

with con:

	cur = con.cursor()

	cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id",
			{"Id": uId})
	con.commit()

	row = cur.fetchone()
	print row[0], row[1]
