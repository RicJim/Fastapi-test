from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_fast_api():
    return "Hello!"