from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}


# http://127.0.0.1:8000/docs - for getting documentation of FastAPI