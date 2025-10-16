# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You will create a complete API for managing a book library system, including CRUD operations, data validation, and API documentation.

## 📝 Tasks

### 🛠️ Setup FastAPI Application

#### Description
Create a basic FastAPI application with proper project structure and install necessary dependencies. Set up the foundation for your book library API.

#### Requirements
Completed setup should:

- Create a main.py file with a FastAPI application instance
- Install FastAPI and uvicorn dependencies
- Include a basic "Hello World" endpoint at the root path
- Be able to run the server locally on port 8000

### 🛠️ Create Book Data Model

#### Description
Define a Pydantic model for representing books in your library system. This model will handle data validation and serialization.

#### Requirements
Completed model should:

- Include fields for title, author, year, genre, and ISBN
- Use appropriate data types and validation rules
- Include optional fields where appropriate
- Provide clear field descriptions using Pydantic Field annotations

### 🛠️ Implement CRUD Operations

#### Description
Create endpoints for Create, Read, Update, and Delete operations on books. Use proper HTTP methods and status codes for each operation.

#### Requirements
Completed API should:

- GET /books - retrieve all books
- GET /books/{book_id} - retrieve a specific book by ID
- POST /books - create a new book
- PUT /books/{book_id} - update an existing book
- DELETE /books/{book_id} - delete a book
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include proper error handling for invalid requests

### 🛠️ Add Advanced Features

#### Description
Enhance your API with additional features like filtering, searching, and comprehensive documentation.

#### Requirements
Enhanced API should:

- Add query parameters for filtering books by genre or author
- Implement search functionality for book titles
- Include comprehensive API documentation with descriptions
- Add request/response examples in the documentation
- Handle edge cases and provide meaningful error messages