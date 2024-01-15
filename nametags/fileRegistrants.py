from registrants2 import Registrants
import csv

list_of_registrants = []

# Saves a row of the registrant file into person object
# Each row is then appended to an array after each loop
try:
    with open('registrant_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person = Registrants(row)
            list_of_registrants.append(person)

except OSError as err:
    print("OS error: {0}".format(err))

# Variables for HTML code
header = '''<!DOCTYPE html>\n<html lang='en'>\n<head>\n\t<meta charset='UTF-8'>\n\t<title>Name Tags 10gen</title>
\t<link rel='stylesheet' href='CSS/nametags10.css'>\n</head>\n<body>'''

closing = '''\n</div>\n</body>\n</html>'''

divpage = '''\n<div class="page">'''
divrow = '''\n\t<div class="row">'''
divleft = '''\n\t\t<div class="left">'''
divright = '''\n\t\t<div class="right">'''

fname = '''<p class ="first">'''
lname = '''<p class ="last">'''
job = '''<p class ="job">'''
company = '''<p class ="company">'''
city = '''<p class ="city">'''
state = '''<p class ="state">'''

endp = '''</p>'''
enddiv1 = '''</div>'''
enddiv2 = '''\n\t</div>'''

# New HTML file is written from array and HTML variables
row = 0
page = 0
try:
    with open('nametags10gen.html', 'w') as outputFile:
        outputFile.write(header)
        outputFile.write(divpage)
        for person in list_of_registrants:
            row = row + 1
            if row == 1:
                outputFile.write(divrow)
                outputFile.write(divleft)
                outputFile.write(fname + person.firstname + endp + lname + person.lastname + endp + job
                                 + person.job + endp + company + person.company + endp + city + person.city
                                 + endp + state + person.state + endp + enddiv1)
            elif row == 2:
                outputFile.write(divright)
                outputFile.write(fname + person.firstname + endp + lname + person.lastname + endp + job
                                 + person.job + endp + company + person.company + endp + city + person.city
                                 + endp + state + person.state + endp + enddiv1 + enddiv2)
                row = 0

            page = page + 1
            if page == 10:
                outputFile.write(enddiv1 + divpage)
                page = 0
        outputFile.write(closing)

except OSError as err:
    print("OS error: {0}", format(err))
