from fastapi import FastAPI
import uvicorn

app = FastAPI()

books = [
    {
        'id': 1,
        'title': "First Book",
        'author': 'User 1',
    },
    {
        'id': 2,
        'title': "Second Book",
        'author': 'User 2',
    }
]

if __name__ == __main__':
    uvicorn.run(app:"main:app", reload=True)