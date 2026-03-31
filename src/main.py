from fastapi import FastAPI
import uvicorn
from src.api import main_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(main_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:63342/"]
)

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8088, reload=True)