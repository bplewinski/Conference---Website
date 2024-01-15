import sqlite3
import csv

con = sqlite3.connect("../conference.sqlite")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS workshops"
            "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "workshop_title TEXT,"
            "session_ INTEGER,"
            "room_number TEXT,"
            "start_time TEXT,"
            "end_time TEXT)")

shopList = []
# Read csv into dictionary
with open('workshop.csv') as csvInputFile:
    reader = csv.DictReader(csvInputFile)
    for row in reader:
        shopList.append(row)

# Insert values from dict into workshop table
for item in shopList:
    cur.execute("INSERT INTO workshops "
                "('workshop_title','session_','room_number','start_time','end_time') "
                "VALUES (?,?,?,?,?)", (item['workshop_title'], item['session_'],
                                       item['room_number'], item['start_time'],
                                       item['end_time']))
con.commit()
con.close()
