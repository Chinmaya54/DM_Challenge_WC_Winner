from fastapi import FastAPI
from src.routes.winnerPredict import router 

app = FastAPI()

app.include_router(router)