from fastapi import FastAPI

app = FastAPI()

def create_app():

    from app.Api.Hello import HelloController

    return app