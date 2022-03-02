from fastapi import FastAPI
from routes.years_route import year_api_router

app = FastAPI()

app.include_router(year_api_router)