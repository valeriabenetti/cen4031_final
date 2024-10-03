from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from Data_access_layer.Repository import TicketRepo
from api import router

def create_server(session_maker: sessionmaker = None, repositories=None):
    server = FastAPI(debug=True)
    server.include_router(router)
    
    if session_maker is None:
        raise ValueError("session_maker must be provided")
    
    server.session_maker = session_maker
    
    if repositories is None:
        # Initialize repositories if not provided
        repositories = {
            "ticketing_repo": lambda session: TicketRepo(session)
        }
    
    server.repositories = repositories
    
    return server