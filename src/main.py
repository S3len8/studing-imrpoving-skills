import time
from typing import Callable

from fastapi import FastAPI, Request, Response
import uvicorn
from src.api import main_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(main_router)


@app.middleware("http")
async def my_middleware(request: Request, call_next: Callable):
    ip_address = request.client.host
    print(f"{ip_address=}")
    # if ip_address in ["127.0.0.1", "localhost"]:
    #     return Response(status_code=429, content="Занадто багато запитів")

    start = time.perf_counter()
    response = await call_next(request)
    end = time.perf_counter() - start
    print(f"Час обробки запиту: {end}")
    response.headers["X-Special"] = "I am special"
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:63342/"]
)

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8088, reload=True)