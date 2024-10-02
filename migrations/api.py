from datetime import datetime
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, conint
from starlette import status
from starlette.requests import Request

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

@router.get("/ticketing", response_model=TicketingList)

def get_ticketing(request: Request):
    with request.app.session_maker() as session:
        ticketing_repo = request.app.repositories.ticketing_repo(session)
        return {
            "ticketing": ticketing_repo.list()
        }

@router.post("/ticketing", status_code=status.HTTP_201_CREATED, response_model=TicketingPresentation)
def ticket_table(request: Request, ticket_details: TicketTable):
    with request.app.session_maker() as session:
        ticketing_repo = request.app.repositories.ticketing_repo(session)
        ticketing = ticketing_repo.add(
            date=ticket_details.date,
            firstname=ticket_details.firstname,
            lastname=ticket_details.lastname,
            description=ticket_details.description
        )
        session.commit()
        return ticketing.dict()
