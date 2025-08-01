# OrgSchool REST API Documentation

## Overview

The OrgSchool REST API provides endpoints for managing a school management system. The API follows RESTful principles and returns JSON responses. It includes functionality for managing admins, schools, classes, students, and teachers.

**Base URL:** `http://localhost:5001/api/v1`

**Content Type:** `application/json`

## Authentication

Currently, the API does not implement authentication. All endpoints are publicly accessible.

## Error Handling

The API uses standard HTTP status codes:

- `200` - OK: Request successful
- `201` - Created: Resource created successfully
- `400` - Bad Request: Invalid request format or missing required fields
- `404` - Not Found: Resource not found
- `500` - Internal Server Error: Server error

Error responses follow this format:
```json
{
  "error": "Error description"
}
```

## API Endpoints

### System Status

#### Get API Status
- **GET** `/status`
- **Description:** Check if the API is running
- **Response:**
  ```json
  {
    "status": "OK"
  }
  ```

#### Get Statistics
- **GET** `/stats`
- **Description:** Get count of all objects in the system
- **Response:**
  ```json
  {
    "students": 0,
    "schools": 0,
    "sclasses": 0,
    "teachers": 0,
    "admins": 0
  }
  ```

---

## Admins

Admins are the main users who manage schools in the system.

### Get All Admins
- **GET** `/admins`
- **Description:** Retrieve all admins
- **Response:**
  ```json
  [
    {
      "id": "admin-uuid",
      "email": "admin@example.com",
      "school_name": "Example School",
      "created_at": "2023-01-01T00:00:00",
      "updated_at": "2023-01-01T00:00:00"
    }
  ]
  ```

### Get Admin by ID
- **GET** `/admins/{admin_id}`
- **Description:** Retrieve a specific admin
- **Parameters:**
  - `admin_id` (string): Admin UUID
