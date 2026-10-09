
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import create_table, get_connection


class StudentCreate(BaseModel):
    name: str
    date_of_birth: str
    email: str
    phone: str
    course: str | None = None
    address: str | None = None
    enrollment_date: str | None = None


app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "Student CRUD API is running!"}


# CREATE - Add a new student
@app.post("/students")
def create_student(student: StudentCreate):
    connection = get_connection()

    cursor = connection.execute("""
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
    """, (
        student.name,
        student.date_of_birth,
        student.email,
        student.phone,
        student.course,
        student.address,
        student.enrollment_date
    ))

    connection.commit()
    student_id = cursor.lastrowid
    connection.close()

    return {
        "message": "Student created successfully",
        "student_id": student_id
    }


# READ - Get all students
@app.get("/students")
def get_students():
    connection = get_connection()

    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()

    connection.close()

    return [dict(student) for student in students]


# READ - Get one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    connection = get_connection()

    student = connection.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    ).fetchone()

    connection.close()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return dict(student)



# UPDATE - Modify an existing student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate):
    connection = get_connection()

    cursor = connection.execute("""
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
    """, (
        student.name,
        student.date_of_birth,
        student.email,
        student.phone,
        student.course,
        student.address,
        student.enrollment_date,
        student_id
    ))

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    connection.close()

    return {
        "message": "Student updated successfully",
        "student_id": student_id
    }



# DELETE - Remove a student by ID
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    connection.close()

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }