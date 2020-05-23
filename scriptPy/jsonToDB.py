# -*- coding: utf-8 -*-
import json
import mysql.connector
from mysql.connector import Error

class marianDBConnect:
	def __init__(self, sqlcomm):
		self.sqlcomm = sqlcomm

	def connectDB(self):
		connection = mysql.connector.connect(
			host='localhost',
			database='MEMBER',
			user='root',	
			password='123456')

		return connection

	def queryExec(self, conn):
		cursor = conn.cursor()
		cursor.execute(self.sqlcomm)

		return cursor

	def insertExec(self, conn, values):
		cursor = conn.cursor()
		cursor.execute(self.sqlcomm, values)

		conn.commit()
		
		return cursor

	def closeDB(self, cursor, conn):
		if (conn.is_connected()):
			cursor.close()
			conn.close()

def queryMYTABLE():
	query = "SELECT username, passwd FROM MYTABLE"

	db = marianDBConnect(query)
	conn = db.connectDB()
	result = db.queryExec(conn)

	for (username, passwd) in result:
		print("Name: %s, Age: %s" % (username, passwd))

	db.closeDB(result, conn)	

def insertPTTTITLE(date, push, title, url, auth):
	sqlcomm = "insert into ptttitle (date, push, title, url, auth, systime) values (%s, %s, %s, %s, %s, NOW())"
	values = (date, push, title, url, auth)
	db = marianDBConnect(sqlcomm)
	conn = db.connectDB()
	result = db.insertExec(conn, values)			
	db.closeDB(result, conn)	

def scanJSON():
	with open('/Users/leetsunewei/Documents/python_dir/Scrapy/spiderfind/output/titleout.json' , 'r') as reader:
		jf = json.loads(reader.read())

	for i in range(len(jf)):
		date = jf[i]['date']
		push = jf[i]['push']
		title = jf[i]['title']
		url = jf[i]['url']
		auth = jf[i]['author']
		
		insertPTTTITLE(date, push, title, url, auth)

def main():
	scanJSON()
	queryMYTABLE()

if __name__== "__main__":
	main()

