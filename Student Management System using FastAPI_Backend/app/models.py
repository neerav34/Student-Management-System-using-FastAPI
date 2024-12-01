# from pydantic import BaseModel, Field
# from typing import Optional


# # Request body for creating/updating a student
# class Address(BaseModel):
#     city: str = Field(..., example="New York")
#     country: str = Field(..., example="USA")


# class Student(BaseModel):
#     name: str = Field(..., example="John Doe")
#     age: int = Field(..., example=20)
#     address: Address


# class UpdateStudent(BaseModel):
#     name: Optional[str]
#     age: Optional[int]
#     address: Optional[Address]


from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    city: str
    country: str


class Student(BaseModel):
    name: str
    age: int
    address: Address


class UpdateStudent(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Address]
