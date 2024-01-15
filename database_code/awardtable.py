import sqlite3
import csv

con = sqlite3.connect("../conference.sqlite")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS nominees"
            "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "nominee_name TEXT,"
            "description TEXT,"
            "name_of_image_file TEXT,"
            "current_votes INTEGER)")


# Function inserts row into index
def insertNominee(row):
    cur.execute("INSERT INTO nominees "
                "('nominee_name','description','name_of_image_file','current_votes') "
                "VALUES (?,?,?,?)", (row[0], row[1], row[2], row[3]))


# Read csv file
with open('awards.csv') as csvInputFile:
    nomReader = csv.reader(csvInputFile)
    header = next(nomReader)
    for row in nomReader:
        insertNominee(row)
    con.commit()

con.close()
