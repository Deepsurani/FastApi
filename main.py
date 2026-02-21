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
