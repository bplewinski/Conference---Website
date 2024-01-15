import sqlite3
import csv
from registrant import Registrant

con = sqlite3.connect("../conference.sqlite")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS registrants"
            "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "registration_date TEXT,"
            "title TEXT," 
            "firstname TEXT,"
            "lastname TEXT,"
            "address1 TEXT,"
            "address2 TEXT,"
            "city TEXT,"
            "state TEXT,"
            "zipcode INTEGER,"
            "telephone INTEGER,"
            "email TEXT,"
            "position TEXT,"
            "company TEXT,"
            "session1 TEXT,"
            "session2 TEXT,"
            "session3 TEXT)")


# Function iterates registrants list and inserts values into table
def insertReg(regList):
    for reg in regList:
        cur.execute("INSERT INTO registrants ('registration_date','title', "
                    "'firstname','lastname','address1','address2','city','state',"
                    "'zipcode','telephone','email','position','company','session1',"
                    "'session2','session3') "
                    "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (reg.registration_date, reg.title, reg.firstname, reg.lastname,
                     reg.address1, reg.address2, reg.city, reg.state, reg.zipcode,
                     reg.telephone, reg.email, reg.position, reg.company, reg.session1,
                     reg.session2, reg.session3))
    con.commit()


regList = []
# Reads file into a list of objects
with open('registrant_data.csv') as csvInputFile:
    regReader = csv.DictReader(csvInputFile, delimiter=',')
    for row in regReader:
        this_reg = Registrant(row)
        regList.append(this_reg)
    insertReg(regList)

con.close()
