import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Data_access_layer.repo_ticket_reg import RepoTicketReg
from Data_access_layer.Repository import TicketRepo
from server import create_server

session_maker = sessionmaker(bind=create_engine(os.getenv("DB_URL")))

repositories_registry = RepositoriesRegistry(ticketing_repo=TicketRepo)

server = create_engine(session_maker=session_maker, repositories=repo_ticket_reg)
