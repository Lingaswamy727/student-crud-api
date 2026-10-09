
# Student CRUD API

A beginner-friendly REST API built with FastAPI and SQLite to manage student records.

## Features

* Create a student record
* Retrieve all students
* Retrieve a student by ID
* Update student details
* Delete a student record
* Validate email addresses, phone numbers, names, and dates
* Store student data in an SQLite database
* Interactive API documentation using Swagger UI

## Technologies Used

* Python
* FastAPI
* SQLite
* Pydantic
* Uvicorn

## Project Structure

```text
student_crud_api/
├── main.py
├── database.py
├── requirements.txt
├── README.md
└── students.db  # Created automatically when the app starts
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Lingaswamy727/student-crud-api.git
cd student-crud-api
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn main:app --reload
```

### 5. Open the API documentation

Visit: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint                 | Purpose               |
| ------ | ------------------------ | --------------------- |
| POST   | `/students`              | Create a student      |
| GET    | `/students`              | Retrieve all students |
| GET    | `/students/{student_id}` | Retrieve one student  |
| PUT    | `/students/{student_id}` | Update a student      |
| DELETE | `/students/{student_id}` | Delete a student      |

## Learning Outcomes

* Building REST APIs with FastAPI
* Performing CRUD operations
* Connecting Python applications to SQLite
* Validating input using Pydantic
* Testing endpoints with Swagger UI
* Handling HTTP errors such as 404 and 422

## Author

Lingaswamy
