from unittest.mock import MagicMock

from starlette.testclient import TestClient

from ticketing import Ticketing
from Data_access_layer.repo_ticket_reg import RepoTicketReg
from server import create_server

class DummyTicketingRepo:
    def __init__(self, _):
        self.ticketing = []

        def add(self, date, firstname, lastname, description):
            ticketings = Ticketing(date=date, firstname=firstname, lastname=lastname, description=description)
            self.ticketing.append(ticketings)
            return ticketings

server = create_server(session_maker=MagicMock(), repositories=RepoTicketReg(ticketing_repo=DummyTicketingRepo))

test_client = testclient(app=server)

def test():
    payload= {
        "date": 1,
        "firstname": "john",
        "lastname": "smith",
        "description": "this is a test description"
    }
    response = test_client.post('/ticketings', json=payload)
    assert response.status_code == 201
