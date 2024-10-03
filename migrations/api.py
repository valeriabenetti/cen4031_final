from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from starlette import status
from starlette.requests import Request
from .application import TicketingService

router = APIRouter()

class TicketTable(BaseModel):
    date: datetime
    firstname: str
    lastname: str
    description: str

class TicketingPresentation(BaseModel):
    date: datetime
    firstname: str
    lastname: str
    description: str

class TicketingList(BaseModel):
    ticketing: List[TicketingPresentation]

def get_ticketing_service(request: Request) -> TicketingService:
    with request.app.session_maker() as session:
        ticket_repo = request.app.repositories.ticketing_repo(session)
        return TicketingService(ticket_repo)

@router.get("/ticketing", response_model=TicketingList)
def get_ticketing(service: TicketingService = Depends(get_ticketing_service)):
    tickets = service.get_all_tickets()
    return {
        "ticketing": [ticket.dict for ticket in tickets]
    }

@router.post("/ticketing", status_code=status.HTTP_201_CREATED, response_model=TicketingPresentation)
def ticket_table(ticket_details: TicketTable, service: TicketingService = Depends(get_ticketing_service)):
    new_ticket = service.create_ticket(
        firstname=ticket_details.firstname,
        lastname=ticket_details.lastname,
        date=ticket_details.date,
        description=ticket_details.description
    )
    return new_ticket.dict