
# Student Database CRUD API

A beginner-friendly Python backend project developed as part of the Python Backend Development internship assignment at EWB Edu Tech Pvt. Ltd.

## Project Overview

This project is a REST API for managing student records. It uses Python, FastAPI, and SQLite to perform CRUD operations.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* SQLite
* REST API
* Swagger UI

## Features

* Create a new student record
* Retrieve all student records
* Retrieve a student by ID
* Update student information
* Delete a student record
* Handle requests for student IDs that do not exist

## Student Fields

* `student_id` — unique student identifier
* `name` — student name
* `date_of_birth` — date of birth
* `email` — email address
* `phone` — phone number
* `course` — course name
* `address` — address
* `enrollment_date` — enrollment date

## Project Structure

```text
student-crud-api/
├── main.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `.venv` folder and `students.db` are local files and should not be committed to GitHub.

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Lingaswamy727/student-crud-api.git
cd student-crud-api
```

### 2. Create and activate a virtual environment

On Linux or WSL Ubuntu:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
uvicorn main:app --reload
```

### 5. Open the API documentation

Visit:

http://127.0.0.1:8000/docs

Use Swagger UI to test the API endpoints.

## API Endpoints

| Method | Endpoint                 | Description           |
| ------ | ------------------------ | --------------------- |
| POST   | `/students`              | Create a student      |
| GET    | `/students`              | Retrieve all students |
| GET    | `/students/{student_id}` | Retrieve one student  |
| PUT    | `/students/{student_id}` | Update a student      |
| DELETE | `/students/{student_id}` | Delete a student      |

## Error Handling

The API returns HTTP `404 Not Found` when a requested student ID does not exist.

## Database

SQLite stores student records locally. The database table is created automatically when the application starts.

## Testing

The endpoints were tested using FastAPI's interactive Swagger UI. Create, read, update, and delete operations were tested, including the response for a deleted student ID.

## Future Improvements

* Add input validation for dates, emails, and phone numbers
* Add automated API tests
* Add optional AI-powered student assistance

## Author

Python Backend Development Intern

