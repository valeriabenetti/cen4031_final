from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_base


Base - declarative_base()

class TicketDB(Base):

    __tablename__ = "tickets"

    date = Column("date", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    description = Column("description", String)

    def dict(self):
        return {
            "date": self.date,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "created": self.created,
            "description": self.description,
        }

#    def __init__(self, firstname, lastname, date, description):
#
#        self.firstname = firstname
#        self.lastname = lastname
#        self.date = date
#        self.description = description
#
#    def __repr__(self):
#        return f"{self.firstname} {self.lastname} ({self.date}) {self.description}"
#
#engine = create_engine("sqlite:///myhelpdesktickets.db", echo=True)
#Base.metadata.create_all(bind=engine)
#
#Session = sessionmaker(bind=engine)
#session = Session()
#
#ticket = Tickets()
#session.add(ticket)
#session.commit()
