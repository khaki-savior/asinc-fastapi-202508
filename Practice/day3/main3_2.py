from fastapi import FastAPI
import uvicorn

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

@app.get_books("GET/books")
def get_books():
    pass

@app.get_book_by_id("GET/books/{book_id}")
def get_book_by_id():
    pass

@app.postbooks("POST/books")
def add_books():
    pass

@app.put_books("PUT/books/{book_id}")
def update_book_by_id():
    pass

@app.del_books("DELETE /books/{book_id}")
def update_book_by_id():
    pass

if __name__ == '__main__':
    uvicorn.run("main3_1:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)