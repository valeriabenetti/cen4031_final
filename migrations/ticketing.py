from datetime import datetime

class Ticketing:

    def __init__(self, date: datetime, firstname, lastname, description):
        self.date = date
        self.firstname = firstname
        self.lastname = lastname
        self. description = description

    @property

    def dict(self):
        return {
            "date": self.date,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "description": self.description,
        }
