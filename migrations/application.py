# /migrations/application.py

from datetime import datetime
from typing import List
from .ticketing import Ticketing
from Data_access_layer.Repository import TicketRepo

class TicketingService:
  def __init__(self, ticket_repo: TicketRepo):
    self.ticket_repo = ticket_repo

  def get_all_tickets(self) -> List[Ticketing]:
    tickets = self.ticket_repo.list()
    return [Ticketing(**ticket) for ticket in tickets]
  
  def create_ticket(self, firstname: str, lastname: str, date: datetime, description: str) -> Ticketing:
    new_ticket = self.ticket_repo.add(
      date=date,
      firstname=firstname,
      lastname=lastname,
      description=description
    )
    return new_ticket
  
  def get_ticket_by_date(self, date: datetime) -> Ticketing:
    ticket = self.ticket_repo.get(date=date)
    if ticket:
      return Ticketing(**ticket.dict())
    return None
    