from .DAticketmodel import TicketDB
from migrations.ticketing import Ticketing

class TicketRepo:

    def __init__(self, session):
        self.session = session

    def get(self, **filters):
        ticket = self.session.query(TicketDB).filter_by(**filters).first()
        if ticket:
            return Ticketing(
                date=ticket.date,
                firstname=ticket.firstname,
                lastname=ticket.lastname,
                description=ticket.description
            )
        return None

    def list(self):
        return [
            Ticketing(
                date=ticket.date,
                firstname=ticket.firstname,
                lastname=ticket.lastname,
                description=ticket.description
            ) for ticket in self.session.query(TicketDB).all()
        ]

    def add(self, date, firstname, lastname, description):
        ticket = TicketDB(
            date=date,
            firstname=firstname,
            lastname=lastname,
            description=description
        )
        self.session.add(ticket)
        self.session.flush()
        return Ticketing(
            date=ticket.date,
            firstname=ticket.firstname,
            lastname=ticket.lastname,
            description=ticket.description
        )