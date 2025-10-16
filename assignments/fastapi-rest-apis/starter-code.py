# FastAPI Book Library Starter Code

# TODO: Import necessary modules from FastAPI and Pydantic
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from typing import List, Optional

# TODO: Create FastAPI application instance
# app = FastAPI(title="Book Library API", version="1.0.0")

# TODO: Define Book model using Pydantic
class Book:
    """
    Define your Book model here with the following fields:
    - id: integer (auto-generated)
    - title: string (required)
    - author: string (required) 
    - year: integer (required, should be reasonable year)
    - genre: string (optional)
    - isbn: string (optional, should follow ISBN format)
    """
    pass

# TODO: Create in-memory storage for books (use a list or dictionary)
books_db = []

# TODO: Implement the following endpoints:

# Root endpoint - returns welcome message
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Book Library API"}

# Get all books
# @app.get("/books")
# def get_books():
#     pass

# Get book by ID
# @app.get("/books/{book_id}")
# def get_book(book_id: int):
#     pass

# Create new book
# @app.post("/books")
# def create_book(book: Book):
#     pass

# Update existing book
# @app.put("/books/{book_id}")
# def update_book(book_id: int, book: Book):
#     pass

# Delete book
# @app.delete("/books/{book_id}")
# def delete_book(book_id: int):
#     pass

# TODO: Add query parameters for filtering
# @app.get("/books/search")
# def search_books(genre: Optional[str] = None, author: Optional[str] = None):
#     pass

if __name__ == "__main__":
    # TODO: Add uvicorn run command
    # import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    print("Run with: uvicorn main:app --reload")