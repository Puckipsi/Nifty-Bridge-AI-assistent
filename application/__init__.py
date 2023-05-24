from fastapi import FastAPI, APIRouter
from utils.asserts import assert_startup


assert_startup()

app = FastAPI(title='Nifty Brifge AI assistant')

api_router = APIRouter(prefix="/api/v1")

app.include_router(api_router)

import application.routes
