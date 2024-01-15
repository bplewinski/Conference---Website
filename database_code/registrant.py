class Registrant:
    def __init__(self, regDictionary):
        for key in regDictionary:
            setattr(self, key, regDictionary[key])
