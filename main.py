from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.get("/tambah")
def operator_tambah(a: int, b: int):
    if a < 0 or b < 0:
        raise ValueError("a dan b harus positif")
    return {"result": a + b}


@app.get("/pengurangan")
def operator_pengurangan(a: int, b: int):
    return {"result": a - b}
