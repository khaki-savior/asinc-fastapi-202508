from fastapi import FastAPI, Response
import uvicorn
from pydantic import BaseModel
from typing import Optional
import asyncio

class Book(BaseModel):
    title: str
    author: Optional[str] = None

books_db = {
    1:{"title": "Война и мир", "author": "Толстой Л.Н."}
}    

app = FastAPI(
    title="FastAPI 'Hello World!'",
    contact={
        "name": "KASHIRO Victoria",
        "email": "victoria.kashiro@wedomain.ru"
    }
)

hello_msg = {
    "message": "Hello, World!"
}

@app.get("/")
def root():
    """
    При обращении возвращает JSON-ответ «Hello, World!».
    """
    return hello_msg

@app.get("/books")
async def get_books():
    books_to_show = books_db
    return books_to_show

@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int, response: Response):
    if book_id not in books_db:
        response.status_code = 404
        return {"detail": "Book not found"}
    
    book_data = books_db[book_id]
    book = Book(**book_data)
    return book

@app.post("/books")
def add_books(book: Book, response: Response):
    new_book_id = len(books_db) + 1
    if book.title == "":
        response.status_code = 404
        return {"detail": "Title required"}
    books_db[new_book_id] = {"title": book.title, "author": book.author}
    return {"book_id": new_book_id, "book": books_db[new_book_id]}

@app.put("/books/{book_id}")
def update_book_by_id(book_id: int, book: Book, response: Response):
    if book_id not in books_db:
        response.status_code = 404
        return {"detail": "Book not found"}
    books_db[book_id] = {"title": book.title, "author": book.author}
    return {"detail": "Book updated successfully"}

@app.delete("/books/{book_id}")
def delete_book_by_id(book_id: int, response: Response):
    if book_id not in books_db:
        response.status_code = 404
        return {"detail": "Book not found"}
    
    deleted_book = books_db.pop(book_id) 
    return {"message": "Book deleted successfully", "deleted_book": deleted_book}

if __name__ == '__main__':
    uvicorn.run("main3_2:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)
    #print(asyncio.run(get_books()))
    #print(asyncio.run(get_book_by_id(1)))