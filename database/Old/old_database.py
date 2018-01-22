import csv
from sqlalchemy import *


db = create_engine('sqlite:///projectdb.db')

db.echo = False  # Try changing this to True and see what happens

metadata = MetaData(db)



table = Table('genoTable', metadata,
    Column('genoId', Integer, primary_key=True, autoincrement=True),
    Column('genoName', Integer),
    Column('genoStart', Integer),
    Column('genoEnd', Integer),
    Column('strand', String(1)),
    Column('repName', String),
    Column('repClass', String),
    Column('repFamily', String),
    Column('repStart', Integer),
    Column('repEnd', Integer),
    Column('sequence', String),
    Column('aminoAcid', String)
)
table.create()
# i = table.insert()

# with open('L1.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#     	i.execute(genoName=row[1], genoStart=row[2], strand=row [3], repName=row[4], repClass=row[5], repFamily=row[6], repStart=row[7], retpEnd=row[8], sequence=row[9], aminoacid=row[10])

# s = table.select()
# rs = s.execute()

# row = rs.fetchone()
# print ('Id:', row[0])
# print ('genoName:', row['genoName'])
# print ('genoStart:', row.genoStart)
# print ('strand:', row[table.c.strand])

# for row in rs:
#     print (row.name,'is', row.age, 'years old')