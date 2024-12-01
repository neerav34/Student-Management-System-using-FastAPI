
from fastapi import FastAPI
from app.routers import student_router

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

app.include_router(student_router.router, prefix="/students", tags=["students"])
