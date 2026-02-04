from fastapi import FastAPI
from project.api.routes import router
app=FastAPI()
app.include_router(router)