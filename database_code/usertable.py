import sqlite3
import csv

con = sqlite3.connect("../conference.sqlite")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users"
            "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "username TEXT,"
            "firstname TEXT,"
            "lastname TEXT,"
            "password TEXT)")


# Function inserts row into index
def insertUser(row):
    cur.execute("INSERT INTO users "
                "('username','firstname','lastname','password') "
                "VALUES (?,?,?,?)", (row[0], row[1], row[2], row[3]))


# Read csv file
with open('users.csv') as csvInputFile:
    userReader = csv.reader(csvInputFile)
    header = next(userReader)
    for row in userReader:
        insertUser(row)
    con.commit()

con.close()
