from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "qual a massa do sol??"