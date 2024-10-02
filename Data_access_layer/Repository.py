from ticketing import Ticketing

from Data_access_layer.DAticketmodel import TicketDB as TicketModel

class TicketRepo:

    def __init__(self, session):
        self.session = session

    def get(self, **filters):
        pass

    def list(self):
        return [
            tickets.dict() for tickets in self.query(TicketModel).all()
        ]
    def add(self, date, firstname, lastname, description):
        ticketing = TicketModel(
            date = date
            firstname = firstname
            lastname = lastname
            description = description
        )
        self.session.add(ticketing)
        return Ticketing(date=ticketing.date, firstname=ticketing.firstname, lastname=ticketing.lastname, description=tickering.description)

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass
