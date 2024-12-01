# from fastapi import FastAPI
# from app.routes import router

# app = FastAPI(
#     title="Backend Intern Hiring Task",
#     description="APIs for Student Management System",
#     version="1.0.0",
# )

# app.include_router(router, prefix="/students", tags=["Students"])

from fastapi import FastAPI
from app.routers import student_router

app = FastAPI()

app.include_router(student_router.router, prefix="/students", tags=["students"])
