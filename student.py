from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    id: int
    grade: int

Students = [
    Student(name="Husam", id=24, grade=10),
    Student(name="Ali", id=23, grade=9),
]
@app.get('/students/')
def read_students():
    return Students

@app.post('/students/')
def create_student(New_student: Student):
    Students.append(New_student)
    return Students

@app.put('/students/{id}')
def update_student(id: int, updated_student: Student):
    for index, student in enumerate(Students):
        if student.id == id:
            Students[index] = updated_student
            return update_student
    return {"Error": "Student not found"}

@app.delete('/students/{id}')
def delete_student(id: int):
    for index, student in enumerate(Students):
        if student.id == id:
            del Students[index]
            return {"message": "Student deleted successfully"}
    return {"Message": "Student deleted successfully"}