- **Response:**
  ```json
  {
    "id": "admin-uuid",
    "email": "admin@example.com",
    "school_name": "Example School",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Create Admin
- **POST** `/admins`
- **Description:** Create a new admin
- **Request Body:**
  ```json
  {
    "email": "admin@example.com",
    "password": "securepassword",
    "school_name": "Example School"
  }
  ```
- **Required Fields:** `email`, `password`, `school_name`
- **Response:** `201 Created`
  ```json
  {
    "email": "admin@example.com",
    "password": "hashed_password",
    "school_name": "Example School"
  }
  ```

### Update Admin
- **PUT** `/admins/{admin_id}`
- **Description:** Update an existing admin
- **Parameters:**
  - `admin_id` (string): Admin UUID
- **Request Body:**
  ```json
  {
    "school_name": "Updated School Name"
  }
  ```
- **Note:** `id`, `email`, and `password` fields cannot be updated
- **Response:**
  ```json
  {
    "id": "admin-uuid",
    "email": "admin@example.com",
    "school_name": "Updated School Name",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Delete Admin
- **DELETE** `/admins/{admin_id}`
- **Description:** Delete an admin
- **Parameters:**
  - `admin_id` (string): Admin UUID
- **Response:** `200 OK`
  ```json
  {}
  ```

---

## Schools

Schools are managed by admins and contain classes.

### Get All Schools
- **GET** `/schools`
- **Description:** Retrieve all schools
- **Response:**
  ```json
  [
    {
      "id": "school-uuid",
      "name": "Example School",
      "admin_id": "admin-uuid",
      "created_at": "2023-01-01T00:00:00",
      "updated_at": "2023-01-01T00:00:00"
    }
  ]
  ```

### Get School by ID
- **GET** `/schools/{school_id}`
- **Description:** Retrieve a specific school
- **Parameters:**
  - `school_id` (string): School UUID
- **Response:**
  ```json
  {
    "id": "school-uuid",
    "name": "Example School",
    "admin_id": "admin-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Create School
- **POST** `/admins/{admin_id}/schools`
- **Description:** Create a new school for an admin
- **Parameters:**
  - `admin_id` (string): Admin UUID
- **Request Body:**
  ```json
  {
    "name": "New School Name"
  }
  ```
- **Required Fields:** `name`
- **Response:** `201 Created`
  ```json
  {
    "id": "school-uuid",
    "name": "New School Name",
    "admin_id": "admin-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Update School
- **PUT** `/schools/{school_id}`
- **Description:** Update an existing school
- **Parameters:**
  - `school_id` (string): School UUID
- **Request Body:**
  ```json
  {
    "name": "Updated School Name"
  }
  ```
- **Note:** `id`, `created_at`, `updated_at`, and `admin_id` fields cannot be updated
- **Response:**
  ```json
  {
    "id": "school-uuid",
    "name": "Updated School Name",
    "admin_id": "admin-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Delete School
- **DELETE** `/schools/{school_id}`
- **Description:** Delete a school
- **Parameters:**
  - `school_id` (string): School UUID
- **Response:** `200 OK`
  ```json
  {}
  ```

---

## Classes (SClasses)

Classes belong to schools and contain students and teachers.

### Get All Classes in School
- **GET** `/schools/{school_id}/sclasses`
- **Description:** Retrieve all classes in a school
- **Parameters:**
  - `school_id` (string): School UUID
- **Response:**
  ```json
  [
    {
      "id": "class-uuid",
      "name": "Grade 1A",
      "school_id": "school-uuid",
      "created_at": "2023-01-01T00:00:00",
      "updated_at": "2023-01-01T00:00:00"
    }
  ]
  ```

### Get Class by ID
- **GET** `/schools/{school_id}/sclasses/{sclass_id}`
- **Description:** Retrieve a specific class
- **Parameters:**
  - `school_id` (string): School UUID
  - `sclass_id` (string): Class UUID
- **Response:**
  ```json
  {
    "id": "class-uuid",
    "name": "Grade 1A",
    "school_id": "school-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Create Class
- **POST** `/schools/{school_id}/sclasses`
- **Description:** Create a new class in a school
- **Parameters:**
  - `school_id` (string): School UUID
- **Request Body:**
  ```json
  {
    "name": "Grade 2B"
  }
  ```
- **Required Fields:** `name`
- **Response:** `201 Created`
  ```json
  {
    "id": "class-uuid",
    "name": "Grade 2B",
    "school_id": "school-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Update Class
- **PUT** `/schools/{school_id}/sclasses/{sclass_id}`
- **Description:** Update an existing class
- **Parameters:**
  - `school_id` (string): School UUID
  - `sclass_id` (string): Class UUID
- **Request Body:**
  ```json
  {
    "name": "Updated Class Name"
  }
  ```
- **Note:** `id`, `created_at`, and `updated_at` fields cannot be updated
- **Response:**
  ```json
  {
    "id": "class-uuid",
    "name": "Updated Class Name",
    "school_id": "school-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Delete Class
- **DELETE** `/schools/{school_id}/sclasses/{sclass_id}`
- **Description:** Delete a class
- **Parameters:**
  - `school_id` (string): School UUID
  - `sclass_id` (string): Class UUID
- **Response:** `200 OK`
  ```json
  {}
  ```

---

## Students

Students belong to classes.

### Get All Students in Class
- **GET** `/sclasses/{sclass_id}/students`
- **Description:** Retrieve all students in a class
- **Parameters:**
  - `sclass_id` (string): Class UUID
- **Response:**
  ```json
  [
    {
      "id": "student-uuid",
      "name": "John Doe",
      "age": 10,
      "sclass_id": "class-uuid",
      "created_at": "2023-01-01T00:00:00",
      "updated_at": "2023-01-01T00:00:00"
    }
  ]
  ```

### Get Student by ID
- **GET** `/sclasses/{sclass_id}/students/{student_id}`
- **Description:** Retrieve a specific student
- **Parameters:**
  - `sclass_id` (string): Class UUID
  - `student_id` (string): Student UUID
- **Response:**
  ```json
  {
    "id": "student-uuid",
    "name": "John Doe",
    "age": 10,
    "sclass_id": "class-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Create Student
- **POST** `/sclasses/{sclass_id}/students`
- **Description:** Create a new student in a class
- **Parameters:**
  - `sclass_id` (string): Class UUID
- **Request Body:**
  ```json
  {
    "name": "Jane Smith",
    "age": 11
  }
  ```
- **Required Fields:** `name`, `age`
- **Response:** `201 Created`
  ```json
  {
    "id": "student-uuid",
    "name": "Jane Smith",
    "age": 11,
    "sclass_id": "class-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Update Student
- **PUT** `/sclasses/{sclass_id}/students/{student_id}`
- **Description:** Update an existing student
- **Parameters:**
  - `sclass_id` (string): Class UUID
  - `student_id` (string): Student UUID
- **Request Body:**
  ```json
  {
    "name": "Updated Name",
    "age": 12
  }
  ```
- **Note:** `id`, `created_at`, and `updated_at` fields cannot be updated
- **Response:**
  ```json
  {
    "id": "student-uuid",
    "name": "Updated Name",
    "age": 12,
    "sclass_id": "class-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Delete Student
- **DELETE** `/sclasses/{sclass_id}/students/{student_id}`
- **Description:** Delete a student
- **Parameters:**
  - `sclass_id` (string): Class UUID
  - `student_id` (string): Student UUID
- **Response:** `200 OK`
  ```json
  {}
  ```

---

## Teachers

Teachers belong to classes.

### Get All Teachers in Class
- **GET** `/sclasses/{sclass_id}/teachers`
- **Description:** Retrieve all teachers in a class
- **Parameters:**
  - `sclass_id` (string): Class UUID
- **Response:**
  ```json
  [
    {
      "id": "teacher-uuid",
      "name": "Mr. Johnson",
      "subject": "Mathematics",
      "sclass_id": "class-uuid",
      "created_at": "2023-01-01T00:00:00",
      "updated_at": "2023-01-01T00:00:00"
    }
  ]
  ```

### Get Teacher by ID
- **GET** `/sclasses/{sclass_id}/teachers/{teacher_id}`
- **Description:** Retrieve a specific teacher
- **Parameters:**
  - `sclass_id` (string): Class UUID
  - `teacher_id` (string): Teacher UUID
- **Response:**
  ```json
  {
    "id": "teacher-uuid",
    "name": "Mr. Johnson",
    "subject": "Mathematics",
    "sclass_id": "class-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Create Teacher
- **POST** `/sclasses/{sclass_id}/teachers`
- **Description:** Create a new teacher in a class
- **Parameters:**
  - `sclass_id` (string): Class UUID
- **Request Body:**
  ```json
  {
    "name": "Ms. Williams",
    "subject": "English"
  }
  ```
- **Required Fields:** `name`
- **Response:** `201 Created`
  ```json
  {
    "id": "teacher-uuid",
    "name": "Ms. Williams",
    "subject": "English",
    "sclass_id": "class-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Update Teacher
- **PUT** `/sclasses/{sclass_id}/teachers/{teacher_id}`
- **Description:** Update an existing teacher
- **Parameters:**
  - `sclass_id` (string): Class UUID
  - `teacher_id` (string): Teacher UUID
- **Request Body:**
  ```json
  {
    "name": "Updated Teacher Name",
    "subject": "Science"
  }
  ```
- **Note:** `id`, `created_at`, and `updated_at` fields cannot be updated
- **Response:**
  ```json
  {
    "id": "teacher-uuid",
    "name": "Updated Teacher Name",
    "subject": "Science",
    "sclass_id": "class-uuid",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
  ```

### Delete Teacher
- **DELETE** `/sclasses/{sclass_id}/teachers/{teacher_id}`
- **Description:** Delete a teacher
- **Parameters:**
  - `sclass_id` (string): Class UUID
  - `teacher_id` (string): Teacher UUID
- **Response:** `200 OK`
  ```json
  {}
  ```

---

## Data Models

### Admin
```json
{
  "id": "string (UUID)",
  "email": "string",
  "password": "string (hashed)",
  "school_name": "string",
  "created_at": "string (ISO 8601)",
  "updated_at": "string (ISO 8601)"
}
```

### School
```json
{
  "id": "string (UUID)",
  "name": "string",
  "admin_id": "string (UUID)",
  "created_at": "string (ISO 8601)",
  "updated_at": "string (ISO 8601)"
}
```

### Class (SClass)
```json
{
  "id": "string (UUID)",
  "name": "string",
  "school_id": "string (UUID)",
  "created_at": "string (ISO 8601)",
  "updated_at": "string (ISO 8601)"
}
```

### Student
```json
{
  "id": "string (UUID)",
  "name": "string",
  "age": "integer",
  "sclass_id": "string (UUID)",
  "created_at": "string (ISO 8601)",
  "updated_at": "string (ISO 8601)"
}
```

### Teacher
```json
{
  "id": "string (UUID)",
  "name": "string",
  "subject": "string (optional)",
  "sclass_id": "string (UUID)",
  "created_at": "string (ISO 8601)",
  "updated_at": "string (ISO 8601)"
}
```

---

## Example Usage

### Create Complete School Structure

1. **Create Admin:**
   ```bash
   curl -X POST http://localhost:5001/api/v1/admins \
     -H "Content-Type: application/json" \
     -d '{
       "email": "admin@school.com",
       "password": "securepassword",
       "school_name": "Example High School"
     }'
   ```

2. **Create School:**
   ```bash
   curl -X POST http://localhost:5001/api/v1/admins/{admin_id}/schools \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Example High School"
     }'
   ```

3. **Create Class:**
   ```bash
   curl -X POST http://localhost:5001/api/v1/schools/{school_id}/sclasses \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Grade 10A"
     }'
   ```

4. **Add Student:**
   ```bash
   curl -X POST http://localhost:5001/api/v1/sclasses/{sclass_id}/students \
     -H "Content-Type: application/json" \
     -d '{
       "name": "John Doe",
       "age": 16
     }'
   ```

5. **Add Teacher:**
   ```bash
   curl -X POST http://localhost:5001/api/v1/sclasses/{sclass_id}/teachers \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Mr. Smith",
       "subject": "Mathematics"
     }'
   ```

---

## Environment Variables

- `ORG_API_HOST`: API host (default: `0.0.0.0`)
- `ORG_API_PORT`: API port (default: `5000`)
- `ORG_TYPE_STORAGE`: Storage type (default: `db`)

---

## Swagger Documentation

The API includes Swagger documentation accessible at:
- `http://localhost:5001/apidocs/`

This provides an interactive interface to test the API endpoints.

---

## Notes

- All UUIDs are automatically generated using UUID4
- Passwords are automatically hashed using MD5 (consider upgrading to bcrypt for production)
- The API uses SQLAlchemy with MySQL for data persistence
- All timestamps are in ISO 8601 format
- The API supports CORS for cross-origin requests
