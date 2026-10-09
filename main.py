
import re
from datetime import date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, field_validator

from database import create_table, get_connection


# Student input validation
class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    date_of_birth: date
    email: EmailStr
    phone: str
    course: str | None = Field(default=None, max_length=100)
    address: str | None = Field(default=None, max_length=250)
    enrollment_date: date | None = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Name cannot contain only spaces.")

        return value

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        value = value.strip()

        if not re.fullmatch(r"\+?[0-9]{10,15}", value):
            raise ValueError(
                "Phone must contain 10-15 digits, optionally starting with +."
            )

        return value

    @field_validator("course", "address")
    @classmethod
    def validate_optional_text(cls, value):
        if value is not None:
            value = value.strip()

            if not value:
                raise ValueError(
                    "This field cannot contain only spaces."
                )

        return value


# Create the FastAPI application
app = FastAPI(
    title="Student CRUD API",
    description="API to create, read, update, and delete student records.",
    version="1.0.0"
)

# Create the database table when the application starts
create_table()


# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Student CRUD API"}


# Create a student
@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            INSERT INTO students (
                name,
                date_of_birth,
                email,
                phone,
                course,
                address,
                enrollment_date
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                student.name,
                student.date_of_birth.isoformat(),
                str(student.email),
                student.phone,
                student.course,
                student.address,
                (
                    student.enrollment_date.isoformat()
                    if student.enrollment_date
                    else None
                )
            )
        )

        connection.commit()
        student_id = cursor.lastrowid

        return {
            "message": "Student created successfully",
            "student_id": student_id
        }

    finally:
        connection.close()


# Get all students
@app.get("/students")
def get_students():
    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT * FROM students ORDER BY student_id"
        )

        students = [dict(row) for row in cursor.fetchall()]

        return {
            "count": len(students),
            "students": students
        }

    finally:
        connection.close()


# Get one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT * FROM students WHERE student_id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return dict(student)

    finally:
        connection.close()


# Update a student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            UPDATE students
            SET
                name = ?,
                date_of_birth = ?,
                email = ?,
                phone = ?,
                course = ?,
                address = ?,
                enrollment_date = ?
            WHERE student_id = ?
            """,
            (
                student.name,
                student.date_of_birth.isoformat(),
                str(student.email),
                student.phone,
                student.course,
                student.address,
                (
                    student.enrollment_date.isoformat()
                    if student.enrollment_date
                    else None
                ),
                student_id
            )
        )

        connection.commit()

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "message": "Student updated successfully",
            "student_id": student_id
        }

    finally:
        connection.close()


# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "DELETE FROM students WHERE student_id = ?",
            (student_id,)
        )

        connection.commit()

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "message": "Student deleted successfully",
            "student_id": student_id
        }

    finally:
        connection.close()