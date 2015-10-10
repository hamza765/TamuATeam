import sqlite3
import wave

conn = sqlite3.connect('mash.db')
c = conn.cursor()
conn2 = sqlite3.connect('users.db')
c2 = conn2.cursor()
conn3 = sqlite3.connect('fullmashes')
c3 = conn3.cursor()

def storemash():
	#create a table
	c.execute(' ' ' CREATE TABLE mash(title text, author text, file text) ' ' ')
	c.execute("INSERT INTO mash VALUES (' If I Were A Boy', 'keelay17', 'ifiwereaboy.wav')")
	conn.commit()
	conn.close()

def storeusers():
	c.execute(' ' ' CREATE TABLE users(uid text, password text)' ' ')
	

	