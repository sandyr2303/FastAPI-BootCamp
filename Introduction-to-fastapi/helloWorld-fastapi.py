from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}


# Command to run FastAPI locally- uvicorn helloWorld-fastapi:app --reload 

# http://127.0.0.1:8000/docs - for getting documentation of FastAPI