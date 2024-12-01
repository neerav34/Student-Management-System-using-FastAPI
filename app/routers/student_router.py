from fastapi import APIRouter, HTTPException
from typing import Optional
from app.database import student_collection
from app.models import Student, UpdateStudent
from app.schemas import student_helper
from bson import ObjectId

router = APIRouter()


# Create a student
@router.post("/", response_model=dict, status_code=201)
async def create_student(student: Student):
    student_data = student.model_dump()
    new_student = await student_collection.insert_one(student_data)
    created_student = await student_collection.find_one(
        {"_id": new_student.inserted_id}
    )
    return {"id": str(created_student["_id"])}


# List students with optional filters
@router.get("/", response_model=dict, status_code=200)
async def get_students(country: Optional[str] = None, age: Optional[int] = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}

    students = []
    async for student in student_collection.find(query):
        students.append(student_helper(student))
    return {"data": students}


# Fetch a student by ID
@router.get("/{id}", response_model=dict, status_code=200)
async def get_student(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_helper(student)


# Update a student
@router.patch("/{id}", status_code=204)
async def update_student(id: str, student: UpdateStudent):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    update_data = {k: v for k, v in student.model_dump().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    result = await student_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": update_data}
    )

    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

    # No return value is needed when status_code=204
    return None


# Delete a student
@router.delete("/{id}", status_code=200)
async def delete_student(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    result = await student_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
