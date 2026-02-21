from pydantic import BaseModel

class StudentSchema(BaseModel):
    Name:str
    Email:str
    Age:int
