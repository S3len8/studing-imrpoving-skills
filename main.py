import time
import asyncio

import uvicorn
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()


def sync_func():
    time.sleep(5)
    print("sync_func")


async def async_func():
    await asyncio.sleep(5)
    print("async_func")


@app.post("/")
async def some_route(back_ground_tasks: BackgroundTasks):
    ...
    # asyncio.create_task(async_func())
    back_ground_tasks.add_task(sync_func)
    return {"ok": True}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=False)