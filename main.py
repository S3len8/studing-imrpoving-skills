import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse

app = FastAPI()


@app.post("/upload_files")
async def upload_files(uploaded_file: UploadFile):
    file = uploaded_file.file
    filename = uploaded_file.filename
    with open(f"1_{filename}", "wb") as f:
        f.write(file.read())


@app.post("/many_upload_files")
async def upload_files(uploaded_files: list[UploadFile]):
    for uploaded_file in uploaded_files:
        file = uploaded_file.file
        filename = uploaded_file.filename
        with open(f"1_{filename}", "wb") as f:
            f.write(file.read())


@app.get("/files/{filename}")
async def get_file(filename: str):
    return FileResponse(filename)


def iterfile(filename: str):
    with open(f"{filename}", "rb") as f:
        while chunk := f.read(1024 * 1024):
            yield chunk


@app.get("/files/streaming/{filename}")
async def get_streaming_file(filename: str):
    return StreamingResponse(iterfile(filename), media_type="video/mp4")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=False)