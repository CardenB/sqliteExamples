import sqlite3 as lite
import sys


def writeData(data):

	f = open('cars.sql', 'w')
	with f:
		f.write(data)

db_con = lite.connect('test.db')
mem_con = lite.connect(':memory:')
with db_con and mem_con:
	db_cur = db_con.cursor()
	mem_cur = mem_con.cursor()
	db_cur.execute("SELECT * FROM Cars")
	rows = db_cur.fetchall()
	mem_cur.execute("DROP TABLE IF EXISTS Cars")
	mem_cur.execute("DROP TABLE IF EXISTS cars")
	mem_cur.execute("CREATE TABLE cars(Id INT, Name TEXT, Price INT)")
	mem_cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", rows)
	mem_cur.execute("DELETE FROM Cars WHERE Price < 30000")

	data = '\n'.join(mem_con.iterdump())

	writeData(data)

