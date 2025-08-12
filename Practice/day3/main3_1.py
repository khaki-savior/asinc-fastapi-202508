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

if __name__ == '__main__':
    uvicorn.run("main3_1:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)