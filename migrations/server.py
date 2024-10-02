from fastapi import FastAPI

from api import router

def create_server(session_maker=none, repositories=none):
    server = FastAPI(debug=True)
    server.include_router(router)
    server.session_maker = session_maker
    server.repositories = repositories
    return server
