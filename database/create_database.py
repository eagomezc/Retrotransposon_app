import csv
import sqlite3
from sqlite3 import Error

############ CONFIGURATION
# source file names
source_files = ("ERV.csv", "L1.csv")
# path to sqlite3 db file
db_file = "mainsqlite.db"
# table name to store the data
table_name = "maintable1"
########### END OF CONFIGURATION

print("Starting the importer")


# The logic is executed here
def importData(source_filename):
    try:
        # Connecting to the DB or to create a new DB if not exists
        dbconn = sqlite3.connect(db_file)
        dbcursor = dbconn.cursor()
        print("Connected, sqlite3.version", sqlite3.version)

        # Check if the table exists
        dbcursor.execute("""
            SELECT COUNT(*)
            FROM sqlite_master
            WHERE type='table' AND name='{0}'
            """.format(table_name.replace('\'', '\'\'')))
        if dbcursor.fetchone()[0] != 1:
            # Table does not exist, we have to create it.\
            print("Table does not exist, we have to create it")
            dbcursor.execute('''CREATE TABLE '{0}'
                  (genoName	TEXT,
                  genoStart	INT,
                  genoEnd	INT,
                  strand	TEXT,
                  repName	TEXT,
                  repClass	TEXT,
                  repFamily	TEXT,
                  repStart	INT,
                  repEnd	INT,
                  Sequence	TEXT,
                  Gag 		TEXT,
		          Pol 		TEXT,
		          Env		TEXT,
		          ORF1		TEXT,
		          ORF2		TEXT,
		          ORF0		TEXT)'''
                             .format(table_name.replace('\'', '\'\'')))

        # Open source file and read line by line from it
        with open(source_filename) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                dbcursor.execute('''INSERT INTO '{0}' (
                                    "genoName",
                                    "genoStart",
                                    "genoEnd",
                                    "strand",
                                    "repName",
                                    "repClass",
                                    "repFamily",
                                    "repStart",
                                    "repEnd",
                                    "Sequence",
                                    "Gag"
				                    "Pol"
				                    "Env"
				                    "ORF1"
				                    "ORF2"
				                    "ORF0") VALUES (
                                    :genoName,
                                    :genoStart,
                                    :genoEnd,
                                    :strand,
                                    :repName,
                                    :repClass,
                                    :repFamily,
                                    :repStart,
                                    :repEnd,
                                    :Sequence,
                                    :Gag
				                    :Pol
				                    :Env
				                    :ORF1
				                    :ORF2
				                    :ORF0
                                    );'''.format(table_name.replace('\'', '\'\'')),
                                 {
                                     "genoName": row["genoName"],
                                     "genoStart": row["genoStart"],
                                     "genoEnd": row["genoEnd"],
                                     "strand": row["strand"],
                                     "repName": row["repName"],
                                     "repClass": row["repClass"],
                                     "repFamily": row["repFamily"],
                                     "repStart": row["repStart"],
                                     "repEnd": row["repEnd"],
                                     "Sequence": row["Sequence"],
                                     "Gag": row["Gag"]
				                     "Pol": row["Pol"]
				                     "Env": row["Env"]
				                     "ORF1": row["ORF1"]
				                     "ORF2": row["ORF2"]
				                     "ORF0": row["ORF0"]
                                 })
                print("Created a new row")
        dbconn.commit()
        dbcursor.close()
    except Error as e:
        # In case of an error print the message
        print(e)
    finally:
        dbconn.close()


# Method to search for the data in the db
def search_str(query):
    result = None
    try:
        # Connecting to the DB or to create a new DB if not exists
        dbconn = sqlite3.connect(db_file)
        dbcursor = dbconn.cursor()
        print("Connected, sqlite3.version", sqlite3.version)
        dbcursor.execute("""
            SELECT *
            FROM '{0}'
            WHERE genoName=:genoName
            """.format(table_name.replace('\'', '\'\'')), {"genoName": query})
        result = dbcursor.fetchall()
        dbcursor.close()
    except Error as e:
        # In case of an error print the message
        print(e)
    finally:
        dbconn.close()
    return result

# Iterate over source files and import them
for src_file in source_files:
    importData(src_file)

# Method to search for the data in the db, example of usage
# for entry in search_str('chr1'):
#     print(entry)



print("Importer finished")
