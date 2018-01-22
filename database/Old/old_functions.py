import sqlite3
import pandas as pd

from sqlalchemy import create_engine

conn = sqlite3.connect("projectdb.db")
c = conn.cursor()

def getByRepName(repName):
	c.execute("select * from genoTable where repName=?",(repName,))
	for row in c.fetchall():
		print(row)

	c.close()
	conn.close()

def getBygenoStart(genoStart):
	c.execute("select * from genoTable where genoStart=?",(genoStart,))
	for row in c.fetchall():
		print(row)

	c.close()
	conn.close()

def insert(genoName, genoStart, genoStart, strand, repName, repClass, repFamily, repStart, repEnd, sequence, aminoacid):
	c.execute("insert into genoTable(genoName, genoStart, genoStart, strand, repName, repClass, repFamily, repStart, repEnd, sequence, aminoacid) values(?,?,?,?,?,?,?,?,?,?,?)", (genoName, genoStart, genoStart, strand, repName, repClass, repFamily, repStart, repEnd, sequence, aminoacid))
	conn.commit()


insert("1","2",'+',"4","5","1","2","3","4","5")
# getByRepName("MLT1A1")
getBygenoStart("2")