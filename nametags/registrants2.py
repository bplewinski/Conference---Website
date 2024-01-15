class Registrants:
    def __init__(self, personDict):
        self.firstname = personDict['firstname']
        self.lastname = personDict['lastname']
        self.job = personDict['position']
        self.company = personDict['company']
        self.city = personDict['city']
        self.state = personDict['state']
