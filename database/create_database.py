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
def importData( source_filename ):
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
                  (genoName	text,
                  genoStart	int,
                  genoEnd	int,
                  strand	text,
                  repName	text,
                  repClass	text,
                  repFamily	text,
                  repStart	int,
                  repEnd	int,
                  Sequence	int,
                  Aminoacid text)'''
                             .format(table_name.replace('\'', '\'\'')))

        # Open source file and read line by line from it
        with open(source_filename, newline='') as csvfile:
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
                                    "Aminoacid") VALUES (
                                    :genoName,
                                    :genoStart,
                                    :genoEnd,
                                    :strand,
                                    :repName,
                                    :repClass,
                                    :repFamily,
                                    :repStart,
                                    :repEnd,
                                    :sequence,
                                    :aminoacid
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
                                     "sequence": row["Sequence"],
                                     "aminoacid": row["Aminoacid"]
                                 })
                print("Created a new row")
                dbconn.commit()
        dbcursor.close()
    except Error as e:
        # In case of an error print the message
        print(e)
    finally:
        dbconn.close()

# Iterate over source files and import them
for src_file in source_files:
    importData(src_file)

print("Importer finished")