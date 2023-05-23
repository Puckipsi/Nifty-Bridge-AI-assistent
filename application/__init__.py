from fastapi import FastAPI, APIRouter

app = FastAPI(title='Nifty Brifge AI assistant')

api_router = APIRouter(prefix="/api/v1")

app.include_router(api_router)

import application.routes
