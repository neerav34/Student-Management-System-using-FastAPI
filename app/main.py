
from fastapi import FastAPI
from app.routers import student_router

app = FastAPI()

app.include_router(student_router.router, prefix="/students", tags=["students"])
