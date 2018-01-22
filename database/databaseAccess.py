import sqlite3
import pandas as pd

from sqlalchemy import create_engine

# Opens a file called projectdb with a SQLite3 DB
conn = sqlite3.connect("mainsqlite.dbb")
# Get a cursor object
c = conn.cursor()

# Get All data against given 'repName'
def getAllByRepName(repName):
	c.execute("select * from genoTable where repName=?",(repName,))
	for row in c.fetchall():
		print(row)

# Get All data against given 'genoStart'
def getByGenoStart(genoStart):
	c.execute("select * from genoTable where genoStart=?",(genoStart,))
	for row in c.fetchall():
		print(row)

# Get All data against given 'repFamily'
def getByRepFamily(repFamily):
	c.execute("select * from genoTable where repFamily=?",(repFamily,))
	for row in c.fetchall():
		print(row)

# Get All data against given 'repClass'
def getByRepClass(repClass):
	c.execute("select * from genoTable where repClass=?",(repClass,))
	for row in c.fetchall():
		print(row)

# Get All chromesome number against given 'repName'
def getChromosomeNumberByRepName(repName):
	c.execute("select genoName,genoStart,genoEnd,strand from genoTable where repName=?",(repName,))
	for row in c.fetchall():
		print(row)

# Insert records into project db database
def insert(genoName, genoStart, genoEnd, strand, repName, repClass, repFamily, repStart, repEnd, sequence, aminoacid):
	c.execute("insert into genoTable(genoName, genoStart, genoEnd, strand, repName, repClass, repFamily, repStart, repEnd, sequence, aminoacid) values(?,?,?,?,?,?,?,?,?,?,?)", (genoName, genoStart, genoEnd, strand, repName, repClass, repFamily, repStart, repEnd, sequence, aminoacid))
	conn.commit() # Commit the 

# Get All data against given 'repClass'
def getByGenoId(id):
	c.execute("select * from genoTable where genoId=?",(id,))
	for row in c.fetchall():
		print(row)

# Update sequence value for given genoId
def updateSequence(id, sequence):
	c.execute("update genoTable set sequence=? where genoId=?", (sequence, id))
	conn.commit() # Commit the 
	getByGenoId(id)

# Update aminoAcid value for given genoId
def updateAminoAcid(id, aminoacid):
	c.execute("update genoTable set aminoacid=? where genoId=?", (aminoacid, id))
	conn.commit() # Commit the 
	getByGenoId(id)

# getByGenoStart("2")
# insert("1","2","2",'+',"4","5","1","2","3","4","5")
# getAllByRepName("MLT1A1")
# getChromosomeNumberByRepName("MLT1A1")
# getByRepFamily("ERVL")
# getByRepClass("LTR")
# getByGenoId(1)
updateSequence(1, "seq")
updateAminoAcid(1, "amino")

# getChromosomeNumberByRepName("MLT1A1")

# Close the cursor
c.close()
# Close the db connection
conn.close()
