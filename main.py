from fastapi import FastAPI
from app.schemas import StudentSchema
from app.crud import *
from app.database import engine,Base

app = FastAPI()

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)


@app.post("/students")
def create(data:StudentSchema):
    return Create(data)

@app.get("/students")
def list():
    return List()

@app.get("/students/{id}")
def get(id: int):
    return Get(id)

@app.put("/students/{id}")
def update(id: int, data: StudentSchema):
    return Update(id, data)

@app.delete("/students/{id}")
def delete(id: int):
    return Delete(id)
