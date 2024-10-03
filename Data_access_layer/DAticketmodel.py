from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TicketDB(Base):
    
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, firstname, lastname, description, date=None):
        self.firstname = firstname
        self.lastname = lastname
        self.description = description
        self.date = date or datetime.timezone.utc()

    def dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "description": self.description,
            "created": self.created
        }

    def __repr__(self):
        return f"<Ticket(id={self.id}, firstname='{self.firstname}', lastname='{self.lastname}', date='{self.date}')>"
