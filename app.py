from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(name: str):
    return {"message": "Hello, World!", "name": name}
